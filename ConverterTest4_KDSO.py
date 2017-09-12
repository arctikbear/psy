# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from os import mkdir, path
# from pathlib import Path


# const
faviconFile = 'favicon.png'
mainWindowTitle = 'Конвертер КДСО (v.1.1)'
# MainWindow dimensions
mainWindowWidth = 600
mainWindowHeight = 400
# MainWindow position
mainWindowXPos = 100
mainWindowYPos = 200
# init data directory and name file
initFilePath = '.\\'
initFileName = 'Cards.txt'
# user data directory and name file
userFilePath = ''
userFileExtension = '.txt'


# UI for Main window
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # work variables
        self.userFileName = ''
        self.reportFileName =''
        self.initDataList = []  # init data
        self.rawData = ''
        self.resultTest1 = []
        self.reportStatTest1 = ''
        self.reportCardsTest1 = ''
        self.resultTest2 = []
        self.categoryTest2 = []
        self.reportStatTest2 = ''
        self.reportCardsTest2 = ''
        self.resultTest3 = []
        self.categoryTest3 = []
        self.reportStatTest3 = ''
        self.reportCardsTest3 = ''
        self.resultTest4 = []
        self.categoryTest4 = ['Холод', 'Голод', 'Боль', 'Никуда']
        self.reportStatTest4 = ''
        self.reportCardsTest4 = ''
        self.fullReport = 'Отчет выполнен в программе Конвертер Тест4 КДСО (v.1.1)\n\n'
        
        self.initUI()
        self.show() # drawing MainWindow

# windows UI
    def initUI(self): # creation Gui depending on the flags
        self.createMainWindow()
        # buttons
        self.btnOpen = QPushButton('Выбрать файл', self)
        self.setBtn(self.btnOpen, 120, 155, 'Helvetica', 10)
        self.btnOpen.clicked.connect(self.openFileDialog)

        self.btnCreate = QPushButton('Создать отчет', self)
        self.setBtn(self.btnCreate, 300, 155, 'Helvetica', 10)
        self.btnCreate.clicked.connect(self.createReport)
        self.btnCreate.setDisabled(True)

        self.btnSave = QPushButton('Сохранить отчет', self)
        self.setBtn(self.btnSave, 480, 155, 'Helvetica', 10)
        self.btnSave.clicked.connect(self.saveFileDialog)
        self.btnSave.setDisabled(True)

        # labels
        self.mainLabel = QLabel('Выберите файл с результатами', self)
        self.setLabel(self.mainLabel, 540, 100, 30, 20,
                            'Helvetica', 16, 'wrap', 'center')

        self.hintLabel = QLabel('Программа для формирования отчетов' +
                                ' из рабочих файлов клиентов.\n\n' +
                                'Файл отчета клиента имеет имя вида: ' +
                                'Тест4_<имя клиента>.txt\n\n' +
                                'Для того, чтобы загрузить результаты клиента, ' +
                                'нажмите кнопку [Выбрать файл]', self)
        self.setLabel(self.hintLabel, 540, 185, 30, 195,
                            'Helvetica', 11, 'wrap')

    def createMainWindow(self):
        self.setFixedSize(mainWindowWidth, mainWindowHeight)
        self.move(mainWindowXPos, mainWindowYPos)
        # self.center()
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

    def setMainLabelText(self, label, text):
        label.setText(text)

# main programm logig

    def welcomeWindow(self):
        self.mainLabel.setText('Выберите файл с результатми')
        self.hintLabel.setText('Программа для формирования отчетов' +
                                ' из рабочих файлов клиентов.\n\n' +
                                'Файл отчета клиента имеет имя вида: ' +
                                'Тест4_<имя клиента>.txt\n\n' +
                                'Для того, чтобы загрузить результаты клиента, ' +
                                'нажмите кнопку [Выбрать файл]')
        self.userFileName = ''
        self.reportFileName =''
        self.initDataList = []  # init data
        self.rawData = ''
        self.resultTest1 = []
        self.reportStatTest1 = ''
        self.reportCardsTest1 = ''
        self.resultTest2 = []
        self.categoryTest2 = []
        self.reportStatTest2 = ''
        self.reportCardsTest2 = ''
        self.resultTest3 = []
        self.categoryTest3 = []
        self.reportStatTest3 = ''
        self.reportCardsTest3 = ''
        self.resultTest4 = []
        self.categoryTest4 = ['Холод', 'Голод', 'Боль', 'Никуда']
        self.reportStatTest4 = ''
        self.reportCardsTest4 = ''
        self.fullReport = 'Отчет выполнен в программе Конвертер Тест4 КДСО (v.1.0)\n\n'

    def openFileDialog(self):
        file = QFileDialog.getOpenFileName(directory='.\\')
        self.userFileName = file[0]
        if self.userFileName != '':
            self.mainLabel.setText('Вы выбрали файл:\n\n' + str(file[0]))
            self.hintLabel.setText('Для того, чтобы создать отчет, ' +
                                    'нажмите кнопку [Создать отчет]')
            self.btnOpen.setDisabled(True)
            self.btnCreate.setDisabled(False)

    def createReport(self):
        self.btnCreate.setDisabled(True)
        self.btnCreate.clearFocus()
        self.rawData = self.openFile(self.userFileName)
        data = self.rawData.split('\n')
        # font = QFont('Helvetica', 10)
        # self.mainLabel.setFont(font)
        self.resultTest1 = self.parseData(data[0], 'textTest1')
        self.resultTest2 = self.parseData(data[2])
        self.resultTest3 = self.parseData(data[4])
        self.resultTest4 = self.parseData(data[6])
        self.mainLabel.setText('resultTest1= ' + str(self.resultTest1))
        self.categoryListFrom(self.resultTest2, self.categoryTest2)
        self.categoryListFrom(self.resultTest3, self.categoryTest3)
        groupTest2 = self.createGroup(self.resultTest2, self.categoryTest2)
        groupTest3 = self.createGroup(self.resultTest3, self.categoryTest3)
        groupTest4 = self.createGroup(self.resultTest4, self.categoryTest4)
        self.readInitData()

        quantityFull = len(self.initDataList)
        quantityKnown = len(self.resultTest1)
        quantityUnknown = quantityFull - quantityKnown
        self.reportStatTest1 = str('Количественный анализ: ' + str(quantityFull) +
                            ' карточек (100%)\n\n' +
                            '"Знакомое"/"Незнакомое": ' +
                            str(quantityKnown) + '/' + str(quantityUnknown) +
                        ' (' + '{0:.0f}'.format(self.percent(quantityKnown, quantityFull)) +
                        '%/' + '{0:.0f}'.format(self.percent(quantityUnknown, quantityFull)) +
                            '%)\n')
        self.reportCardsTest1 = str('Карточки из категории "Незнакомое" ('+
                            str(len(self.initDataList) - len(self.resultTest1)) +
                            '):\n' + self.parseData(self.resultTest1, 'reportCardsTest1'))
        self.reportStatTest2 = str('по частям тела:\n' +
                            self.parseData(groupTest2, 'reportStat'))
        self.reportCardsTest2 = self.parseData(groupTest2, 'reportCards')
        self.reportStatTest3 = str('по произвольному признаку:\n' +
                            self.parseData(groupTest3, 'reportStat'))
        self.reportCardsTest3 = self.parseData(groupTest3, 'reportCards')
        self.reportStatTest4 = str('по исследуемой теме:\n' +
                            self.parseData(groupTest4, 'reportStat'))
        self.reportCardsTest4 = self.parseData(groupTest4, 'reportCards')
        self.fullReport += str(self.reportStatTest1 + '\n' +
                            self.reportStatTest2 + '\n' +
                            self.reportStatTest3 + '\n' +
                            self.reportStatTest4 +
                            '---------------------------------------------\n' +
                            'Результаты блока #1\n' +
                            self.reportCardsTest1 +
                            '---------------------------------------------\n' +
                            'Результаты блока #2\n' +
                            self.reportStatTest2 +
                            self.reportCardsTest2 +
                            '---------------------------------------------\n' +
                            'Результаты блока #3\n' +
                            self.reportStatTest3 +
                            self.reportCardsTest3 +
                            '---------------------------------------------\n' +
                            'Результаты блока #4\n' +
                            self.reportStatTest4 +
                            self.reportCardsTest4)
        self.mainLabel.setText('Отчет успешно создан')
        self.hintLabel.setText('Для того, чтобы сохранить отчет, нажмите ' +
                                'кнопку [Сохранить отчет]')
        self.btnSave.setDisabled(False)


    def createGroup(self, data, keyWords):
        summary = []

        for keyWord in keyWords:
            sumWords = 0
            members = []
            for pair in data:
                if pair[1] == keyWord:
                    sumWords += 1
                    members.append(pair[0])
            summary.append([keyWord, sumWords, members])
        return summary

    def categoryListFrom(self, resultTest, categoryList):
        for i in resultTest:
            if i[1] not in categoryList:
                categoryList.append(i[1])

    def saveFileDialog(self):
        file = QFileDialog.getSaveFileName(directory='.\\', filter='Text (*.txt)')
        self.reportFileName = file[0]
        if self.reportFileName != '':
            self.saveFile(file[0], self.fullReport)
            self.btnSave.setDisabled(True)
            self.btnSave.clearFocus()
            self.welcomeWindow()
            self.btnOpen.setDisabled(False)


# work with file
    def openFile(self, name, flag='r'):
        file = open(name, flag, encoding='utf-8')
        data = file.read()
        file.close()
        return data

    def saveFile(self, fileName, data):
        file = open(fileName, 'w', encoding='utf-8')
        file.write(data)
        file.close()

    def readInitData(self):
        file = self.openFile(initFilePath + initFileName)
        self.initDataList = self.parseData(file, 'init')

    def parseData(self, data, flag=None): # parsing
        # parsing by flag
        result = []
        if flag == 'init':
            # print(data)
            result = []
            tempList = (data.split('\n'))
            for i in tempList:
                result.append(i.split('. '))
        elif flag == 'textTest1':
            strList = data.split(',')
            for i in strList:
                result.append(int(i))

        elif flag == 'reportStat':
            result = ''
            resultTest1 = self.resultTest1
            for group in data:
                nameGroup = group[0]
                sumInGroup = group[1]
                percent = self.percent(sumInGroup, len(resultTest1))
                result += str(nameGroup + ' ' + str(sumInGroup) +
                                ' (' + '{0:.0f}'.format(percent) + '%)\n')

        elif flag == 'reportCardsTest1':
            result = ''
            initData = self.initDataList
            resultTest1 = data
            for pair in initData:
                if int(pair[0]) not in resultTest1:
                    result += pair[0] + '. ' + pair[1] + '\n'

        elif flag == 'reportCards':
            result = ''
            initData = self.initDataList
            resultTest1 = self.resultTest1
            for group in data:
                nameGroup = group[0]
                sumInGroup = group[1]
                listInGroup = group[2]
                result += str('\nгруппа ' + nameGroup + ' (' + str(sumInGroup) + '):\n')
                for key in listInGroup:
                    initKey = key
                    initWord = initData[int(key) - 1][1]
                    result += str(initKey + '. ' + initWord + '\n')
            self.hintLabel.setText(str(self.categoryTest2) + '\n' + str(data))
            # self.mainLabel.setText(result)

        else:
            tempList1 = data.split(';')
            for i in tempList1:
                tempList2 = i.split(',')
                result.append(tempList2)

        return result

    def readInitData(self):
        file = self.openFile(initFilePath + initFileName)
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

    def percent(self, part, full):
        return (part * 100) / full


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
