from flask import Flask, render_template, request, redirect, url_for, session
import random
import json

app = Flask(__name__)
app.secret_key = 'BigChungus'

# Load abilities from JSON file
with open('abilities.json') as f:
    abilities = json.load(f)

# Initialize vote counts
def initialize_votes():
    return {ability['name']: 0 for ability in abilities}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'votes' not in session:
        session['votes'] = initialize_votes()

    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'stop':
            save_votes()
            return redirect(url_for('results'))

        item_chosen = request.form[choice]
        session['votes'][item_chosen] += 1
        session.modified = True

        ability1, ability2 = random.sample(abilities, 2)
        return render_template('index.html', ability1=ability1, ability2=ability2)

    ability1, ability2 = random.sample(abilities, 2)
    return render_template('index.html', ability1=ability1, ability2=ability2)

@app.route('/results')
def results():
    save_votes()
    return render_template('results.html', votes=session['votes'])

def save_votes():
    with open('votes.json', 'w') as f:
        json.dump(session['votes'], f)

if __name__ == '__main__':
    app.run()
