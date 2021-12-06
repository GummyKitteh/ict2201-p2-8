
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
            CarController.stopCar(carObj)
            return True
        else:
            return False

    def detectEndPoint(carObj): 
        if carObj.getStatus() == "completed":
            CarController.stopCar(carObj)
            return True
        else:
            return False

    def executeInstruction(carData):
        carObject = Car(carData.command,0,0,"executing")

        return carObject
    
    def sendData(carData):
        carObject = Car(carData.command,carData.speed,carData.distance,carData.status)

        return carObject

        
    
    


