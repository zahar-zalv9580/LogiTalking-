from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton,QHBoxLayout, QVBoxLayout, QListWidget, QFormLayout, QGroupBox, QSpinBox, QButtonGroup

app = QApplication([])
win = QWidget()
btn_menu = QPushButton("Меню")
btn_pause = QPushButton("Пауза")
box_minutes = QSpinBox()
box_minutes.setValue(30)
btn_answer = QPushButton("Відповісти")
lb_qustion = QLabel("")

radioGroupBox = QGroupBox("Варіанти відповідей")
radioGroup = QButtonGroup()
rbtn_1 = QRadioButton("")
rbtn_2 = QRadioButton("")
rbtn_3 = QRadioButton("")
rbtn_4 = QRadioButton("")

ansGroup=QGroupBox("Результат")
lb_Result = QLabel("")
lb_Correct = QLabel("")
radioGroup.addButton(rbtn_1)
radioGroup.addButton(rbtn_2)
radioGroup.addButton(rbtn_3)
radioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_pause)
layout_line1.addWidget(box_minutes)
layout_line1.addWidget(QLabel("хвилини"))

layout_line2.addWidget(lb_qustion)
layout_line3.addWidget(radioGroupBox)
layout_line4.addWidget(btn_answer)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addLayout(layout_line4, stretch=1)

def show_answer():
    radioGroupBox.hide()
    ansGroup.show()
    btn_answer.setText("Наступне запитання")
def show_question():
    radioGroupBox.show()
    ansGroup.hide()
    btn_answer.setText("Відповісти")
    radioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radioGroup.setExclusive(True)
    

win.show()
app.exec_()




