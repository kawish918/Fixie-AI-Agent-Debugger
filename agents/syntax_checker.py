# agents/syntax_checker.py

from core.llama_interface import query_llama
import json
import re

class SyntaxChecker:
    def __init__(self, model='llama3.2'):
        self.model = model
    
    def check(self, code: str) -> dict:
        prompt = f"""Analyze this Python code for syntax and runtime errors:

{code}

Respond ONLY with valid JSON:
{{"bug_explanation": "...", "line_number": "...", "severity": "high|medium|low"}}

If no issues found, respond with:
{{"bug_explanation": "No syntax or obvious runtime errors detected", "line_number": "N/A", "severity": "none"}}
"""
        
        response = query_llama(prompt, model=self.model)
        return self._parse_response(response)
    
    def _parse_response(self, response: str) -> dict:
        try:
            return json.loads(response.strip())
        except:
            # Fallback parsing
            return {
                "bug_explanation": "Could not parse syntax check response",
                "line_number": "Unknown",
                "severity": "unknown"
            }