color = 'green'

# Fix the function below:


def change_color(new_color):
    to_update = new_color

    global color

    def disp_color():
        print('The original color was: ' + color)

    disp_color()

    color = to_update

    print('The new color is: ' + color)


change_color('blue')
