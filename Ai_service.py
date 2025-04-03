from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyAxEoutxU_w1OamJUe4FMOzr5ZdUyz8R4k")

model = genai.GenerativeModel("gemini-1.5-flash-latest")

@app.route('/generate', methods=['POST'])
def generate_survey():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = model.generate_content(f"Generate 20 survey questions about {prompt}")
        questions = response.text.strip().split("\n")

        return jsonify({"questions": questions})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
