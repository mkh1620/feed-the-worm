# Feed the Worm - README

## Overview

Feed the Worm is a classic Snake game implemented using Pygame, a set of Python modules designed for writing video games. In this game, you control a worm that grows longer as it eats apples. The objective is to eat as many apples as possible without colliding with the walls or the worm's own body.

## Features

- **Classic Snake Gameplay**: Navigate the worm to eat apples and grow longer.
- **Game Over Screen**: Displays "Game Over" with options to play again or quit.
- **Score Display**: Shows the player's current score.
- **Sound Effects**: Includes a sound effect when the worm eats an apple.
- **Graphical Elements**: Custom graphics for the worm's head, body, and tail.


 **Download the Project**: Clone or download the project files from the repository.

## Usage

1. **Navigate to the Project Directory**: Open your terminal or command prompt and change to the directory where the project files are located.

2. **Run the Game**: Execute the Python script to start the game:
    ```bash
    python thegame1.py
    ```

3. **Controls**:
    - Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to control the direction of the worm.

## Project Structure

- `thegame1.py`: Main script that contains the game logic and execution.
- `graphics/`: Directory containing images for the worm and apple.
- `sound/`: Directory containing sound effects.
- `font/`: Directory containing font files used for text rendering.
- `assets/`: Directory containing additional assets like background images and buttons.

## Game Logic

- **Worm Movement**: The worm moves in the direction indicated by the arrow keys. Each time it eats an apple, a new segment is added to its body.
- **Collision Detection**: The game checks for collisions with the walls and the worm's own body. If a collision is detected, the game is over.
- **Fruit Positioning**: The apple randomly appears on the grid. If the apple's new position overlaps with the worm's body, it is repositioned.

## Customization

- **Graphics**: You can customize the worm and apple images by replacing the files in the `graphics/` directory.
- **Sound**: Change the sound effect by replacing the file in the `sound/` directory.
- **Speed**: Modify the game speed by changing the timer interval in the main game loop:
    ```python
    pygame.time.set_timer(SCREEN_UPDATE, 150)  # Lower value for faster game, higher for slower
    ```

## License

This project is open source and available under the MIT License. Feel free to modify and distribute as per the license terms.

## Acknowledgments

- Thanks to the Pygame community for providing tutorials and resources.
- Special thanks to the creators of the assets used in the game.

## Contact

For any questions or suggestions, please reach out to [herzallahmkh1620@gmail.com].

Enjoy the game!
