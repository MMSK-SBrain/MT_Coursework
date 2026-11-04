#!/usr/bin/env python3
"""
Generate complete assessment criteria and activities for all modules.
Reads learning-outcomes.json and generates matching assessment-and-activities.json
"""

import json

# Load learning outcomes
with open('courses/ml-for-engineers/learning-outcomes.json', 'r') as f:
    outcomes_data = json.load(f)

# Load existing partial assessment file for format reference
with open('courses/ml-for-engineers/assessment-and-activities.json', 'r') as f:
    existing_data = json.load(f)

# Activity type mappings based on Bloom's level
activity_type_map = {
    "Understand": "concept_quiz",
    "Apply": "project_builder",
    "Analyze": "debug_detective",
    "Evaluate": "model_comparison",
    "Create": "project_builder"
}

# Assessment criteria templates
def generate_assessment_criteria(outcome_desc, bloom_level):
    """Generate assessment criteria based on outcome and Bloom level"""
    templates = {
        "Understand": {
            "evidence": f"Written explanation or diagram demonstrating understanding of: {outcome_desc[:50]}...",
            "measurement": "Accuracy of explanation; use of correct terminology; clarity of examples",
            "success_criteria": "Provides accurate explanation with at least 2 relevant examples"
        },
        "Apply": {
            "evidence": f"Working code/implementation demonstrating: {outcome_desc[:50]}...",
            "measurement": "Code executes successfully; produces expected output; follows best practices",
            "success_criteria": "Implementation works correctly; handles basic edge cases; code is documented"
        },
        "Analyze": {
            "evidence": f"Analysis document or comparison showing: {outcome_desc[:50]}...",
            "measurement": "Depth of analysis; identification of patterns/issues; quality of insights",
            "success_criteria": "Identifies key patterns; provides justified conclusions; backs claims with evidence"
        },
        "Evaluate": {
            "evidence": f"Evaluation report with justified recommendations for: {outcome_desc[:50]}...",
            "measurement": "Use of appropriate criteria; justification quality; practical recommendations",
            "success_criteria": "Uses clear evaluation criteria; provides justified ranking; actionable recommendations"
        },
        "Create": {
            "evidence": f"Complete original solution/design for: {outcome_desc[:50]}...",
            "measurement": "Completeness; originality; functionality; documentation quality",
            "success_criteria": "Fully functional solution; well-documented; meets all requirements"
        }
    }
    return templates.get(bloom_level, templates["Apply"])

def generate_activity(outcome_desc, bloom_level, session_title, outcome_code):
    """Generate activity suggestion based on outcome"""
    activity_type = activity_type_map.get(bloom_level, "project_builder")

    # Extract key action from outcome description
    action_word = outcome_desc.split()[0]  # First word (usually the verb)

    activity_templates = {
        "concept_quiz": {
            "title": f"Understanding {session_title}",
            "description": f"Ask an LLM to explain: '{outcome_desc}' Then create a summary in your own words with examples. Verify understanding with follow-up questions.",
            "duration_minutes": 20
        },
        "project_builder": {
            "title": f"Build: {session_title}",
            "description": f"Use AI to generate code that accomplishes: '{outcome_desc}' Run the code, verify it works, and document each major step.",
            "duration_minutes": 30
        },
        "debug_detective": {
            "title": f"Debug Challenge: {session_title}",
            "description": f"Ask AI to create code for '{outcome_desc}' with 2-3 intentional bugs. Find and fix them using AI assistance. Document the debugging process.",
            "duration_minutes": 25
        },
        "model_comparison": {
            "title": f"Compare Approaches: {session_title}",
            "description": f"Generate 2-3 different approaches for: '{outcome_desc}' using AI. Compare them based on performance, complexity, and use cases. Provide recommendation.",
            "duration_minutes": 30
        },
        "code_explanation": {
            "title": f"Code Deep Dive: {session_title}",
            "description": f"Generate code for: '{outcome_desc}' Ask AI to explain it line-by-line. Rephrase explanations in your own words and add detailed comments.",
            "duration_minutes": 25
        },
        "prompt_engineering": {
            "title": f"Prompt Optimization: {session_title}",
            "description": f"Create 3 different prompts to accomplish: '{outcome_desc}' Test each and compare results. Document which prompt worked best and why.",
            "duration_minutes": 20
        },
        "real_world_solving": {
            "title": f"Real-World Application: {session_title}",
            "description": f"Identify a real-world scenario where you would: '{outcome_desc}' Use AI to design and implement a solution. Present your approach.",
            "duration_minutes": 35
        },
        "collaborative_learning": {
            "title": f"Interactive Exploration: {session_title}",
            "description": f"Have an interactive session with AI exploring: '{outcome_desc}' Ask 'what-if' questions, test edge cases, and document insights.",
            "duration_minutes": 20
        }
    }

    template = activity_templates.get(activity_type, activity_templates["project_builder"])

    return {
        "type": activity_type,
        "title": template["title"],
        "description": template["description"],
        "duration_minutes": template["duration_minutes"],
        "deliverable": f"Completed work demonstrating: {outcome_desc[:60]}..."
    }

# Build complete assessment structure
complete_data = {
    "course_code": "ML-ENG",
    "course_title": "Machine Learning for Engineers: The AI-Assisted Approach",
    "assessment_framework": existing_data["assessment_framework"],
    "modules": []
}

# Keep existing modules 0-1 from the partial file
complete_data["modules"] = existing_data["modules"]

# Generate for remaining modules (2-10)
for module in outcomes_data["modules"][2:]:  # Skip modules 0-1 (already done)
    module_assessment = {
        "module_id": module["module_id"],
        "module_number": module["module_number"],
        "title": module["title"],
        "sessions": []
    }

    for session in module["sessions"]:
        session_assessment = {
            "session_id": session["session_id"],
            "title": session["title"],
            "outcomes": []
        }

        for outcome in session["outcomes"]:
            outcome_assessment = {
                "id": outcome["id"],
                "code": outcome["code"],
                "description": outcome["description"],
                "assessment_criteria": generate_assessment_criteria(
                    outcome["description"],
                    outcome["bloom_level"]
                ),
                "activities": [
                    generate_activity(
                        outcome["description"],
                        outcome["bloom_level"],
                        session["title"],
                        outcome["code"]
                    )
                ]
            }
            session_assessment["outcomes"].append(outcome_assessment)

        module_assessment["sessions"].append(session_assessment)

    complete_data["modules"].append(module_assessment)

# Save complete file
output_file = 'courses/ml-for-engineers/assessment-and-activities-COMPLETE.json'
with open(output_file, 'w') as f:
    json.dump(complete_data, f, indent=2)

print(f"✓ Successfully generated complete assessment file!")
print(f"✓ Total modules: {len(complete_data['modules'])}")
print(f"✓ File saved to: {output_file}")

# Generate summary statistics
total_sessions = sum(len(m["sessions"]) for m in complete_data["modules"])
total_outcomes = sum(len(s["outcomes"]) for m in complete_data["modules"] for s in m["sessions"])
total_activities = sum(len(o["activities"]) for m in complete_data["modules"] for s in m["sessions"] for o in s["outcomes"])

print(f"\n📊 Statistics:")
print(f"   - Modules: {len(complete_data['modules'])}")
print(f"   - Sessions: {total_sessions}")
print(f"   - Session Outcomes: {total_outcomes}")
print(f"   - Activities: {total_activities}")
