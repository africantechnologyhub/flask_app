from flask install Flask

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>hello</h1>'

if__name__ = "__main__":
    app.run()
