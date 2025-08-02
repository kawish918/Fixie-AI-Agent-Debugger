# core/langgraph_runner.py

from typing import Dict, List, TypedDict, Optional, Any

class FixieState(TypedDict):
    code: str
    syntax_report: Optional[str]
    logic: Optional[str]
    fix: Optional[str]
    error: Optional[str]
    context: Optional[List[str]] # Add conversation history
    confidence_scores: Optional[Dict[str, float]] # Track agent confidence


# Create Nodes

from langgraph.graph import StateGraph
from langgraph.pregel import Pregel

from agents.syntax_checker import SyntaxChecker
from agents.logic_reasoner import LogicReasoner
from agents.fix_suggester import FixSuggester



checker = SyntaxChecker()
reasoner = LogicReasoner()
fixer = FixSuggester()

def syntax_node(state: FixieState) -> FixieState:
    report = checker.check(state["code"])
    return {**state, "syntax_report": report}

def logic_node(state: FixieState) -> FixieState:
    logic = reasoner.reason(state["code"])
    return {**state, "logic": logic}

def fix_node(state: FixieState) -> FixieState:
    fix = fixer.suggest(state["syntax_report"], state["logic"])
    return {**state, "fix": fix}


def should_retry(state: FixieState) -> str:
    """Decide whether to retry or finish"""
    validation = state.get("validation_result", {})
    iteration = state.get("iteration_count", 0)
    
    if validation.get("valid", False) or iteration >= 3:
        return "END"
    return "RetryFix"

# Create Graph

def build_fixie_graph():

    builder = StateGraph(FixieState)

    # Add all nodes
    builder.add_node("SyntaxChecker", syntax_node)
    builder.add_node("LogicReasoner", logic_node)
    builder.add_node("FixSuggester", fix_node)

    # Set entry point
    builder.set_entry_point("SyntaxChecker")

    # Add edges
    builder.add_edge("SyntaxChecker", "LogicReasoner")
    builder.add_edge("LogicReasoner", "FixSuggester")
    builder.add_edge("FixSuggester", "__end__")


    return builder.compile()
# Run Graph

def run_fixie_graph(code: str):
    graph = build_fixie_graph()
    result = graph.invoke({"code": code})
    return result