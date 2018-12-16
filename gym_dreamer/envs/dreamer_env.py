import gym
from gym import error, spaces, utils
from gym.utils import seeding


class DreamerEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def step(self, action):
        return 1.0, 2.0, False, 'info'

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass
