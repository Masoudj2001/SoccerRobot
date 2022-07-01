import math
import time
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

class PID:
    def __init__(self, kp=2, ki=0.0, kd=0.0, sample_time=0.01, current_time=None):
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0
        self.output = 0.0
        self.sample_time = sample_time
        self.current_time = current_time if current_time is not None else time.time()
        self.last_time = self.current_time

    def update(self, feedback_value, target ,current_time=None):
        error = target - feedback_value
        # print(error)
        self.current_time = current_time if current_time is not None else time.time()
        delta_time = self.current_time - self.last_time
        delta_error = error - self.last_error

        if delta_time >= self.sample_time:
            self.PTerm = self.Kp * error
            self.ITerm += error * delta_time
            
            self.DTerm = 0.0
            self.DTerm = delta_error / delta_time

            self.last_time = self.current_time
            self.last_error = error
            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

class Angular(PID):
    def __init__(self,des_pi):
        PID.__init__(self,-10, 0, 0)
        self.des_pi=des_pi
        self.pi=0
    def update_robot_pi(self,robot_pi):
        self.pi=robot_pi
        self.update(self.pi,self.des_pi)
    def motor_speed(self):
        return max(min(-self.output,10),-10),max(min(self.output,10),-10)
class MyRobot1(RCJSoccerRobot):
    def run(self):
        control = Angular(-1.57)
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()
                while self.is_new_team_data():
                    team_data = self.get_new_team_data()

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue
                control.update_robot_pi(self.get_compass_heading())
                vl,vr=control.motor_speed()
                self.left_motor.setVelocity(vl)
                self.right_motor.setVelocity(vr)