from flask import Flask, render_template, request

app = Flask(__name__)

artworks = [
    {"id": 1, "title": "Sunset Dreams", "image": "art1.jpeg"},
    {"id": 2, "title": "Urban Vibes", "image": "art2.jpg"},
    {"id": 3, "title": "Golden Silence", "image": "art3.jpg"},
    {"id": 4, "title": "Abstract Rhythm", "image": "art4.jpg"},
    {"id": 5, "title": "Mystic Forest", "image": "art5.jpg"}
]

@app.route('/')
def index():
    return render_template('rate.html', artworks=artworks)  # 🛠️ Fixed

@app.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'POST':
        responses = []
        for art in artworks:
            rating = request.form.get(f"rating_{art['id']}")
            feedback = request.form.get(f"feedback_{art['id']}")
            responses.append({
                "title": art['title'],
                "image": art['image'],
                "rating": rating,
                "feedback": feedback
            })
        return render_template('thank_you.html', responses=responses)
    return render_template('rate.html', artworks=artworks)

if __name__ == '__main__':
    app.run(debug=True)
