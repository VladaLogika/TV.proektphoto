from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QListWidget, QLabel, QFileDialog
app = QApplication([])

window = QWidget()
window.setWindowTitle('Easy  editor')
window.resize(700,600)
window.move(300,90)

workdir = ""

def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   folder1()
   filenames = filter(os.listdir(workdir), extensions)
   listimg.clear()
   for filename in filenames:
       listimg.addItem(filename)


def folder1():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   folder1()
   filenames = filter(os.listdir(workdir), extensions)
   listimg.clear()
   for filename in filenames:
       listimg.addItem(filename)
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result



folder = QPushButton()
folder.setText('Папка')

listimg = QListWidget()
winning = QLabel()
winning.setText("Типу картинка")


lineH = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH1 = QHBoxLayout()

buttLeft = QPushButton()
buttLeft.setText('Вліво')
buttRight = QPushButton()
buttRight.setText('Вправо')
mir = QPushButton()
mir.setText('Дзеркально')
buttRR = QPushButton()
buttRR.setText("Різкість")
buttBW = QPushButton()
buttBW.setText("Ч\Б")



lineH1.addWidget(buttLeft)
lineH1.addWidget(buttRight)
lineH1.addWidget(mir)
lineH1.addWidget(buttRR)
lineH1.addWidget(buttBW)


lineV1.addWidget(folder)
lineV1.addWidget(listimg)
lineV2.addWidget(winning)

lineH.addLayout(lineV1, 20)
lineH.addLayout(lineV2, 80)
lineV2.addLayout(lineH1)


folder.clicked.connect(folder1)
window.setLayout(lineH)
window.show()
app.exec_()