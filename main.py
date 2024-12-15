import math
import os
import time


space_char = "."
point = "*"



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



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def base_figure(width,height):

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


    return grid

def plot_points_dot(num, grid, width, height):

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





def plot_points_bar(num, grid, width, height):

    for i in range(3):

        x = ((i+num)*15)
        sine_value = math.sin(math.radians(x))
        truncated_value = int(sine_value*10)/10
        y = sine_to_grid[truncated_value]


        for j in range(3):
            start = (i*6)+2

            current_y = y
            while(True):

                grid[current_y][start+j] = point

                if current_y > (height-1)/2:
                    current_y-=1
                elif current_y < (height-1)/2:
                    current_y+=1
                elif current_y == (height-1)/2:
                    break





def print_grid(grid):

    #printing the grid to the console
    for row in grid:
        print("".join(row))










def dot_graph(num, width, height):


    #generating the empty grid
    grid_dot = base_figure(width, height)

    plot_points_dot(num, grid_dot, width, height)
    print_grid(grid_dot)





def bar_graph(num, width, height):
    
    #generating the empty grid
    grid_bar = base_figure(width, height)

    plot_points_bar(num, grid_bar, width, height)
    print_grid(grid_bar)



    

#width and height of the graph
width_dot = 25
height_dot = 13

width_bar = 17
height_bar = 13

    
num = 0
while(True):
    clear_console()

    print("Sine Graph Plotter")
    print("\nPress \'ctrl+c\' to exit\n\n")


    dot_graph(num, width_dot, height_dot)
    
    print("\n\n\n")

    bar_graph(num, width_bar, height_bar)

    num+=1
    time.sleep(1)
