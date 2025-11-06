from flask import Flask, render_template, request

app = Flask(__name__)


SUGGESTIONS = {
    "Happy": {
        "text": "'Happy' by Pharrell Williams — keep the vibes going!",
        "link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    },
    "Sad": {
        "text": "'Fix You' by Coldplay might cheer you up.",
        "link": "https://www.youtube.com/watch?v=k4V3Mo61fJM"
    },
    "Angry": {
        "text": "'Lose Yourself' by Eminem — channel that energy.",
        "link": "https://www.youtube.com/watch?v=_JZom_gVfuw"
    },
    "Romantic": {
        "text": "'Perfect' by Ed Sheeran is a sweet pick.",
        "link": "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
    },
}


@app.route("/")
def index():
    mood = request.args.get("mood", "").strip()
    suggestion = SUGGESTIONS.get(mood) if mood else None
    return render_template("index.html", mood=mood, suggestion=suggestion)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500, debug=True)


