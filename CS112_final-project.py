import sys
import time
import turtle

screen = turtle.Screen()
screen.screensize(20, 20, "white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("black")
pen.pensize(5)
pen.hideturtle()


# Creating a class for the parts of the bear
class BearParts:
    @staticmethod
    def draw_circle(pen, x, y, radius):
        pen.penup()
        pen.goto(x, y)
        pen.down()
        pen.circle(radius)


# Creating object for the class
BearParts.draw_circle(pen, -155, -190, 60)  # Circle 1
BearParts.draw_circle(pen, 155, -190, 60)  # Circle 2
BearParts.draw_circle(pen, 0, -190, 150)  # Body
BearParts.draw_circle(pen, 0, 110, 80)  # Head
BearParts.draw_circle(pen, 100, 195, 50)  # Ear 1
BearParts.draw_circle(pen, -100, 195, 50)  # Ear 2
BearParts.draw_circle(pen, 115, -50, 60)  # Hand 1
BearParts.draw_circle(pen, -115, -50, 60)  # Hand 2


# Defining how the circle should be filled
def fill_circle(pen, x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fillcolor(color)
    pen.circle(radius)
    pen.end_fill()


# Defining the primary color
def color_choice1():
    if choice1 == 1:
        return "RED"
    elif choice1 == 2:
        return "YELLOW"
    elif choice1 == 3:
        return "BLUE"


# Defining the secondary color
def color_choice2():
    if choice2 == 5:
        return "GREEN"
    elif choice2 == 6:
        return "ORANGE"
    elif choice2 == 7:
        return "PURPLE"


# Introduction
text = ("\nWELCOME TO THE BEAR STATION"
        "\nLET'S FILL SOME BABY'S UP!!!!!"
        "\n\nFOLLOW INSTRUCTIONS FOR BETTER RESULT. ENJOY!!!")

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)

delay_second = 1
time.sleep(delay_second)

# Main loop
while True:
    text2 = "\n\n****Select your primary color****"
    while True:
        text2 = "\n\n****Select your primary color****"
        for char in text2:
            print(char, end='', flush=True)
            time.sleep(0.050)

        choice1 = input("\nFor RED press [1]"
                        "\nFor YELLOW press [2]"
                        "\nFor BLUE press [3]"
                        "\nEnter here:")

        if choice1.isdigit() and 1 <= int(choice1) <= 3:
            break
        else:
            print("Invalid input. Please enter a valid number between 1 and 3.")

    choice1 = int(choice1)
    primary_color = color_choice1()
    print("The primary color is", primary_color)

    while True:
        text3 = "\n****Select your secondary color****"
        for char in text3:
            print(char, end='', flush=True)
            time.sleep(0.050)

        choice2 = input("\nFor GREEN press [5]"
                        "\nFor ORANGE press [6]"
                        "\nFor PURPLE press [7]"
                        "\nEnter here:")

        if choice2.isdigit() and 5 <= int(choice2) <= 7:
            break
        else:
            print("Invalid input. Please enter a valid number between 5 and 7.")

    choice2 = int(choice2)
    secondary_color = color_choice2()
    print("The secondary color is", secondary_color)

    print("\n=================================================="
          "\n-----THE RESULT OF THE COLORS YOU HAVE CHOSEN-----"
          "\n==================================================")

    delay_second = 0.5
    time.sleep(delay_second)

    text4 = "\nThe tertiary result is:"
    for char in text4:
        print(char, end='', flush=True)
        time.sleep(0.050)

    inputs = choice1 * choice2

    if inputs == 5:
        print("YELLOW\nColor Code: #FFFF00")
    elif inputs == 6:
        print("VERMILION\nColor code: #E34234")
    elif inputs == 7:
        print("MAGENTA/RED-VIOLET\nColor code: #C71585")
    elif inputs == 8:
        print("REDDISH-PURPLE\nColor code: #953553")
    elif inputs == 10:
        print("YELLOW-GREEN\nColor code: #9ACD32")
    elif inputs == 12:
        print("AMBER\nColor code: #FFBF00")
    elif inputs == 14:
        print("BROWN\nColor code: #964B00")
    elif inputs == 15:
        print("TEAL\nColor code: #008080")
    elif inputs == 18:
        print("REDDISH-BROWN OF BURNT SIENNA\nColor code: #E97451")
    elif inputs == 21:
        print("BLUE-VIOLET\nColor code: #8a2be2")

    delay_second = 1
    time.sleep(delay_second)

    while True:
        part_selector = input("\nIn which part do you want to fill? (Please refer to the choices.)"
                              "\n[1] Feet"
                              "\n[2] Hands"
                              "\n[3] Body"
                              "\n[4] Head"
                              "\n[5] Ears"
                              "\nEnter here:")

        if part_selector.isdigit() and 1 <= int(part_selector) <= 5:
            part_selector = int(part_selector)
        else:
            print("Invalid input. Please enter a valid number between 1 and 5.")
            continue  # Restart

        if part_selector == 0:
            print("Program Completed.")
            turtle.bye()  # Close turtle graphics window
            sys.exit()

        tcolor = input("Enter color code:")

        if part_selector == 1:
            fill_circle(pen, -155, -190, 60, tcolor)
            fill_circle(pen, 155, -190, 60, tcolor)
        elif part_selector == 2:
            fill_circle(pen, 115, -50, 60, tcolor)
            fill_circle(pen, -115, -50, 60, tcolor)
        elif part_selector == 3:
            fill_circle(pen, 0, -190, 150, tcolor)
        elif part_selector == 4:
            fill_circle(pen, 0, 110, 80, tcolor)
        elif part_selector == 5:
            fill_circle(pen, 100, 195, 50, tcolor)
            fill_circle(pen, -100, 195, 50, tcolor)
        else:
            print("Invalid part selection. Please enter a valid part number.")
            continue  # Restart the loop

        screen.update()

        # A question for the user
        while True:
            end_question1 = input("\nAre all the parts filled?"
                                  "\nIf yes press [1]"
                                  "\nIf no press [2]"
                                  "\nEnter here:")

            if end_question1.isdigit() and int(end_question1) in [1, 2]:
                end_question1 = int(end_question1)
                break
            else:
                print("Invalid input. Please enter either 1 or 2.")
                continue  # Restart the loop

        if end_question1 == 1:
            print("Program Completed.")
            sys.exit()
        else:
            print("Well let's proceed.")

        delay_second = 1
        time.sleep(delay_second)

        end_question2 = None
        while end_question2 not in [1, 2]:
            end_question2 = input("\nDo you want to continue?"
                                  "\nIf yes press [1]"
                                  "\nIf no press [2]"
                                  "\nEnter here:")

            if end_question2.isdigit() and int(end_question2) in [1, 2]:
                end_question2 = int(end_question2)
                break
            else:
                print("Invalid input. Please enter either 1 or 2.")
                continue  # Restart the loop

        if end_question2 == 1:
            print("Program Continued.")
            break  # Exit the inner loop and go back to the main loop
        else:
            print("Program terminated.\nThank you!!!")
            sys.exit()
