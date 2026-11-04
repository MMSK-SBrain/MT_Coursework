"""
Response Generator Module
=========================

Handles response generation for the chatbot based on predicted intents.
Supports template-based responses with random selection.
"""

import random
import json
from typing import Dict, List, Optional


class ResponseGenerator:
    """
    Generates appropriate responses based on predicted intent.
    
    Attributes:
        intents (Dict): Mapping of intent tags to response templates
        fallback_response (str): Default response for unknown intents
    """
    
    def __init__(self, intents_file: str = 'intents.json'):
        """
        Initialize the response generator.
        
        Args:
            intents_file (str): Path to intents JSON file
        """
        self.intents = {}
        self.fallback_response = (
            "I'm not quite sure how to help with that. "
            "Could you rephrase your question or try asking something else?"
        )
        self._load_intents(intents_file)
    
    def _load_intents(self, intents_file: str):
        """Load intents from JSON file."""
        try:
            with open(intents_file, 'r') as f:
                data = json.load(f)
                for intent in data['intents']:
                    self.intents[intent['tag']] = intent['responses']
        except FileNotFoundError:
            print(f"Warning: {intents_file} not found. Using empty intent mapping.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {intents_file}")
    
    def generate(self, intent: str, confidence: float = 1.0) -> str:
        """
        Generate response for given intent.
        
        Args:
            intent (str): Predicted intent tag
            confidence (float): Prediction confidence (0-1)
        
        Returns:
            str: Generated response
        """
        # If confidence is very low, use fallback
        if confidence < 0.3:
            return self.fallback_response
        
        # Get responses for intent
        if intent in self.intents:
            response = random.choice(self.intents[intent])
            
            # For medium confidence, add qualifier
            if confidence < 0.7:
                response = f"I think you're asking about {intent}. {response}"
            
            return response
        else:
            return self.fallback_response
    
    def get_all_intents(self) -> List[str]:
        """Get list of all supported intents."""
        return list(self.intents.keys())
    
    def add_intent(self, tag: str, responses: List[str]):
        """
        Add new intent dynamically.
        
        Args:
            tag (str): Intent tag
            responses (List[str]): List of response templates
        """
        self.intents[tag] = responses
    
    def __repr__(self):
        return f"ResponseGenerator(intents={len(self.intents)})"


# Example usage
if __name__ == "__main__":
    generator = ResponseGenerator()
    
    print(f"Loaded {len(generator.get_all_intents())} intents")
    print("\nSupported intents:")
    for intent in generator.get_all_intents():
        print(f"  • {intent}")
    
    # Test responses
    print("\nExample responses:")
    test_intents = ['greeting', 'check_order', 'thanks', 'goodbye']
    for intent in test_intents:
        response = generator.generate(intent, confidence=0.95)
        print(f"\n{intent}: {response}")
