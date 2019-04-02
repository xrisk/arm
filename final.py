from dxl2 import Motor, Connection, Instruction, MotorType
from math import sqrt, acos, pi
from time import sleep

import math


conn = Connection("/dev/tty.usbserial-A5052MJ8")
conn.open_port()

m_upper = Motor(conn, 5, MotorType.AX)
m_lower = Motor(conn, 4, MotorType.AX)
m_pencil = Motor(conn, 6, MotorType.AX)

m_upper.write(Instruction.MOVING_SPEED, 100)
m_lower.write(Instruction.MOVING_SPEED, 100)

m_upper.write(Instruction.TORQUE_ENABLE, 1)
m_lower.write(Instruction.TORQUE_ENABLE, 1)

PENCIL_UP = 608
PENCIL_DOWN = 502


def to_degree(x):
    return x * 180 / pi

def map(x, in_min, in_max, out_min, out_max):
    ret = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(ret)

def move_to(
    x, y
):  # (x, y) are coords to move to. z is positon of arm either to be up or down. a is for the stationary motor. b is for gripper angle initially.
    # lengths
    l1 = 10 # shoulder to elbow
    l2 = 14   # elbow to wrist
    r = sqrt(x ** 2 + y ** 2)

    if r > (l1 + l2):
        print("math error: ", r, l1 + l2)
        return

    theta_2 = pi - acos((l1 ** 2 + l2 ** 2 - r ** 2) / (2 * l1 * l2))
    theta_1 = acos(x / r) - acos((l1 ** 2 + r ** 2 - l2 ** 2) / (2 * l1 * r))

    theta_1 = theta_1 - pi / 2

    theta_1 = to_degree(theta_1)
    theta_2 = to_degree(theta_2)

    print(f"theta_1: {theta_1}")
    print(f"theta_2: {theta_2}")

    theta_2 = map(theta_2, -150, +150, 0, 1023)
    theta_1 = map(theta_1, -150, +150, 0, 1023)

    m_upper.write(Instruction.GOAL_POSITION, theta_2))
    m_lower.write(Instruction.GOAL_POSITION, theta_1))

# for x_start in rage()
# move_to(0, 17)


def y(x):
    return x ** 2 + 12

# print(m_pencil.write(Instruction.GOAL_POSITION, PENCIL_UP))
# print(m_lower.write(Instruction.GOAL_POSITION, 800))
# move_to(0, 24)
# sleep(2)

x_start = -2

# m_pencil.write(Instruction.GOAL_POSITION, PENCIL_DOWN)
while x_start <= +10:
    move_to(x_start, y(x_start))
    x_start += 0.05
    sleep(1)
