# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from os import mkdir, path
# from pathlib import Path


# const
faviconFile = 'favicon.png'
mainWindowTitle = 'Тест 4 КДСО (1.1)'
# MainWindow dimensions
mainWindowWidth = 700
mainWindowHeight = 670
# MainWindow position
mainWindowXPos = 100
mainWindowYPos = 200
# init data directory and name file
initFilePath = '.\\'
initFileName = 'cards.txt'
# user work directory and extension file
# if path.isdir('userData'):
#     pass
# else:
#     mkdir('userData')
userFilePath = '.\\'
# userFilePath = '.\\userData\\'
userFileExtension = '.txt'
# fonts for labels for <label>.setFont()
# fontMain = QFont('Arial', 16)

# text for labels
textHintHead = '<html><b>Инструкция</b></html>'

textMainPreTest1 = str('<html>' +
                '<p>Прочитайте инструкцию ниже </p>' +
                '<p>Затем нажмите [Блок #1]</p>' +
                '</html>')
textHintPreTest1 = str('<html>' +
                '<p>Вверху окна вам будут показываться ' +
                'слова-прилагательные</p>' +
                '</html>')
textHintTest1 = str('<html>' +
                '<p>- прочитайте слово</p>' +
                '<p>- нажмите кнопку [Знакомое], если вы знаете/слышали ' +
                'это слово</p>' +
                '<p>- нажмите кнопку [Незнакомое], если это слово вам ' +
                'незнакомо/непонятно</p>' +
                '</html>')
textMainPreTest2 = str('<html>' +
                '<p>Блок #1 пройден</p>' +
                '<p>Теперь прочитайте инструкцию ниже</p>' +
                '<p>Затем нажмите [Блок #2]</p>' +
                '</html>')
textHintPreTest2 = str('<html>' +
                '<p>Вверху окна вам будут показываться ' +
                'слова-прилагательные, которые вы выбрали как знакомые</p>' +
                '</html>')
textHintTest2 = str('<html>' +
                '<p>- прочитайте слово. ' +
                'Представьте, к какой части тела оно подойдет или с какой ' +
                'частью тела оно ассоциируется<br/>' +
                '- нажмите кнопку [Новая часть тела] и напишите туда часть ' +
                'тела, с которой соотносится это слово. ' +
                'Например: <i>ноги, голова, руки, живот, всё тело, ' +
                'зубы, душа</i> и т.д. Придумайте своё<br/>' +
                '- нажмите [Ок]<br/>' +
                '- каждое следующее новое слово относите к какой-то части ' +
                'тела, при этом вы можете выбирать созданные ранее группы и ' +
                'создавать новые, в том числе группу <i>"никуда"</i></p>' +
                '</html>')
textMainPreTest3 = str('<html>' +
                '<p>Блок #2 пройден</p>' +
                '<p>Теперь прочитайте инструкцию ниже</p>' +
                '<p>Затем нажмите [Блок #3]</p>' +
                '</html>')
textHintPreTest3 = str('<html>' +
                '<p>Вверху окна вам будут показываться ' +
                'слова-прилагательные, которые вы выбрали как знакомые. ' +
                'Их нужно разделить на 2 группы по любому признаку, ' +
                'какой вы придумаете сами. Например: <i>"сложное" и ' +
                '"простое", "движение" и "покой", "боль" и "радость", ' +
                '"могу управлять" и "не могу управлять"</i> ' +
                'и т.д. Подумайте о том, как бы вы могли разделить все эти ' +
                'слова на 2 группы</p>' +
                '</html>')
textHintTest3 = str('<html>' +
                '<p>- прочитайте слово. Мысленно отнесите это слово к одной из ' +
                '2 придуманных групп<br/>' +
                '- нажмите кнопку [Новая группа] и дайте ей название<br/>' +
                '- каждое следующее слово относите к заданной 1 группе ' +
                'или ко 2 группе<br/>' +
                '- вторую группу вы можете создать нажатием на кнопку ' +
                '[Новая группа]</p>' +
                '<p>! Помните, что создать можно будет только 2 группы</p>' +
                '</html>')
textMainPreTest4 = str('<html>' +
                '<p>Блок #3 пройден</p>' +
                '<p>Теперь прочитайте инструкцию ниже</p>' +
                '<p>Затем нажмите [Блок #4]</p>' +
                '</html>')
textHintTest4 = str('<html>' +
                '<p>- прочитайте слово<br/>' +
                '- нажмите кнопку [Голод], если это слово напоминает вам ' +
                'состояние, когда вы были очень голодны<br/>' +
                '- нажмите кнопку [Холод], если это слово напоминает вам ' +
                'состояние, когда вы замерзли<br/>' +
                '- нажмите кнопку [Боль], если это слово напоминает вам ' +
                'состояние, когда у вас что-то болит или получена травма<br/>' +
                '- нажмите кнопку [Никуда], если не можете никуда отнести это ' +
                'слово</p>' +
                '</html>')
textMainEndTest4 = str('<html>' +
                '<p>Блок #4 пройден</p>' +
                '<p>Теперь прочитайте инструкцию ниже, как отправить мне ' +
                'результат</p>' +
                '</html>')

# UI for Main window
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # work variables
        self.currentTest = 0
        self.userName = ''

        self.initDataList = []  # init data
        self.workKeysList = []  # data keys from user file
        self.endKeyPos = 0      # end position member in workKeysList
        self.currentKeyPos = 0  # current position member in workKeysList
        self.resultDataList =[]

        self.listCBTest2 = [] # список категорий из теста №2
        self.listCBTest3 = [] # список категорий из теста №2

        
        self.initUI()
        self.show() # drawing MainWindow

# windows UI
    def initUI(self): # creation Gui depending on the flags
        self.createMainWindow()
        # buttons
        self.btnStart = QPushButton('', self)
        self.btnOn(self.btnStart, 'Войти')
        self.setBtn(self.btnStart, 170, 355, 'Arial', 10)
        self.btnStart.clicked.connect(self.startTests)

        self.btnStartTest1 = QPushButton('', self) #Блок #1
        self.setBtn(self.btnStartTest1, 170, 155, 'Arial', 10)
        self.btnStartTest1.clicked.connect(self.test1)
        self.btnOff(self.btnStartTest1)

        self.btnTest1Known = QPushButton('', self)
        self.setBtn(self.btnTest1Known, 350, 155, 'Arial', 10)
        self.btnTest1Known.clicked.connect(self.test1Known)
        self.btnOff(self.btnTest1Known)

        self.btnTest1Unknown = QPushButton('', self)
        self.setBtn(self.btnTest1Unknown, 530, 155, 'Arial', 10)
        self.btnTest1Unknown.clicked.connect(self.test1Unknown)
        self.btnOff(self.btnTest1Unknown)

        self.btnStartTest2 = QPushButton('', self)
        self.setBtn(self.btnStartTest2, 170, 205, 'Arial', 10)
        self.btnStartTest2.clicked.connect(self.test2)
        self.btnOff(self.btnStartTest2)

        self.btnTest2New = QPushButton('', self)
        self.setBtn(self.btnTest2New, 350, 205, 'Arial', 10)
        self.btnTest2New.clicked.connect(self.test2New)
        self.btnOff(self.btnTest2New)

        self.btnStartTest3 = QPushButton('', self)
        self.setBtn(self.btnStartTest3, 170, 255, 'Arial', 10)
        self.btnStartTest3.clicked.connect(self.test3)
        self.btnOff(self.btnStartTest3)

        self.btnTest3New = QPushButton('', self)
        self.setBtn(self.btnTest3New, 350, 255, 'Arial', 10)
        self.btnTest3New.clicked.connect(self.test3New)
        self.btnOff(self.btnTest3New)

        self.btnStartTest4 = QPushButton('', self)
        self.setBtn(self.btnStartTest4, 170, 305, 'Arial', 10)
        self.btnStartTest4.clicked.connect(self.test4)
        self.btnOff(self.btnStartTest4)

        self.btnTest4Cold = QPushButton('', self)
        self.setBtn(self.btnTest4Cold, 350, 305, 'Arial', 10)
        self.btnTest4Cold.clicked.connect(self.test4Cold)
        self.btnOff(self.btnTest4Cold)

        self.btnTest4Hunger = QPushButton('', self)
        self.setBtn(self.btnTest4Hunger, 530, 305, 'Arial', 10)
        self.btnTest4Hunger.clicked.connect(self.test4Hunger)
        self.btnOff(self.btnTest4Hunger)

        self.btnTest4Pain = QPushButton('', self)
        self.setBtn(self.btnTest4Pain, 350, 355, 'Arial', 10)
        self.btnTest4Pain.clicked.connect(self.test4Pain)
        self.btnOff(self.btnTest4Pain)

        self.btnTest4Nowhere = QPushButton('', self)
        self.setBtn(self.btnTest4Nowhere, 530, 355, 'Arial', 10)
        self.btnTest4Nowhere.clicked.connect(self.test4Nowhere)
        self.btnOff(self.btnTest4Nowhere)

        # labels
        self.mainLabel = QLabel('Нажмите кнопку [Войти]', self)
        self.setLabel(self.mainLabel, 540, 100, 80, 20,
                            'Arial', 16, 'wrap', 'center')

        self.hintLabel = QLabel('', self)
        self.setLabel(self.hintLabel, 640, 255, 30, 395,
                            'Arial', 12, 'wrap')

        # combo boxes
        self.comboBoxTest2 = QComboBox(self)
        self.setComboBox(self.comboBoxTest2,
                        self.listCBTest2, 530, 205)
        self.comboBoxTest2.addItems(self.listCBTest2)
        self.comboBoxTest2.activated[str].connect(self.onActivatedCBTest2)
        self.comboBoxOff(self.comboBoxTest2)

        self.comboBoxTest3 = QComboBox(self)
        self.setComboBox(self.comboBoxTest3,
                        self.listCBTest3, 530, 255)
        self.comboBoxTest3.activated[str].connect(self.onActivatedCBTest3)
        self.comboBoxOff(self.comboBoxTest3)

    def createMainWindow(self):
        self.setFixedSize(mainWindowWidth, mainWindowHeight)
        # self.move(mainWindowXPos, mainWindowYPos)
        self.center()
        self.setWindowTitle(mainWindowTitle)
        self.setWindowIcon(QIcon(faviconFile))

# modify properties of elements (buttons, labels, combo boxrs, etc.)
    def center(self):
        fg = self.frameGeometry()
        c = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(c)
        self.move(fg.topLeft())

    def setBtn(self, btn, posX, posY,
                fontName, fontSize): # set button in window
        font = QFont(fontName, fontSize)
        btn.setFont(font)
        btn.resize(125, 25) # btn.sizeHint()
        btnWidth = btn.width()
        btnHeight = btn.height()
        btn.move(posX - btnWidth / 2, posY - btnHeight / 2)

    def setLabel(self, label, width, height,
                posX, posY, fontName, fontSize,
                flag1=None, flag2=None): # set label in window
        label.resize(width, height)
        label.move(posX, posY)
        font = QFont(fontName, fontSize)
        label.setFont(font)
        if flag1 == 'wrap':
            label.setWordWrap(True)
        if flag2 == 'center':
            label.setAlignment(Qt.AlignCenter)

    def setComboBox(self, combo, list, posX, posY):
        combo.addItems(list)
        combo.resize(125, 25)
        comboWidth = combo.width()
        comboHeight = combo.height()
        combo.move(posX - comboWidth / 2, posY - comboHeight / 2)

    def btnOn(self, btn, name):
        btn.setText(name)
        btn.setDisabled(False)

    def btnOff(self, btn):
        btn.clearFocus()
        btn.setText('')
        btn.setDisabled(True)

    def comboBoxOn(self, comboBox):
        comboBox.setDisabled(False)

    def comboBoxOff(self, comboBox):
        comboBox.clearFocus()
        comboBox.setDisabled(True)

    def setMainLabelText(self, label, text):
        label.setText(text)

# main programm logig
    def startTests(self):
        # check user (authorization), switch state
        oldUser = self.userExist()
        if oldUser == 'cancel':
            pass
        elif oldUser == True:
            self.initState('userExist')
        elif oldUser == False:
            self.initState('startTest1')

# work with state
    def initState(self, flag): # set current state
        self.btnOff(self.btnStart)
        if flag == 'userExist':
            finished = self.checkTestFinished()
            if finished == 'test4':
                self.mainLabel.setText(textMainEndTest4)
                self.hintLabel.setText(textHintHead +
                        str('<html>' +
                        '<p>Ваши результаты сохранены в файле, который ' +
                        'называется ' + self.userName + '.txt</p>' +
                        '<p>Этот файл находится в той же папке, где и ' +
                        'эта программа</p>' +
                        '<p>Отправьте его мне на e-mail:  ' +
                        '<i>zorina-margarita@mail.ru</i>  ' +
                        'вместе с другими результатами тестов 1, 2, 3</p>' +
                        '<p>Теперь закройте это окно</p>' +
                        '</html>'))
            elif finished == 'test3':
                self.mainLabel.setText('Вы закончили тест 3')
                self.preTest4()
            elif finished == 'test2':
                self.mainLabel.setText('Вы закончили тест 2')
                self.preTest3()
            elif finished == 'test1':
                self.preTest2()
        elif flag == 'startTest1':
            self.preTest1()

# user authentication
    def userExist(self):
        # get user name
        text, ok = QInputDialog.getText(self, 'Авторизация',
            'Введите ваш номер:')
        if ok:
            if text == '':
                return 'cancel' # if pressed <Cancel>
            else:
                self.userName = 'Тест4_' + text
                userFile = userFilePath + self.userName + userFileExtension
                if path.exists(userFile):
                    # return flag new user True/False
                    return True
                else:
                    return False
        else:
            return 'cancel' # if pressed <Cancel>

# tests logic
    def preTest1(self):
        self.btnStartTest1.setText('Блок #1')
        self.btnOn(self.btnStartTest1, 'Блок #1')
        self.btnTest1Known.setText('Знакомое')
        self.btnTest1Unknown.setText('Незнакомое')
        self.mainLabel.setText(textMainPreTest1)
        self.hintLabel.setText(textHintHead + textHintPreTest1 + textHintTest1)

    def test1(self):
        self.btnOff(self.btnStartTest1)
        self.btnOn(self.btnTest1Known, 'Знакомое')
        self.btnOn(self.btnTest1Unknown, 'Незнакомое')
        self.readInitData()
        for i in self.initDataList:
            self.workKeysList.append(int(i[0]))
        currentKeyPos = 0
        workWord = self.extractWordByKey()
        self.mainLabel.setText(workWord)
        self.hintLabel.setText(textHintHead + textHintTest1)

    def test1Known(self):
        self.resultDataList.append(self.workKeysList[self.currentKeyPos])
        self.currentKeyPos += 1
        if self.currentKeyPos < len(self.workKeysList):
            workWord = self.extractWordByKey()
            self.mainLabel.setText(workWord)
        else:
            self.endTest1()

    def test1Unknown(self):
        self.currentKeyPos += 1
        if self.currentKeyPos < len(self.workKeysList):
            workWord = self.extractWordByKey()
            self.mainLabel.setText(workWord)
        else:
            self.endTest1()

    def endTest1(self):
        if self.resultDataList == []:
            self.crashTest1()
        else:
            self.mainLabel.setText('Test 1 finished')
            data = self.parseData(self.resultDataList, 'saveTest1')
            self.saveFile(userFilePath, self.userName + userFileExtension,
                        data, 'test1')
            self.btnOff(self.btnTest1Known)
            self.btnOff(self.btnTest1Unknown)
            self.preTest2()

    def crashTest1(self):
        self.btnOff(self.btnTest1Known)
        self.btnOff(self.btnTest1Unknown)
        self.mainLabel.setText('Вы не указали ни одного знакомого слова,\n' +
                                'тест завершен, спасибо!')
        self.hintLabel.setText('')
        # add save in file?

    def preTest2(self):
        self.btnOn(self.btnStartTest2, 'Блок #2')
        self.btnTest2New.setText('Новая часть тела')
        self.mainLabel.setText(textMainPreTest2)
        self.hintLabel.setText(textHintHead + textHintPreTest2 + textHintTest2)

    def test2(self):
        self.btnOff(self.btnStartTest2)
        self.btnOn(self.btnTest2New, 'Новая часть тела')
        self.prepareforTests2_4()
        self.hintLabel.setText(textHintHead + textHintTest2)

    def test2New(self):
        text, ok = QInputDialog.getText(self, 'Новая категория',
                            'Введите новую категорию:')
        if ok:
            self.addItemComboBox(text, 'test2')
            tempSubList = [self.workKeysList[self.currentKeyPos], text]
            self.resultDataList.append(tempSubList)
            self.currentKeyPos += 1
            if self.currentKeyPos < len(self.workKeysList):
                workWord = self.extractWordByKey()
                self.mainLabel.setText(workWord)
            else:
                self.endTest2()

    def onActivatedCBTest2(self, text):
        self.addItemComboBox(text, 'test2')
        tempSubList = [self.workKeysList[self.currentKeyPos], text]
        self.resultDataList.append(tempSubList)
        self.currentKeyPos += 1
        if self.currentKeyPos < len(self.workKeysList):
            workWord = self.extractWordByKey()
            self.mainLabel.setText(workWord)
        else:
            self.endTest2()

    def endTest2(self):
        self.mainLabel.setText('Finished test 2')
        self.btnOff(self.btnTest2New)
        self.comboBoxOff(self.comboBoxTest2)
        self.comboBoxTest2.clear()
        data = self.parseData(self.resultDataList, 'saveTest2')
        self.saveFile(userFilePath, self.userName + userFileExtension,
                    data, 'test2')
        self.preTest3()

    def preTest3(self):
        self.btnOn(self.btnStartTest3, 'Блок #3')
        self.mainLabel.setText(textMainPreTest3)
        self.hintLabel.setText(textHintHead + textHintPreTest3 + textHintTest3)

    def test3(self):
        self.btnOff(self.btnStartTest3)
        self.btnOn(self.btnTest3New, 'Новая группа')
        self.prepareforTests2_4()
        self.hintLabel.setText(textHintHead + textHintTest3)

    def test3New(self):
        text, ok = QInputDialog.getText(self, 'Новая категория',
                            'Введите новую категорию:')
        if ok:
            self.addItemComboBox(text, 'test3')
            tempSubList = [self.workKeysList[self.currentKeyPos], text]
            self.resultDataList.append(tempSubList)
            self.currentKeyPos += 1
            if self.currentKeyPos < len(self.workKeysList):
                workWord = self.extractWordByKey()
                self.mainLabel.setText(workWord)
            else:
                self.endTest3()

    def onActivatedCBTest3(self, text):
        self.addItemComboBox(text, 'test3')
        tempSubList = [self.workKeysList[self.currentKeyPos], text]
        self.resultDataList.append(tempSubList)
        self.currentKeyPos += 1
        if self.currentKeyPos < len(self.workKeysList):
            workWord = self.extractWordByKey()
            self.mainLabel.setText(workWord)
        else:
            self.endTest3()

    def endTest3(self):
        self.mainLabel.setText('Finished test 3')
        self.btnOff(self.btnTest3New)
        self.comboBoxOff(self.comboBoxTest3)
        self.comboBoxTest3.clear()
        data = self.parseData(self.resultDataList, 'saveTest3')
        self.saveFile(userFilePath, self.userName + userFileExtension,
                    data, 'test3')
        self.preTest4()

    def preTest4(self):
        self.btnOn(self.btnStartTest4, 'Блок #4')
        self.btnTest4Cold.setText('Холод')
        self.btnTest4Hunger.setText('Голод')
        self.btnTest4Pain.setText('Боль')
        self.btnTest4Nowhere.setText('Никуда')
        self.mainLabel.setText(textMainPreTest4)
        self.hintLabel.setText(textHintHead + textHintPreTest2 + textHintTest4)

    def test4(self):
        self.btnOff(self.btnStartTest4)
        self.btnOn(self.btnTest4Cold, 'Холод')
        self.btnOn(self.btnTest4Hunger, 'Голод')
        self.btnOn(self.btnTest4Pain, 'Боль')
        self.btnOn(self.btnTest4Nowhere, 'Никуда')
        self.prepareforTests2_4()
        self.hintLabel.setText(textHintHead + textHintTest4)

    def test4Cold(self):
        self.operationTest4('Холод')

    def test4Hunger(self):
        self.operationTest4('Голод')

    def test4Pain(self):
        self.operationTest4('Боль')

    def test4Nowhere(self):
        self.operationTest4('Никуда')

    def operationTest4(self, flag):
        tempSubList = [self.workKeysList[self.currentKeyPos], flag]
        self.resultDataList.append(tempSubList)
        self.currentKeyPos += 1
        if self.currentKeyPos < len(self.workKeysList):
            workWord = self.extractWordByKey()
            self.mainLabel.setText(workWord)
        else:
            self.endTest4()

    def endTest4(self):
        self.mainLabel.setText('Вы закончили все тесты')
        self.btnOff(self.btnTest4Cold)
        self.btnOff(self.btnTest4Hunger)
        self.btnOff(self.btnTest4Pain)
        self.btnOff(self.btnTest4Nowhere)
        data = self.parseData(self.resultDataList, 'saveTest4')
        self.saveFile(userFilePath, self.userName + userFileExtension,
                    data, 'test4')
        self.mainLabel.setText(textMainEndTest4)
        self.hintLabel.setText(textHintHead +
                        str('<html>' +
                        '<p>Ваши результаты сохранены в файле, который ' +
                        'называется ' + self.userName + '.txt</p>' +
                        '<p>Этот файл находится в той же папке, где и ' +
                        'эта программа</p>' +
                        '<p>Отправьте его мне на e-mail:  ' +
                        '<i>zorina-margarita@mail.ru</i>  ' +
                        'вместе с другими результатами тестов 1, 2, 3</p>' +
                        '<p>Теперь закройте это окно</p>' +
                        '</html>'))

    def prepareforTests2_4(self):
        self.currentKeyPos = 0
        self.workKeysList = []
        self.resultDataList = []
        self.readInitData()
        self.readTest1Result()
        workWord = self.extractWordByKey()
        self.mainLabel.setText(workWord)

    def existInList(self, list, text):
        for i in list:
            if i == text:
                return True
                break
        return False

    def addItemComboBox(self, text, flag):
        if flag == 'test2':
            if not self.existInList(self.listCBTest2, text):
                self.listCBTest2.append(text)
                self.updateComboBox('test2')
        elif flag == 'test3':
            if not self.existInList(self.listCBTest3, text):
                self.listCBTest3.append(text)
                self.updateComboBox('test3')

    def updateComboBox(self, flag):
        if flag == 'test2':
            self.comboBoxTest2.clear()
            self.comboBoxTest2.addItems(self.listCBTest2)
            if not self.comboBoxTest2.isEnabled():
                self.comboBoxOn(self.comboBoxTest2)
        elif flag == 'test3':
            self.comboBoxTest3.clear()
            self.comboBoxTest3.addItems(self.listCBTest3)
            if not self.comboBoxTest3.isEnabled():
                self.comboBoxOn(self.comboBoxTest3)
            if len(self.listCBTest3) == 2:
                self.btnOff(self.btnTest3New)

# work with file
    def openFile(self, path, fileName, flag='r'):
        # open file
        file = open(path + fileName, flag, encoding='utf-8')
        # read data
        data = file.read()
        # close file
        file.close()
        # return raw data
        return data

    def saveFile(self, path, fileName, data, flag):
        file = open(path + fileName, 'a', encoding='utf-8')
        if flag == 'test1':
            file.write(data + '\ntest1')
        elif flag == 'test2':
            file.write('\n' + data + '\ntest2')
        elif flag == 'test3':
            file.write('\n' + data + '\ntest3')
        elif flag == 'test4':
            file.write('\n' + data + '\ntest4')
        file.close()

    def parseData(self, data, flag): # parsing
        # parsing by flag
        if flag == 'progress':
            pass
        # return work variables
        elif flag == 'init':
            # print(data)
            result = []
            tempList = (data.split('\n'))
            for i in tempList:
                result.append(i.split('. '))
            self.endKeyPos = len(result) - 1
        elif flag == 'test1Result':
            result = []
            strList = data.split(',')
            for i in strList:
                result.append(int(i))
            self.endKeyPos = len(result) - 1
        elif flag == 'saveTest1':
            result = ''
            for i in data[:-1]:
                result += str(i) + ','
            result += str(data[-1])
        elif flag == 'saveTest2':
            result = ''
            for i in data[:-1]:
                result += str(i[0]) + ',' + i[1] + ';'
            result += str(data[-1][0]) + ',' + data[-1][1]
        elif flag == 'saveTest3':
            result = ''
            for i in data[:-1]:
                result += str(i[0]) + ',' + i[1] + ';'
            result += str(data[-1][0]) + ',' + data[-1][1]
        elif flag == 'saveTest4':
            result = ''
            for i in data[:-1]:
                result += str(i[0]) + ',' + i[1] + ';'
            result += str(data[-1][0]) + ',' + data[-1][1]

        return result

    def readInitData(self):
        file = self.openFile(initFilePath, initFileName)
        self.initDataList = self.parseData(file, 'init')

    def readTest1Result(self):
        file = open(userFilePath + self.userName + userFileExtension, 'r',
                    encoding='utf-8')
        for i, line in enumerate(file):
            if i == 0:
                self.workKeysList = self.parseData(line[0:-1], 'test1Result')
            else:
                break
        file.close()

    def checkTestFinished(self):
        file = open(userFilePath + self.userName + userFileExtension, 'r',
                    encoding='utf-8')
        lastTest = file.readlines()[-1]
        file.close()
        return lastTest

    def extractWordByKey(self):
        tempKey = self.workKeysList[self.currentKeyPos]
        workWord = self.initDataList[tempKey - 1][1]
        return workWord


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
