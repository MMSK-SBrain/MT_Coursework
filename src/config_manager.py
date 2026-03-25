"""
Configuration Manager for Student Handout Generator

Loads and validates YAML configuration files against schema,
provides sensible defaults, and merges global + module-specific configs.
"""

import os
import json
from pathlib import Path
from typing import Any, Dict, Optional
import yaml


class ConfigValidationError(Exception):
    """Raised when configuration validation fails."""
    pass


class ConfigManager:
    """
    Manages configuration loading, validation, and access.

    Loads YAML config files, validates against JSON schema,
    provides sensible defaults, and merges global + module-specific configs.
    """

    # JSON Schema for configuration validation (from PRD Appendix C)
    CONFIG_SCHEMA = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "global": {
                "type": "object",
                "properties": {
                    "output_directory": {"type": "string"},
                    "archive_old_versions": {"type": "boolean"},
                    "page_size": {"type": "string", "enum": ["A4", "Letter"]},
                    "fonts": {
                        "type": "object",
                        "properties": {
                            "body": {"type": "string"},
                            "heading": {"type": "string"},
                            "code": {"type": "string"}
                        }
                    }
                },
                "required": ["output_directory"]
            },
            "branding": {
                "type": "object",
                "properties": {
                    "logo_path": {"type": "string"},
                    "theme": {"type": "string", "enum": ["dark", "light"]},
                    "colors": {
                        "type": "object",
                        "properties": {
                            "background_primary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "background_secondary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "background_tertiary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "text_primary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "text_secondary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "text_muted": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "accent_blue": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "accent_green": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "accent_orange": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "accent_red": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "accent_purple": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
                            "border_default": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"}
                        }
                    }
                }
            },
            "questions": {
                "type": "object",
                "properties": {
                    "enabled": {"type": "boolean"},
                    "require_review": {"type": "boolean", "const": True},
                    "questions_per_section": {"type": "integer", "minimum": 1, "maximum": 20},
                    "types": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["multiple_choice", "true_false", "short_answer", "reflection", "application"]
                        }
                    },
                    "ai_generation": {
                        "type": "object",
                        "properties": {
                            "enabled": {"type": "boolean"},
                            "provider": {"type": "string", "enum": ["anthropic"]},
                            "api_key_env_var": {"type": "string"},
                            "model": {"type": "string"},
                            "max_retries": {"type": "integer"},
                            "timeout_seconds": {"type": "integer"}
                        }
                    },
                    "staging_directory": {"type": "string"},
                    "approved_directory": {"type": "string"},
                    "rejected_directory": {"type": "string"}
                },
                "required": ["enabled", "require_review"]
            },
            "content": {
                "type": "object",
                "properties": {
                    "exclude_patterns": {"type": "array", "items": {"type": "string"}},
                    "include_toc": {"type": "boolean"},
                    "include_learning_outcomes": {"type": "boolean"},
                    "include_assessments": {"type": "boolean"}
                }
            },
            "images": {
                "type": "object",
                "properties": {
                    "base_directory": {"type": "string"},
                    "max_width": {"type": "integer"},
                    "placeholder_on_missing": {"type": "boolean"},
                    "placeholder_color": {"type": "string"},
                    "formats_supported": {"type": "array", "items": {"type": "string"}}
                }
            },
            "pdf": {
                "type": "object",
                "properties": {
                    "margins": {
                        "type": "object",
                        "properties": {
                            "top": {"type": "string"},
                            "bottom": {"type": "string"},
                            "left": {"type": "string"},
                            "right": {"type": "string"}
                        }
                    },
                    "header": {
                        "type": "object",
                        "properties": {
                            "enabled": {"type": "boolean"},
                            "format": {"type": "string"},
                            "color": {"type": "string"}
                        }
                    },
                    "footer": {
                        "type": "object",
                        "properties": {
                            "enabled": {"type": "boolean"},
                            "format": {"type": "string"},
                            "color": {"type": "string"}
                        }
                    },
                    "page_break_before_sections": {"type": "boolean"}
                }
            },
            "logging": {
                "type": "object",
                "properties": {
                    "level": {"type": "string", "enum": ["DEBUG", "INFO", "WARNING", "ERROR"]},
                    "format": {"type": "string"},
                    "file": {"type": "string"},
                    "console": {"type": "boolean"},
                    "max_file_size": {"type": "string"},
                    "backup_count": {"type": "integer"}
                }
            },
            "modules": {
                "type": "object",
                "additionalProperties": {
                    "type": "object"
                }
            }
        },
        "required": ["global", "questions"]
    }

    # Default configuration values
    DEFAULT_CONFIG = {
        "global": {
            "output_directory": "./handouts",
            "archive_old_versions": True,
            "page_size": "A4",
            "fonts": {
                "body": "Inter",
                "heading": "Inter",
                "code": "JetBrains Mono"
            }
        },
        "branding": {
            "logo_path": "./assets/logo.png",
            "theme": "dark",
            "colors": {
                "background_primary": "#0D1117",
                "background_secondary": "#161B22",
                "background_tertiary": "#21262D",
                "text_primary": "#E6EDF3",
                "text_secondary": "#8B949E",
                "text_muted": "#484F58",
                "accent_blue": "#58A6FF",
                "accent_green": "#3FB950",
                "accent_orange": "#D29922",
                "accent_red": "#F85149",
                "accent_purple": "#A371F7",
                "border_default": "#30363D"
            }
        },
        "questions": {
            "enabled": True,
            "require_review": True,
            "questions_per_section": 7,
            "types": ["multiple_choice", "true_false", "short_answer", "reflection", "application"],
            "ai_generation": {
                "enabled": True,
                "provider": "anthropic",
                "api_key_env_var": "ANTHROPIC_API_KEY",
                "model": "claude-sonnet-4-20250514",
                "max_retries": 3,
                "timeout_seconds": 60
            },
            "staging_directory": "./question_banks/staging",
            "approved_directory": "./question_banks/approved",
            "rejected_directory": "./question_banks/rejected"
        },
        "content": {
            "exclude_patterns": [
                "## Video Production Notes",
                "### For Instructors",
                "<!-- INSTRUCTOR ONLY -->"
            ],
            "include_toc": True,
            "include_learning_outcomes": True,
            "include_assessments": True
        },
        "images": {
            "base_directory": "./images",
            "max_width": 500,
            "placeholder_on_missing": True,
            "placeholder_color": "#21262D",
            "formats_supported": ["png", "jpg", "jpeg", "svg"]
        },
        "pdf": {
            "margins": {
                "top": "20mm",
                "bottom": "20mm",
                "left": "25mm",
                "right": "25mm"
            },
            "header": {
                "enabled": True,
                "format": "{module_title}",
                "color": "#8B949E"
            },
            "footer": {
                "enabled": True,
                "format": "Page {page_number}",
                "color": "#484F58"
            },
            "page_break_before_sections": True
        },
        "logging": {
            "level": "INFO",
            "format": "[{timestamp}] [{level}] [{module}] {message}",
            "file": "./logs/handout_generation.log",
            "console": True,
            "max_file_size": "10MB",
            "backup_count": 3
        },
        "modules": {}
    }

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize ConfigManager.

        Args:
            config_path: Path to YAML configuration file. If None, uses default config.
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        """
        Load configuration from file or use defaults.

        Raises:
            ConfigValidationError: If configuration is invalid.
        """
        # Start with default config
        self.config = self._deep_copy(self.DEFAULT_CONFIG)

        # If config path provided, load and merge
        if self.config_path:
            if not os.path.exists(self.config_path):
                raise ConfigValidationError(
                    f"Configuration file not found: {self.config_path}"
                )

            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    user_config = yaml.safe_load(f)

                if user_config is None:
                    raise ConfigValidationError(
                        f"Configuration file is empty: {self.config_path}"
                    )

                # Merge user config with defaults
                self.config = self._deep_merge(self.config, user_config)

            except yaml.YAMLError as e:
                raise ConfigValidationError(
                    f"Invalid YAML in configuration file: {self.config_path}\n"
                    f"Error: {str(e)}"
                )

        # Validate configuration
        self._validate_config()

    def _validate_config(self) -> None:
        """
        Validate configuration against schema.

        Raises:
            ConfigValidationError: If configuration is invalid.
        """
        # Check required top-level keys
        if "global" not in self.config:
            raise ConfigValidationError("Missing required 'global' section in configuration")

        if "questions" not in self.config:
            raise ConfigValidationError("Missing required 'questions' section in configuration")

        # Validate global.output_directory
        if "output_directory" not in self.config["global"]:
            raise ConfigValidationError("Missing required 'global.output_directory' in configuration")

        # Validate questions.require_review is always True
        if not self.config["questions"].get("require_review", False):
            raise ConfigValidationError(
                "Configuration error: 'questions.require_review' must be True. "
                "Question review is mandatory and cannot be disabled."
            )

        # Validate page_size if present
        if "page_size" in self.config.get("global", {}):
            valid_sizes = ["A4", "Letter"]
            if self.config["global"]["page_size"] not in valid_sizes:
                raise ConfigValidationError(
                    f"Invalid page_size: {self.config['global']['page_size']}. "
                    f"Must be one of: {', '.join(valid_sizes)}"
                )

        # Validate question types if present
        if "types" in self.config.get("questions", {}):
            valid_types = ["multiple_choice", "true_false", "short_answer", "reflection", "application"]
            for qtype in self.config["questions"]["types"]:
                if qtype not in valid_types:
                    raise ConfigValidationError(
                        f"Invalid question type: {qtype}. "
                        f"Must be one of: {', '.join(valid_types)}"
                    )

        # Validate logging level if present
        if "logging" in self.config and "level" in self.config["logging"]:
            valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
            if self.config["logging"]["level"] not in valid_levels:
                raise ConfigValidationError(
                    f"Invalid logging level: {self.config['logging']['level']}. "
                    f"Must be one of: {', '.join(valid_levels)}"
                )

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get configuration value by dot-separated key path.

        Args:
            key_path: Dot-separated path to configuration value (e.g., "global.output_directory")
            default: Default value if key not found

        Returns:
            Configuration value or default

        Example:
            >>> config = ConfigManager()
            >>> config.get("global.output_directory")
            "./handouts"
        """
        keys = key_path.split('.')
        value = self.config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value

    def get_module_config(self, module_id: str) -> Dict[str, Any]:
        """
        Get merged configuration for a specific module.

        Merges global config with module-specific overrides.

        Args:
            module_id: Module identifier (e.g., "module-0")

        Returns:
            Merged configuration dictionary for the module
        """
        # Start with base config
        module_config = self._deep_copy(self.config)

        # Get module-specific overrides
        module_overrides = self.config.get("modules", {}).get(module_id, {})

        # Merge overrides
        if module_overrides:
            module_config = self._deep_merge(module_config, module_overrides)

        return module_config

    def _deep_copy(self, obj: Any) -> Any:
        """Deep copy a configuration object."""
        if isinstance(obj, dict):
            return {k: self._deep_copy(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._deep_copy(item) for item in obj]
        else:
            return obj

    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep merge two dictionaries.

        Override values take precedence over base values.

        Args:
            base: Base dictionary
            override: Override dictionary

        Returns:
            Merged dictionary
        """
        result = self._deep_copy(base)

        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = self._deep_copy(value)

        return result

    @classmethod
    def from_file(cls, config_path: str) -> 'ConfigManager':
        """
        Create ConfigManager from configuration file.

        Args:
            config_path: Path to YAML configuration file

        Returns:
            ConfigManager instance
        """
        return cls(config_path=config_path)

    @classmethod
    def from_defaults(cls) -> 'ConfigManager':
        """
        Create ConfigManager with default configuration.

        Returns:
            ConfigManager instance with defaults
        """
        return cls(config_path=None)

    def to_dict(self) -> Dict[str, Any]:
        """
        Get configuration as dictionary.

        Returns:
            Configuration dictionary
        """
        return self._deep_copy(self.config)

    def save(self, output_path: str) -> None:
        """
        Save current configuration to YAML file.

        Args:
            output_path: Path to save configuration file
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
