import turtle


def spiral(my_turtle, line_length):
    my_turtle.speed(1)  # slow speed
    if line_length > 0:
        my_turtle.forward(line_length)
        my_turtle.right(90)
        spiral(my_turtle, line_length-5)


def tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        tree(branch_length-10, t)
        t.left(40)
        tree(branch_length-10, t)
        t.right(20)
        t.backward(branch_length)


def draw_spiral():
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()
    spiral(my_turtle, 100)
    my_window.exitonclick()


def draw_tree():
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()

    my_turtle.speed(1)
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color('brown')
    tree(75, my_turtle)

    my_window.exitonclick()


if __name__ == "__main__":
    # draw_spiral()
    draw_tree()
