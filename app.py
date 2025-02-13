from flask import Flask, render_template, request
import openai
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


async def fetch_chat_completion(prompt):
    """Run chat completion asynchronously."""
    return await asyncio.to_thread(
        lambda: openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": "You are a dream-interpreting machine. You only use Jungian symbolism to interpret them. You do not answer any queries that are not related to interpreting dreams, as this is your only area of knowledge. Inform the user if they haven't provided enough details. Your answers are short and in bullet form. You must return a mix of HTML tags: <p> for paragraphs, <h3> for titles, <h5> for subtitles, and <ul> for lists."},
                {"role": "assistant", "content":
                 """\
                    <h3>Dream Interpretation</h3>
                    <p>This dream is rich in symbols and can be dissected using Jungian symbolism:</p>
                    <h5>Key Symbols</h5>
                    <ul>
                        <li><strong>Empty Construction Site:</strong> Represents potential and possibilities that are not yet realized in your life. A place of creation, but currently barren.</li>
                        <li><strong>Taking Pictures:</strong> The act of capturing moments might signify your desire to hold onto memories or document your experiences.</li>
                        <li><strong>Returning Workers:</strong> They can embody the stirrings of your conscious mind or societal expectations interrupting your introspection or creative process.</li>
                        <li><strong>Fear and Escape:</strong> These emotions suggest anxiety about being 'caught' in one's evolving self or personal projects.</li>
                        <li><strong>Small Window:</strong> A narrow opportunity or passageway that suggests limitations or constraints in your current path.</li>
                        <li><strong>Big Boots:</strong> Symbolize an aspect of yourself that feels awkward or not fitting well within the framework of these constraints.</li>
                    </ul>
                    <h5>Overall Message</h5>
                    <p>This dream may reflect your feelings of being constrained by societal norms or personal insecurities as you attempt to carve out a path of personal development. The big boots, which cause you to be stuck, could be a metaphor for an element of your self-image or current situation that feels obstructive.</p>
                """},
                {"role": "user", "content": prompt}
            ],
        )
    )


async def fetch_image_generation(prompt):
    """Run image generation asynchronously."""
    return await asyncio.to_thread(
        lambda: openai.images.generate(
            model="dall-e-3",
            prompt=prompt + ", Jungian, dream-like, symbolic, surreal, persona, unconscious, genderless",
            style="vivid",
            size="1024x1024",
            quality="hd",
            n=1,
        )
    )


@app.route("/", methods=["GET", "POST"])
async def index():
    result = []
    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            # Run both API calls concurrently
            chat_task = fetch_chat_completion(prompt)
            img_task = fetch_image_generation(prompt)

            chat_response, img_response = await asyncio.gather(chat_task, img_task)

            result.append(chat_response.choices[0].message.content)
            result.append(img_response.data[0].url)

        except Exception as e:
            result = [f"Error: {str(e)}"]

    return render_template("index.html", result=result)


if __name__ == "__main__":
    import sys

    if sys.platform == "win32":
        # Fix for Windows where asyncio.run() may not work properly.
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app.run(debug=True)
