"""
High-level outline of how to move a tower from the starting pole, to the goal pole,
using an intermediate pole:

1. Move a tower of height-1 to an intermediate pole, using the final pole.
2. Move the remaining disk to the final pole.
3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

Note:
    Number of moves required to correctly move a tower of n disks is 2^n - 1.
    For example: in case of 3 disks, number of moves = 7

"""


def move_disk(from_pole, to_pole):
    print(f"moving disk from {from_pole} to {to_pole}")


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


if __name__ == "__main__":
    # Suppose there are 5 disks in pole A and we want to move them
    # to pole C, using intermediate pole B
    move_tower(5, "A", "C", "B")  # takes 31 moves
