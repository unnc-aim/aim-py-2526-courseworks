import random

from main import AdvancedGrid, Facing, Grid


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

    # ===================== Question 4 Tests (字典操作) =====================
    def test_record_position(self):
        """测试记录位置到字典"""
        self.grid.current_pos = (1, 2)
        self.grid.record_position(1)
        assert 1 in self.grid.position_history
        assert self.grid.position_history[1] == (1, 2)

        self.grid.current_pos = (3, 4)
        self.grid.record_position(2)
        assert 2 in self.grid.position_history
        assert self.grid.position_history[2] == (3, 4)

    def test_get_position_at_step(self):
        """测试从字典获取位置"""
        self.grid.current_pos = (1, 2)
        self.grid.record_position(1)
        self.grid.current_pos = (3, 4)
        self.grid.record_position(2)

        result = self.grid.get_position_at_step(1)
        assert result == (1, 2)

        result = self.grid.get_position_at_step(2)
        assert result == (3, 4)

        # 测试不存在的步数
        result = self.grid.get_position_at_step(99)
        assert result is None


class TestAdvancedGrid:
    """测试 Question 5 - 类的继承"""

    def setup_method(self):
        """在每个测试方法之前运行"""
        # choose a width large enough for two right moves from x=2 -> ensure tests stable
        self.width = random.randint(5, 7)
        self.height = random.randint(3, 7)
        self.enemy_pos = (5, 5)
        self.grid = AdvancedGrid(self.width, self.height, self.enemy_pos)

    def test_inheritance_initialization(self):
        """测试子类正确继承并初始化父类属性"""
        assert self.grid.width == self.width
        assert self.grid.height == self.height
        assert self.grid.current_pos == (0, 0)
        assert self.grid.current_direction == Facing.UP
        assert self.grid.enemy_pos == self.enemy_pos
        # 测试新增的属性
        assert hasattr(self.grid, 'steps')
        assert self.grid.steps == 0

    def test_move_forward_with_steps(self):
        """测试重写的 move_forward 方法会增加步数"""
        initial_steps = self.grid.steps
        self.grid.current_direction = Facing.RIGHT
        self.grid.current_pos = (2, 2)

        self.grid.move_forward()
        assert self.grid.steps == initial_steps + 1
        assert self.grid.current_pos == (3, 2)

        self.grid.move_forward()
        assert self.grid.steps == initial_steps + 2
        assert self.grid.current_pos == (4, 2)

    def test_distance_to_enemy(self):
        """测试计算到敌人的曼哈顿距离"""
        # 敌人在 (5, 5)，机器人在 (0, 0)
        self.grid.current_pos = (0, 0)
        distance = self.grid.distance_to_enemy()
        assert distance == 10  # |5-0| + |5-0| = 10

        # 机器人在 (3, 2)
        self.grid.current_pos = (3, 2)
        distance = self.grid.distance_to_enemy()
        assert distance == 5  # |5-3| + |5-2| = 5

        # 机器人和敌人重合
        self.grid.current_pos = (5, 5)
        distance = self.grid.distance_to_enemy()
        assert distance == 0

    def test_advanced_grid_has_parent_methods(self):
        """测试子类可以使用父类的方法"""
        # 测试 turn_left
        self.grid.current_direction = Facing.UP
        new_direction = self.grid.turn_left()
        assert new_direction == Facing.LEFT

        # 测试 find_enemy
        self.grid.current_pos = self.enemy_pos
        assert self.grid.find_enemy() == True
