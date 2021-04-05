from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain0.nndf brain1.nndf")
        os.system("rm fitness0.txt fitness1.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1

    def Evolve(self):

        self.Evaluate(self.parents)

        # self.parent.Evaluate("GUI")
        #
        for currentGeneration in range(c.numberOfGenerations):

            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        self.Spawn()
        #
        self.Mutate()
        #
        self.Evaluate(self.children)

        # self.Print()
        #
        # self.Select()


    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1

    def Mutate(self):

        for x in self.children:
            self.children[x].Mutate()

    def Select(self):

        if(self.parent.fitness > self.child.fitness):

            self.parent = self.child

    def Evaluate(self, solutions):

        for x in range(0, c.populationSize):
            solutions[x].Start_Simulation("DIRECT")
        for x in range(0, c.populationSize):
            solutions[x].Wait_For_Simulation_To_End()

    def Print(self):

        print("\n\n", self.parent.fitness, self.child.fitness, "\n\n")

    def Show_Best(self):

        # self.parent.Evaluate("GUI")
        pass
