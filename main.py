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

		self.setStyleSheet("background-color: #2E3440;") 
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{RESOURCES_PATH}/images/what is this anime.jpg")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(300,300),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel)
		self.mainLayout.addSpacing(15)
		self.playButton = QtWidgets.QPushButton("スタート (Start)")
		self.playButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #67C240;
					color: white;
					border-radius: 5px;
					font-size: 16px;
					padding: 8px;
					font-family: Noto Serif JP;
					font-weight: bold;
				}
				QPushButton:hover{
					background-color: #ffa6c1;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.playButton.clicked.connect(self.clickPlay)
		self.mainLayout.addWidget(self.playButton)
		self.mainLayout.addSpacing(8)
		self.surrenderButton = QtWidgets.QPushButton("まける (Surrender)")
		self.surrenderButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FF4F4F;
					color: white;
					border-radius: 5px;
					font-size: 16px;
					padding: 8px;
					font-family: Noto Serif JP;
					font-weight: normal;
				}
				QPushButton:hover{
					background-color: #ffa6c1;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.surrenderButton.clicked.connect(self.close)
		self.mainLayout.addWidget(self.surrenderButton)
		self.mainLayout.addStretch()
		self.surrenderButton = QtWidgets.QPushButton("มันคืออะไรหรอ ?")
		self.surrenderButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #EBB438;
					color: white;
					border-radius: 5px;
					font-size: 16px;
					padding: 8px;
					font-family: Noto Serif JP;
					font-weight: normal;
				}
				QPushButton:hover{
					background-color: #ffa6c1;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.surrenderButton.clicked.connect(self.soraStage)
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

	def soraStage(self):
		self.close()

		global soraStage
		try :
			sora.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		
		soraStage = soraStage(parent = ptr)
		soraStage.show()
		
class Stage01(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setWindowTitle("Being otaku isn’t wrong")
		self.resize(300,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet("background-color: #2E3440;") 
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
		self.button01.setStyleSheet(
			'''
				QPushButton {
					background-color: #B35281;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.button02 = QtWidgets.QPushButton("俺妹")
		self.button02.clicked.connect(self.nextStage)
		self.button02.setStyleSheet(
			'''
				QPushButton {
					background-color: #E8CC07;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.button03 = QtWidgets.QPushButton("Моя сестрёнка не может быть такой милой!")
		self.button03.clicked.connect(self.nextStage)
		self.button03.setStyleSheet(
			'''
				QPushButton {
					background-color: #0960DB;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.button04 = QtWidgets.QPushButton("น้องสาวของผมไม่น่ารักขนาดนั้นหรอก")
		self.button04.clicked.connect(self.nextStage)
		self.button04.setStyleSheet(
			'''
				QPushButton {
					background-color: #DB094B;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.mainLayout.addSpacing(12)
		self.mainLayout.addWidget(self.button01)
		self.mainLayout.addWidget(self.button02)
		self.mainLayout.addWidget(self.button03)
		self.mainLayout.addWidget(self.button04)
		self.mainLayout.addStretch()
		
		self.noneButton = QtWidgets.QPushButton("ไม่มีข้อถูก")
		self.noneButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #000000;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

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
		self.setWindowTitle("I might fail, but at least I tried")
		self.resize(300,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet("background-color: #2E3440;") 
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{RESOURCES_PATH}/images/bocchi the rock.png")
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
		self.quiz01 = QtWidgets.QLabel("     ตัวละครจากรูปภาพดังกล่าวมีชื่อเรียกว่าอะไร")
		self.quiz01.setStyleSheet("font-size : 15px")
		self.mainLayout.addWidget(self.quiz01)

		self.button01 = QtWidgets.QPushButton("Bocchi The Rock!")
		self.button01.clicked.connect(self.nextStage)
		self.button01.setStyleSheet(
			'''
				QPushButton {
					background-color: #B35281;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.button02 = QtWidgets.QPushButton("Bocchi The Glock!")
		self.button02.clicked.connect(self.nextStage)
		self.button02.setStyleSheet(
			'''
				QPushButton {
					background-color: #E8CC07;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.button03 = QtWidgets.QPushButton("Bocchi The Rock Johnson With Glock!")
		self.button03.clicked.connect(self.nextStage)
		self.button03.setStyleSheet(
			'''
				QPushButton {
					background-color: #0960DB;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.button04 = QtWidgets.QPushButton("Bocchi The Fuck Is This")
		self.button04.clicked.connect(self.nextStage)
		self.button04.setStyleSheet(
			'''
				QPushButton {
					background-color: #DB094B;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

		self.mainLayout.addSpacing(12)
		self.mainLayout.addWidget(self.button01)
		self.mainLayout.addWidget(self.button02)
		self.mainLayout.addWidget(self.button03)
		self.mainLayout.addWidget(self.button04)
		self.mainLayout.addStretch()
		self.noneButton = QtWidgets.QPushButton("ไม่มีข้อถูก")
		self.noneButton.clicked.connect(self.loseStage)
		self.noneButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #000000;
					color: white;
				}
				QPushButton:hover{
					background-color: #67C240;
				}
				QPushButton:pressed{
				background-color: #ff7096;
				}
			''')

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
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle("Congratulations")
		self.resize(400, 400)
		self.setFixedSize(400, 400)
		self.setStyleSheet("background-color: #2E3440;") 
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.winLabel = QtWidgets.QLabel("สุดยอดคุณผ่านการทดสอบเเล้ว")
		self.winLabel.setStyleSheet(
			"""
    			font-family: "M PLUS Rounded 1c";
   		 		font-size: 24px;   
   		 		font-weight: bold;  
   				color: white;      
			""")
		self.winLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.winLabel)
		self.imageLabel = QtWidgets.QLabel()
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		gif_path = f"{RESOURCES_PATH}/images/evangelion.gif"
		self.movie = QtGui.QMovie(gif_path)
		if not self.movie.isValid():
			print("ไม่สามารถโหลด GIF ได้:", gif_path)

		self.imageLabel.setMovie(self.movie)
		self.movie.start()
		self.mainLayout.addWidget(self.imageLabel)

		self.set_gif_size(400, 300)

	def set_gif_size(self, width: int, height: int):
		set_size = QtCore.QSize(width, height)
		if set_size.isValid():
			self.movie.setScaledSize(set_size)
			
class loseStage(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle("God will not abandon you.")
		self.resize(300, 400)
		self.setFixedSize(300, 400)
		self.setStyleSheet("background-color: #2E3440;") 
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.winLabel = QtWidgets.QLabel("ยินดีด้วย คุณคือผู้บริสุทธิ์")
		self.winLabel.setStyleSheet(
			"""
    			font-family: "M PLUS Rounded 1c";
   		 		font-size: 24px;   
   		 		font-weight: bold;  
   				color: white;      
			""")
		self.winLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.winLabel)
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
			
class soraStage(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		
		self.setWindowTitle("เชื่อผมเรื่องนี้ดีจริง เเล้วเพื่อนของผมมีน้องสาว")
		self.resize(800,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet("background-color: #2E3440;") 
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{RESOURCES_PATH}/images/yosuga no sora.jpg")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(800,400),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel)
		self.anime = QtWidgets.QLabel("“แม้ความรักทางสายเลือดคือสิ่งต้องห้ามที่ไม่ควรแตะต้อง แต่หัวใจของสองเรามิอาจหยุดยั้งความรู้สึกนั้นได้ สายสัมพันธ์ของเราจะคงอยู่… ตราบเท่าที่หัวใจของเราสองยังคงรักกันชั่วนิรันดร์“")
		self.mainLayout.addWidget(self.anime)
		self.anime.setStyleSheet(
			"""
   		 		font-size: 15px;   
   		 		font-weight: mormal;  
   				color: white;      
			""")


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

