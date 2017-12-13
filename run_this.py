"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable
import time
import os

def update():
    for episode in range(200):
        os.system('cls')
        print('Episode: {}'.format(episode))
        print(RL.q_table)
        # initial position
        position = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on position
            action = RL.choose_action(str(position))

            # RL take action and get next position and reward
            position_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(position), action, reward, str(position_), done)

            # swap position
            position = position_

            time.sleep(0.04)

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
