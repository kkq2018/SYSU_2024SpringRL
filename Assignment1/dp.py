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
    v = np.zeros([6, 6])
    v_new = np.zeros([6, 6])
    count = 0
    while np.max(np.abs(v_new - v)) > EPSILON or count == 0:
        count += 1
        v = np.copy(v_new)
        for i in range(v.shape[0]):
            if i == 4:
                a = 1
            for j in range(v.shape[1]):
                if i * v.shape[0] + j in BLOCKS:
                    v_new[i][j] = 0
                    continue
                if i * v.shape[0] + j == 9:
                    v_new[i][j] = 1
                    continue
                if i * v.shape[0] + j == 23:
                    v_new[i][j] = 0
                    continue
                v_up, v_down, v_left, v_right = -1, -1, -1, -1

                # 判断能否往上走
                if i > 0:
                    if (i - 1) * v.shape[0] + j in BLOCKS:
                        v_next = v[i][j]
                    else:
                        v_next = v[i - 1][j]
                    v_up = R[i * v.shape[0] + j] + GAMMA * v_next
                else:
                    v_up = -1

                # 判断能否往下走
                if i < v.shape[0] - 1:
                    if (i + 1) * v.shape[0] + j in BLOCKS:
                        v_next = v[i][j]
                    else:
                        v_next = v[i + 1][j]
                    v_down = R[i * v.shape[0] + j] + GAMMA * v_next
                else:
                    v_down = -1

                # 判断能否往右走
                if j < v.shape[1] - 1:
                    if i * v.shape[0] + j + 1 in BLOCKS:
                        v_next = v[i][j]
                    else:
                        v_next = v[i][j + 1]
                    v_right = R[i * v.shape[0] + j] + GAMMA * v_next
                else:
                    v_right = -1

                # 判断能否往左走
                if j > 0:
                    if i * v.shape[0] + j - 1 in BLOCKS:
                        v_next = v[i][j]
                    else:
                        v_next = v[i][j - 1]
                    v_left = R[i * v.shape[0] + j] + GAMMA * v_next
                else:
                    v_left = -1

                v_new[i][j] = np.max([v_up, v_down, v_left, v_right])

    return v

if __name__ == "__main__":

    env = MiniWorld()
    env.reset()
    n_state = env.observation_space.n
    n_action = env.action_space.n
    v = value_iteration()

    ######################################################
    # write your code to get a convergent value table v. #
    ######################################################

    env.update_r(np.reshape(v, [-1]))
    for x in range(2000):
        env.render()
