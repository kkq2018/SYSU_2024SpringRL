import copy
import sys
import os
import numpy as np
# 将当前文件的父目录添加到 sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件的绝对路径
parent_dir = os.path.dirname(current_dir)  # 获取父目录

# 将祖父目录添加到 sys.path
sys.path.append(parent_dir)

from env.grid_scenarios import MiniWorld


# Hypar-parameters that could be helpful.
GAMMA = 0.9
EPSILON = 0.001
BLOCKS = [14, 15, 21, 27]
R = [
    0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0,
]


def policy_iteration():
    pass


def value_iteration():
    pass

if __name__ == "__main__":

    env = MiniWorld()
    env.reset()
    n_state = env.observation_space.n
    n_action = env.action_space.n

    ######################################################
    # write your code to get a convergent value table v. #
    ######################################################

    env.update_r(v)
    for x in range(2000):
        env.render()
