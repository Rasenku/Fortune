import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/fortune')
def index():
    return render_template('fortune_form.html')


@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = requests.args.get('Naruto')
    # ... etc

    if users_favorite_animal == 'unicorn':
        print ("You'll have a magical day!")
    elif users_favorite_animal == 'bear':
        print("Your future is fish")
    elif users_favorite_animal == 'toad':
        print("Something sticky")
    else:
        print("no other fortune applies, return default fortune")
    return render_template('fortune_results.html')
