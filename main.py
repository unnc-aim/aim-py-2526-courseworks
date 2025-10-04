
from enum import Enum
from typing import Tuple
import random
random.seed(114514)

class Facing(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Grid():
    def __init__(self):
        self.width : int = 5
        self.height : int = 5
        self.current_pos : tuple = (0,0)
        self.current_direction = Facing.UP
        self.enemy_pos : tuple = (random.randint(0,5), random.randint(0,5))

####### 不要改上面的代码 #######

    def move_forward(self) -> Tuple[int, int]:
        ####### Question 1 #######
        '''
        让机器人向当前方向走一格
        返回新的坐标 (x,y) 同时更新成员变量
        记得别让机器人走出界 [0,width] [0,height]
        以右为X轴正方向，上为Y轴正方向
        '''
        pass
        ##### Question 1 End #####


        ####### Question 2 #######
    def turn_left(self) -> Facing:
        '''
        让机器人逆时针转向
        返回一个新方向 (Facing.UP/DOWN/LEFT/RIGHT)
        '''
        pass
    def turn_right(self) -> Facing:
        '''
        让机器人顺时针转向
        '''
        pass
        ##### Question 2 End #####
    
        ####### Question 3 #######
    def find_enemy(self) -> bool:
        '''
        如果找到敌人（机器人和敌人坐标一致），就返回true
        '''
        pass
        ##### Question 3 End #####

        ####### Question 4 #######
    def patrol_around(self, step: int) -> int:
        '''
        让机器人随机巡逻step次（每次都随机选一个方向前进一步）
        遇到敌人就返回遇到敌人的步数
        没有遇到返回-1
        '''
        pass
        ##### Question 4 End #####