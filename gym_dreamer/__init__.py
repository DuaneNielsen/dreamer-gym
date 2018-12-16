from gym.envs.registration import register

register(
    id='dreamer-v0',
    entry_point='gym_dreamer.envs:DreamerEnv',
)