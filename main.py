import math
import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def dot_graph():

    plot = True
    while(plot):
        clear_console()
        print("...")



def bar_graph():

    plot = True
    while(plot):
        clear_console()
        print("[]")


run = True


print("Sine Graph Plotter")

while(run):

    print("\n press \'q\' to return back to the main menu once the plotting has started")
    
    print("\n1. Dot Graph\n 2. Bar Graph 3. Exit")
    graph_type = input(": ")

    if graph_type == 1:
        dot_graph();
    elif graph_type == 2:
        bar_graph();
    elif graph_type == 3:
        run = False
    else:
        print("\n invalid input!")

print("exiting...")