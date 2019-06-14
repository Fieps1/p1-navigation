import torch

from unityagents import UnityEnvironment
import numpy as np


class BananaEnvWrapper(object):

    blank_state = torch.zeros(1, 37, dtype=torch.uint8)

    """ Wraps the udacity enviroment into an object behaving like an atari env
    """

    def __init__(self, train_mode=True, device='cuda'):
        self.train_mode = train_mode
        self.device = device
        self.unity_env = UnityEnvironment(
            file_name="/home/philipp/udacity/deep-reinforcement-learning/p1_navigation/Banana_Linux/Banana.x86_64")

        # get the default brain
        self.brain_name = self.unity_env.brain_names[0]
        brain = self.unity_env.brains[self.brain_name]

        # reset the environment
        env_info = self.unity_env.reset(train_mode=self.train_mode)[self.brain_name]

        # number of agents in the environment
        print('Number of agents:', len(env_info.agents))

        # number of actions
        self.action_space = brain.vector_action_space_size
        print('Number of actions:', self.action_space)

        # examine the state space
        state = env_info.vector_observations[0]
        print('States look like:', state)
        self.state_size = len(state)
        print('States have length:', self.state_size)

        self.score = 0
        self.episode = 0

    def eval(self):
        self.train_mode = False

    def train(self):
        self.train_mode = True

    def reset(self):
        # print("Score: %d, epsiode: %d" % (self.score, self.episode))
        self.episode += 1
        self.score = 0
        env_info = self.unity_env.reset(train_mode=self.train_mode)[self.brain_name]
        return env_info.vector_observations[0]  # Return current state

    def step(self, action):
        env_info = self.unity_env.step(action)[self.brain_name]
        state = env_info.vector_observations[0]  # get the current state
        reward = env_info.rewards[0]  # get the reward
        done = env_info.local_done[0]  # see if episode has finished
        self.score += reward  # update the score
        return state, reward, done

    def close(self):
        self.unity_env.close()


if __name__ == '__main__':
    env = BananaEnvWrapper(train_mode=False)
    state = env.reset()

    score = 0  # initialize the score
    while True:
        action = np.random.randint(env.action_space())  # select an action
        next_state, reward, done = env.step(action)

        score += reward  # update the score
        state = next_state  # roll over the state to next time step
        if done:  # exit loop if episode finished
            break

    print("Score: {}".format(score))
    env.close()
