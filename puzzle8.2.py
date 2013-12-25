from Tkinter import *
import tkFont
from sys import exit
from time import sleep

from search import *

class PuzzleApp(Problem):
    def __init__(self,master,puzzle,goalState):
        self.w = 100
        self.s = 10
        self.tx= 50
        self.ty= 50
        self.customFont = tkFont.Font(family="Helvetica", size=24)
        self.frame = Frame(master)
        self.frame.grid()
        self.title = Label(self.frame,text="8 Puzzle")
        self.title.grid(row=0,column=1)
        self.goalTitle = Label(self.frame,text="Goal State")
        self.goalTitle.grid(row=0,column=4)
        self.puzzle = puzzle
        self.goalState = goalState
        self.initial = puzzle ;  self.goal = goalState
        #self.puzzlePieces = [[],[],[]]
        #self.goalPieces = [[],[],[]]
        self.puzzlePieces=[]
        self.goalPieces=[]
        self.solution_display = []
        self.solution_cost = 0
        for j in range(len(puzzle[0])):
            self.puzzlePieces.append([])
            self.goalPieces.append([])
            
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                self.puzzlePieces[i].append(Canvas(self.frame,width=self.w,height=self.w))
                self.puzzlePieces[i][j].create_rectangle(self.s,self.s,self.w,self.w, fill="red")
                if(puzzle[i][j] != 0):
                    self.puzzlePieces[i][j].create_rectangle(self.s,self.s,self.w,self.w, fill="red")
                    self.puzzlePieces[i][j].create_text(self.tx,self.ty,text=puzzle[i][j], font=self.customFont)
                    self.puzzlePieces[i][j].bind('<ButtonPress-1>', self.on_puzzle_click)
                else:
                    self.puzzlePieces[i][j].create_rectangle(self.s,self.s,self.w,self.w, fill="white")
                self.puzzlePieces[i][j].grid(row=i+1, column=j)
                self.goalPieces[i].append(Canvas(self.frame,width=self.w,height=self.w))
                if(goalState[i][j] != 0):
                    self.goalPieces[i][j].create_rectangle(self.s,self.s,self.w,self.w,fill="blue")
                    self.goalPieces[i][j].create_text(self.tx,self.ty,text=goalState[i][j], font=self.customFont)
                    self.goalPieces[i][j].bind('<ButtonPress-1>', self.on_goal_click)
                else:
                    self.goalPieces[i][j].create_rectangle(self.s,self.s,self.w,self.w,fill="white")
                self.goalPieces[i][j].grid(row=i+1, column=j+3)
        self.button = Button(self.frame, text="Find Solution", command=self.run_simulation, font=self.customFont)
        self.button.grid(row=4,columnspan=6)
        self.solution_display= Label(self.frame,text="Goal State", font=self.customFont)
        self.solution_display.grid(row=5,columnspan=20)
    def find_move(self,state1, state2):
        print state1, state2
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[0])):
                if(state1[i][j] == 0):
                    x1 = i
                    y1= j
                if(state2[i][j] == 0):
                     x2 = i
                     y2 = j
        if (x1 == x2) and (y1 < y2):
              move = "LEFT"
        elif (x1 == x2) and (y1 > y2):
               move = "RIGHT"
        elif (y1 == y2) and (x1 < x2):
               move = "UP"
        elif (y1 == y2) and (x1 > x2):
               move = "DOWN"
        return move
      
    def run_simulation(self):
 #       actions = astar(self.puzzle,self.goalState,heuristic_evaluation)
 #       print actions
 #       for move in ['LEFT','UP','RIGHT','RIGHT']:
 #          self.update_puzzle(self.doMove(move))
         count = 0
         #[node, count] = breadth_first_tree_search(self)
         node = iterative_deepening_search(self)
         print 'node count = ', count
         moves = []
         x = node.path()
         for i in range(len(x)-1):
             moves.insert(0,self.find_move(x[i].state, x[i+1].state))
         print moves
         outstr = str(count)
         self.solution_display.grid_forget()
         self.solution_display= Label(self.frame,text="count: "+outstr,font=self.customFont)
         self.solution_display.grid(row=5,columnspan=20)
         self.frame.update()
         sleep(0.5)
                                         
   
    def update_puzzle(self,puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                self.puzzlePieces[i][j].grid_forget()
                self.puzzlePieces[i][j] = Canvas(self.frame,width=self.w,height=self.w)
                if(puzzle[i][j] != 0):
                    self.puzzlePieces[i][j].create_rectangle(self.s,self.s,self.w,self.w,fill="red")
                    self.puzzlePieces[i][j].create_text(self.tx,self.ty,text=puzzle[i][j], font=self.customFont)
                    self.puzzlePieces[i][j].bind('<ButtonPress-1>', self.on_puzzle_click)
                else:
                    self.puzzlePieces[i][j].create_rectangle(self.s,self.s,self.w,self.w,fill="white")
                self.puzzlePieces[i][j].grid(row=i+1, column=j)
        self.frame.update()
        sleep(0.5)
        self.puzzle = puzzle
        self.initial = puzzle
    def update_goal(self,goalState):
        for i in range(len(goalState)):
            for j in range(len(goalState)):
                self.goalPieces[i][j].grid_forget()
                self.goalPieces[i][j] = Canvas(self.frame,width=self.w,height=self.w)
                if(goalState[i][j] != 0):
                    self.goalPieces[i][j].create_rectangle(self.s,self.s,self.w,self.w,fill="blue")
                    self.goalPieces[i][j].create_text(self.tx,self.tx,text=goalState[i][j], font=self.customFont)
                    self.goalPieces[i][j].bind('<ButtonPress-1>', self.on_goal_click)                    
                else:
                    self.goalPieces[i][j].create_rectangle(self.s,self.s,self.w,self.w,fill="white")
                self.goalPieces[i][j].grid(row=i+1, column=j+3)
        self.frame.update()
        self.goalState = goalState
        self.goal = goalState
    def on_puzzle_click(self,event):
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[0])):
                if(self.puzzle[i][j] == 0):
                    zeroi = i
                    zeroj = j
                if(self.puzzlePieces[i][j] == event.widget):
                    piecei = i
                    piecej = j
        if((abs(zeroi-piecei) == 1 and abs(zeroj - piecej) == 0) or (abs(zeroi-piecei) == 0 and abs(zeroj - piecej) == 1)):
            self.puzzle[zeroi][zeroj] = self.puzzle[piecei][piecej]
            self.puzzle[piecei][piecej] = 0
            self.update_puzzle(self.puzzle)
    def on_goal_click(self,event):
        for i in range(len(self.goalState)):
            for j in range(len(self.goalState[0])):
                if(self.goalState[i][j] == 0):
                    zeroi = i
                    zeroj = j
                if(self.goalPieces[i][j] == event.widget):
                    piecei = i
                    piecej = j
        if((abs(zeroi-piecei) == 1 and abs(zeroj - piecej) == 0) or (abs(zeroi-piecei) == 0 and abs(zeroj - piecej) == 1)):
            self.goalState[zeroi][zeroj] = self.goalState[piecei][piecej]
            self.goalState[piecei][piecej] = 0
            self.update_goal(self.goalState)

#Logic to find the possible moves at the current state.
    def getMoves(self, state):
        successors = []
        for i in range(len(state)):
            for j in range(len(state[0])):
                if(state[i][j] == 0):
                    x = i
                    y = j
        if(x>0):
            successors.append('UP')
        if(x<len(state)-1):
            successors.append('DOWN')
        if(y>0):
            successors.append('LEFT')
        if(y<len(state)-1):
            successors.append('RIGHT')
        return successors

    def doMove(self, move):
        tempPuzzle = [row[:] for row in self.puzzle]
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                if(self.puzzle[i][j] == 0):
                    x = i
                    y = j
        if(x>0 and move == 'UP'):
            tempPuzzle[x-1][y] = self.puzzle[x][y]
            tempPuzzle[x][y] = self.puzzle[x-1][y]
        elif(x<2 and move == 'DOWN'):
            tempPuzzle[x+1][y] = self.puzzle[x][y]
            tempPuzzle[x][y] = self.puzzle[x+1][y]
        elif(y>0 and move == 'LEFT'):
            tempPuzzle[x][y-1] = self.puzzle[x][y]
            tempPuzzle[x][y] = self.puzzle[x][y-1]
        elif(y<2 and move == 'RIGHT'):
            tempPuzzle[x][y+1] = self.puzzle[x][y]
            tempPuzzle[x][y] = self.puzzle[x][y+1]
        return tempPuzzle

    def tryMove(self, move, state):
        tempPuzzle = [row[:] for row in state]
        for i in range(len(state)):
            for j in range(len(state[0])):
                if(state[i][j] == 0):
                    x = i
                    y = j
        if(x>0 and move == 'UP'):
            tempPuzzle[x-1][y] = state[x][y]
            tempPuzzle[x][y] = state[x-1][y]
        elif(x<2 and move == 'DOWN'):
            tempPuzzle[x+1][y] = state[x][y]
            tempPuzzle[x][y] = state[x+1][y]
        elif(y>0 and move == 'LEFT'):
            tempPuzzle[x][y-1] = state[x][y]
            tempPuzzle[x][y] = state[x][y-1]
        elif(y<2 and move == 'RIGHT'):
            tempPuzzle[x][y+1] = state[x][y]
            tempPuzzle[x][y] = state[x][y+1]
        return tempPuzzle

    def doMoves(self, moves):
        tempPuzzle = [row[:] for row in self.puzzle]
        for i in range(len(moves)):
            tempPuzzle = self.doMove(moves[i], self.puzzle)
        return tempPuzzle

    def successor(self, state):
        """Given a state, return a sequence of (action, state) pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once. Iterators will work fine within the framework."""
        successors = []
        for move in self.getMoves(state):
            a = self.tryMove(move, state)
            successors.append([move, a])
        return successors

    
#Main function
s1 = [[1,2,3],[4,5,6],[0,7,8]]
s2 = [[1, 3, 0], [4, 2, 5], [7, 8, 6]]
s3 = [[0, 1, 5], [7, 3, 6], [2, 4, 8]]
examplePuzzle = [[2,1,6],[0,4,8],[7,5,3]]
goalState = [[1,2,3],[4,5,6],[7,8,0]]
root = Tk()
app = PuzzleApp(root,s3,goalState)
root.mainloop()
