# 🐍 Snake & Ladder Game

A responsive and interactive **Snake & Ladder web game** developed using **Python Flask, HTML, CSS, and JavaScript** featuring multiple game modes and an interactive 10×10 board.

The project provides a game menu where users can select between different game modes and then play Snake & Ladder on a dynamically generated 10×10 board.

## 📌 Features

* 🎮 **Multiple Game Modes**

  * 1 Player vs Bot
  * 2 Players
  * 3 Players
  * 4 Players
* 🎲 Random dice rolling
* 🐍 Snakes with automatic downward movement
* 🪜 Ladders with automatic upward movement
* 🏆 Automatic winner detection
* 🤖 Basic bot gameplay
* 👥 Multiple player support
* 🎨 Responsive and modern user interface
* 📱 Mobile, tablet, and desktop support
* 🔄 Dynamic board generation using JavaScript
* 🎯 Player tokens with different colors
* 🔗 Game mode selection through URL parameters
* 🔙 Quit-to-menu functionality

## 🛠️ Technologies Used

| Technology   | Purpose                       |
| ------------ | ----------------------------- |
| Python       | Backend programming           |
| Flask        | Web application framework     |
| HTML5        | Webpage structure             |
| CSS3         | Styling and responsive design |
| JavaScript   | Game logic and interactions   |
| Google Fonts | Fredoka and Nunito fonts      |

## 📂 Project Structure

```text
Snake-Ladder/
│
├── app.py
│
└── templates/
    ├── menu.html
    └── index.html
```

### `app.py`

The Flask backend is responsible for starting the web server and rendering the HTML templates.

It provides the following routes:

* `/` → Opens the game menu
* `/index.html` → Opens the Snake & Ladder game
* `/menu.html` → Opens the game menu

### `templates/menu.html`

This page acts as the **main menu**.

Users can select:

* 1 Player vs Bot
* 2 Players
* 3 Players
* 4 Players

The selected game mode is passed to the game page using URL parameters.

Example:

```text
/index.html?players=2&bot=false
```

### `templates/index.html`

This is the main game page.

It contains:

* 10×10 Snake & Ladder board
* Dice
* Player tokens
* Turn management
* Snake and ladder logic
* Bot logic
* Winning condition
* Quit to Menu button

## ⚙️ Game Logic

The board contains numbers from **1 to 100** in a zig-zag pattern.

### 🐍 Snakes

```javascript
const snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
};
```

If a player lands on the head of a snake, the player moves down to the corresponding position.

### 🪜 Ladders

```javascript
const ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
};
```

If a player lands on the bottom of a ladder, the player moves upward to the corresponding position.

## 🎲 Dice System

The dice value is generated randomly between **1 and 6** using JavaScript.

```javascript
const diceValue = Math.floor(Math.random() * 6) + 1;
```

Players move according to the generated dice value.

If a player rolls a **6**, they receive another turn.

## 🤖 Bot Mode

In **1 Player vs Bot** mode, there are two players:

* Player 1
* Bot

The bot automatically rolls the dice after a short delay.

The bot is identified using the URL parameter:

```text
bot=true
```

The bot automatically takes its turn when the current player is the bot.

## 🏆 Winning Condition

A player must reach exactly **position 100** to win.

If the dice roll would move the player beyond 100, the move is not performed.

For example:

```text
Current position = 97
Dice = 5

97 + 5 = 102

Move is not allowed.
```

The player must roll exactly the required number to reach 100.

## 🎨 Player Colors

Each player has a different color:

| Player         | Color  |
| -------------- | ------ |
| Player 1 / Bot | Purple |
| Player 2       | Blue   |
| Player 3       | Green  |
| Player 4       | Orange |

## 🔗 How Game Mode Selection Works

When a user selects a game mode from `menu.html`, the JavaScript function:

```javascript
function selectMode(players, isBot) {
    window.location.href = `index.html?players=${players}&bot=${isBot}`;
}
```

passes the selected settings to `index.html`.

For example:

### 1 Player vs Bot

```text
index.html?players=2&bot=true
```

### 2 Players

```text
index.html?players=2&bot=false
```

### 3 Players

```text
index.html?players=3&bot=false
```

### 4 Players

```text
index.html?players=4&bot=false
```

The game page reads these values using:

```javascript
const urlParams = new URLSearchParams(window.location.search);
const numPlayers = parseInt(urlParams.get('players')) || 2;
const isBotPlaying = urlParams.get('bot') === 'true';
```

## 🚀 Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### 2. Install Flask

Open a terminal in the project directory and run:

```bash
pip install flask
```

### 3. Project Structure

Make sure your files are arranged as:

```text
Snake-Ladder/
│
├── app.py
│
└── templates/
    ├── menu.html
    └── index.html
```

The HTML files must be inside the `templates` folder because Flask uses:

```python
render_template()
```

to load them.

## ▶️ Running the Project

Open the terminal in the project folder.

Run:

```bash
python app.py
```

The Flask server will start on:

```text
http://127.0.0.1:5000
```

Open the address in your browser.

The application starts at:

```text
/
```

which displays the game menu.

## 🌐 Application Flow

```text
                Start Flask Server
                       │
                       ▼
                 Game Menu (/)
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Bot Mode     2 Players    3 Players
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  4 Players
                       │
                       ▼
              Snake & Ladder Game
                       │
                       ▼
                  Roll Dice
                       │
                       ▼
                Move Player
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          Snake?               Ladder?
             │                   │
             ▼                   ▼
        Move Down            Move Up
             │                   │
             └─────────┬─────────┘
                       ▼
                  Check Winner
                       │
                ┌──────┴──────┐
                ▼             ▼
              Yes             No
                │             │
                ▼             ▼
            Game Over      Next Turn
```

## 💻 Flask Backend

The backend is implemented using Flask:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/index.html')
def game():
    return render_template('index.html')

@app.route('/menu.html')
def menu_redirect():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Flask is mainly used for serving the application pages, while the actual game mechanics are handled on the client side using JavaScript.

## 📱 Responsive Design

The interface is designed to work across different screen sizes.

### Mobile

The board and controls are displayed vertically.

### Desktop

The board and controls are displayed side-by-side.

CSS media queries are used to change the layout depending on the screen width.

## 🔮 Future Enhancements

Possible improvements include:

* Online multiplayer
* Player name customization
* Sound effects
* Background music
* Animated dice
* Animated movement between cells
* Better AI for the bot
* Game history
* Score tracking
* Restart Game button
* Difficulty levels
* Leaderboard
* Database integration
* User authentication
* Multiplayer using WebSockets
* Deployment to a cloud platform

## 📄 License

This project is developed for educational and academic purposes.

## 👨‍💻 Author

**Jai Patil**

Bachelor of Engineering – Information Technology
Atharva College of Engineering, Mumbai
