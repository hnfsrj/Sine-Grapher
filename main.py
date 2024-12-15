import math
import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def dot_graph():

    #width and height of the graph
    width = 25
    height = 13
    space_char = "."
    point = "*"

    #generating the empty grid
    grid = []

    #translating the sine result to the y axis on our grid
    sine_to_grid = {
        0.0:6, 
        0.2:5, 
        0.4:4, 
        0.5:4, 
        0.7:3, 
        0.8:2, 
        0.9:1, 
        1:0,
        -0.2:7, 
        -0.4:8, 
        -0.5:8, 
        -0.7:9, 
        -0.8:10, 
        -0.9:11, 
        -1:12
    }

    def base_figure():
        global grid

        #initializing grid
        grid = [[space_char for _ in range(width)] for _ in range(height)]

        #inserting the 1,0, and -1 marks
        grid[0][1] = "1"
        grid[6][1] = "0"
        grid[12][0] = "-"
        grid[12][1] = "1"


        #inserting the lines which mark the borders of the graph
        for i in range(width-2):
            grid[0][i+2] = "-"

        for i in range(width-2):
            grid[6][i+2] = "-"

        for i in range(width-2):
            grid[12][i+2] = "-"

        for i in range(height):
            if grid[i][1] == space_char:
                grid[i][1] = "|"



    def plot_points(num):
        global grid
        
        for i in range(width-1):

            x = ((i+num)*15)
            sine_value = math.sin(math.radians(x))
            truncated_value = int(sine_value*10)/10
            y = sine_to_grid[truncated_value]

            if y == 0:
                grid[y][i+1] = "n"

            elif y == height-1:
                grid[y][i+1] = "u"

            else:
                grid[y][i+1] = point





    def print_grid():
        global grid

        #printing the grid to the console
        for row in grid:
            print("".join(row))


    num = 0
    while(True):
        clear_console()

        base_figure()
        plot_points(num)
        print_grid()

        num+=1
        time.sleep(1)




def bar_graph():

    while(True):
        clear_console()
        print("[]")

        time.sleep(1)





print("Sine Graph Plotter")

while(True):

    print("\nPress \'ctrl+c\' to exit once the plotting has started")
    
    print("\n1. Dot Graph\n2. Bar Graph\n3. Exit")
    graph_type = int(input(": "))

    if graph_type == 1:
        dot_graph();
    elif graph_type == 2:
        bar_graph();
    elif graph_type == 3:
        break
    else:
        print("\n invalid input!")

print("exiting...")