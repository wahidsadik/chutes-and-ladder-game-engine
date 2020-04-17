[![Build Status](https://travis-ci.org/wahidsadik/chutes-and-ladder-game-engine.svg?branch=master)](https://travis-ci.org/wahidsadik/chutes-and-ladder-game-engine)
[![Coverage Status](https://coveralls.io/repos/github/wahidsadik/chutes-and-ladder-game-engine/badge.svg?branch=master)](https://coveralls.io/github/wahidsadik/chutes-and-ladder-game-engine?branch=master)

# About

This repo is for a simple game-engine for *chutes-and-ladders* game. While playing the physical game with my kids, I had an itch to build a computer game of it. Hence, this codebase.

I am building the game in phases. Not all features of a real chutes-and-ladders game will be present in the `v1` version of the game. I look forward to adding more features to it.

# Rules of the game

## v1

- You need 1 or players to start the game
- A default gameboard has 100 steps before you reach the finish line.
- You roll a dice to randomly move forward.
- A player starts with any dice value.
- A player ends the game when he/she lands on/gets past the last step.

# Development

I used `python 3` to build the game.

Dependency for development/running:
- `docker`
- `docker-compose`
- `make`

To run the game, follow these steps.
- Build the image. `$ make docker_build`
- Run the conainer and use it. `$ make docker_enter`. This should put you in a `bash` prompt.
- Run this to activate `pipenv`. `$ pipenv shell`
- For the first ever run, do this: `$pipenv install -d`. This install all the dependencies. Run this again if you update your dependency.

To stop the docker container, `$ make docker_stop`

Running from cli:
- `$ make python_run`

Runing tests:
- `$ make python_test`

Lint:
- `$ flake8`

# TODO

- Features to add
    - [ ] Assign uuid to a game
    - [ ] Serialize/deserialize game state to/from json file
    - [ ] Use exception to comminucate failure
    - [ ] Identify things not tackled: player moves, etc.
    - [ ] Add chute and ladders
    - [ ] Switch for ending the game on exact landing

- Fix these bugs
    - [ ] Players can go out of turns. It should not happen
    - [ ] *Iteration should not start after game ends*
    - [ ] Iteration can end without even a single player move
    - [ ] Iteration can end without not all players making a move
- Add stronger validation
    - [ ] Trim player names, and convert to lowercase to find uniqueness
- Add more tests
    - [ ] Tests to show that public fields are not modifiable from out side.
