try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance

except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import importlib
import maya.OpenMayaUI as omui
import os 
from . import config
importlib.reload(config)
RESOURCES_PATH = os.path.join(os.path.dirname(__file__),'resources').replace("\\","/")

class Oreimo(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.setWindowTitle("I am the bone of my sword")
		self.resize(300,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{RESOURCES_PATH}/images/name_game.png")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(128,128),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setStyleSheet("background-color: 0;")
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel)

		self.playButton = QtWidgets.QPushButton("Start")
		self.playButton.clicked.connect(self.clickPlay)
		self.mainLayout.addWidget(self.playButton)
		self.surrenderButton = QtWidgets.QPushButton("Close")
		self.surrenderButton.clicked.connect(self.close)
		self.mainLayout.addWidget(self.surrenderButton)
		self.mainLayout.addStretch()

	def clickPlay(self):
		self.close()

		global stage01
		try :
			stage01.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		
		stage01 = Stage01(parent = ptr)
		stage01.show()

class Stage01(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setWindowTitle("I am the bone of my sword")
		self.resize(300,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{RESOURCES_PATH}/images/oreimo.jpg")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(300,300),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setStyleSheet("background-color: 0;")
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel)

		self.mainLayout.addSpacing(8)
		self.quiz01 = QtWidgets.QLabel("ตัวละครจากรูปภาพดังกล่าวมาจากอนิเมะเรื่องอะไร")
		self.quiz01.setStyleSheet("font-size : 15px")
		self.mainLayout.addWidget(self.quiz01)

		self.button01 = QtWidgets.QPushButton("Ore no Imōto ga Konna ni Kawaii Wake ga Nai")
		self.button01.clicked.connect(self.nextStage)
		self.button02 = QtWidgets.QPushButton("俺妹")
		self.button02.clicked.connect(self.nextStage)
		self.button03 = QtWidgets.QPushButton("Моя сестрёнка не может быть такой милой!")
		self.button03.clicked.connect(self.nextStage)
		self.button04 = QtWidgets.QPushButton("น้องสาวของผมไม่น่ารักขนาดนั้นหรอก")
		self.button04.clicked.connect(self.nextStage)

		self.mainLayout.addSpacing(12)
		self.mainLayout.addWidget(self.button01)
		self.mainLayout.addWidget(self.button02)
		self.mainLayout.addWidget(self.button03)
		self.mainLayout.addWidget(self.button04)

		self.mainLayout.addStretch()

		self.noneButton = QtWidgets.QPushButton("ไม่มีข้อถูก")
		self.noneButton.clicked.connect(self.loseStage)
		self.mainLayout.addWidget(self.noneButton)

	def nextStage(self):
		self.close()

		global stage02
		try :
			stage02.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		
		stage02 = Stage02(parent = ptr)
		stage02.show()

	def loseStage(self):
		self.close()

		global loseStage
		try :
			loseStage.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		
		loseStage = loseStage(parent = ptr)
		loseStage.show()

class Stage02(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setWindowTitle("I am the bone of my sword")
		self.resize(300,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{RESOURCES_PATH}/images/mambo.png")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(128,128),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setStyleSheet("background-color: 0;")
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel)

		self.quiz01 = QtWidgets.QLabel("บลาๆาาๆ2")
		self.mainLayout.addWidget(self.quiz01)

		self.button01 = QtWidgets.QPushButton("Oreimo")
		self.button01.clicked.connect(self.nextStage)
		self.button02 = QtWidgets.QPushButton("俺の妹")
		self.button02.clicked.connect(self.nextStage)
		self.button03 = QtWidgets.QPushButton("awfawfa")
		self.button03.clicked.connect(self.nextStage)
		self.button04 = QtWidgets.QPushButton("aykykygdgt")
		self.button04.clicked.connect(self.nextStage)

		self.mainLayout.addStretch()
		self.mainLayout.addWidget(self.button01)
		self.mainLayout.addWidget(self.button02)
		self.mainLayout.addWidget(self.button03)
		self.mainLayout.addWidget(self.button04)

		self.mainLayout.addStretch()

		self.noneButton = QtWidgets.QPushButton("ไม่มีข้อถูก")
		self.noneButton.clicked.connect(self.loseStage)
		self.mainLayout.addWidget(self.noneButton)
	
	def nextStage(self):
		self.close()

		global winStage
		try :
			winStage.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		
		winStage = winStage(parent = ptr)
		winStage.show()

	def loseStage(self):
		self.close()

		global loseStage
		try :
			loseStage.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		
		loseStage = loseStage(parent = ptr)
		loseStage.show()

class winStage(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.setWindowTitle("I am the bone of my sword")
		self.resize(300,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.winLabel = QtWidgets.QLabel("Stand Proud you are strong")
		self.mainLayout.addWidget(self.winLabel)

	def run():
		global ui
		try :
			ui.close()
			stage01.close()
			stage02.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		ui = Oreimo(parent = ptr)
		ui.show()

# class loseStage(QtWidgets.QDialog):
# 	def __init__(self, parent = None):
# 		super().__init__(parent)

# 		self.setWindowTitle("I am the bone of my sword")
# 		self.resize(300,500)
# 		self.mainLayout = QtWidgets.QVBoxLayout()
# 		self.setLayout(self.mainLayout)
# 		self.winLabel = QtWidgets.QLabel("กูเหลือจะเชื่อ")
# 		self.mainLayout.addWidget(self.winLabel)
		
# 		self.mainLayout.addStretch()
# 		self.imageLabel = QtWidgets.QLabel(self)
# 		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
# 		# self.imageLabel.setScaledContents(True)

# 		movie = f"{RESOURCES_PATH}/images/ayase.gif"
# 		self.movie = QtGui.QMovie(movie)
# 		resize = self.movie.setScaledSize(QtCore.QSize(10,200))
# 		self.imageLabel.setPixmap(resize)
# 		self.imageLabel.setMovie(self.movie)
# 		self.movie.start()

	


class loseStage(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle("I am the bone of my sword")
		self.resize(300, 500)
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.winLabel = QtWidgets.QLabel("กูเหลือจะเชื่อ")
		self.winLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.winLabel)

		self.mainLayout.addStretch()

		self.imageLabel = QtWidgets.QLabel()
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		gif_path = f"{RESOURCES_PATH}/images/ayase.gif"
		self.movie = QtGui.QMovie(gif_path)
		if not self.movie.isValid():
			print("ไม่สามารถโหลด GIF ได้:", gif_path)

		self.imageLabel.setMovie(self.movie)
		self.movie.start()
		self.mainLayout.addWidget(self.imageLabel)

		self.set_gif_size(300, 300)

	def set_gif_size(self, width: int, height: int):
		set_size = QtCore.QSize(width, height)
		if set_size.isValid():
			self.movie.setScaledSize(set_size)
			
def run():
		global ui
		try :
			ui.close()
			stage01.close()
			stage02.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		ui = Oreimo(parent = ptr)
		ui.show()