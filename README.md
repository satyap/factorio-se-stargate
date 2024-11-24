# Factorio 1.1 Space Exploration ending calculations

This repository has **spoilers** for the Space Exploration mod of the game [Factorio](https://www.factorio.com/).

> If you haven't played Factorio, try it! 99.999...% of the game does not require any coding. There is a very good [demo](https://www.factorio.com/download).

This code is for finding a solution to the secret ending of _one_ popular mod of the game. 

I'm _not_ going to explain the solution here, because the community has decided that everyone should have the pleasure of seeking it themselves first.

If you do decide to use this code, read on.

The entry point is [main.py](main.py). It needs numpy for some minor vector calculations and can be refactored to not use such a heavy-weight library.

The code here should first be tailored to your specific coordinates, found from within the game.
The coordinates in the `.ini` files are from my game and will not work for anyone else. You have to find your own coordinates first.
Then you have to refine the coordinates.


You would need to run this code several times, getting successively closer to the solution.
