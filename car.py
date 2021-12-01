# class Instruction:
import sys


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

    def setCommand(self,command):
        self.command = command
        return 

    def setSpeed(self,speed):
        self.speed = speed
        return 

    def setDistance(self,distance):
        self.distance = distance
        return 

    def setStatus(self,status):
        self.status = status
        return 



class CarController:
    def stopCar():
        Car.setStatus("stopped")
        return

    def detectObstacle(car0):
        if car0.getStatus() == "obstacle":
            print('OBSTACLE DETECTED!')
            CarController.stopCar()
            return True
        else:
            print("NO OBSTACLE")
            return False

        
        

    def detectEndPoint(self): #not needed?
        if Car.getStatus == "completed":
            return True
        else:
            return False

    

    def executeInstruction(request, carData, db):
        postData = request.form
        json = str(postData['command'])
        car = carData(command=json, speed="0",distance="0",status="executing") 
        db.session.query(carData).delete()
        db.session.commit()
        db.session.add(car)
        db.session.commit()
            
        return 
    
    def sendData(request, carData, db):
        command = request.args.get('command')
        speed = request.args.get('speed')
        distance = request.args.get('distance')
        status = request.args.get('status')
        car = carData(command=command,speed=speed,distance=distance,status=status)
        db.session.query(carData).delete()
        db.session.commit()
        db.session.add(car)
        db.session.commit()

        return


    
   
# def testCase1():
#     testCar = Car("command",10,50,"obstacle")
#     cc = CarController
#     print(cc.detectObstacle(testCar))
#     print(testCar.getStatus())



        
        
        
    
    
    
    
# testCase1()  


    

