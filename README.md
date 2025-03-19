# Artificial-Intelligence-Assignment
Tic-Tac-Toe Game (Minimax AI)

ScreenShots

![Screenshot 2025-03-19 175903](https://github.com/user-attachments/assets/aae8ba45-1407-4c6c-94f7-45ef6afdcd87)

![Screenshot 2025-03-19 181231](https://github.com/user-attachments/assets/c7ab2d91-21a6-43d6-9a83-713978f52433)

This repository contains a Tic-Tac-Toe game in Python featuring:

- A human player vs. an AI player
- The AI makes optimal moves using the Minimax algorithm
- A graphical interface built with pygame

Repository Contents

tictactoe.py

Contains the core game logic including:

- Board representation and initialization
- Functions to determine the current player (player)
- Finding available actions (actions)
- Generating the result of a move (result)
- Checking for a winner (winner)
- Determining terminal states (terminal)
- Evaluating board utility (utility) -The Minimax algorithm and its helper functions (minimax, max_value, min_value)

runner.py

Contains the pygame graphical interface that:

- Draws the Tic-Tac-Toe board
- Handles user clicks and updates the game state
- Integrates with tictactoe.py to process moves requirements.txt
- Lists the required Python packages (e.g., pygame) for running the project.

How to Run the Game

1- Install Python 3.x (if not already installed) from python.org.

2- Clone or Download the Repository:

git clone https://github.com/YourUsername/Artificial-Intelligence-Assignments.git

3- Navigate to the Project Directory:

cd Artificial-Intelligence-Assignments

4- Install Dependencies:

pip install -r requirements.txt

5- Run the Game:

python runner.py A pygame window should open where you can play Tic-Tac-Toe against the AI.
