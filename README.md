# NKSTUDY — AI Study Tool (Flask + HTML)

An **AI-powered study assistant** that turns user input into either a **study guide** or **practice questions** using OpenAI’s API and the `gpt-4o-mini` model.

**Created by Niklas Ekebergh.** © 2025 Niklas — Licensed under the [MIT License](./LICENSE).

---

##  Features
- Two modes:  
  - **Study Guide** — Generates structured summaries with definitions and examples.  
  - **Practice Questions** — Creates short-answer questions based on the provided terms.
- Clean and responsive HTML frontend.
- Smooth loading animation and transitions.
- Markdown, LaTeX, and sanitized HTML support in output.
- Flask backend for OpenAI API communication.

---

##  Tech Stack
| Layer | Tools |
| **Frontend** | HTML, CSS, JS (with [Marked.js](https://marked.js.org/), [DOMPurify](https://github.com/cure53/DOMPurify), [MathJax](https://www.mathjax.org/)) |
| **Backend** | Python, Flask |
| **AI Model** | OpenAI `gpt-4o-mini` |

---

##  Usage
**1. Install Dependencies**
  ```bash
   pip install flask openai python-dotenv
```

**2. Create .env file in project root and add:**
  `OPENAI_API_KEY="your_openai_key_here"`

**3. Run flask app python Prompt.py and open browser at *http://127.0.0.1:(Port)***
