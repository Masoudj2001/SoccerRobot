# SoccerRobot
***

### Masoud Jafari 9823024
### Mohammadmasih Shalchian 9823051

we program this project together
The purpose in this project is to design a controller and an algorithm for two soccer robots to play against the same team and prevent scoring and score goals if possible.

## Astrategy And Algorithm
***
### Defender
At first, the defender robot stands in front of the blue goal with `class GotoXY` (position (0,0.7)) and if the ball enters the penalty box, the robot moves towards it with `class TraceBall` and hits with 10 velocity it to make the ball go away.
### Attacker
The attacker goes behind the ball with `class TraceBall` and stands towards the yellow goal and hits the ball, and the approach is to trace the ball and hit the ball towards the goal until the ball becomes a goal.


