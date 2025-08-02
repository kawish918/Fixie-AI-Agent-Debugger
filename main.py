# main.py

from core.input_handler import read_python_file
from core.langgraph_runner import run_fixie_graph
import json

if __name__ == "__main__":
    code = read_python_file('examples/buggy_code.py')
    
    print("\n--- Fixie AI Debugger ---\n")
    print(f"Original Code:\n{code}\n")
    
    result = run_fixie_graph(code)
    
    # Clean output with line numbers
    syntax_report = result.get("syntax_report", {})
    fix = result.get("fix", {})
    
    print("🔍 Debug Results:")
    print("=" * 50)
    
    # Show syntax issues
    if syntax_report:
        bug_explanation = syntax_report.get("bug_explanation", "N/A")
        line_number = syntax_report.get("line_number", "N/A")
        severity = syntax_report.get("severity", "N/A")
        
        print(f"🐛 Bug Found: {bug_explanation}")
        print(f"📍 Line Number: {line_number}")
        print(f"⚠️  Severity: {severity.upper()}")
        print("-" * 50)
    
    # Show fix
    if fix and isinstance(fix, dict):
        print(f"📊 Fix Confidence: {fix.get('confidence', 'N/A')}")
        print(f"💡 Explanation: {fix.get('explanation', 'N/A')}")
        print(f"\n🔧 Suggested Fix:\n{fix.get('fix', 'N/A')}")
    else:
        print("❌ No fix could be generated")
        print(f"Raw result: {result}")