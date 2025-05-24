from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QRadioButton,
        QVBoxLayout, QGroupBox, 
        QButtonGroup, QPushButton,
        QLabel,
        )
from random import *
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('какой дан сложнее?', 'theta dan', 'delta dan', '10th dan', 'zeta dan'))
question_list.append(Question('привет', 'Operatin Zenithfall', 'OOPart', 'Parallel univers shifter', 'Hello (BPM) 2024' ))
question_list.append(Question('сколько нужно аккуратности что бы клирнуть 4k Dan ~ REFORM ~', '96%', '100%', '90%', '99%'))
app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def start_test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно Пупс!')
        Window.score += 1
        statistic()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('На колени на колени!')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignHCenter))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=25, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
AnsGroupBox.hide()
layout_quest = QHBoxLayout()

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=2)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def next_question():
    Window.total += 1
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)
    
    statistic()

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def statistic():
    print('Статистика')
    print('Всего вопросов:', Window.total)
    print('Правильных ответов:', Window.score)
    print('Рейтинг:', (Window.score / Window.total) * 100)

Window = QWidget()
Window.setLayout(layout_card)
Window.setWindowTitle('Memory Card')
  
#Window.cur_question = -1

btn_OK.clicked.connect(click_OK)
Window.score = 0
Window.total = 0
next_question()
Window.show()
app.exec_()