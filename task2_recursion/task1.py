import turtle

def draw_branch(t, branch_length, angle, level):
    if level > 0:
        t.forward(branch_length)

        t.left(angle)
        draw_branch(t, branch_length * 0.7, angle, level - 1)

        t.right(2 * angle)

        draw_branch(t, branch_length * 0.7, angle, level - 1)

        t.left(angle)
        t.backward(branch_length)


def draw_tree(level):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.shape("classic")
    t.color("green")
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    draw_branch(t, 100, 30, level)

    turtle.done()


recursion_level = int(input("Введіть рівень рекурсії: "))
draw_tree(recursion_level)
