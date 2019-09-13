# Udacity deep reinforcement learning nano degree

### Project 1: Navigation

This repo contains my solution to the first project of Udacity deep RL Nanodegree.

I first tried to port an existing implementation of the Rainbow algorithm, see https://github.com/Fieps1/Rainbow.
However after a while of trying out different parameters, I just could not get it to work.
Thus, I decided to go for the standard approach and base my solution on the examples provided by Udacity, which worked 
out quite fast.

##### Banana environment
The environment is a 3d closed world. An agent has to navigate through it by avoiding to collect blue bananas 
and managing to collect yellow bananas.

The state space is 37-dimensional vector giving ray based perception of the agent field of view.
The action space size is 4: left, right, straight and backwards.

Banana env is considered to be solved if an agent is able to score a reward of more than 13 per episode.

##### Lessons learned:
It looks like simply taking a well performing RL algorithmn and moving it over to a different environment is more 
challenging than I thought. The set of parameter's needs to be tuned individual for a new environment, given the 
environment is not similar enough to the old one.

Second lession learned: Start easy and don't try to hit a fairly simple environment with Rainbow :-)

##### Dependencies
Note: Only tested on Linux x64!

You will need some Python libs:,
```sh
pip3 install -r requirements.txt
```
And a copy of the unity banana env:
```sh
wget https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip
unzip Banana_Linux.zip
```

##### How to run the code
```sh
python3 dqn.py
```
To train the agent instead of evaluating, just uncomment the line at the end of dqn.py.


##### Implementation details and results:
See Report.md