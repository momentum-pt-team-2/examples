import turtle

my_colors = ['purple', 'yellow', 'red', 'green', 'blue', 'pink']

def get_color_from_user():
    color = input("Would you like purple, yellow, red, or green: ")
    return color

def draw_square():
    turtle.shape('turtle')
    # asking the user about each color
    # turtle.color(get_color_from_user())
    for side in range(4):
        # print("my position in the list is currenly = ", side)
        turtle.forward(100)
        turtle.right(90)


def draw_colored_squares(colors):
    repeat = 'Y'
    while repeat.upper() == "Y":
        turtle.shape('turtle')
        turtle.up()
        turtle.right(20)
        turtle.forward(50)
        turtle.down()
        for color in colors:
            answer = input(f'Would you like a {color} square? Y/N ')
            if answer.upper() == 'N':
                continue
            turtle.color(color)
            draw_square()
            turtle.left(30)
        repeat = input("Would you like to keep drawing? Y/N ")
    # refactor as a while loop
    # if repeat.upper == 'Y':
    #     #recursion
    #     draw_colored_squares(colors)
    # else:
    #     return


draw_colored_squares(my_colors)
# draw_square()
turtle.done()