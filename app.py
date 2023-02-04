from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def show_form():
    prompts = story.prompts
    return render_template('home.html', prompts = prompts)

@app.route('/story')
def generate_story():
    madlib = story.generate(request.args)
    return render_template('madlib.html', madlib=madlib)