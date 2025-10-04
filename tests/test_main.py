import os
import sys
import pytest

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from main import Grid, Facing


class TestGrid:
    def setup_method(self):
        """在每个测试方法之前运行"""
        self.grid = Grid()
    
    def test_initialization(self):
        """测试Grid初始化是否正确"""
        assert self.grid.width == 5
        assert self.grid.height == 5
        assert self.grid.current_pos == (0, 0)
        assert self.grid.current_direction == Facing.UP
        x, y = self.grid.enemy_pos
        assert 0 <= x <= 5
        assert 0 <= y <= 5
    
    def test_move_forward_up(self):
        """测试向上移动"""
        self.grid.current_direction = Facing.UP
        self.grid.current_pos = (2, 2)
        new_pos = self.grid.move_forward()
        assert new_pos == (2, 3)
        assert self.grid.current_pos == new_pos
    
    def test_move_forward_right(self):
        """测试向右移动"""
        self.grid.current_direction = Facing.RIGHT
        self.grid.current_pos = (2, 2)
        new_pos = self.grid.move_forward()
        assert new_pos == (3, 2)
        assert self.grid.current_pos == new_pos
    
    def test_move_forward_down(self):
        """测试向下移动"""
        self.grid.current_direction = Facing.DOWN
        self.grid.current_pos = (2, 2)
        new_pos = self.grid.move_forward()
        assert new_pos == (2, 1)
        assert self.grid.current_pos == new_pos
    
    def test_move_forward_left(self):
        """测试向左移动"""
        self.grid.current_direction = Facing.LEFT
        self.grid.current_pos = (2, 2)
        new_pos = self.grid.move_forward()
        assert new_pos == (1, 2)
        assert self.grid.current_pos == new_pos
    
    def test_move_forward_boundary_check(self):
        """测试边界检查"""
        self.grid.current_direction = Facing.RIGHT
        self.grid.current_pos = (5, 2)
        new_pos = self.grid.move_forward()
        assert new_pos == (5, 2)
        
        self.grid.current_direction = Facing.LEFT
        self.grid.current_pos = (0, 2)
        new_pos = self.grid.move_forward()
        assert new_pos == (0, 2)
    
    def test_turn_left(self):
        """测试左转"""
        # UP -> LEFT
        self.grid.current_direction = Facing.UP
        new_direction = self.grid.turn_left()
        assert new_direction == Facing.LEFT
        assert self.grid.current_direction == Facing.LEFT
        
        # LEFT -> DOWN
        self.grid.current_direction = Facing.LEFT
        new_direction = self.grid.turn_left()
        assert new_direction == Facing.DOWN
        assert self.grid.current_direction == Facing.DOWN
        
        # DOWN -> RIGHT
        self.grid.current_direction = Facing.DOWN
        new_direction = self.grid.turn_left()
        assert new_direction == Facing.RIGHT
        assert self.grid.current_direction == Facing.RIGHT
        
        # RIGHT -> UP
        self.grid.current_direction = Facing.RIGHT
        new_direction = self.grid.turn_left()
        assert new_direction == Facing.UP
        assert self.grid.current_direction == Facing.UP
    
    def test_turn_right(self):
        """测试右转"""
        # UP -> RIGHT
        self.grid.current_direction = Facing.UP
        new_direction = self.grid.turn_right()
        assert new_direction == Facing.RIGHT
        assert self.grid.current_direction == Facing.RIGHT
        
        # RIGHT -> DOWN
        self.grid.current_direction = Facing.RIGHT
        new_direction = self.grid.turn_right()
        assert new_direction == Facing.DOWN
        assert self.grid.current_direction == Facing.DOWN
        
        # DOWN -> LEFT
        self.grid.current_direction = Facing.DOWN
        new_direction = self.grid.turn_right()
        assert new_direction == Facing.LEFT
        assert self.grid.current_direction == Facing.LEFT
        
        # LEFT -> UP
        self.grid.current_direction = Facing.LEFT
        new_direction = self.grid.turn_right()
        assert new_direction == Facing.UP
        assert self.grid.current_direction == Facing.UP
    
    def test_find_enemy_true(self):
        """测试找到敌人的情况"""
        # 将机器人移动到敌人位置
        self.grid.current_pos = self.grid.enemy_pos
        result = self.grid.find_enemy()
        assert result == True
    
    def test_find_enemy_false(self):
        """测试没找到敌人的情况"""
        enemy_x, enemy_y = self.grid.enemy_pos
        if (0, 0) != (enemy_x, enemy_y):
            self.grid.current_pos = (0, 0)
        else:
            self.grid.current_pos = (1, 1)
        
        result = self.grid.find_enemy()
        assert result == False
    
    def test_patrol_around_basic(self):
        """测试基本的巡逻功能"""
        result = self.grid.patrol_around(10)
        # 结果应该是 -1（没找到敌人）或者是找到敌人的步数（0-9）
        assert result == -1 or (0 <= result <= 9)
    
    def test_patrol_around_zero_steps(self):
        """测试0步巡逻"""
        result = self.grid.patrol_around(0)
        assert result == -1  # 0步应该返回-1（没找到敌人）


def test_main():
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    try:
        sys.path.insert(0, project_root)
        import main
        grid = main.Grid()
        print("main.py found")
        assert True
    except Exception as e:
        print(f" main.py not found: {e}")
        assert False, f"failed: {e}"
    
