# class Instruction:
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class carData(db.Model):
   id = db.Column('car_id', db.Integer, primary_key = True)
   command = db.Column(db.String(100))
   speed = db.Column(db.String(50))  
   distance = db.Column(db.String(200))
   status = db.Column(db.String(10))

def __init__(self, command, speed, distance,status):
   self.command = command
   self.speed = speed
   self.distance = distance
   self.status = status

class Car: 
    def __init__(self, command, speed, distance, status):
        self.command = command
        self.speed = speed
        self.distance = distance
        self.status = status

    def getCommand(self):
        return self.command

    def getSpeed(self):
        return self.speed

    def getDistance(self):
        return self.distance

    def getStatus(self):
        return self.status
        
    def setSpeed(self,speed):
        self.speed = speed
        return 

    def setStatus(self,status):
        self.status = status
        return 



class CarController:
    def stopCar(carObj):
        carObj.setStatus("stopped")
        carObj.setSpeed(0)
        return

    def detectObstacle(carObj):
        if carObj.getStatus() == "obstacle":
            print('OBSTACLE DETECTED!')
            CarController.stopCar(carObj)
            return True
        else:
            print("NO OBSTACLE")
            return False

        
        

    def detectEndPoint(self): #not needed?
        if Car.getStatus == "completed":
            return True
        else:
            return False

    

    def executeInstruction(carData):
        carObject = Car(carData.command,0,0,"executing")
        print("Command: "+carObject.getCommand())
        print("Speed: "+str(carObject.getSpeed()))
        print("Distance: "+str(carObject.getDistance()))
        print("Status: "+carObject.getStatus())

            
        return carObject
    
    def sendData(carData):
        carObject = Car(carData.command,carData.speed,carData.distance,carData.status)
        print("Command: "+carObject.getCommand())
        print("Speed: "+ str(carObject.getSpeed()))
        print("Distance: "+str(carObject.getDistance()))
        print("Status: "+carObject.getStatus())


        return carObject


    
   
def testCase1():
    print("\nTest Case 1: detectObstacle() and stopCar()\n")

    testCar = Car("command",10,50,"obstacle")
    #Car object with status of "obstacle"
    cc = CarController
    #print the return of detectObstacle, True if detected, False if not
    print("Detect object: (T/F)" + str(cc.detectObstacle(testCar)))
    #print the status of car, (stopped) since detected obstacle
    print("Car status:"+testCar.getStatus())

def testCase2():
    print("\nTest Case 2: detectEndPoint() and stopCar() \n")
    testCar = Car("command",10,50,"completed")
    #Car object with status of "completed"
    cc = CarController
    #print the return of detectEndPoint, True if endpoint, False if not completed
    print("Detect end point: (T/F)" + str(cc.detectEndPoint(testCar)))
    #print the status of car, (stopped) since completed 
    print(testCar.getStatus())

def testCase3():
    print("\nTest Case 3: executeInstruction() \n")
    cc = CarController
    car = carData(command="up", speed=0,distance=0,status="executing")
    #carData object with the commands.
    cc.executeInstruction(car)
    #execute instruction will print details of car object.
    

def testCase4():
    print("\nTest Case 4: detectObstacle() and stopCar() \n")
    cc = CarController
    car = carData(command="left", speed=20,distance=60,status="executing")
    #carData object with the updated data.
    cc.sendData(car)
    #execute instruction will print details of car object.




        
        
        
    
    
    
    
testCase1()
testCase2()
testCase3()
testCase4()
        
        
        
    
    


