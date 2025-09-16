# qqqzai – Quick & Quirky AI Chat

A lightweight, **Streamlit‑based** chat UI that lets you talk to an AI model (OpenAI GPT‑3.5, GPT‑4, or your own LLM) with a single click.  
Perfect for quick prototyping, demos, or embedding a conversational agent into your own web page.

> **Live Demo** – Try it out here: <https://qqqzai.streamlit.app/>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Instant chat** | Send messages and receive AI responses in real‑time. |
| **Multiple model support** | Choose from GPT‑3.5‑turbo, GPT‑4, or a custom model via the sidebar. |
| **Conversation history** | Scroll back through the full dialogue; the history is stored only in memory (no DB required). |
| **Simple deployment** | Works out‑of‑the‑box on Streamlit Cloud, Heroku, or any VPS with Python 3.10+. |
| **Extensible** | Plug‑in new LLM providers or add custom logic (e.g., sentiment analysis) by editing a single file. |

---

## 📦 Installation

### Prerequisites

- Python 3.10 or newer
- `pip` (or `pipenv`, `poetry` – any package manager works)

> **Tip:** Use a virtual environment to avoid polluting your global Python installation.

```bash
# Clone the repo
git clone https://github.com/your-username/qqqzai.git
cd qqqzai

# Create a venv (optional but recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
