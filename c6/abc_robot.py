#abcモジュールの取り込み
from abc import ABCMeta, abstractmethod

#基底抽象クラスの定義
class MazeRobot(metaclass=ABCMeta):

	@abstractmethod
	def init_robot(self): pass
	
	@abstractmethod
	def choose_dir(self): pass
