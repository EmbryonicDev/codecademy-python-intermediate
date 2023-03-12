color = 'green'

# Fix the function below:


def change_color(new_color):

    global color
    color = to_update

    def disp_color():
        print('The original color was: ' + color)
        to_update = new_color

    disp_color()

    print('The new color is: ' + color)


change_color('blue')
