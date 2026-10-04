from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the main menu of the game
@app.route('/')
def home():
    return render_template('menu.html')

# Route for loading the Snake & Ladder game
@app.route('/index.html')
def game():
    return render_template('index.html')

@app.route('/menu.html')
def menu_redirect():
    return render_template('menu.html')

# Start the Flask development server when this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
