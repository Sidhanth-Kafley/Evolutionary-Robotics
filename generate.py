import pyrosim.pyrosim as pyrosim


def Create_World():

    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    i=-3
    y=3
    z=0.5

    pyrosim.Send_Cube(name="Box", pos=[i,y,z] , size=[length, width, height])
    
    pyrosim.End()
    
    
def Create_Robot():

    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1
    
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0.5 0 1")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "-0.5 0 1")
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length, width, height])

    pyrosim.End()


Create_World()
Create_Robot()
#for x in range(6):
#    for a in range(6):
#        for j in range(10):
#            pyrosim.Send_Cube(name="Box", pos=[i,y,z] , size=[length, width, height])
#            z+=height/1.05
#            length*=0.9
#            width*=0.9
#            height*=0.9
#        length = 1
#        width = 1
#        height = 1
#        z=0.5
#        i+=1
#    length = 1
#    width = 1
#    height = 1
#    i=0
#    y+=1
