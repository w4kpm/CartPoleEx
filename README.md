# CartPoleEx-V0
Updated version of the AIGym CartPole - This allows a full rotation of the pole, multiple force values and only stops when the cart goes off the side, not when it falls down.

You should have the open AI gym installed - clone this into your local directory and then you can use the following code:

```
import gym
import gym.spaces
import CartPoleEx
import random
env = gym.make("CartPoleEx-v0")
observation = env.reset()
for a in range(5):
  for _ in range(999):
    #env.render(mode='rgb_array')
    env.render()
    action = random.randint(0,8)
    observation, reward, done, info = env.step(action)
    print(a,reward,action)
    if done:
      env.reset()
      break

env.close()
```

Actions are now 0-8 with 0 being a force of -20  4 a force of 0 and 8 a force of 20

rewards are a bit different, 100* the cosine of the angle + 100 (0-200) minus 10*the absolute of the current X value

I've disabled the rendering if you use 'rgb_array' but nothing is returned - so please don't rely on this (same thing as just getting rid of the render step - makes it faster to train)

