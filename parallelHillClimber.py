from solution import SOLUTION
import constants as c
import copy

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

        for x in range(0, c.populationSize):
            self.parents[x].Start_Simulation("DIRECT")
        for x in range(0, c.populationSize):
            self.parents[x].Wait_For_Simulation_To_End()

        # self.parent.Evaluate("GUI")
        #
        for currentGeneration in range(c.numberOfGenerations):

            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        # self.Spawn()
        #
        # self.Mutate()
        #
        # self.child.Evaluate("DIRECT")
        #
        # self.Print()
        #
        # self.Select()
        pass

    def Spawn(self):

        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID+=1


    def Mutate(self):

        self.child.Mutate()

    def Select(self):

        if(self.parent.fitness > self.child.fitness):

            self.parent = self.child

    def Print(self):

        print("\n\n", self.parent.fitness, self.child.fitness, "\n\n")

    def Show_Best(self):

        # self.parent.Evaluate("GUI")
        pass
