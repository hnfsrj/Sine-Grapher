import math
import os
import time
import keyboard


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def dot_graph():

    while(True):
        clear_console()
        print("...")

        if keyboard.is_pressed('q'):
            clear_console()
            break

        time.sleep(1)


def bar_graph():

    while(True):
        clear_console()
        print("[]")

        if keyboard.is_pressed('q'):
            clear_console()
            break

        time.sleep(1)

run = True


print("Sine Graph Plotter")

while(run):

    print("\nPress \'q\' to return back to the main menu once the plotting has started")
    
    print("\n1. Dot Graph\n2. Bar Graph\n3. Exit")
    graph_type = int(input(": "))

    if graph_type == 1:
        dot_graph();
    elif graph_type == 2:
        bar_graph();
    elif graph_type == 3:
        run = False
    else:
        print("\n invalid input!")

print("exiting...")