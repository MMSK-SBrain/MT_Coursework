"""
Unit tests for ConfigManager

Tests configuration loading, validation, merging, and error handling.
"""

import os
import tempfile
import pytest
import yaml
from pathlib import Path

# Add parent directory to path to import src modules
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config_manager import ConfigManager, ConfigValidationError


class TestConfigManager:
    """Test suite for ConfigManager"""

    def test_default_config_loads(self):
        """Test that default configuration loads successfully"""
        config = ConfigManager.from_defaults()
        assert config is not None
        assert config.get("global.output_directory") == "./handouts"
        assert config.get("questions.enabled") is True
        assert config.get("questions.require_review") is True

    def test_config_from_file(self, tmp_path):
        """Test loading configuration from file"""
        config_file = tmp_path / "test_config.yaml"
        config_data = {
            "global": {
                "output_directory": "./custom_output"
            },
            "questions": {
                "enabled": True,
                "require_review": True,
                "questions_per_section": 10
            }
        }

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        config = ConfigManager.from_file(str(config_file))
        assert config.get("global.output_directory") == "./custom_output"
        assert config.get("questions.questions_per_section") == 10

    def test_config_file_not_found(self):
        """Test error when config file doesn't exist"""
        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path="/nonexistent/config.yaml")
        assert "Configuration file not found" in str(exc_info.value)

    def test_empty_config_file(self, tmp_path):
        """Test error when config file is empty"""
        config_file = tmp_path / "empty_config.yaml"
        config_file.write_text("")

        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path=str(config_file))
        assert "Configuration file is empty" in str(exc_info.value)

    def test_invalid_yaml(self, tmp_path):
        """Test error when config file has invalid YAML"""
        config_file = tmp_path / "invalid_config.yaml"
        config_file.write_text("invalid: yaml: content: [")

        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path=str(config_file))
        assert "Invalid YAML" in str(exc_info.value)

    def test_missing_required_global_section(self, tmp_path):
        """Test that defaults fill in missing global section"""
        config_file = tmp_path / "no_global.yaml"
        config_data = {"questions": {"enabled": True, "require_review": True}}

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        # Defaults should fill in global section
        config = ConfigManager(config_path=str(config_file))
        assert config.get("global.output_directory") is not None

    def test_missing_required_questions_section(self, tmp_path):
        """Test that defaults fill in missing questions section"""
        config_file = tmp_path / "no_questions.yaml"
        config_data = {"global": {"output_directory": "./test"}}

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        # Defaults should fill in questions section
        config = ConfigManager(config_path=str(config_file))
        assert config.get("questions.enabled") is not None
        assert config.get("questions.require_review") is True

    def test_require_review_must_be_true(self, tmp_path):
        """Test that require_review cannot be disabled"""
        config_file = tmp_path / "review_false.yaml"
        config_data = {
            "global": {"output_directory": "./test"},
            "questions": {"enabled": True, "require_review": False}
        }

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path=str(config_file))
        assert "require_review' must be True" in str(exc_info.value)

    def test_invalid_page_size(self, tmp_path):
        """Test error for invalid page size"""
        config_file = tmp_path / "invalid_page_size.yaml"
        config_data = {
            "global": {"output_directory": "./test", "page_size": "INVALID"},
            "questions": {"enabled": True, "require_review": True}
        }

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path=str(config_file))
        assert "Invalid page_size" in str(exc_info.value)

    def test_invalid_question_type(self, tmp_path):
        """Test error for invalid question type"""
        config_file = tmp_path / "invalid_question_type.yaml"
        config_data = {
            "global": {"output_directory": "./test"},
            "questions": {
                "enabled": True,
                "require_review": True,
                "types": ["invalid_type"]
            }
        }

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path=str(config_file))
        assert "Invalid question type" in str(exc_info.value)

    def test_invalid_logging_level(self, tmp_path):
        """Test error for invalid logging level"""
        config_file = tmp_path / "invalid_log_level.yaml"
        config_data = {
            "global": {"output_directory": "./test"},
            "questions": {"enabled": True, "require_review": True},
            "logging": {"level": "INVALID"}
        }

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        with pytest.raises(ConfigValidationError) as exc_info:
            ConfigManager(config_path=str(config_file))
        assert "Invalid logging level" in str(exc_info.value)

    def test_get_nested_value(self):
        """Test getting nested configuration value"""
        config = ConfigManager.from_defaults()
        assert config.get("branding.theme") == "dark"
        assert config.get("branding.colors.background_primary") == "#0D1117"
        assert config.get("pdf.margins.top") == "20mm"

    def test_get_with_default(self):
        """Test getting value with default"""
        config = ConfigManager.from_defaults()
        assert config.get("nonexistent.key", "default_value") == "default_value"

    def test_module_config_merge(self):
        """Test module-specific configuration merging"""
        # Load from actual config file which has module overrides
        config = ConfigManager.from_file("handout_config.yaml")
        module_config = config.get_module_config("module-0")

        # Module-0 should have 5 questions per section (override from file)
        assert module_config["questions"]["questions_per_section"] == 5

        # But should still have global settings
        assert module_config["questions"]["enabled"] is True

    def test_module_config_no_override(self):
        """Test module config when no override exists"""
        config = ConfigManager.from_defaults()
        module_config = config.get_module_config("module-5")

        # Should use global default of 7 (no override)
        assert module_config["questions"]["questions_per_section"] == 7

    def test_deep_merge(self):
        """Test deep merging of configurations"""
        config = ConfigManager.from_defaults()

        # Should have all default colors
        colors = config.get("branding.colors")
        assert "background_primary" in colors
        assert "text_primary" in colors
        assert "accent_blue" in colors

    def test_config_to_dict(self):
        """Test converting config to dictionary"""
        config = ConfigManager.from_defaults()
        config_dict = config.to_dict()

        assert isinstance(config_dict, dict)
        assert "global" in config_dict
        assert "questions" in config_dict
        assert "branding" in config_dict

    def test_config_save(self, tmp_path):
        """Test saving configuration to file"""
        config = ConfigManager.from_defaults()
        output_file = tmp_path / "saved_config.yaml"

        config.save(str(output_file))

        assert output_file.exists()

        # Load saved config and verify
        loaded_config = ConfigManager.from_file(str(output_file))
        assert loaded_config.get("global.output_directory") == "./handouts"

    def test_partial_config_merge(self, tmp_path):
        """Test that partial user config merges with defaults"""
        config_file = tmp_path / "partial_config.yaml"
        config_data = {
            "global": {"output_directory": "./my_handouts"},
            "questions": {"enabled": True, "require_review": True}
        }

        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)

        config = ConfigManager.from_file(str(config_file))

        # User value
        assert config.get("global.output_directory") == "./my_handouts"

        # Default values (not in user config)
        assert config.get("global.archive_old_versions") is True
        assert config.get("branding.theme") == "dark"
        assert config.get("pdf.margins.top") == "20mm"

    def test_all_question_types_valid(self):
        """Test that all default question types are valid"""
        config = ConfigManager.from_defaults()
        question_types = config.get("questions.types")

        valid_types = ["multiple_choice", "true_false", "short_answer", "reflection", "application"]
        for qtype in question_types:
            assert qtype in valid_types

    def test_default_config_completeness(self):
        """Test that default config has all required sections"""
        config = ConfigManager.from_defaults()

        # Check all main sections exist
        assert config.get("global") is not None
        assert config.get("branding") is not None
        assert config.get("questions") is not None
        assert config.get("content") is not None
        assert config.get("images") is not None
        assert config.get("pdf") is not None
        assert config.get("logging") is not None
        assert config.get("modules") is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
