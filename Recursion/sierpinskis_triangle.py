import turtle


def get_midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def draw_triangle(points, color, my_turtle):
    my_turtle.speed(1)
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def sierpinski(points, degree, my_turtle):
    color_map = ['red', 'green', 'blue', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], my_turtle)

    if degree > 0:
        sierpinski([points[0],
                    get_midpoint(points[0], points[1]),
                    get_midpoint(points[0], points[2])
                    ],
                   degree-1,
                   my_turtle)

        sierpinski([points[1],
                    get_midpoint(points[0], points[1]),
                    get_midpoint(points[1], points[2])
                    ],
                   degree - 1,
                   my_turtle)

        sierpinski([points[2],
                    get_midpoint(points[2], points[1]),
                    get_midpoint(points[0], points[2])
                    ],
                   degree - 1,
                   my_turtle)


if __name__ == "__main__":
    my_turtle = turtle.Turtle()

    my_window = turtle.Screen()

    my_points = [[-100, -50], [0, 100], [100, -50]]

    sierpinski(my_points, 3, my_turtle)

    my_window.exitonclick()
