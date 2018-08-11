from gym.envs.registration import register


register(
    id='CartPoleEx-v0',
    entry_point='CartPoleEx.cartpole2:CartPoleEnv2',
    max_episode_steps=1000,
    reward_threshold=475.0,
)

