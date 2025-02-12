from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key


@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            responseCompletion = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "developer", "content": "You are Carl Jung and you are interpreting my dream. Tell me if I didn't provide enough details. Your answer are short and in bullet form. You should return a mix of HTML tags: <p> for paragraphs, <h2> for titles and subtitles and <ul> for lists. Avoid predictable phrasing."},
                          {"role": "user", "content": prompt}],
            )
            result.append(responseCompletion.choices[0].message.content)
            if (prompt != ""):
                responseImg = openai.images.generate(
                    model="dall-e-3",
                    prompt=prompt + ", dream-like, abstract, genderless",
                    style="vivid",
                    size="1024x1024",
                    quality="hd",
                    n=1,
                )
                result.append(responseImg.data[0].url)
            else:
                result.append("No image generated")
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
