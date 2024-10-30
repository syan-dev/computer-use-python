# CUPI (Computer Use Python Installer)

[![PyPI version](https://badge.fury.io/py/cupi.svg)](https://badge.fury.io/py/cupi)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

CUPI (Computer Use Python Installer) enables seamless integration of Claude AI's computer control capabilities without the need for Docker or virtual machines. Run Claude AI directly on your native operating system with just Python.

## ✨ Features

- 🚀 Native OS support (Windows, MacOS, Linux)
- 💻 Direct system control through Claude AI
- 📝 Automatic conversation logging
- 🖼️ Screenshot capabilities
- 🔍 Web browsing and research
- 📂 File system operations

## 🔧 Prerequisites

- Python 3.6 or higher
- Claude AI API key
- System permissions for computer control

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install cupi
```

### From Source

```bash
git clone https://github.com/syan-dev/computer-use-python-installer
cd computer-use-python-installer
pip install .
```

## 🚀 Quick Start

1. Set your API key:

```bash
# Linux/MacOS
export ANTHROPIC_API_KEY=your_api_key_here

# Windows (CMD)
set ANTHROPIC_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your_api_key_here"
```

2. Run CUPI:

```bash
cupi "Take a screenshot of this window"
```

## 💡 Example Use Cases

```bash
# Web Research
cupi "Find the cheapest flights from Vietnam to France"

# System Operations
cupi "Create a new folder named 'projects' and open VS Code there"

# File Management
cupi "Organize my Downloads folder by file type"

# Web Browsing
cupi "Search for recent news about artificial intelligence"
```

## 🛠️ Advanced Usage

### Custom Configuration

```bash
# Set custom log directory
cupi "Take a screenshot" --log-dir "my_logs"

# Use different Claude model
cupi "Browse the web" --model "claude-3-opus"

# Enable verbose output
cupi "Create a file" --verbose
```

### Available Options

```
--model, -m        Choose Claude model (default: claude-3-5-sonnet)
--log-dir, -l      Set log directory (default: ./logs)
--verbose, -v      Enable detailed output
--max-tokens       Set maximum response tokens
--recent-images    Control number of cached images
```

## 📝 Logging

CUPI automatically logs all interactions, including:
- Conversations with Claude
- Screenshots taken
- System operations performed
- Error messages

Logs are stored in JSON format at `./logs` by default.

## 🔒 Security Notes

- CUPI requires system permissions to control your computer
- API keys should be kept secure and never shared
- Review Claude's actions before confirming sensitive operations
- Use environment variables for API keys, never hardcode them

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) for Claude AI
- All contributors and users of CUPI
- The Python community

## 📫 Support

- 📚 [Documentation](https://github.com/syan-dev/computer-use-python-installer/wiki)
- 🐛 [Issue Tracker](https://github.com/syan-dev/computer-use-python-installer/issues)
- 💬 [Discussions](https://github.com/syan-dev/computer-use-python-installer/discussions)

