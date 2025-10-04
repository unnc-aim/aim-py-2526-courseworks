"""
A simple robot simulator on a 2D grid.
The robot can move forward, turn left, turn right and find an enemy on the grid.
"""

from enum import Enum
from typing import Tuple


class Facing(Enum):  # Facing 是一个枚举类，用于定义方向
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Grid():
    def __init__(self, width: int, height: int, enemy_pos: tuple):  # DO NOT EDIT THIS METHOD
        self.width: int = width
        self.height: int = height
        self.current_pos: tuple = (0, 0)
        self.current_direction = Facing.UP
        self.enemy_pos: tuple = enemy_pos
        self.position_history: dict = {}  # 用于存储位置历史，键为步数，值为坐标

    def move_forward(self) -> Tuple[int, int]:  # type: ignore
        '''
        让机器人向当前方向走一格
        返回新的坐标 (x,y) 同时更新成员变量
        记得别让机器人走出界 [0,width] [0,height]
        以右为X轴正方向，上为Y轴正方向
        '''
        pass  # TODO: Question 1

    def turn_left(self) -> Facing:  # type: ignore
        '''
        让机器人逆时针转向
        返回一个新方向 (Facing.UP/DOWN/LEFT/RIGHT)
        '''
        pass

    def turn_right(self) -> Facing:  # type: ignore
        '''
        让机器人顺时针转向
        '''
        pass  # TODO: Question 2

    def find_enemy(self) -> bool:  # type: ignore
        '''
        如果找到敌人（机器人和敌人坐标一致），就返回true
        '''
        pass  # TODO: Question 3

    def record_position(self, step: int) -> None:
        '''
        将当前位置记录到 position_history 字典中
        键(key)为步数 step，值(value)为当前坐标 self.current_pos
        例如：step=1 时，记录 {1: (0, 0)}
        '''
        pass  # TODO: Question 4a

    def get_position_at_step(self, step: int) -> tuple:  # type: ignore
        '''
        从 position_history 字典中获取指定步数的坐标
        如果该步数不存在，返回 None
        提示：使用字典的 get 方法
        '''
        pass  # TODO: Question 4b


"""
在这里你需要实现 AdvancedGrid 类，继承自 Grid 类，并添加以下功能：
1. 追踪移动步数
2. 计算到敌人的曼哈顿距离

类名：AdvancedGrid
继承自：Grid
包含以下新属性：
- steps: int - 追踪移动步数，初始值为 0

包含以下方法：
1. move_forward(self) -> Tuple[int, int]
   调用父类的 move_forward 方法完成移动
   新增实现：移动步数 self.steps 加 1
   返回：移动后新坐标

2. distance_to_enemy(self) -> int
   计算当前位置到敌人位置的曼哈顿距离
   曼哈顿距离 = |x1 - x2| + |y1 - y2|
   返回：距离值

"""
# TODO: Question 5
