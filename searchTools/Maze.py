import random
import turtle

from objects import Cell
from searchTools import Location


class Maze():
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[Cell.Cell() for x in range(height + 2)] for y in range(width + 2)]
        self.visited = [[False for x in range(height + 2)] for y in range(width + 2)]
        self.defineInitialState()
        self.startLocation;
        self.endLocation;

    def defineInitialState(self):

        for x in range(0, self.width + 2):
            self.visited[x][0] = True
            self.visited[x][self.height + 1] = True

        for y in range(0, self.height + 2):
            self.visited[0][y] = True
            self.visited[self.width + 1][y] = True

    def generateMaze(self, startX, startY):
        self.visited[startX][startY] = True
        while (not self.visited[startX][startY + 1]) or (not self.visited[startX + 1][startY]) or (
        not self.visited[startX][startY - 1]) or (not self.visited[startX - 1][startY]):
            while (True):
                chosen_direction = random.randint(1,4)  # Choose a direction to move to 1 = North, 2 = East , 3 = South , 4 = West
                if chosen_direction == 1 and not self.visited[startX][startY + 1]:
                    self.cells[startX][startY].north = False
                    self.cells[startX][startY + 1].south = False
                    self.generateMaze(startX, startY + 1)
                    break
                if chosen_direction == 2 and not self.visited[startX + 1][startY]:
                    self.cells[startX][startY].east = False
                    self.cells[startX + 1][startY].west = False
                    self.generateMaze(startX + 1, startY)
                    break
                if chosen_direction == 3 and not self.visited[startX][startY - 1]:
                    self.cells[startX][startY].south = False
                    self.cells[startX][startY - 1].north = False
                    self.generateMaze(startX, startY - 1)
                    break
                if chosen_direction == 4 and not self.visited[startX - 1][startY]:
                    self.cells[startX][startY].west = False
                    self.cells[startX - 1][startY].east = False
                    self.generateMaze(startX - 1, startY)
                    break

    def genMaze(self):
        self.startLocation = self.genRandomLocation()
        self.endLocation = self.genRandomLocation()
        if (self.startLocation.x == self.endLocation.x and self.startLocation.y == self.endLocation.y):
            self.endLocation = self.genRandomLocation()
        self.generateMaze(self.startLocation.x, self.startLocation.y)
        self.drawMaze()

    def genRandomLocation(self):
        loc = Location.Location(random.randint(1, self.width), random.randint(1, self.height))
        return loc


    def drawMaze(self):
        # Initialise Window with its attributes
        turtle.title("Pokemon Maze")
        window = turtle.Screen()
        turtle.setworldcoordinates(0, 0, self.width+0.5, self.height+0.5)
        window.bgcolor("white")

        # Initialise my drawing Turtle
        drawingTurtle = turtle.Turtle()
        drawingTurtle.speed(0)
        for x in range(1,self.width+1):
            for y in range(1,self.height+1):
                drawingTurtle.penup()
                drawingTurtle.setpos(x-1, y-1)
                cell = self.cells[x][y]
                if cell.south :
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor() + 1, drawingTurtle.ycor())
                if cell.east:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor(), drawingTurtle.ycor()+1)
                if cell.north:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor() - 1, drawingTurtle.ycor())
                if cell.west:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor(), drawingTurtle.ycor()-1)






        window.exitonclick()

    def drawCell(self, cell):
        if cell.north == False:
            return