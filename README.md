# Factorio 1.1 Space Exploration ending calculations

This repository has near-complete spoilers for the Space Exploration mod of the game [Factorio](https://www.factorio.com/).

The code here should first be tailored to your specific coordinates, found from within the game.
The coordinates in the `.ini` files are from my game and will not work for anyone else. You have to find your own coordinates first.
Then you have to repeatedly do an eight-step process to refine the coordinates.

I'm _not_ going to explain the solution here.

The entry point is [main.py](main.py). It needs numpy for some minor vector calculations and can be refactored to not use such a heavy-weight library.

You would need to run it several times, getting successively closer to the solution.
