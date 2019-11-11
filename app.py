from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fortune')
def fortune_form():
    return render_template('fortune_form.html')


@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    anime = request.args.get("anime")
    # ... etc
    fortune = " "
    if anime == 'Naruto':
        fortune = "You'll have a magical day!"
    elif anime == 'One Piece':
        fortune = "Your super power will be Teleportation"
    elif anime == 'Angel Beats':
        fortune = "You will be very rich"
    else:
        fortune = "no other fortune applies, return default fortune"
    return render_template('fortune_results.html', fortune=fortune)
