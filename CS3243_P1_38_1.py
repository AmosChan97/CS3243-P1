import os
import sys
import queue


def solvable (state):
    inv = 0 #number of inversions
    flattened = state.flatten()
    for i in range flattened:
        for j in range (i + 1, a):
            if (a[i] > a[j]): 
                inv += 1
    return inv

def heurstic1 (state):
    for i in range (0, 3):
        for j in range

class Puzzle(object):
    def __init__(self, init_state, goal_state):
        # you may add more attributes if you think is useful
        self.init_state = init_state
        self.goal_state = goal_state
        self.current_state
        self.actions = list()
        self.n = len(init_state)
        self.empty_space = find_empty_space(init_state)
        self.visited = set()

    def solve(self):
        #TODO
        # implement your search algorithm here
        if (solvable(init_state) == False):
            return ["UNSOLVABLE"]
        return ["LEFT", "RIGHT"] # sample output 

    # you may add more functions if you think is useful
    def bfs(self):
        q = queue.Queue() 
        move = list()
        q.put([init_state, self.empty_space, move])
        for rows in queue_rows(q):
            x, y = rows[2]
            if (x == 0):
                



    def find_empty_space(init_state):
        i, j = 0, 0
        for i in range(n):
            for j in range(n):
                if init_state[i][j] == 0:
                    return [i, j]
                else j += 1
            i += 1

    def generateNodes(current_state):
        if 

    def up_move:
        




if __name__ == "__main__":
    # do NOT modify below

    # argv[0] represents the name of the file that is being executed
    # argv[1] represents name of input file
    # argv[2] represents name of destination output file
    if len(sys.argv) != 3:
        raise ValueError("Wrong number of arguments!")

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        raise IOError("Input file not found!")

    lines = f.readlines()
    
    # n = num rows in input file
    n = len(lines)
    # max_num = n to the power of 2 - 1
    max_num = n ** 2 - 1

    # Instantiate a 2D list of size n x n
    init_state = [[0 for i in range(n)] for j in range(n)]
    goal_state = [[0 for i in range(n)] for j in range(n)]
    

    i,j = 0, 0
    for line in lines:
        for number in line.split(" "):
            if number == '':
                continue
            value = int(number , base = 10)
            if  0 <= value <= max_num:
                init_state[i][j] = value
                j += 1
                if j == n:
                    i += 1
                    j = 0

    for i in range(1, max_num + 1):
        goal_state[(i-1)//n][(i-1)%n] = i
    goal_state[n - 1][n - 1] = 0

    puzzle = Puzzle(init_state, goal_state)
    ans = puzzle.solve()

    with open(sys.argv[2], 'a') as f:
        for answer in ans:
            f.write(answer+'\n')







