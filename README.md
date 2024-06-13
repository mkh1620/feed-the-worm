<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feed the Worm - README</title>
    <style>
      body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2, h3, h4, h5, h6 {
    color: #333;
}

h1 {
    text-align: center;
    color: #4CAF50;
}

section {
    margin-bottom: 20px;
}

ul, ol {
    padding-left: 20px;
}

pre {
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
}

code {
    font-family: "Courier New", Courier, monospace;
    color: #c7254e;
}

footer {
    text-align: center;
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #e4e4e4;
}

a {
    color: #4CAF50;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

    </style>
</head>
<body>
    <div class="container">
        <h1>Feed the Worm - README</h1>
        
        <section>
            <h2>Overview</h2>
            <p>Feed the Worm is a classic Snake game implemented using Pygame, a set of Python modules designed for writing video games. In this game, you control a worm that grows longer as it eats apples. The objective is to eat as many apples as possible without colliding with the walls or the worm's own body.</p>
        </section>
        
        <section>
            <h2>Features</h2>
            <ul>
                <li>Classic Snake Gameplay: Navigate the worm to eat apples and grow longer.</li>
                <li>Game Over Screen: Displays "Game Over" with options to play again or quit.</li>
                <li>Score Display: Shows the player's current score.</li>
                <li>Sound Effects: Includes a sound effect when the worm eats an apple.</li>
                <li>Graphical Elements: Custom graphics for the worm's head, body, and tail.</li>
            </ul>
        </section>
        
        <section>
            <h2>Requirements</h2>
            <ul>
                <li>Python 3.x</li>
                <li>Pygame library</li>
            </ul>
        </section>
        
        <section>
            <h2>Installation</h2>
            <ol>
                <li><strong>Install Python</strong>: Make sure you have Python 3.x installed. You can download it from <a href="https://www.python.org/" target="_blank">python.org</a>.</li>
                <li><strong>Install Pygame</strong>: Install the Pygame library using pip:
                    <pre><code>pip install pygame</code></pre>
                </li>
                <li><strong>Download the Project</strong>: Clone or download the project files from the repository.</li>
            </ol>
        </section>
        
        <section>
            <h2>Usage</h2>
            <ol>
                <li><strong>Navigate to the Project Directory</strong>: Open your terminal or command prompt and change to the directory where the project files are located.</li>
                <li><strong>Run the Game</strong>: Execute the Python script to start the game:
                    <pre><code>python thegame1.py</code></pre>
                </li>
                <li><strong>Controls</strong>:
                    <ul>
                        <li>Use the arrow keys (<strong>Up, Down, Left, Right</strong>) to control the direction of the worm.</li>
                    </ul>
                </li>
            </ol>
        </section>
        
        <section>
            <h2>Project Structure</h2>
            <ul>
                <li><strong>thegame1.py</strong>: Main script that contains the game logic and execution.</li>
                <li><strong>graphics/</strong>: Directory containing images for the worm and apple.</li>
                <li><strong>sound/</strong>: Directory containing sound effects.</li>
                <li><strong>font/</strong>: Directory containing font files used for text rendering.</li>
                <li><strong>assets/</strong>: Directory containing additional assets like background images and buttons.</li>
            </ul>
        </section>
        
        <section>
            <h2>Game Logic</h2>
            <ul>
                <li><strong>Worm Movement</strong>: The worm moves in the direction indicated by the arrow keys. Each time it eats an apple, a new segment is added to its body.</li>
                <li><strong>Collision Detection</strong>: The game checks for collisions with the walls and the worm's own body. If a collision is detected, the game is over.</li>
                <li><strong>Fruit Positioning</strong>: The apple randomly appears on the grid. If the apple's new position overlaps with the worm's body, it is repositioned.</li>
            </ul>
        </section>
        
        <section>
            <h2>Customization</h2>
            <ul>
                <li><strong>Graphics</strong>: You can customize the worm and apple images by replacing the files in the <strong>graphics/</strong> directory.</li>
                <li><strong>Sound</strong>: Change the sound effect by replacing the file in the <strong>sound/</strong> directory.</li>
                <li><strong>Speed</strong>: Modify the game speed by changing the timer interval in the main game loop:
                    <pre><code>pygame.time.set_timer(SCREEN_UPDATE, 150)  # Lower value for faster game, higher for slower</code></pre>
                </li>
            </ul>
        </section>
        
        <section>
            <h2>License</h2>
            <p>This project is open source and available under the MIT License. Feel free to modify and distribute as per the license terms.</p>
        </section>
        
        <section>
            <h2>Acknowledgments</h2>
            <ul>
                <li>Thanks to the Pygame community for providing tutorials and resources.</li>
                <li>Special thanks to the creators of the assets used in the game.</li>
            </ul>
        </section>
        
        <section>
            <h2>Contact</h2>
            <p>For any questions or suggestions, please reach out to [Your Email] or open an issue on the project repository.</p>
        </section>
        
        <footer>
            <p>Enjoy the game!</p>
        </footer>
    </div>
</body>
</html>
