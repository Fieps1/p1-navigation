# Udacity deep reinforcement learning

### Project 1: Navigation

This repo contains my solution to the first project of Udacity deep RL Nanodegree.

After trying to port an existing implementation of the Rainbow algorithm, see https://github.com/Fieps1/Rainbow, 
I decided to go for the standard approach and base my solution on the examples provided by Udacity.

Lesson Learned: Start easy, most implementations seem to be adapted and optimized for quite invidual projects.

##### Banana environment
The environment is a 3d closed world. An agent has to navigate through it by avoiding to collect blue bananas 
and managing to collect yellow bananas.

The state space is 37-dimensional vector giving ray based perception of the agent field of view.
The action space size is 4: left, right, straight and backwards.

##### Dependencies
Note: Only tested on Linux x64!

You will need some Python libs, as well as a copy of the unity banana env:
```sh
pip3 install -r requirements.txt
```


##### How to run the code
```sh
python3 dqn.py
```