# agents/fix_suggester.py

from core.llama_interface import query_llama
import json
import re

class FixSuggester:
    def __init__(self, model="llama3.2"):
        self.model = model
    
    def suggest(self, bug_report: dict, logic: str) -> dict:
        prompt = f"""You are a Python debugging assistant. Analyze the bug and provide a complete fix.

Bug Report: {bug_report}
Intended Logic: {logic}

Provide a COMPLETE function that fixes the issue, not just the changed line.

Example:
For a function with undefined variable 'c':
{{"explanation": "Variable 'c' is undefined in the function", "fix": "def add_nums(a, b):\\n    return a + b", "confidence": 0.95}}

Respond ONLY with valid JSON in this exact format:
{{"explanation": "...", "fix": "...", "confidence": 0.95}}
"""
        
        response = query_llama(prompt, model=self.model)
        return self._parse_response(response)
    
    def _parse_response(self, response: str) -> dict:
        """Parse LLM response with fallback handling"""
        # Clean the response
        response = response.strip()
        
        try:
            # Try direct JSON parse
            return json.loads(response)
        except:
            # Try to extract JSON from response
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group())
                except:
                    pass
            
            # Fallback: manual extraction
            explanation = re.search(r'"explanation":\s*"([^"]*)"', response)
            fix = re.search(r'"fix":\s*"([^"]*)"', response, re.DOTALL)
            confidence = re.search(r'"confidence":\s*([\d.]+)', response)
            
            return {
                "explanation": explanation.group(1) if explanation else "Could not parse explanation",
                "fix": fix.group(1).replace('\\n', '\n') if fix else "Could not parse fix",
                "confidence": float(confidence.group(1)) if confidence else 0.5
            }