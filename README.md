# SoccerRobot
***

## Masoud Jafari 9823024
## Mohammadmasih Shalchian 9823051

In this homwork we controll a Robot for play soccer, and we must design the suitable compensator to trcking a certian feature 

### PID Compensator
***
In the code designed for controlling the robot, a PID controller class is used, So all 4 types of controllers (P, PI, PD, PID) are attainable by changing the gains in objects created from this class. This class uses a member variable called sample-time, as soon as delta-time reaches the sample-time, it calculates the PTerm, the DTerm (deviding the error by delta-time) and the ITerm (using error summation) and defines the output as the sum of all this terms.
A P controller output is proportional to the error its input by a kp gain, so there is no Overshoot, decrease rise time and SS(Steady State) error. A PI controller uses an integrator to eliminate the steady state error but increase the overshoot and settling time. A PD contoller uses a derivative block to decrease the setteling time and overshoot of the process. A PID contoller is mixture of all the controllers explained above and can be used to achieve critically damped response with minimum final error.
### Discretization
For disceteization of every section of the PID contoller we can use the ZOH method, which consists of sampler with specific frequency.
### Deadzone
Deadzones causes the process error to become larger (the motor does not respond until the input gets to a specific value). for example if the deadzone bound for our DC motor is 0.5 and we use a P contorller with kp=10, the errors lower than 0.05 correspond to a value lowers than 0.5 for motor input.
## 1D Controller
***
### Code Functionality
In this section the user set the x_position and and robot must go to the desire y_position with small overshhot and fast.
## Angular Controller
***
### Code Functionality

