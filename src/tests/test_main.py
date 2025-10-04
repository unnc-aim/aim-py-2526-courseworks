import random

from main import Facing, Grid


class TestGrid:
    def setup_method(self):
        """在每个测试方法之前运行"""
        # choose sizes large enough for the movement tests
        self.width = random.randint(3, 7)
        self.height = random.randint(3, 7)
        enemy_x = random.randint(0, self.width)
        enemy_y = random.randint(0, self.height)
        self.enemy_pos = (enemy_x, enemy_y)
        self.grid = Grid(self.width, self.height, self.enemy_pos)

    def test_initialization(self):
        """测试Grid初始化是否正确"""
        assert self.grid.width == self.width
        assert self.grid.height == self.height
        assert self.grid.current_pos == (0, 0)
        assert self.grid.current_direction == Facing.UP
        x, y = self.grid.enemy_pos
        assert 0 <= x <= self.width
        assert 0 <= y <= self.height

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
        # place at the right boundary
        self.grid.current_pos = (self.grid.width, min(2, self.grid.height))
        new_pos = self.grid.move_forward()
        assert new_pos == (self.grid.width, min(2, self.grid.height))

        self.grid.current_direction = Facing.LEFT
        self.grid.current_pos = (0, min(2, self.grid.height))
        new_pos = self.grid.move_forward()
        assert new_pos == (0, min(2, self.grid.height))

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
