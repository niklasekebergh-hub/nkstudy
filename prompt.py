from openai import OpenAI
import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'design.html')

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/study', methods=['POST'])
def study():
    data = request.get_json(force=True)
    topic = (data.get('topic') or '').strip()
    terms_raw = (data.get('terms') or '').strip()
    mode = (data.get('mode') or 'learn').strip()

    if not topic or not terms_raw:
        return jsonify({"error": "Please provide both topic and terms."}), 400

    terms = [t.strip() for t in terms_raw.split(',') if t.strip()]

    # Build user prompt
    if mode == 'learn':
        user_prompt = (
            f"Create a clear, easy-to-understand study guide for the topic '{topic}'. "
            f"Explain these terms: {', '.join(terms)}. "
            f"For each term, provide a short definition and an example to help the user learn what it means in relation to {topic}."
        )
    elif mode == 'practice':
        user_prompt = (
            f"Create a set of challenging practice questions for the topic '{topic}'. "
            f"Focus on these terms: {', '.join(terms)}. "
            "Each question should test understanding of one or more terms, with short answers provided at the end."
        )
    else:
        user_prompt = "Invalid mode selected."

    # ---- Your fixed try block ----
    try:
        system_msg = (
            "You are a helpful study assistant. "
            "Format all responses in **Markdown**. "
            "Use headings, bullet lists, and bold for key terms. "
            "For math, use LaTeX between $...$ or $$...$$ (e.g., $E=mc^2$ or $$\\frac{a}{b}$$). "
            "For chemical formulas, you may use HTML subscripts/superscripts like H<sub>2</sub>O."
        )

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_prompt}
            ]
        )

        answer = completion.choices[0].message.content
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # pip install flask openai
    # export OPENAI_API_KEY=YOUR_KEY
    # python app.py
    app.run(debug=True)
