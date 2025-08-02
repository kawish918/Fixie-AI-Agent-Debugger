# 🔧 Fixie: AI Agent Debugger

An intelligent Python debugging assistant powered by AI agents using LangChain and Ollama Llama 3.2. Fixie automatically detects bugs, analyzes code logic, and suggests fixes through a coordinated multi-agent workflow.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-orange.svg)

## ✨ Features

- 🤖 **Multi-Agent Architecture**: Specialized agents for syntax checking, logic reasoning, and fix suggestions
- 🔍 **Intelligent Bug Detection**: Identifies syntax errors, runtime issues, and logic problems
- 📍 **Line-by-Line Analysis**: Pinpoints exact locations of bugs with line numbers
- 🎯 **Confidence Scoring**: Provides confidence levels for suggested fixes
- 🔄 **LangGraph Workflow**: Orchestrated agent coordination using LangGraph
- 🦙 **Local AI**: Powered by Ollama Llama 3.2 for privacy and offline usage

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Ollama installed and running
- Git (for cloning)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kawish918/Fixie-AI-Agent-Debugger.git
   cd fixie-ai-debugger
   ```

2. **Create virtual environment**
   ```bash
   python -m venv fixie
   fixie\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install langchain langgraph
   ```

4. **Install and setup Ollama**
   
   Visit [Ollama's official website](https://ollama.ai) for installation instructions, or:
   
   **Windows/Mac/Linux:**
   ```bash
   # Download from: https://ollama.ai/download
   # Then pull the Llama model:
   ollama pull llama3.2
   ```

5. **Verify Ollama is running**
   ```bash
   ollama list
   # Should show llama3.2 in the list
   ```

### Usage

1. **Run on the example buggy code**
   ```bash
   python main.py
   ```

2. **Add your own buggy Python files**
   ```bash
   # Place your .py file in the examples/ directory
   # Update main.py to point to your file:
   code = read_python_file('examples/your_buggy_file.py')
   ```

## 📁 Project Structure

```
fixie-ai-debugger/
├── agents/
│   ├── fix_suggester.py      # AI agent for generating fixes
│   ├── logic_reasoner.py     # AI agent for understanding code logic
│   └── syntax_checker.py     # AI agent for detecting syntax errors
├── core/
│   ├── agent_runner.py       # Simple agent orchestration
│   ├── input_handler.py      # File reading utilities
│   ├── langgraph_runner.py   # LangGraph workflow management
│   └── llama_interface.py    # Ollama API interface
├── examples/
│   └── buggy_code.py         # Sample buggy code for testing
├── main.py                   # Main application entry point
└── README.md
```

## 🔄 How It Works

Fixie uses a coordinated multi-agent workflow:

1. **Syntax Checker Agent** 🔍
   - Analyzes code for syntax and runtime errors
   - Identifies problematic lines and severity levels

2. **Logic Reasoner Agent** 🧠
   - Understands the intended purpose of the code
   - Provides context for fix generation

3. **Fix Suggester Agent** 🛠️
   - Combines bug report and logic analysis
   - Generates complete, executable fix suggestions
   - Provides confidence scores

4. **LangGraph Orchestration** 🔄
   - Manages agent workflow and data flow
   - Ensures proper sequencing and state management

## 📊 Example Output

```
--- Fixie AI Debugger ---

Original Code:
def add_nums(a, b):
    return a + b + c

🔍 Debug Results:
==================================================
🐛 Bug Found: NameError - variable 'c' is not defined
📍 Line Number: 2
⚠️  Severity: HIGH
--------------------------------------------------
📊 Fix Confidence: 0.95
💡 Explanation: Variable 'c' is undefined in the function
🔧 Suggested Fix:
def add_nums(a, b):
    return a + b
```

## ⚙️ Configuration

### Using Different Models

Update the model in any agent:

```python
# In agents/fix_suggester.py
class FixSuggester:
    def __init__(self, model="llama3.2"):  # Change model here
        self.model = model
```

### Customizing Prompts

Modify prompts in each agent class to suit your debugging needs:

```python
# In agents/syntax_checker.py
def check(self, code: str) -> dict:
    prompt = f"""Your custom prompt here..."""
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Future Enhancements

- [ ] Support for multiple programming languages
- [ ] Integration with popular IDEs
- [ ] Web interface for easier usage
- [ ] Code execution validation
- [ ] Integration with static analysis tools
- [ ] Custom rule definitions
- [ ] Batch processing of multiple files

## 🔧 Troubleshooting

### Common Issues

**Ollama not found:**
```bash
# Make sure Ollama is installed and in PATH
ollama --version
```

**Model not available:**
```bash
# Pull the required model
ollama pull llama3.2
```

**LangChain import errors:**
```bash
# Install missing dependencies
pip install langchain langgraph
```

**Permission errors on Windows:**
```bash
# Run as administrator or check antivirus settings
```

## 📚 Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Ollama Documentation](https://ollama.ai/docs)
- [Llama 3.2 Model Card](https://ollama.ai/library/llama3.2)
- [Get LangSmith API Key](https://docs.smith.langchain.com/administration/how_to_guides/organization_management/create_account_api_key)
- [LangGraph Local Server](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- [LangChain](https://langchain.com/) for the agent framework
- [Ollama](https://ollama.ai/) for local AI model hosting
- [Meta](https://ai.meta.com/) for the Llama 3.2 model

---

*Star ⭐ this repo if you find it helpful!*
