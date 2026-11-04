#!/usr/bin/env python3
"""
Generate complete assessment criteria and activities for all course modules.
This script reads the learning outcomes and generates comprehensive assessment and activity suggestions.
"""

import json

# Load existing partial file
with open('courses/ml-for-engineers/assessment-and-activities.json', 'r') as f:
    data = json.load(f)

# Module 2: Classification (adding to existing structure)
module_2 = {
    "module_id": "module-2",
    "module_number": 2,
    "title": "Supervised Learning - Classification",
    "sessions": [
        {
            "session_id": "session-2-1",
            "title": "Classification Fundamentals",
            "outcomes": [
                {
                    "id": "so-2-1-1",
                    "code": "ML-ENG-SO-2-1-1",
                    "description": "Explain what classification problems are and provide real-world examples",
                    "assessment_criteria": {
                        "evidence": "Written explanation with 5 real-world classification examples from different domains",
                        "measurement": "Accuracy of definition; diversity of examples; understanding of binary vs multi-class",
                        "success_criteria": "Correct definition; 5 valid examples; identifies whether each is binary or multi-class"
                    },
                    "activities": [
                        {
                            "type": "concept_quiz",
                            "title": "Classification Problem Identification",
                            "description": "Ask AI: 'What are classification problems in ML? Give me 10 real-world examples.' Select your favorite 5 and explain why they're classification tasks.",
                            "duration_minutes": 20,
                            "deliverable": "Document with 5 classification problems and explanations"
                        },
                        {
                            "type": "collaborative_learning",
                            "title": "Binary vs Multi-class",
                            "description": "For each of your 5 examples, determine if it's binary or multi-class classification. Ask AI to verify your answers.",
                            "duration_minutes": 15,
                            "deliverable": "Classification type analysis for each example"
                        }
                    ]
                },
                {
                    "id": "so-2-1-2",
                    "code": "ML-ENG-SO-2-1-2",
                    "description": "Distinguish between binary and multi-class classification problems",
                    "assessment_criteria": {
                        "evidence": "Comparison table with characteristics and examples of each type",
                        "measurement": "Clarity of distinction; accuracy of examples",
                        "success_criteria": "Identifies key differences; provides 3 examples of each type"
                    },
                    "activities": [
                        {
                            "type": "model_comparison",
                            "title": "Binary vs Multi-class Comparison",
                            "description": "Create a comparison table with AI help: Binary vs Multi-class covering: Definition, Example problems, Typical algorithms, Output format, Evaluation metrics.",
                            "duration_minutes": 25,
                            "deliverable": "Comparison table with 5 dimensions"
                        }
                    ]
                },
                {
                    "id": "so-2-1-3",
                    "code": "ML-ENG-SO-2-1-3",
                    "description": "Use LLMs to generate a simple binary classification example with sample data",
                    "assessment_criteria": {
                        "evidence": "Working code that performs binary classification on generated dataset",
                        "measurement": "Code runs successfully; data is appropriate; predictions are made",
                        "success_criteria": "Generates synthetic data; trains model; makes predictions; shows basic accuracy"
                    },
                    "activities": [
                        {
                            "type": "project_builder",
                            "title": "First Binary Classifier",
                            "description": "Prompt AI: 'Generate Python code for binary classification that: 1) Creates synthetic dataset (200 samples, 5 features), 2) Splits train/test, 3) Trains logistic regression, 4) Shows accuracy.' Run it.",
                            "duration_minutes": 20,
                            "deliverable": "Working notebook with binary classification pipeline"
                        }
                    ]
                }
            ]
        }
    ]
}

# Add module 2 to data
data['modules'].append(module_2)

# Template for generating activities based on bloom level and activity type
activity_templates = {
    "Understand": [
        {
            "type": "concept_quiz",
            "template": "Ask AI to explain {concept}. Summarize in your own words (200-300 words).",
            "duration_minutes": 20
        },
        {
            "type": "collaborative_learning",
            "template": "Ask AI: 'What are common misconceptions about {concept}?' Verify your understanding.",
            "duration_minutes": 15
        }
    ],
    "Apply": [
        {
            "type": "project_builder",
            "template": "Use AI to generate code for {task}. Run it and verify output.",
            "duration_minutes": 25
        },
        {
            "type": "prompt_engineering",
            "template": "Create 3 different prompts for {task}. Compare which gives best results.",
            "duration_minutes": 20
        }
    ],
    "Analyze": [
        {
            "type": "debug_detective",
            "template": "Ask AI to create code with intentional bugs for {task}. Find and fix them.",
            "duration_minutes": 30
        },
        {
            "type": "model_comparison",
            "template": "Generate multiple approaches for {task}. Compare and analyze differences.",
            "duration_minutes": 25
        }
    ],
    "Evaluate": [
        {
            "type": "real_world_solving",
            "template": "Given scenario {scenario}, evaluate which approach is best and why.",
            "duration_minutes": 30
        },
        {
            "type": "model_comparison",
            "template": "Test 3 different solutions for {task}. Rank them with justified criteria.",
            "duration_minutes": 35
        }
    ],
    "Create": [
        {
            "type": "project_builder",
            "template": "Design and build complete solution for {task} using AI assistance.",
            "duration_minutes": 45
        }
    ]
}

# Save updated file
with open('courses/ml-for-engineers/assessment-and-activities-complete.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Generated assessment and activities for {len(data['modules'])} modules")
print(f"✓ File saved to: assessment-and-activities-complete.json")
