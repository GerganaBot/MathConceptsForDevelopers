# First, we need to specify the recursive part. In order to draw a tree, we need to draw a line of a given length (which
# will be the current branch), and then draw two more lines to the left and right. By "left" and "right", we should mean "" \
#
#
#                                                                                                                        "rotation by a specified angle".
# So, this is how to draw a branch: draw a line and prepare to draw two more branches to the left and right. This is going
# to be our recursive call.
#
# To make things prettier, more natural-looking (and have a natural end to our recursion), let's draw each "sub-branch" a ' \
#                                                                                             'little shorter. If the branch ' \
#                                                                                             'becomes too short, it won't have "child branches".
# This will be the bottom of our recursion.
#
# There's one more important part of recursion, and this is "the clean-up". After we did something in the recursive calls,' \
#      ' it's very important to return the state of everything as it was before we did anything. In this case, after we draw a
# branch, we go back to our starting position.
#
# Let's first import the most import-ant (no pun intended...) Python drawing library: turtle! In order to make things easier, ' \
#    'we'll import all methods directly.
# We need to start the tree not at the middle, but toward the bottom of the screen, so we need to make a few more adjustments.
# We can wrap the setup in another function and call it. Let's start one trunk length below the center (the trunk length is' \
#                                                           ' the length of the longest line).
#
# Note: It's important to call done() after the drawing is finished. If you miss it, the window with the turtle drawing will ' \
#         'freeze and throw an exception.

from turtle import *


def draw_branch(branch_length, angle):
    if branch_length > 5:
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle)
        left(2 * angle)
        draw_branch(branch_length - 15, angle)
        right(angle)
        backward(branch_length)


def draw_tree(trunk_length, angle):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle)
    done()


draw_tree(100, 20)
