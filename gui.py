# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-desain.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 738)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(36, 31, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 321, 751))
        self.frame.setMaximumSize(QtCore.QSize(1366, 768))
        self.frame.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 30, 101, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo/logo_blu.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 111, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo/logo_unej.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pb_input_model = QtWidgets.QPushButton(self.frame)
        self.pb_input_model.setGeometry(QtCore.QRect(50, 580, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_input_model.setFont(font)
        self.pb_input_model.setStyleSheet("background-color: rgb(38, 162, 105);")
        self.pb_input_model.setObjectName("pb_input_model")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 301, 261))
        font = QtGui.QFont()
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 60, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalWidget.setFont(font)
        self.horizontalWidget.setStyleSheet("background-color: rgb(92, 53, 102);\n"
"color : white;")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.pb_start_mode = QtWidgets.QPushButton(self.groupBox)
        self.pb_start_mode.setGeometry(QtCore.QRect(30, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pb_start_mode.setFont(font)
        self.pb_start_mode.setStyleSheet("QPushButton:enabled {\n"
"    background-color: blue;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: gray;\n"
"    color: rgb(94, 92, 100);\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}")
        self.pb_start_mode.setObjectName("pb_start_mode")
        self.pb_stop_mode = QtWidgets.QPushButton(self.groupBox)
        self.pb_stop_mode.setGeometry(QtCore.QRect(170, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pb_stop_mode.setFont(font)
        self.pb_stop_mode.setStyleSheet("QPushButton:enabled {\n"
"    background-color: red;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: gray;\n"
"    color: rgb(94, 92, 100);\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}")
        self.pb_stop_mode.setObjectName("pb_stop_mode")
        self.radioButton_active = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_active.setGeometry(QtCore.QRect(20, 20, 112, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_active.setFont(font)
        self.radioButton_active.setStyleSheet("\n"
"QRadioButton{\n"
"   color: rgb(51, 218, 122);\n"
"}\n"
"\n"
"QRadioButton:unchecked {\n"
"   color: rgb(94, 92, 100);\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"   color: rgb(51, 218, 122);\n"
"}")
        self.radioButton_active.setCheckable(True)
        self.radioButton_active.setChecked(False)
        self.radioButton_active.setObjectName("radioButton_active")
        self.choose_mode = QtWidgets.QComboBox(self.groupBox)
        self.choose_mode.setGeometry(QtCore.QRect(30, 110, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.choose_mode.setFont(font)
        self.choose_mode.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"\n"
"QComboBox{\n"
"        font-family: \"Poppins\";\n"
"        font-size: 10pt;\n"
"        font-weight: bold;\n"
"}")
        self.choose_mode.setObjectName("choose_mode")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 430, 301, 131))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.choose_baudrate = QtWidgets.QComboBox(self.groupBox_4)
        self.choose_baudrate.setGeometry(QtCore.QRect(20, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.choose_baudrate.setFont(font)
        self.choose_baudrate.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.choose_baudrate.setObjectName("choose_baudrate")
        self.choose_baudrate.addItem("")
        self.choose_baudrate.addItem("")
        self.choose_baudrate.addItem("")
        self.choose_com = QtWidgets.QComboBox(self.groupBox_4)
        self.choose_com.setGeometry(QtCore.QRect(180, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.choose_com.setFont(font)
        self.choose_com.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.choose_com.setObjectName("choose_com")
        self.choose_com.addItem("")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(92, 53, 102);\n"
"color : white;")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_4.addWidget(self.label_19)
        self.pb_input_model_3 = QtWidgets.QPushButton(self.frame)
        self.pb_input_model_3.setGeometry(QtCore.QRect(50, 640, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_input_model_3.setFont(font)
        self.pb_input_model_3.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.pb_input_model_3.setObjectName("pb_input_model_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 100, 1061, 651))
        self.frame_2.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 130, 991, 461))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(248, 228, 92);\n"
"")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(30, 80, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(350, 80, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_15.setObjectName("label_15")
        self.camera_view = QtWidgets.QLabel(self.groupBox_3)
        self.camera_view.setGeometry(QtCore.QRect(350, 120, 291, 301))
        self.camera_view.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.camera_view.setText("")
        self.camera_view.setObjectName("camera_view")
        self.error_view = QtWidgets.QLabel(self.groupBox_3)
        self.error_view.setGeometry(QtCore.QRect(670, 120, 291, 301))
        self.error_view.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.error_view.setText("")
        self.error_view.setObjectName("error_view")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(670, 80, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_16.setObjectName("label_16")
        self.plot_view = QtWidgets.QLabel(self.groupBox_3)
        self.plot_view.setGeometry(QtCore.QRect(30, 120, 291, 301))
        self.plot_view.setStyleSheet("background-color: rgb(36, 31, 49);")
        self.plot_view.setText("")
        self.plot_view.setObjectName("plot_view")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 30, 261, 81))
        self.groupBox_2.setStyleSheet("color: rgb(248, 228, 92);\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lowSpeed = QtWidgets.QLabel(self.groupBox_2)
        self.lowSpeed.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lowSpeed.setFont(font)
        self.lowSpeed.setStyleSheet("background-color: transparent;\n"
"padding: 5px;\n"
"color :rgb(246, 211, 45);")
        self.lowSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lowSpeed.setObjectName("lowSpeed")
        self.cmd_view = QtWidgets.QLabel(self.groupBox_2)
        self.cmd_view.setGeometry(QtCore.QRect(110, 30, 131, 31))
        self.cmd_view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:blackl;")
        self.cmd_view.setText("")
        self.cmd_view.setTextFormat(QtCore.Qt.PlainText)
        self.cmd_view.setAlignment(QtCore.Qt.AlignCenter)
        self.cmd_view.setObjectName("cmd_view")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 10, 221, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("color: rgb(248, 228, 92);\n"
"")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.lowSpeed_2 = QtWidgets.QLabel(self.groupBox_5)
        self.lowSpeed_2.setGeometry(QtCore.QRect(-10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lowSpeed_2.setFont(font)
        self.lowSpeed_2.setStyleSheet("background-color: transparent;\n"
"padding: 5px;\n"
"color : rgb(26, 95, 180);")
        self.lowSpeed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lowSpeed_2.setObjectName("lowSpeed_2")
        self.lowSpeed_3 = QtWidgets.QLabel(self.groupBox_5)
        self.lowSpeed_3.setGeometry(QtCore.QRect(-10, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lowSpeed_3.setFont(font)
        self.lowSpeed_3.setStyleSheet("background-color: transparent;\n"
"padding: 5px;\n"
"color : rgb(26, 95, 180);")
        self.lowSpeed_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lowSpeed_3.setObjectName("lowSpeed_3")
        self.timer_set = QtWidgets.QSpinBox(self.groupBox_5)
        self.timer_set.setGeometry(QtCore.QRect(70, 30, 131, 31))
        self.timer_set.setObjectName("timer_set")
        self.count_set = QtWidgets.QSpinBox(self.groupBox_5)
        self.count_set.setGeometry(QtCore.QRect(70, 80, 131, 31))
        self.count_set.setObjectName("count_set")
        self.lowSpeed_4 = QtWidgets.QLabel(self.groupBox_5)
        self.lowSpeed_4.setGeometry(QtCore.QRect(150, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lowSpeed_4.setFont(font)
        self.lowSpeed_4.setStyleSheet("background-color: transparent;\n"
"padding: 5px;\n"
"color :rgb(246, 211, 45);")
        self.lowSpeed_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lowSpeed_4.setObjectName("lowSpeed_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(320, 0, 1061, 101))
        self.frame_3.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(40, 60, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(51, 218, 122);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_input_model.setText(_translate("MainWindow", "Input Model"))
        self.label_18.setText(_translate("MainWindow", "SET MODE"))
        self.pb_start_mode.setText(_translate("MainWindow", "Start"))
        self.pb_stop_mode.setText(_translate("MainWindow", "Stop"))
        self.radioButton_active.setText(_translate("MainWindow", "Active"))
        self.choose_baudrate.setItemText(0, _translate("MainWindow", "Baudrate"))
        self.choose_baudrate.setItemText(1, _translate("MainWindow", "9600"))
        self.choose_baudrate.setItemText(2, _translate("MainWindow", "115200"))
        self.choose_com.setItemText(0, _translate("MainWindow", "COM"))
        self.label_19.setText(_translate("MainWindow", "DEVICE"))
        self.pb_input_model_3.setText(_translate("MainWindow", "Update Model"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Display"))
        self.label_14.setText(_translate("MainWindow", "Plot View"))
        self.label_15.setText(_translate("MainWindow", "camera"))
        self.label_16.setText(_translate("MainWindow", "Error View"))
        self.lowSpeed.setText(_translate("MainWindow", "Perintah"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Set Perintah"))
        self.lowSpeed_2.setText(_translate("MainWindow", "Timer"))
        self.lowSpeed_3.setText(_translate("MainWindow", "count"))
        self.lowSpeed_4.setText(_translate("MainWindow", "sec"))
        self.label_7.setText(_translate("MainWindow", "Robby Ardianysah"))
        self.label_8.setText(_translate("MainWindow", "Magister Teknik Elektro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
