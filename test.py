from car import carData,Car,CarController

def testCase1():
    print("\nTest Case 1: detectObstacle() and stopCar()\n")
    #Car object with status of "obstacle"
    carA = Car("command",10,50,"obstacle")
    #Car object with status of "executing"
    carB = Car("command",10,50,"executing")
    cc = CarController

    try:
        assert cc.detectObstacle(carA), "Car A: No obstacles detected"
        print("Car A: Obstacle detected")
        assert cc.detectObstacle(carB), "Car B: No obstacles detected"
        print("Car B: Obstacle detected")

    except AssertionError as msg:
        print(msg)

    try:
        assert carA.getStatus() == "stopped", "Car A: still moving"
        print("Car A: has stopped")
        assert carB.getStatus() == "stopped", "Car B: still moving"
        print("Car B: has stopped")        

    except AssertionError as msg:
        print(msg)

def testCase2():
    print("\nTest Case 2: detectEndPoint() and stopCar() \n")
    #Car object with status of "completed"
    carA = Car("command",10,50,"completed")
    #Car object with status of "executing"
    carB = Car("command",10,50,"executing")
    cc = CarController

    try:
        assert cc.detectEndPoint(carA), "Car A: still executing"
        print("Car A: completed instruction")
        assert cc.detectEndPoint(carB), "Car B: still executing"
        print("Car B: completed instruction")

    except AssertionError as msg:
        print(msg)

    try:
        assert carA.getStatus() == "stopped", "Car A: still moving"
        print("Car A: has stopped")
        assert carB.getStatus() == "stopped", "Car B: still moving"
        print("Car B: has stopped")        

    except AssertionError as msg:
        print(msg)


def testCase3():
    print("\nTest Case 3: executeInstruction() \n")
    cc = CarController
    #carData object with the up command.
    car = carData(command="up", speed=0,distance=0,status="executing")
    carObject = cc.executeInstruction(car)
    try:
        assert carObject.getCommand()=="up", "command not == 'up'"
        print("Car executed instruction")
        print("Command: "+carObject.getCommand())
        print("Speed: "+str(carObject.getSpeed()))
        print("Distance: "+str(carObject.getDistance()))
        print("Status: "+carObject.getStatus())

    except AssertionError as msg:
        print(msg)
    

def testCase4():
    print("\nTest Case 4: sendData() \n")
    cc = CarController
    #carData object with the commands
    car = carData(command="left", speed=20,distance=60,status="executing")
    carObject = cc.sendData(car)
    try:
        assert (carObject.getCommand()== "left"and carObject.getSpeed()==20 and carObject.getDistance()==60),"Data not sent"
        print("Car data sent successfully")
        print("Command: "+carObject.getCommand())
        print("Speed: "+str(carObject.getSpeed()))
        print("Distance: "+str(carObject.getDistance()))
        print("Status: "+carObject.getStatus())

    except AssertionError as msg:
        print(msg)

    
    
testCase1()
testCase2()
testCase3()
testCase4()