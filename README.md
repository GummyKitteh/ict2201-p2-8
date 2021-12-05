# Wreckvee - Robotic Car with Web Interface
Our Team:

(Yip Jia Cheng - JCBlitzNight) - Tech Lead

(Kho Wen Jie - GummyKitteh)

(Muhamad Suhaili Bin Suri - suhailii)

(Ain Munirah Binte Makmor - ainmm00)

## How to Run
- Install Python (at least Version 3.6)
- Open command prompt in Administrator
- Navigate command prompt to directory containing requirements.txt and app.py
- Run `pip install -r requirements.txt` to install required modules
- Run `python app.py` to run portal and keep command prompt running
- Open Internet Edge or Google Chrome and enter the URL `http://localhost:5000/`

## Development Workflow
All development work is done on each team member's individual feature branch. Each team member will be working on their allocated features on their individual feature branch. An additional `Document branch` was created to allow all members to modify the `README.md` on this branch. To merge into `dev branch`, a member has to open a pull request on Github which will be reviewed by either Jia Cheng (Tech Lead) or Wen Jie (Assistant Tech Lead). Only Jia Cheng will be allowed to merge `dev branch` into `master branch`. The main reason for allocating several features to an individual branch is for ease of tracking pertaining to M3 grading. Since it is an extremely small project, creating a huge number of branches may in fact harm the implementation proccess instead.

<img src="https://user-images.githubusercontent.com/90367927/144000696-f2e36988-a9ba-4cb5-a3cd-8cd8de243464.png" width="550" height="650">

Each team member were assigned an individual feature branch to work on their allocated features as shown below:
| Branch | Allocated Features |
| --- | --- |
| wenjiekho |<ul><li>Dashboard Page</li><li>Storing Instruction History</li><li>Display Sensor Data</li></ul>|
| jiacheng |<ul><li>Challenge Page</li><li>Connect Page</li><li>Blockly Coding Enviroment</li><li>Tutorial</li><li>Log out</li><li>Answer Checking</li><li>Display hint</li></ul>|
| suhaili |<ul><li>Backend Coding Implementation</li><li>System Integration</li></ul>|
| ain |<ul><li>View Challenges Page</li><li>Maze Map Design & Generation</li><li>View Answer</li></ul>|


## User Acceptance Test
- Embedded video running through all system test case we created (refined test case), 3 minutes long covering all system test case

## Whitebox Testing
- Conducted Whitebox Testing on the CarController class which interacts with multiple classes, Car, Instruction and CarIO.
- 4 test cases on the CarController class(car.py) which is located in test.py.
- Test case 1: 
    - Testing detectObstacle() and stopCar()
![IMAGE 2021-12-05 02:42:01](https://user-images.githubusercontent.com/74708728/144720928-170cae23-485f-4546-b781-cb4c5910eb5a.jpg)
- Test case 2:
    -  Testing detectEndPoint() and stopCar()
![IMAGE 2021-12-05 02:42:38](https://user-images.githubusercontent.com/74708728/144720953-a72c4488-c4c4-4f82-acc8-4a6ddbf14c6c.jpg)
- Test case 3:
    -  Testing executeInstruction
![IMAGE 2021-12-05 02:43:02](https://user-images.githubusercontent.com/74708728/144720962-e074eb6b-9c4e-418e-aa7b-22569cd45afd.jpg)
- Test case 4:
    -  Testing sendData()
![IMAGE 2021-12-05 02:43:14](https://user-images.githubusercontent.com/74708728/144720972-98f11fbd-3de5-4378-b13e-24331923a07a.jpg)

 Coverage information generated using Coverage.py:
> Coverage.py measures code coverage, typically during test execution.
> It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.
- Steps to run test suite:
    - Install coverage for python:
    ```
    pip install coverage
    ```
    - Enter project folder:
    ```
    cd ict2201-p2-8
    ```
    - Run the testcase:
    ```
    coverage run test.py
    ```
    - Generate the coverage report: 
    ```
    coverage report
    ```


https://user-images.githubusercontent.com/74708728/144734922-b2413401-d4c4-421f-8ae4-d60333d50b91.mp4
`
