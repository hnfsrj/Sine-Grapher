import math
import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def dot_graph():

    while(True):
        clear_console()
        print("...")

        time.sleep(1)


def bar_graph():

    while(True):
        clear_console()
        print("[]")

        time.sleep(1)

run = True


print("Sine Graph Plotter")

while(run):

    print("\nPress \'ctrl+c\' to exit once the plotting has started")
    
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