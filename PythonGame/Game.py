import random
class Maze(object):

    maze=[]

    def __init__(self,fruits=1,size=3):
        if(size>5 or fruits>(size*size)):
            print("Failed to intialize Maze (Invalid Size or Fruits)")
            return
        
        self.maze=[]

        for i in range(size):
            self.maze.append([""] * size)

        self.populateMaze(fruits,size)    
        

    def populateMaze(self,fruits,size):
        for i in range(size):
            for j in range(size):
                self.maze[i][j]="*"
            

        for i in range(fruits):
            x=random.randint(0,size-1)
            y=random.randint(0,size-1)
            self.maze[x][y]="0"

        return    

    def printMaze(self,size):
        for i in range(size):
            for j in range(size):
                
                if(j==size-1):
                    print(self.maze[i][j],end="\n")
                    continue

                print(self.maze[i][j], end="\t")
        return        


def main():
    maze=Maze(2,4)
    maze.printMaze(4)

if __name__=="__main__":
    main()
    


            

        


        