from math import sin, cos, pi, tan


class Robot:
    def __init__(self, x, y, angle, max_vel, wheel_radius):
        # x (meters), y (meters), angle (rad), m/s, meters
        self.x = x
        self.y = y
        self.angle = angle
        self.max_vel = max_vel
        self.wheel_radius = wheel_radius
        self.right_vel, self.left_vel = 0, 0

    def turn_to(self, new_theta):
        d_theta = self.angle - new_theta
        if d_theta >= 0:
            time = -(d_theta * self.wheel_radius) / self.max_vel
            self.right_vel = -self.max_vel
            self.left_vel = self.max_vel
        else:
            time = -(d_theta * self.wheel_radius) / self.max_vel
            self.right_vel = self.max_vel
            self.left_vel = -self.max_vel
        self.angle = new_theta
        return time

    def get_pose(self):
        return self.x, self.y, self.angle


def main():
    Robbie = Robot(0, 0, 0, 4, 4)
    print(Robbie.turn_to(pi))
    print(Robbie.right_vel, Robbie.left_vel)
    print(Robbie.get_pose())



if __name__ == '__main__':
    main()
