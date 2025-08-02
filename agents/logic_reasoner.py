# agents/logic_reasoner.py
from core.llama_interface import query_llama

class LogicReasoner:
    def __init__(self, model='llama3.2'):
        self.model = model
    
    def reason(self, code: str) -> str:
        prompt = f"""You are a Python logic explainer. Read the following function and explain 
        in simple terms what it is supposed to do:
        
        {code}
        Respond with only:
        - intended Logic:
        """
        return query_llama(prompt, model=self.model)