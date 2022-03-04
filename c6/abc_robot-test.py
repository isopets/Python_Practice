from abc_robot import MazeRobot

class MazeRobotTest(MazeRobot):

	def init_robot(self):
		print("ロボットを初期します")
	def choose_dir(self):
		print("前進します")

robot = MazeRobotTest()
robot.init_robot()
