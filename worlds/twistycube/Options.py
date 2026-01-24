from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle
  
class SizeOfCube(Choice):
    """
    Which size of cube you want to play.
    Note! This game is harder than just solving the cube!
    """

    display_name = "Size of Cube"
    option_2x2x2 = 2
    option_3x3x3 = 3
    option_4x4x4 = 4
    option_5x5x5 = 5
    default = 2
    
class StartingStickers(Range):
    """
    How many stickers you start with.
    """

    display_name = "Starting Stickers"
    range_start = 1
    range_end = 15
    default = 5

class RandomizeColorLayout(Toggle):
    """
    Whether you want to use the default color layout (off) or randomize it (on).
    """

    display_name = "Randomize color layout"
    default = 0
    
class MinStickersToGoalOnSolve(Range):
    """
    The game will goal when the cube is solved, even if you don't have all stickers yet.
    This option lets you set the minimum number of stickers you need to have collected for it to goal.
    Setting it to 0 means you will goal as soon as you solve the cube.
    Setting it to the max means you will have to wait until you have collected all stickers.
    """

    display_name = "Minimum stickers to goal on solve"
    range_start = 0
    range_end = 150
    default = 0

@dataclass
class TwistyCubeOptions(PerGameCommonOptions):
    size_of_cube: SizeOfCube
    starting_stickers: StartingStickers
    randomize_color_layout: RandomizeColorLayout
    min_stickers_to_goal_on_solve: MinStickersToGoalOnSolve