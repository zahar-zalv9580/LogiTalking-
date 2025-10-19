from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog
from PIL import Image
from PIL import ImageFilter

app = QApplication([])
win = QWidget
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel('Картинка')
btn_folder = QPushButton('Папка')
list_files = QListWidget()


btn_left = QPushButton('Ліворуч')
btn_right = QPushButton('Праворуч')
btn_mirror = QPushButton('Відзеркалити')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('Ч/Б')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_folder)
col1.addWidget(list_files)
col2.addWidget(lb_image)
row_btn = QHBoxLayout()
row_btn.addWidget(btn_left)
row_btn.addWidget(btn_right)
row_btn.addWidget(btn_mirror)
row_btn.addWidget(btn_sharp)
row_btn.addWidget(btn_bw)
col2.addLayout(row_btn)
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.show()

workfolder =  ''
def filter(files, extensions):
    result=[]
    for filename in files: 
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
        return result

def chooseWorkdir():
    global Workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenameList():
    extension = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    filename = filter(os.listdir(workdir),extensions)
list_files.clear()
for filename in filenames:
    list_files.addItem(filename)
btn_folder.clicked.connect(showFilenameList)

class ImageChanger():
    def __init__(self):
        self.image = None
        self.dir  = None
        self.filename = None
        self.save_dir = 'Modificated/'
    def loadImage(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
    def do_bw(self):
        self.image = self.image.convert('L')
        
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def showImage(self):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scale(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()