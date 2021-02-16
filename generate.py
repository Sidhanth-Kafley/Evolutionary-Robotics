import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
i=0
y=0
z=0.5
for x in range(6):
    for a in range(6):
        for j in range(10):
            pyrosim.Send_Cube(name="Box", pos=[i,y,z] , size=[length, width, height])
            z+=height/1.05
            length*=0.9
            width*=0.9
            height*=0.9
        length = 1
        width = 1
        height = 1
        z=0.5
        i+=1
    length = 1
    width = 1
    height = 1
    i=0
    y+=1
    
    
#for x in range(10):
#    pyrosim.Send_Cube(name="Box", pos=[i,y,z] , size=[length, width, height])
#    z+=height/1.05
#    length*=0.9
#    width*=0.9
#    height*=0.9

    
    
            
pyrosim.End()
