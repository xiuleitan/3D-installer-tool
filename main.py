import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QDesktopWidget,QMessageBox
from PyQt5.QtWidgets import QApplication,QPushButton,\
    QWidget,QVBoxLayout,QLabel,QDialog,QFormLayout,\
    QCheckBox,QHBoxLayout,QFrame,QLineEdit
from PyQt5.QtGui import QIcon,QFont
import os
import sys
import fileReadAndWrite
from qt_material import apply_stylesheet
from qt_material import list_themes


class MainRender(QMainWindow):
    def __init__(self):
        super(MainRender, self).__init__()
        self.setWindowTitle("三维软件安装包")
        self.setWindowIcon(QIcon('./icon/bit.png'))
        # self.resize(800, 600)  # 设置宽度和高度
        self.center() # 让应用打开居中显示
        self.route = fileReadAndWrite.readCSV('data/software_route.csv')[0][0]
        self.main_UI()
        # self.AE_StepUp()
        # self._3dmax_StepUp()
        self.c4d_StepUp()
        # self.maya_StepUp()
        # self.houdini_StepUp()


    # ok 让应用打开居中显示
    def center(self):
        # 获取屏幕的坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取主窗口的坐标
        size = self.geometry()

        # 设置新的left 和 top
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        # 通过move方法移动窗口
        self.move(newLeft, newTop)

    # AE 安装包
    def AE_StepUp(self):
        pass
        # self.AE_Layout = QVBoxLayout()

    def c4d_StepUp(self):
        pass
        # self.c4d_Layout = QVBoxLayout()
        # button_c4d_R21 = QPushButton('安装c4d R21',self)
        # button_c4d_R21.resize(40,15)
        # self.c4d_Layout.addWidget(button_c4d_R21)
    def install_rar(self):
        self.cmd_run(f'"{self.route}\\winrar-x64-602scp.exe"')
    def main_UI(self):
        mainLayout = QHBoxLayout(self)
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
        # WinRar安装
        self.cb_rar = QCheckBox()
        self.cb_rar.setChecked(False)
        button_rar = QPushButton('安装WinRAR')  # 开始添加按钮
        button_rar.clicked.connect(self.install_rar)

        # AE 安装部分***********************
        line1 = QFrame()
        line1.setLineWidth(2)
        line1.setMidLineWidth(2)
        line1.setFrameShadow(QFrame.Plain)
        line1.setFrameShape(QFrame.VLine)
        label_AE = QLabel('AE安装')
        label_AE.setAlignment(Qt.AlignCenter)
        label_AE.setFont(QFont('黑体', 15, QFont.Bold))
            # 安装AE2021
        self.cb_AE_2021 = QCheckBox()
        self.cb_AE_2021.setChecked(False)
        button_AE_2021 = QPushButton('安装AE 2021')  # 开始添加按钮
        button_AE_2021.clicked.connect(self.install_AE_2021)
        # 安装AE2020
        self.cb_AE_2020 = QCheckBox()
        self.cb_AE_2020.setChecked(False)
        button_AE_2020 = QPushButton('安装AE 2020')  # 开始添加按钮
        button_AE_2020.clicked.connect(self.install_AE_2020)

        layoutV_AE = QVBoxLayout()
        layoutForm_AE = QFormLayout()
        layoutV_AE.addWidget(label_AE)
        layoutForm_AE.addRow(self.cb_rar,button_rar)
        layoutForm_AE.addRow(self.cb_AE_2021, button_AE_2021)  # 添加行
        layoutForm_AE.addRow(self.cb_AE_2020, button_AE_2020) #添加行
        layoutV_AE.addLayout(layoutForm_AE)

        mainLayout.addLayout(layoutV_AE)
        mainLayout.addWidget(line1)

        # ****************** c4d安装部分 ****************************
        line2 = QFrame()
        line2.setLineWidth(2)
        line2.setMidLineWidth(2)
        line2.setFrameShadow(QFrame.Plain)
        line2.setFrameShape(QFrame.VLine)
        label_c4d = QLabel('C4D安装')
        label_c4d.setAlignment(Qt.AlignCenter)
        label_c4d.setFont(QFont('黑体', 15, QFont.Bold))
            # 安装C4D R25
        self.cb_c4d_R25 = QCheckBox()
        self.cb_c4d_R25.setChecked(False)
        button_c4d_R25 = QPushButton('安装C4D R25')
        button_c4d_R25.clicked.connect(self.install_c4d_R25)
            # 安装C4D R24
        # self.cb_c4d_R24 = QCheckBox()
        # self.cb_c4d_R24.setChecked(False)
        # button_c4d_R24 = QPushButton('安装C4D R24')
        # button_c4d_R24.clicked.connect(self.install_c4d_R24)
            # 安装C4D R23
        self.cb_c4d_R23 = QCheckBox()
        self.cb_c4d_R23.setChecked(False)
        button_c4d_R23 = QPushButton('安装C4D R23')
        button_c4d_R23.clicked.connect(self.install_c4d_R23)
             # 安装C4D R22
        # self.cb_c4d_R22 = QCheckBox()
        # self.cb_c4d_R22.setChecked(False)
        # button_c4d_R22 = QPushButton('安装C4D R22')
        # button_c4d_R22.clicked.connect(self.install_c4d_R22)
            # 安装C4D R21
        self.cb_c4d_R21 = QCheckBox()
        self.cb_c4d_R21.setChecked(False)
        button_c4d_R21 = QPushButton('安装C4D R21')
        button_c4d_R21.clicked.connect(self.install_c4d_R21)
            # 安装C4D R20
        # self.cb_c4d_R20 = QCheckBox()
        # self.cb_c4d_R20.setChecked(False)
        # button_c4d_R20 = QPushButton('安装C4D R20')
        # button_c4d_R20.clicked.connect(self.install_c4d_R20)

        layoutV_c4d = QVBoxLayout()
        layoutForm_c4d = QFormLayout()
        layoutV_c4d.addWidget(label_c4d)
        layoutForm_c4d.addRow(self.cb_c4d_R25, button_c4d_R25)
        # layoutForm_c4d.addRow(self.cb_c4d_R24, button_c4d_R24)
        layoutForm_c4d.addRow(self.cb_c4d_R23, button_c4d_R23)
        # layoutForm_c4d.addRow(self.cb_c4d_R22, button_c4d_R22)
        layoutForm_c4d.addRow(self.cb_c4d_R21, button_c4d_R21)
        # layoutForm_c4d.addRow(self.cb_c4d_R20, button_c4d_R20)

        layoutV_c4d.addLayout(layoutForm_c4d)
        mainLayout.addLayout(layoutV_c4d)
        mainLayout.addWidget(line2)

        # 3dmax 安装部分*****************************
        line3 = QFrame()
        line3.setLineWidth(2)
        line3.setMidLineWidth(2)
        line3.setFrameShadow(QFrame.Plain)
        line3.setFrameShape(QFrame.VLine)
        label_3dmax = QLabel('3Ds Max安装')
        label_3dmax.setAlignment(Qt.AlignCenter)
        label_3dmax.setFont(QFont('黑体', 15, QFont.Bold))
            # 安装3dmax2022
        self.cb_3dmax_2022 = QCheckBox()
        self.cb_3dmax_2022.setChecked(False)
        button_3dmax_2022 = QPushButton('安装3DsMax 2022')#开始添加按钮
        button_3dmax_2022.clicked.connect(self.install_3dmax_2022)

             # 安装3dmax2021
        # self.cb_3dmax_2021 = QCheckBox()
        # self.cb_3dmax_2021.setChecked(False)
        # button_3dmax_2021 = QPushButton('安装3DsMax 2021')  # 开始添加按钮
        # button_3dmax_2021.clicked.connect(self.install_3dmax_2021)

             # 安装3dmax2020
        self.cb_3dmax_2020 = QCheckBox()
        self.cb_3dmax_2020.setChecked(False)
        button_3dmax_2020 = QPushButton('安装3DsMax 2020')  # 开始添加按钮
        button_3dmax_2020.clicked.connect(self.install_3dmax_2020)

        # 安装3dmax2019
        # self.cb_3dmax_2019 = QCheckBox()
        # self.cb_3dmax_2019.setChecked(False)
        # button_3dmax_2019 = QPushButton('安装3DsMax 2019')  # 开始添加按钮
        # button_3dmax_2019.clicked.connect(self.install_3dmax_2019)

        # 安装3dmax2018
        # self.cb_3dmax_2018 = QCheckBox()
        # self.cb_3dmax_2018.setChecked(False)
        # button_3dmax_2018 = QPushButton('安装3DsMax 2018')  # 开始添加按钮
        # button_3dmax_2018.clicked.connect(self.install_3dmax_2018)

        layoutV_3dmax = QVBoxLayout()
        layoutForm_3dmax = QFormLayout()
        layoutForm_3dmax.addRow(self.cb_3dmax_2022,button_3dmax_2022)# 添加行
        # layoutForm_3dmax.addRow(self.cb_3dmax_2021,button_3dmax_2021)
        layoutForm_3dmax.addRow(self.cb_3dmax_2020,button_3dmax_2020)
        # layoutForm_3dmax.addRow(self.cb_3dmax_2019,button_3dmax_2019)
        # layoutForm_3dmax.addRow(self.cb_3dmax_2018,button_3dmax_2018)
        layoutV_3dmax.addWidget(label_3dmax)
        layoutV_3dmax.addLayout(layoutForm_3dmax)

        mainLayout.addLayout(layoutV_3dmax)
        mainLayout.addWidget(line3)

        # Maya 安装部分*****************************
        line4 = QFrame()
        line4.setLineWidth(2)
        line4.setMidLineWidth(2)
        line4.setFrameShadow(QFrame.Plain)
        line4.setFrameShape(QFrame.VLine)
        label_maya = QLabel('Maya安装')
        label_maya.setAlignment(Qt.AlignCenter)
        label_maya.setFont(QFont('黑体', 15, QFont.Bold))
            # 安装Maya 2022
        self.cb_maya_2022 = QCheckBox()
        self.cb_maya_2022.setChecked(False)
        button_maya_2022 = QPushButton('安装Maya 2022')#开始添加按钮
        button_maya_2022.clicked.connect(self.install_maya_2022)

        # 安装Maya 2020
        self.cb_maya_2020 = QCheckBox()
        self.cb_maya_2020.setChecked(False)
        button_maya_2020 = QPushButton('安装Maya 2020')  # 开始添加按钮
        button_maya_2020.clicked.connect(self.install_maya_2020)

        # 安装Maya 2019
        # self.cb_maya_2019 = QCheckBox()
        # self.cb_maya_2019.setChecked(False)
        # button_maya_2019 = QPushButton('安装Maya 2019')  # 开始添加按钮
        # button_maya_2019.clicked.connect(self.install_maya_2019)

        # 安装Maya 2018
        # self.cb_maya_2018 = QCheckBox()
        # self.cb_maya_2018.setChecked(False)
        # button_maya_2018 = QPushButton('安装Maya 2018')  # 开始添加按钮
        # button_maya_2018.clicked.connect(self.install_maya_2018)

        layoutV_maya = QVBoxLayout()
        layoutForm_maya = QFormLayout()
        layoutV_maya.addWidget(label_maya)
        layoutForm_maya.addRow(self.cb_maya_2022, button_maya_2022)# 添加row
        layoutForm_maya.addRow(self.cb_maya_2020, button_maya_2020)# 添加row
        # layoutForm_maya.addRow(self.cb_maya_2019, button_maya_2019)# 添加row
        # layoutForm_maya.addRow(self.cb_maya_2018, button_maya_2018)# 添加row
        layoutV_maya.addLayout(layoutForm_maya)

        mainLayout.addLayout(layoutV_maya)
        mainLayout.addWidget(line4)

        # Houdini 安装部分*****************************
        line5 = QFrame()
        line5.setLineWidth(2)
        line5.setMidLineWidth(2)
        line5.setFrameShadow(QFrame.Plain)
        line5.setFrameShape(QFrame.VLine)
        label_houdini = QLabel('Houdini安装')
        label_houdini.setAlignment(Qt.AlignCenter)
        label_houdini.setFont(QFont('黑体', 15, QFont.Bold))
            # 安装houdini18.5.696
        self.cb_houdini_696 = QCheckBox()
        self.cb_houdini_696.setChecked(False)
        button_houdini_18_5_696 = QPushButton('安装Houdini 18.5.696')#开始添加按钮
        button_houdini_18_5_696.clicked.connect(self.install_houdini_185_696)

        layoutV_houdini = QVBoxLayout()
        layoutForm_houdini = QFormLayout()
        layoutV_houdini.addWidget(label_houdini)
        layoutForm_houdini.addRow(self.cb_houdini_696, button_houdini_18_5_696)
        layoutV_houdini.addLayout(layoutForm_houdini)
        mainLayout.addLayout(layoutV_houdini)
        mainLayout.addWidget(line5)

        # Nuke 安装部分*****************************
        line6 = QFrame()
        line6.setLineWidth(2)
        line6.setMidLineWidth(2)
        line6.setFrameShadow(QFrame.Plain)
        line6.setFrameShape(QFrame.VLine)
        label_nuke = QLabel('Nuke安装')
        label_nuke.setAlignment(Qt.AlignCenter)
        label_nuke.setFont(QFont('黑体', 15, QFont.Bold))
            # 安装Nuke
        self.cb_nuke_12_2 = QCheckBox()
        self.cb_nuke_12_2.setChecked(False)
        button_nuke_12_2 = QPushButton('安装Nuke 12.2')  # 开始添加按钮
        button_nuke_12_2.clicked.connect(self.install_nuke_12_2)

        layoutV_nuke = QVBoxLayout()
        layoutForm_nuke = QFormLayout()
        layoutV_nuke.addWidget(label_nuke)
        layoutForm_nuke.addRow(self.cb_nuke_12_2, button_nuke_12_2)
        layoutV_nuke.addLayout(layoutForm_nuke)
        mainLayout.addLayout(layoutV_nuke)
        mainLayout.addWidget(line6)

        # 插件 安装部分*****************************
        label_plugins = QLabel('插件安装')
        label_plugins.setAlignment(Qt.AlignCenter)
        label_plugins.setFont(QFont('黑体', 12, QFont.Bold))
            # 安装Maxon
        self.cb_c4d_Maxon = QCheckBox()
        self.cb_c4d_Maxon.setChecked(False)
        button_maxon = QPushButton('安装Maxon APP')  # 开始添加按钮
        button_maxon.clicked.connect(self.install_Maxon)
            # 安装redshift
        self.cb_plugins_redshift = QCheckBox()
        self.cb_plugins_redshift.setChecked(False)
        button_plugins_redshift = QPushButton('安装redshift')  # 开始添加按钮
        button_plugins_redshift.clicked.connect(self.install_plugins_redshift)

        layoutV_plugins = QVBoxLayout()
        layoutForm_plugins = QFormLayout()
        layoutForm_plugins.addRow(self.cb_c4d_Maxon, button_maxon)  # 添加复选框和按钮
        layoutForm_plugins.addRow(self.cb_plugins_redshift,button_plugins_redshift) # 添加行
        layoutV_plugins.addWidget(label_plugins)
        layoutV_plugins.addLayout(layoutForm_plugins)

        mainLayout.addLayout(layoutV_plugins)
    def cmd_run(self, cmd):
        xxx = f'C:\\Windows\\system32\\cmd.exe /c "{cmd}"' #cmd是一个完整的命令,注意双引号
        print(xxx)
        subprocess.Popen(xxx)
    def cmd_run_txt(self, txt_route):
        xxx = f'C:\\Windows\\system32\\notepad.exe "{txt_route}"' #cmd是一个完整的命令,注意双引号
        print(xxx)
        subprocess.Popen(xxx)
    def cmd_run1(self, cmd):
        xxx = f'cmd.lnk /c "{cmd}"' #cmd是一个完整的命令,注意双引号
        print(xxx)
        os.system(xxx)



    def install_c4d_R25(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装c4d R25')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装c4d R25应用', dialog)
        def install01():
            self.cmd_run('"'+self.route + '\\c4d\\R25\\Cinema4D_R25_25.010_Win.exe'+'"')
        button1.clicked.connect(install01)

        button1_1 = QPushButton('第2步: 破解c4d R25', dialog)
        def install01_1():
            self.cmd_run('taskkill /F /IM "Cinema 4D.exe" /T')
            self.cmd_run(f'copy "{self.route}\\c4d\\R25\\c4dplugin.xdl64" "C:\\Program Files\\Maxon Cinema 4D R25\\corelibs"')
            QMessageBox.about(self,'消息','破解成功')
        button1_1.clicked.connect(install01_1)

        button2 = QPushButton('第3步: 复制octane文件夹', dialog)
        def install02():
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R25\\plugins"')
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R25\\plugins\\c4doctane"')
            self.cmd_run(f'xcopy "{self.route}\\c4d\\R25\\c4doctane" "C:\\Program Files\\Maxon Cinema 4D R25\\plugins\\c4doctane" /e /f /h')
        button2.clicked.connect(install02)

        edit5_0 = QLineEdit()
        button5 = QPushButton('第4步: 打开软件,安装语言包,登录octane', dialog)
        def install05():
            # 打开资源管理器,安装语言包
            self.cmd_run(f'explorer "{self.route}\\c4d\\R25"')
            # 运行c4d
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R25\\Cinema 4D.exe"')
            edit5_0.setText('"C:\\Program Files\\Maxon Cinema 4D R25\\Cinema 4D.exe"')
        button5.clicked.connect(install05)

        edit4_0 = QLineEdit()
        button4 = QPushButton('第5步: 将cudnn_8_0_4win文件夹复制到指定文件夹', dialog)
        def install04():
            # 运行命令行
            self.cmd_run(
                f'xcopy "{self.route}\\c4d\\cudnn_8_0_4_win" "C:\\Users\\Administrator\\AppData\\Local\\OctaneRender\\thirdparty\\cudnn_8_0_4" /e /f /h')
            QMessageBox.about(self, '消息', '登录octane账号,并关闭软件')
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R25\\Cinema 4D.exe"')
            edit4_0.setText('"C:\\Program Files\\Maxon Cinema 4D R25\\Cinema 4D.exe"')
        button4.clicked.connect(install04)

        button6 = QPushButton('第6步: 破解命令行登录', dialog)
        def install06():
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.cinebench.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.cineware.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.cineware_dll.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.commandline.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.trclient.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.trserver.txt"')
            QMessageBox.about(self,'破解','打开的文本账号复制到config.txt最下面并保存退出')

            self.cmd_run_txt('C:\\Program Files\\Maxon Cinema 4D R25\\resource\\config.txt')
            self.cmd_run_txt(f'{self.route}\\c4d\\R25\\R25config.txt')
        button6.clicked.connect(install06)

        edit7_0 = QLineEdit()
        button7 = QPushButton('第7步: 测试命令调用', dialog)
        def install07():
            self.cmd_run(f'"C:\\Program Files\\Maxon Cinema 4D R25\\Commandline.exe" \
-render {self.route}\\c4d\\R25\\R25test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R25\\test" -oformat jpg')
            self.cmd_run(f'explorer "{self.route}\\c4d\\R25"')
            edit7_0.setText(f'"C:\\Program Files\\Maxon Cinema 4D R25\\Commandline.exe" \
-render {self.route}\\c4d\\R25\\R25test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R25\\test" -oformat jpg')
        button7.clicked.connect(install07)

        button8 = QPushButton('第8步: 卸载C4D R22', dialog)
        def install08():
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R22\\uninstall.exe"')
        button8.clicked.connect(install08)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button1_1)
        layout.addWidget(button2)
        layout.addWidget(button5)
        layout.addWidget(edit5_0)
        layout.addWidget(button4)
        layout.addWidget(edit4_0)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(edit7_0)
        layout.addWidget(button8)
        layout.addWidget(cancle)

        dialog.setLayout(layout)
        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_c4d_R25.setChecked(True)
                dialog.close()
            else:
                dialog.close()
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_c4d_R24(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装c4d R24')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装c4d R24应用', dialog)

        def install01():
            self.cmd_run('"' + self.route + '\\c4d\\R24\\Setup.exe' + '"')

        button1.clicked.connect(install01)

        button1_1 = QPushButton('第2步: 破解c4d R24', dialog)

        def install01_1():
            self.cmd_run('taskkill /F /IM "Cinema 4D.exe" /T')
            self.cmd_run(
                f'copy "{self.route}\\c4d\\R24\\c4dplugin.xdl64" "C:\\Program Files\\Maxon Cinema 4D R24\\corelibs"')
            QMessageBox.about(self, '消息', '破解成功')
        button1_1.clicked.connect(install01_1)

        button2 = QPushButton('第3步: 复制octane文件夹', dialog)
        def install02():
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R24\\plugins"')
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R24\\plugins\\c4doctane"')
            self.cmd_run(
                f'xcopy "{self.route}\\c4d\\R24\\c4doctane" "C:\\Program Files\\Maxon Cinema 4D R24\\plugins\\c4doctane" /e /f /h')
        button2.clicked.connect(install02)

        button5 = QPushButton('第4步: 打开软件,安装语言包,登录octane', dialog)
        def install05():
            # 打开资源管理器,安装语言包
            self.cmd_run(f'explorer "{self.route}\\c4d\\R24"')
            # 运行c4d
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R24\\Cinema 4D.exe"')
        button5.clicked.connect(install05)

        button6 = QPushButton('第6步: 破解命令行登录', dialog)
        def install06():
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.cinebench.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.cineware.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.cineware_dll.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.commandline.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.trclient.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.trserver.txt"')
            QMessageBox.about(self, '破解', '打开的文本账号复制到config.txt最下面并保存退出')
            self.cmd_run_txt(f'{self.route}\\c4d\\R24\\R24config.txt')
            self.cmd_run_txt('C:\\Program Files\\Maxon Cinema 4D R24\\resource\\config.txt')

        button6.clicked.connect(install06)

        button7 = QPushButton('第7步: 测试命令调用', dialog)
        def install07():
            self.cmd_run(f'"C:\\Program Files\\Maxon Cinema 4D R24\\Commandline.exe" \
-render {self.route}\\c4d\\R24\\R24test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R24\\test" -oformat jpg')
            self.cmd_run(f'explorer "{self.route}\\c4d\\R24"')
        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button1_1)
        layout.addWidget(button2)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(cancle)

        dialog.setLayout(layout)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_c4d_R24.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_c4d_R23(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装c4d R23')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装c4d R23应用', dialog)
        def install01():
            self.cmd_run('"' + self.route + '\\c4d\\R23\\Setup.exe' + '"')
        button1.clicked.connect(install01)

        button1_1 = QPushButton('第2步: 先打开注册界面,再破解c4d R23', dialog)
        def install01_1():
            self.cmd_run('taskkill /F /IM "Cinema 4D.exe" /T')
            self.cmd_run(
                f'copy "{self.route}\\c4d\\R23\\licensing.module.xdl64" "C:\\Program Files\\Maxon Cinema 4D R23\\corelibs"')
            QMessageBox.about(self, '消息', '破解成功')

        button1_1.clicked.connect(install01_1)

        button2 = QPushButton('第3步: 复制octane文件夹', dialog)
        def install02():
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R23\\plugins"')
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R23\\plugins\\c4doctane"')
            self.cmd_run(
                f'xcopy "{self.route}\\c4d\\R23\\c4doctane" "C:\\Program Files\\Maxon Cinema 4D R23\\plugins\\c4doctane" /e /f /h')
        button2.clicked.connect(install02)

        edit5_0 = QLineEdit()
        button5 = QPushButton('第4步: 打开软件,安装语言包,登录octane', dialog)
        def install05():
            # 打开资源管理器,安装语言包
            self.cmd_run(f'explorer "{self.route}\\c4d\\R23"')
            # 运行c4d
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R23\\Cinema 4D.exe"')
            edit5_0.setText('"C:\\Program Files\\Maxon Cinema 4D R23\\Cinema 4D.exe"')
        button5.clicked.connect(install05)

        button6 = QPushButton('第6步: 破解命令行登录', dialog)
        def install06():
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.cinebench.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.cineware.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.cineware_dll.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.commandline.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.trclient.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.trserver.txt"')
            QMessageBox.about(self, '破解', '打开的文本账号复制到config.txt最下面并保存退出')

            self.cmd_run_txt('C:\\Program Files\\Maxon Cinema 4D R23\\resource\\config.txt')
            self.cmd_run_txt(f'{self.route}\\c4d\\R23\\R23config.txt')
        button6.clicked.connect(install06)

        edit7_0 = QLineEdit()
        button7 = QPushButton('第7步: 测试命令调用', dialog)
        def install07():
            self.cmd_run(f'"C:\\Program Files\\Maxon Cinema 4D R23\\Commandline.exe" \
-render {self.route}\\c4d\\R23\\R23test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R23\\test" -oformat jpg')
            self.cmd_run(f'explorer "{self.route}\\c4d\\R23"')
            edit7_0.setText(f'"C:\\Program Files\\Maxon Cinema 4D R23\\Commandline.exe" \
-render {self.route}\\c4d\\R23\\R23test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R23\\test" -oformat jpg')
        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button1_1)
        layout.addWidget(button2)
        layout.addWidget(button5)
        layout.addWidget(edit5_0)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(edit7_0)
        layout.addWidget(cancle)

        dialog.setLayout(layout)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_c4d_R23.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_c4d_R22(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装c4d R22')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装c4d R22应用', dialog)
        def install01():
            self.cmd_run('"' + self.route + '\\c4d\\R22\\SetUp.exe' + '"')
        button1.clicked.connect(install01)

        button1_1 = QPushButton('第2步: 先打开注册界面,再破解c4d R22', dialog)
        def install01_1():
            self.cmd_run('taskkill /F /IM "Cinema 4D.exe" /T')
            self.cmd_run(f'"{self.route}\\c4d\\R22\\crack.exe"')
        button1_1.clicked.connect(install01_1)

        button2 = QPushButton('第3步: 复制octane文件夹', dialog)
        def install02():
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R22\\plugins"')
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R22\\plugins\\c4doctane"')
            self.cmd_run(
                f'xcopy "{self.route}\\c4d\\R22\\c4doctane" "C:\\Program Files\\Maxon Cinema 4D R22\\plugins\\c4doctane" /e /f /h')
        button2.clicked.connect(install02)

        button5 = QPushButton('第4步: 打开软件,安装语言包,登录octane', dialog)
        def install05():
            # 打开资源管理器,安装语言包
            self.cmd_run(f'explorer "{self.route}\\c4d\\R22"')
            # 运行c4d
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R22\\Cinema 4D.exe"')
        button5.clicked.connect(install05)

        button6 = QPushButton('第6步: 破解命令行登录', dialog)

        def install06():
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.cinebench.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.cineware.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.cineware_dll.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.commandline.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.trclient.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.trserver.txt"')
            QMessageBox.about(self, '破解', '打开的文本账号复制到config.txt最下面并保存退出')
            self.cmd_run_txt(f'{self.route}\\c4d\\R22\\R22config.txt')
            self.cmd_run_txt('C:\\Program Files\\Maxon Cinema 4D R22\\resource\\config.txt')

        button6.clicked.connect(install06)

        button7 = QPushButton('第7步: 测试命令调用', dialog)
        def install07():
            self.cmd_run(f'"C:\\Program Files\\Maxon Cinema 4D R22\\Commandline.exe" \
-render {self.route}\\c4d\\R22\\R22test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R22\\test" -oformat jpg')
            self.cmd_run(f'explorer "{self.route}\\c4d\\R22"')
        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button1_1)
        layout.addWidget(button2)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(cancle)

        dialog.setLayout(layout)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_c4d_R22.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_c4d_R21(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装c4d R21')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装c4d R21应用', dialog)
        def install01():
            self.cmd_run('"' + self.route + '\\c4d\\R21\\Setup.exe' + '"')
        button1.clicked.connect(install01)

        button1_1 = QPushButton('第2步: 先打开注册界面,再破解c4d R21', dialog)
        def install01_1():
            self.cmd_run('taskkill /F /IM "Cinema 4D.exe" /T')
            self.cmd_run(
                f'copy "{self.route}\\c4d\\R21\\licensing.module.xdl64" "C:\\Program Files\\Maxon Cinema 4D R21\\corelibs"')
        button1_1.clicked.connect(install01_1)

        button2 = QPushButton('第3步: 复制octane文件夹', dialog)
        def install02():
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R21\\plugins"')
            self.cmd_run('mkdir "C:\\Program Files\\Maxon Cinema 4D R21\\plugins\\c4doctane"')
            self.cmd_run(
                f'xcopy "{self.route}\\c4d\\R21\\c4doctane" "C:\\Program Files\\Maxon Cinema 4D R21\\plugins\\c4doctane" /e /f /h')
        button2.clicked.connect(install02)

        edit5_0 = QLineEdit()
        button5 = QPushButton('第4步: 打开软件,安装语言包,登录octane', dialog)
        def install05():
            # 打开资源管理器,安装语言包
            self.cmd_run(f'explorer "{self.route}\\c4d\\R21"')
            # 运行c4d
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R21\\Cinema 4D.exe"')
            edit5_0.setText('"C:\\Program Files\\Maxon Cinema 4D R21\\Cinema 4D.exe"')
        button5.clicked.connect(install05)

        button6 = QPushButton('第6步: 破解命令行登录', dialog)
        def install06():
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.cinebench.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.cineware.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.cineware_dll.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.commandline.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.trclient.txt"')
            self.cmd_run('del "C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.trserver.txt"')
            QMessageBox.about(self, '破解', '打开的文本账号复制到config.txt最下面并保存退出')

            self.cmd_run_txt('C:\\Program Files\\Maxon Cinema 4D R21\\resource\\config.txt')
            self.cmd_run_txt(f'{self.route}\\c4d\\R21\\R21config.txt')
        button6.clicked.connect(install06)

        edit7_0 = QLineEdit()
        button7 = QPushButton('第7步: 测试命令调用', dialog)
        def install07():
            self.cmd_run(f'"C:\\Program Files\\Maxon Cinema 4D R21\\Commandline.exe" \
-render {self.route}\\c4d\\R21\\R21test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R21\\test" -oformat jpg')
            self.cmd_run(f'explorer "{self.route}\\c4d\\R21"')
            edit7_0.setText(f'"C:\\Program Files\\Maxon Cinema 4D R21\\Commandline.exe" \
-render {self.route}\\c4d\\R21\\R21test.c4d -frame 1 5 -oimage "{self.route}\\c4d\\R21\\test" -oformat jpg')
        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button1_1)
        layout.addWidget(button2)
        layout.addWidget(button5)
        layout.addWidget(edit5_0)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(edit7_0)
        layout.addWidget(cancle)

        dialog.setLayout(layout)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_c4d_R21.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_c4d_R20(self):
        pass
    def install_AE_2021(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装AE 2021')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装AE 2021安装包', dialog)
        def install01():
            self.cmd_run('"' + self.route + '\\AE\\AE2021\\AE2021.exe' + '"')
        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 安装插件', dialog)
        def install02():
            self.cmd_run(f'"{self.route}\\AE\\AE2021\\AE2021_plugins.exe"')
            self.cmd_run_txt(f'{self.route}\\AE\\AE2021\\2021_plugins.txt')
        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 打开AE 2021检查', dialog)
        def install03():
            self.cmd_run('"C:\\Program Files\\Adobe\\Adobe After Effects 2021\\Support Files\\AfterFX.exe"')
        button3.clicked.connect(install03)

        button4 = QPushButton('第4步: 测试命令调用', dialog)
        def install04():
            self.cmd_run(f'"C:\\Program Files\\Adobe\\Adobe After Effects 2021\\Support Files\\aerender.exe" \
-project "{self.route}\\AE\\AE2021\\2021test\\2021test.aep" \
-comp "2021test" -s 0 -e 5 \
-output "{self.route}\\AE\\AE2021\\2021test\\Images\\test[####].jpg"')
            self.cmd_run(f'explorer "{self.route}\\AE\\AE2021\\2021test\\Images') # 打开输出图片的文件夹
        button4.clicked.connect(install04)


        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_AE_2021.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_AE_2020(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装AE 2020')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装AE 2020安装包', dialog)

        def install01():
            self.cmd_run('"' + self.route + '\\AE\\AE2020\\Set-up.exe' + '"')

        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 安装插件', dialog)

        def install02():
            self.cmd_run(f'"{self.route}\\AE\\AE2020\\Ae Plug-ins Suite 19.14.exe"')
            self.cmd_run_txt(f'{self.route}\\AE\\AE2020\\2020_plugins.txt')

        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 打开AE 2020检查', dialog)

        def install03():
            self.cmd_run('"C:\\Program Files\\Adobe\\Adobe After Effects 2020\\Support Files\\AfterFX.exe"')

        button3.clicked.connect(install03)

        button4 = QPushButton('第4步: 测试命令调用', dialog)

        def install04():
            self.cmd_run(f'"C:\\Program Files\\Adobe\\Adobe After Effects 2020\\Support Files\\aerender.exe" \
-project "{self.route}\\AE\\AE2020\\2020test\\2020test.aep" \
-comp "2020test" -s 220 -e 225 \
-output "{self.route}\\AE\\AE2020\\2020test\\Images\\test[####].jpg"')
            self.cmd_run(f'explorer "{self.route}\\AE\\AE2020\\2020test\\Images')  # 打开输出图片的文件夹

        button4.clicked.connect(install04)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_AE_2020.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_3dmax_2022(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装3Dmax 2022')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装Step安装包', dialog)
        def install01():
            self.cmd_run(f'"{self.route}\\3dmax\\3dmax2022\\Setup.exe"')
        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 破解3dmax2022', dialog)
        def install02():
            self.cmd_run(f'copy "{self.route}\\3dmax\\3dmax2022\\3dsmax.exe" "C:\\Program Files\\Autodesk\\3ds Max 2022"')
        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 安装Vray5.1 for 2022', dialog)
        def install03():
            self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2022\\vray_adv_51002_max2022_x64.exe"')
        button3.clicked.connect(install03)

        button4 = QPushButton('第4步: 破解Vray5.1', dialog)
        def install04():
            self.cmd_run(f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2022\\Crack" "C:\\Program Files\\Autodesk\\3ds Max 2022\\Plugins" /e /f /h')
            self.cmd_run(f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2022\\Crack" "C:\\ProgramData\\Autodesk\\ApplicationPlugins\\VRay3dsMax2022\\bin\\plugins" /e /f /h')
            self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\汉化补丁2022.exe"')
        button4.clicked.connect(install04)

        button5 = QPushButton('第5步: 安装Vray5.1材质库', dialog)
        def install05():
            self.cmd_run(f'xcopy "{self.route}\\3dmax\\V-Ray Material Library" "C:\\Users\\Administrator\\Documents\\V-Ray Material Library" /e /f /h')
        button5.clicked.connect(install05)

        button6 = QPushButton('第6步: 打开3dmax 2022检查vray5.1, 关闭安全消息', dialog)
        def install06():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\3ds Max 2022\\3dsmax.exe" /Language=CHS')
        button6.clicked.connect(install06)

        edit0 = QLineEdit('"C:\\Program Files\\Autodesk\\3ds Max 2022\\3dsmax.exe" /Language=CHS',dialog)
        edit1 = QLineEdit(dialog)

        button7 = QPushButton('第7步: 测试命令调用', dialog)
        def install07():
            edit1.setText(f'"C:\\Program Files\\Autodesk\\3ds Max 2022\\3dsmaxcmd.exe" \
"{self.route}\\3dmax\\3dmax2022\\2022test\\2022test.max" \
-outputName:"{self.route}\\3dmax\\3dmax2022\\2022test\\test.jpg" \
-start:50 -end:51')
            self.cmd_run(f'explorer "{self.route}\\3dmax\\3dmax2022\\2022test') # 打开输出图片的文件夹
        button7.clicked.connect(install07)


        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(edit0)
        layout.addWidget(button7)
        layout.addWidget(edit1)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_3dmax_2022.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_3dmax_2021(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装3Dmax 2021')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装Step安装包', dialog)

        def install01():
            self.cmd_run(f'"{self.route}\\3dmax\\3dmax2021\\Setup.exe"')

        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 破解3dmax2021', dialog)
        def install02():
            self.cmd_run(
                f'copy "{self.route}\\3dmax\\3dmax2021\\3dsmax.exe" "C:\\Program Files\\Autodesk\\3ds Max 2021"')
        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 安装Vray5.1 for 2021', dialog)
        def install03():
            self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2021\\vray_adv_51002_max2021_x64.exe"')
        button3.clicked.connect(install03)

        button4 = QPushButton('第4步: 破解Vray5.1', dialog)
        def install04():
            self.cmd_run(
                f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2021\\Crack" "C:\\Program Files\\Autodesk\\3ds Max 2021\\Plugins" /e /f /h')
            self.cmd_run(
                f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2021\\Crack" "C:\\ProgramData\\Autodesk\\ApplicationPlugins\\VRay3dsMax2021\\bin\\plugins" /e /f /h')
            self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2021\\汉化补丁2021.exe"')
        button4.clicked.connect(install04)

        # button5 = QPushButton('第5步: 安装Vray5.1材质库', dialog)
        # def install05():
        #     self.cmd_run(
        #         f'xcopy "{self.route}\\3dmax\\V-Ray Material Library" "C:\\Users\\Administrator\\Documents\\V-Ray Material Library" /e /f /h')
        # button5.clicked.connect(install05)

        button6 = QPushButton('第5步: 打开3dmax 2021检查vray5.1, 关闭安全消息', dialog)
        def install06():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\3ds Max 2021\\3dsmax.exe" /Language=CHS')
        button6.clicked.connect(install06)
        edit0 = QLineEdit('"C:\\Program Files\\Autodesk\\3ds Max 2021\\3dsmax.exe" /Language=CHS', dialog)
        edit1 = QLineEdit(dialog)

        button7 = QPushButton('第6步: 测试命令调用', dialog)
        def install07():
            edit1.setText(f'"C:\\Program Files\\Autodesk\\3ds Max 2021\\3dsmaxcmd.exe" \
"{self.route}\\3dmax\\3dmax2021\\2021test\\2021test.max" \
-outputName:"{self.route}\\3dmax\\3dmax2021\\2021test\\test.jpg" \
-start:520 -end:521')
            self.cmd_run(f'explorer "{self.route}\\3dmax\\3dmax2021\\2021test')  # 打开输出图片的文件夹

        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        # layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(edit0)
        layout.addWidget(button7)
        layout.addWidget(edit1)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_3dmax_2021.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_3dmax_2020(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装3Dmax 2020')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装Step安装包', dialog)
        def install01():
            self.cmd_run(f'"{self.route}\\3dmax\\3dmax2020\\Setup.exe"')
        button1.clicked.connect(install01)

        button1_0 = QPushButton('第1.5步: 解决循环无法破解问题', dialog)
        def install01_0():
            self.cmd_run(f'explorer "{self.route}\\3dmax\\3dmax2020\\3dmax_activation')
        button1_0.clicked.connect(install01_0)

        # edit2_0 = QLineEdit(dialog)
        button2 = QPushButton('第2步: 手动打开3dmax2020,666-69696969 128L1', dialog)
        def install02():
            QMessageBox.about(self,'消息','手动打开3dmas2020 Simple Chinese')
            # self.cmd_run('"C:\\Program Files\\Autodesk\\3ds Max 2020\\3dsmax.exe" /Language=CHS')
            # edit2_0.setText('"C:\\Program Files\\Autodesk\\3ds Max 2020\\3dsmax.exe" /Language=CHS')
        button2.clicked.connect(install02)

        button2_0 = QPushButton('第2.5步: 打开3dmax2020的注册机,复制申请号->Patch->Generate', dialog)
        def install02_0():
            self.cmd_run(f'"{self.route}\\3dmax\\3dmax2020\\xf-adesk.exe"')
        button2_0.clicked.connect(install02_0)


        button3 = QPushButton('第3步: 安装Vray5.1 for 2020', dialog)
        def install03():
            self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2020\\vray_adv_51002_max2020_x64.exe"')
        button3.clicked.connect(install03)

        button4 = QPushButton('第4步: 破解Vray5.1', dialog)
        def install04():
            self.cmd_run(
                f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2020\\Crack" "C:\\Program Files\\Autodesk\\3ds Max 2020\\Plugins" /e /f /h')
            self.cmd_run(
                f'copy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2020\\Crack\\vray_v50004_max_fix.dll" "C:\\Program Files\\Chaos Group\\V-Ray\\3ds Max 2020\\bin\\plugins" /e /f /h')
            self.cmd_run('D')
            self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2020\\汉化补丁2020.exe"')
        button4.clicked.connect(install04)

        # button5 = QPushButton('第5步: 安装Vray5.1材质库', dialog)
        # def install05():
        #     self.cmd_run(
        #         f'xcopy "{self.route}\\3dmax\\V-Ray Material Library" "C:\\Users\\Administrator\\Documents\\V-Ray Material Library" /e /f /h')
        # button5.clicked.connect(install05)

        button6 = QPushButton('第5步: 手动打开3dmax 2020检查vray5.1, 关闭安全消息', dialog)
        def install06():
            QMessageBox.about(self,'消息','手动打开3dsmax2020 simple Chinese')
            # self.cmd_run(f'"C:\\Program Files\\Autodesk\\3ds Max 2020\\3dsmax.exe" /Language=CHS')
        button6.clicked.connect(install06)
        # edit0 = QLineEdit('"C:\\Program Files\\Autodesk\\3ds Max 2020\\3dsmax.exe" /Language=CHS', dialog)
        edit1 = QLineEdit(dialog)

        button7 = QPushButton('第6步: 测试命令调用', dialog)
        def install07():
            edit1.setText(f'"C:\\Program Files\\Autodesk\\3ds Max 2020\\3dsmaxcmd.exe" \
"{self.route}\\3dmax\\3dmax2020\\2020test\\2020test.max" \
-outputName:"{self.route}\\3dmax\\3dmax2020\\2020test\\test.jpg" \
-start:380 -end:382')
            self.cmd_run(f'explorer "{self.route}\\3dmax\\3dmax2020\\2020test')  # 打开输出图片的文件夹
        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)

        layout.addWidget(button2)
        layout.addWidget(button1_0)
        # layout.addWidget(edit2_0)
        layout.addWidget(button2_0)
        layout.addWidget(button3)
        layout.addWidget(button4)
        # layout.addWidget(button5)
        layout.addWidget(button6)
        # layout.addWidget(edit0)
        layout.addWidget(button7)
        layout.addWidget(edit1)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_3dmax_2020.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_3dmax_2019(self):
        pass
#         dialog = QDialog()
#         dialog.setWindowTitle('安装3Dmax 2019')
#         dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
#         layout = QVBoxLayout()
#
#         button1 = QPushButton('第1步: 安装Step安装包', dialog)
#         def install01():
#             # self.cmd_run('taskkill /F /IM "3dsmax.exe" /T')
#             self.cmd_run(f'"{self.route}\\3dmax\\3dmax2019\\Setup.exe"')
#         button1.clicked.connect(install01)
#
#         edit2_0 = QLineEdit(dialog)
#         button2 = QPushButton('第2步: 打开3dmax2019,666-69696969 128K1', dialog)
#         def install02():
#             self.cmd_run('"C:\\Program Files\\Autodesk\\3ds Max 2019\\3dsmax.exe" /Language=CHS')
#             edit2_0.setText('"C:\\Program Files\\Autodesk\\3ds Max 2019\\3dsmax.exe" /Language=CHS')
#         button2.clicked.connect(install02)
#
#         button2_0 = QPushButton('第2.5步: 打开3dmax2019的注册机,复制申请号->Patch->Generate', dialog)
#         def install02_0():
#             self.cmd_run(f'"{self.route}\\3dmax\\3dmax2019\\adsk.exe"')
#         button2_0.clicked.connect(install02_0)
#
#         button3 = QPushButton('第3步: 安装Vray5.1 for 2019', dialog)
#         def install03():
#             self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2019\\vray_adv_51002_max2019_x64.exe"')
#         button3.clicked.connect(install03)
#
#         button4 = QPushButton('第4步: 破解Vray5.1', dialog)
#         def install04():
#             self.cmd_run(
#                 f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2019\\Crack" "C:\\Program Files\\Autodesk\\3ds Max 2019\\Plugins" /e /f /h')
#             self.cmd_run(
#                 f'xcopy "{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2019\\Crack" "C:\\ProgramData\\Autodesk\\ApplicationPlugins\\VRay3dsMax2019\\bin\\plugins" /e /f /h')
#             self.cmd_run('D')
#             self.cmd_run(f'"{self.route}\\3dmax\\Vray5_1\\vray_adv_51002_max2019\\汉化补丁2019.exe"')
#         button4.clicked.connect(install04)
#
#         # button5 = QPushButton('第5步: 安装Vray5.1材质库', dialog)
#         # def install05():
#         #     self.cmd_run(
#         #         f'xcopy "{self.route}\\3dmax\\V-Ray Material Library" "C:\\Users\\Administrator\\Documents\\V-Ray Material Library" /e /f /h')
#         # button5.clicked.connect(install05)
#
#         button6 = QPushButton('第5步: 打开3dmax 2019检查vray5.1, 关闭安全消息', dialog)
#         def install06():
#             self.cmd_run(f'"C:\\Program Files\\Autodesk\\3ds Max 2019\\3dsmax.exe" /Language=CHS')
#         button6.clicked.connect(install06)
#         edit0 = QLineEdit('"C:\\Program Files\\Autodesk\\3ds Max 2019\\3dsmax.exe" /Language=CHS', dialog)
#         edit1 = QLineEdit(dialog)
#
#         button7 = QPushButton('第6步: 测试命令调用', dialog)
#         def install07():
#             edit1.setText(f'"C:\\Program Files\\Autodesk\\3ds Max 2019\\3dsmaxcmd.exe" \
# "{self.route}\\3dmax\\3dmax2019\\2019test\\2019test.max" \
# -outputName:"{self.route}\\3dmax\\3dmax2019\\2019test\\test.jpg" \
# -start:500 -end:502')
#             self.cmd_run(f'explorer "{self.route}\\3dmax\\3dmax2019\\2019test')  # 打开输出图片的文件夹
#
#         button7.clicked.connect(install07)
#
#         cancle = QPushButton('退出', dialog)
#         layout.addWidget(button1)
#         layout.addWidget(button2)
#         layout.addWidget(edit2_0)
#         layout.addWidget(button2_0)
#         layout.addWidget(button3)
#         layout.addWidget(button4)
#         # layout.addWidget(button5)
#         layout.addWidget(button6)
#         layout.addWidget(edit0)
#         layout.addWidget(button7)
#         layout.addWidget(edit1)
#         layout.addWidget(cancle)
#
#         def msg():
#             reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#             if reply == QMessageBox.Yes:
#                 self.cb_3dmax_2019.setChecked(True)
#                 dialog.close()
#             else:
#                 dialog.close()
#
#         dialog.setLayout(layout)
#         cancle.clicked.connect(msg)
#         dialog.exec_()
    def install_3dmax_2018(self):
        pass
    def install_maya_2022(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装maya 2022')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装Step安装包', dialog)
        def install01():
            self.cmd_run(f'"{self.route}\\maya\\maya2022\\Setup.exe"')
        button1.clicked.connect(install01)

        edit0 = QLineEdit(dialog)
        button2 = QPushButton('第2步: 打开maya 2022检查,并关闭安全消息', dialog)
        def install02():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\Maya2022\\bin\\maya.exe"')
            edit0.setText('"C:\\Program Files\\Autodesk\\Maya2022\\bin\\maya.exe"')
        button2.clicked.connect(install02)

        edit1 = QLineEdit(dialog)
        button3 = QPushButton('第3步: 测试命令调用', dialog)
        def install03():
            edit1.setText(f'"C:\\Program Files\\Autodesk\\Maya2022\\bin\\Render.exe" \
-r file -rd {self.route}\\maya\\maya2022 -im test -of png -s 0 -e 5 {self.route}\\maya\\maya2022\\2022test.mb')
            self.cmd_run(f'explorer "{self.route}\\maya\\maya2022"')
        button3.clicked.connect(install03)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(edit0)
        layout.addWidget(button3)
        layout.addWidget(edit1)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_maya_2022.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_maya_2020(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装maya 2020')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装Step安装包', dialog)
        def install01():
            self.cmd_run(f'"{self.route}\\maya\\maya2020\\Setup.exe"')
        button1.clicked.connect(install01)

        button1_0 = QPushButton('第1.5步: 解决循环无法破解问题', dialog)
        def install01_0():
            self.cmd_run(f'explorer "{self.route}\\3dmax\\3dmax2020\\3dmax_activation')
        button1_0.clicked.connect(install01_0)

        edit0 = QLineEdit(dialog)
        button2 = QPushButton('第2步: 打开maya 2020,666-69696969,657L1', dialog)
        def install02():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe"')
            edit0.setText('"C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe"')
        button2.clicked.connect(install02)

        button2_0 = QPushButton('第2.5步: 打开注册机,复制申请号->Patch->Generate', dialog)
        def install02_0():
            self.cmd_run(f'"{self.route}\\maya\\maya2020\\2020 KeyGen.exe"')
        button2_0.clicked.connect(install02_0)

        edit1 = QLineEdit(dialog)
        button3 = QPushButton('第3步: 测试命令调用', dialog)
        def install03():
            QMessageBox.about(self,'消息','关闭安全消息')
            edit1.setText(f'"C:\\Program Files\\Autodesk\\Maya2020\\bin\\Render.exe" \
-r file -rd {self.route}\\maya\\maya2020 -im test -of png -s 0 -e 5 {self.route}\\maya\\maya2020\\2020test.mb')
            self.cmd_run(f'explorer "{self.route}\\maya\\maya2020"')
        button3.clicked.connect(install03)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(edit0)
        layout.addWidget(button1_0)
        layout.addWidget(button2_0)
        layout.addWidget(button3)
        layout.addWidget(edit1)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_maya_2020.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_maya_2019(self):
        pass
    def install_maya_2018(self):
        pass
    def install_houdini_185_696(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装houdini 18.5.696')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装houdini安装包', dialog)

        def install01():
            self.cmd_run(f'"{self.route}\\houdini\\Houdini_18_5_696\\houdini-py3-18.5.696-win64-vc141.exe"')
        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 打开注册机,点击patch按钮', dialog)
        def install02():
            self.cmd_run(f'"{self.route}\\houdini\\Houdini_18_5_696\\zhuce\\Houdini-18.5-Keygen-Win.exe"')
        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 打开License Administrator', dialog)
        def install03():
            self.cmd_run('"C:\\Program Files\\Side Effects Software\\Houdini 18.5.696\\bin\\hkey.exe"')
        button3.clicked.connect(install03)

        label01 = QLabel('第4步: 输入Server Name和Server Code, 点击Generate Keys',dialog)
        label02 = QLabel('第5步: 打开file-Manually Enter Keys, 复制前5行序列号',dialog)

        button4 = QPushButton('第6步: 打开houdini软件检查', dialog)
        def install04():
            self.cmd_run('"C:\\Program Files\\Side Effects Software\\Houdini 18.5.696\\bin\\houdinifx.exe"')
        button4.clicked.connect(install04)

        button5 = QPushButton('第7步: 测试命令调用', dialog)
        def install05():
            self.cmd_run(f'"C:\\Program Files\\Side Effects Software\\Houdini 18.5.696\\bin\\hython.exe" \
"C:\\Program Files\\Side Effects Software\\Houdini 18.5.696\\bin\\hrender.py" \
-d /out/man \
-o {self.route}\\houdini\\Houdini_18_5_696\\test_$F.jpg -e -f 4 5 \
{self.route}\\houdini\\Houdini_18_5_696\\696test.hip ')
            self.cmd_run(f'explorer "{self.route}\\houdini\\Houdini_18_5_696"')
        button5.clicked.connect(install05)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(label01)
        layout.addWidget(label02)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_houdini_696.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_nuke_12_2(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装nuke12.2V2')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 安装Step安装包', dialog)
        def install01():
            self.cmd_run(f'"{self.route}\\nuke\\Nuke_12.2v2\\Nuke-12.2v2-win-x86-64-installer.exe"')
        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 破解nuke', dialog)
        def install02():
            self.cmd_run(f'"{self.route}\\nuke\\Nuke_12.2v2\\Crack.exe"')
        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 打开nuke检查,并修改视频路径', dialog)
        def install03():
            self.cmd_run(f'"C:\\Program Files\\Nuke12.2v2\\Nuke12.2.exe" "{self.route}\\nuke\\Nuke_12.2v2\\12_2_test.nk"')
            self.cmd_run(f'explorer "{self.route}\\nuke\\Nuke_12.2v2"')
        button3.clicked.connect(install03)

        button4 = QPushButton('第4步: 测试命令调用', dialog)
        def install04():
            temp_route = self.route
            temp_route_ = temp_route.replace('\\','/')
            self.cmd_run(f'"C:\\Program Files\\Nuke12.2v2\\Nuke12.2.exe" -x \
-X Write1 --cont "{self.route}\\nuke\\Nuke_12.2v2\\12_2_test.nk" "{temp_route_}/nuke/Nuke_12.2v2/test_#####.jpg" 5-10')
            self.cmd_run(f'explorer "{self.route}\\nuke\\Nuke_12.2v2"')
        button4.clicked.connect(install04)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_nuke_12_2.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_Maxon(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装Maxon')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        def installmaxon():
            self.cmd_run('"'+self.route+'\\Maxon_2_0.exe'+'"')
        button1 = QPushButton('第1步: 安装Maxon APP',dialog)
        button1.clicked.connect(installmaxon)

        def installmaxon2():
            self.cmd_run_txt(f'{self.route}\\redshift\\maxonAccounts.txt')
        button2 = QPushButton('第2步: 登录Maxon APP',dialog)
        button2.clicked.connect(installmaxon2)

        cancle = QPushButton('退出', dialog)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(cancle)
        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_c4d_Maxon.setChecked(True)
                dialog.close()
            else:
                dialog.close()
        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()
    def install_plugins_redshift(self):
        dialog = QDialog()
        dialog.setWindowTitle('安装redshift')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当使用对话框是，主窗口是否可用
        layout = QVBoxLayout()

        button1 = QPushButton('第1步: 登录Maxon', dialog)
        def install01():
            self.cmd_run('"C:\\Program Files\\Maxon\\App Manager\\Maxon.exe"')
        button1.clicked.connect(install01)

        button2 = QPushButton('第2步: 安装redshift', dialog)
        def install02():
            self.cmd_run(f'"{self.route}\\redshift\\redshift_v3.0.57_setup.exe"')
        button2.clicked.connect(install02)

        button3 = QPushButton('第3步: 打开C4D R25检查', dialog)
        def install03():
            self.cmd_run('"C:\\Program Files\\Maxon Cinema 4D R25\\Cinema 4D.exe"')
        button3.clicked.connect(install03)

        edit0 = QLineEdit(dialog)
        button4 = QPushButton('第4步: 打开3dmax 2022检查', dialog)
        def install04():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\3ds Max 2022\\3dsmax.exe"')
            edit0.setText('"C:\\Program Files\\Autodesk\\3ds Max 2022\\3dsmax.exe"')
        button4.clicked.connect(install04)

        edit1 = QLineEdit(dialog)
        button5 = QPushButton('第5步: 打开Maya 2022检查,并在插件管理器中设置', dialog)
        def install05():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\Maya2022\\bin\\maya.exe"')
            edit1.setText('"C:\\Program Files\\Autodesk\\Maya2022\\bin\\maya.exe"')
        button5.clicked.connect(install05)

        edit2 = QLineEdit()
        button5_0 = QPushButton('第5.5步: 打开Maya 2020检查,并在插件管理器中设置', dialog)
        def install05_0():
            self.cmd_run(f'"C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe"')
            edit2.setText('"C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe"')
        button5_0.clicked.connect(install05_0)

        button6 = QPushButton('第6步: 替换houdini.env文件', dialog)
        def install06():
            self.cmd_run(f'copy "{self.route}\\redshift\\houdini.env" "C:\\Users\\Administrator\\Documents\\houdini18.5"')
        button6.clicked.connect(install06)

        button7 = QPushButton('第7步: 打开houdini检查', dialog)
        def install07():
            self.cmd_run('"C:\\Program Files\\Side Effects Software\\Houdini 18.5.696\\bin\\houdinifx.exe"')
        button7.clicked.connect(install07)

        cancle = QPushButton('退出', dialog)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(edit0)
        layout.addWidget(button5)

        layout.addWidget(edit1)
        layout.addWidget(button5_0)
        layout.addWidget(edit2)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(cancle)

        def msg():
            reply = QMessageBox.information(self, '消息', '是否安装完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cb_plugins_redshift.setChecked(True)
                dialog.close()
            else:
                dialog.close()

        dialog.setLayout(layout)
        cancle.clicked.connect(msg)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 固定写法
    main = MainRender()  # 创建窗口实例

    apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='dark_amber.xml')
    # apply_stylesheet(app, theme='dark_cyan.xml')
    # apply_stylesheet(app, theme='dark_lightgreen.xml')
    # apply_stylesheet(app, theme='light_amber.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    main.show()  # 展示窗口
    sys.exit(app.exec_())  # 关于系统的