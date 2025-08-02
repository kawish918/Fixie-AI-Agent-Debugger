# core/agent_runner.py      
from agents.syntax_checker import SyntaxChecker
from agents.logic_reasoner import LogicReasoner
from agents.fix_suggester import FixSuggester


def run_agents(code: str):
    checker = SyntaxChecker()
    reasoner = LogicReasoner()
    suggester = FixSuggester()

    syntax_report = checker.check(code)
    logic = reasoner.reason(code)
    fix = suggester.suggest(syntax_report, logic)

    return fix