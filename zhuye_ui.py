# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zhuye.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_zhu_windows(object):
    def setupUi(self, zhu_windows):
        if not zhu_windows.objectName():
            zhu_windows.setObjectName(u"zhu_windows")
        zhu_windows.resize(993, 680)
        zhu_windows.setMinimumSize(QSize(0, 0))
        self.verticalLayout_13 = QVBoxLayout(zhu_windows)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_3 = QLabel(zhu_windows)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 30))
        self.label_3.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.input_file = QLineEdit(zhu_windows)
        self.input_file.setObjectName(u"input_file")
        self.input_file.setMinimumSize(QSize(240, 30))
        self.input_file.setMaximumSize(QSize(66666, 30))

        self.horizontalLayout_2.addWidget(self.input_file)

        self.horizontalLayout_2.setStretch(1, 10)

        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.function_list = QTabWidget(zhu_windows)
        self.function_list.setObjectName(u"function_list")
        self.function_list.setMinimumSize(QSize(430, 0))
        self.function_list.setMaximumSize(QSize(430, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.function_list.setFont(font)
        self.file_tab = QWidget()
        self.file_tab.setObjectName(u"file_tab")
        self.gridLayout_2 = QGridLayout(self.file_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.flag_search_but = QPushButton(self.file_tab)
        self.flag_search_but.setObjectName(u"flag_search_but")
        self.flag_search_but.setMinimumSize(QSize(100, 25))
        self.flag_search_but.setMaximumSize(QSize(100, 25))
        self.flag_search_but.setSizeIncrement(QSize(100, 30))
        self.flag_search_but.setBaseSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.flag_search_but.setFont(font1)

        self.horizontalLayout_26.addWidget(self.flag_search_but)

        self.re_ipnut = QLineEdit(self.file_tab)
        self.re_ipnut.setObjectName(u"re_ipnut")

        self.horizontalLayout_26.addWidget(self.re_ipnut)


        self.gridLayout_2.addLayout(self.horizontalLayout_26, 0, 0, 1, 2)

        self.label_9 = QLabel(self.file_tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.shibie_but = QPushButton(self.file_tab)
        self.shibie_but.setObjectName(u"shibie_but")
        self.shibie_but.setMinimumSize(QSize(100, 25))
        self.shibie_but.setMaximumSize(QSize(100, 25))
        self.shibie_but.setSizeIncrement(QSize(100, 30))
        self.shibie_but.setBaseSize(QSize(100, 30))
        self.shibie_but.setFont(font1)

        self.horizontalLayout_3.addWidget(self.shibie_but)

        self.print_str_but = QPushButton(self.file_tab)
        self.print_str_but.setObjectName(u"print_str_but")
        self.print_str_but.setMinimumSize(QSize(100, 25))
        self.print_str_but.setMaximumSize(QSize(100, 25))
        self.print_str_but.setSizeIncrement(QSize(100, 30))
        self.print_str_but.setBaseSize(QSize(100, 30))
        self.print_str_but.setFont(font1)

        self.horizontalLayout_3.addWidget(self.print_str_but)

        self.fenli_but = QPushButton(self.file_tab)
        self.fenli_but.setObjectName(u"fenli_but")
        self.fenli_but.setMinimumSize(QSize(100, 25))
        self.fenli_but.setMaximumSize(QSize(100, 25))
        self.fenli_but.setSizeIncrement(QSize(100, 30))
        self.fenli_but.setBaseSize(QSize(100, 30))
        self.fenli_but.setFont(font1)

        self.horizontalLayout_3.addWidget(self.fenli_but)

        self.for_but = QPushButton(self.file_tab)
        self.for_but.setObjectName(u"for_but")
        self.for_but.setMinimumSize(QSize(100, 25))
        self.for_but.setMaximumSize(QSize(100, 25))
        self.for_but.setSizeIncrement(QSize(100, 30))
        self.for_but.setBaseSize(QSize(100, 30))
        self.for_but.setFont(font1)

        self.horizontalLayout_3.addWidget(self.for_but)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_26)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.str_down_but = QPushButton(self.file_tab)
        self.str_down_but.setObjectName(u"str_down_but")
        self.str_down_but.setMinimumSize(QSize(100, 25))
        self.str_down_but.setMaximumSize(QSize(100, 25))
        self.str_down_but.setSizeIncrement(QSize(100, 30))
        self.str_down_but.setBaseSize(QSize(100, 30))
        self.str_down_but.setFont(font1)

        self.horizontalLayout_5.addWidget(self.str_down_but)

        self.zipin_but = QPushButton(self.file_tab)
        self.zipin_but.setObjectName(u"zipin_but")
        self.zipin_but.setMinimumSize(QSize(100, 25))
        self.zipin_but.setMaximumSize(QSize(100, 25))
        self.zipin_but.setFont(font1)

        self.horizontalLayout_5.addWidget(self.zipin_but)

        self.cipin_but = QPushButton(self.file_tab)
        self.cipin_but.setObjectName(u"cipin_but")
        self.cipin_but.setMinimumSize(QSize(100, 25))
        self.cipin_but.setMaximumSize(QSize(100, 25))
        self.cipin_but.setSizeIncrement(QSize(100, 30))
        self.cipin_but.setBaseSize(QSize(100, 30))
        self.cipin_but.setFont(font1)

        self.horizontalLayout_5.addWidget(self.cipin_but)

        self.zero_str_but = QPushButton(self.file_tab)
        self.zero_str_but.setObjectName(u"zero_str_but")
        self.zero_str_but.setMinimumSize(QSize(100, 25))
        self.zero_str_but.setMaximumSize(QSize(100, 25))
        self.zero_str_but.setSizeIncrement(QSize(100, 30))
        self.zero_str_but.setBaseSize(QSize(100, 30))
        self.zero_str_but.setFont(font1)

        self.horizontalLayout_5.addWidget(self.zero_str_but)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_27)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 2)

        self.label_10 = QLabel(self.file_tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.input_text = QTextEdit(self.file_tab)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setMinimumSize(QSize(0, 60))
        self.input_text.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.input_text.setFont(font2)
        self.input_text.setReadOnly(False)

        self.gridLayout_2.addWidget(self.input_text, 5, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.html_but = QPushButton(self.file_tab)
        self.html_but.setObjectName(u"html_but")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.html_but.sizePolicy().hasHeightForWidth())
        self.html_but.setSizePolicy(sizePolicy)
        self.html_but.setMinimumSize(QSize(100, 25))
        self.html_but.setMaximumSize(QSize(100, 25))
        self.html_but.setFont(font1)

        self.verticalLayout_7.addWidget(self.html_but)

        self.base_but = QPushButton(self.file_tab)
        self.base_but.setObjectName(u"base_but")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(120)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.base_but.sizePolicy().hasHeightForWidth())
        self.base_but.setSizePolicy(sizePolicy1)
        self.base_but.setMinimumSize(QSize(100, 25))
        self.base_but.setMaximumSize(QSize(100, 25))
        self.base_but.setSizeIncrement(QSize(120, 0))
        self.base_but.setFont(font1)

        self.verticalLayout_7.addWidget(self.base_but)

        self.fuck_but = QPushButton(self.file_tab)
        self.fuck_but.setObjectName(u"fuck_but")
        self.fuck_but.setMinimumSize(QSize(100, 25))
        self.fuck_but.setMaximumSize(QSize(100, 25))
        self.fuck_but.setFont(font1)

        self.verticalLayout_7.addWidget(self.fuck_but)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.url_but = QPushButton(self.file_tab)
        self.url_but.setObjectName(u"url_but")
        sizePolicy.setHeightForWidth(self.url_but.sizePolicy().hasHeightForWidth())
        self.url_but.setSizePolicy(sizePolicy)
        self.url_but.setMinimumSize(QSize(100, 25))
        self.url_but.setMaximumSize(QSize(100, 25))
        self.url_but.setFont(font1)

        self.verticalLayout_15.addWidget(self.url_but)

        self.kaisa_but = QPushButton(self.file_tab)
        self.kaisa_but.setObjectName(u"kaisa_but")
        sizePolicy.setHeightForWidth(self.kaisa_but.sizePolicy().hasHeightForWidth())
        self.kaisa_but.setSizePolicy(sizePolicy)
        self.kaisa_but.setMinimumSize(QSize(100, 25))
        self.kaisa_but.setMaximumSize(QSize(100, 25))
        self.kaisa_but.setSizeIncrement(QSize(120, 30))
        self.kaisa_but.setFont(font1)

        self.verticalLayout_15.addWidget(self.kaisa_but)

        self.ook_but = QPushButton(self.file_tab)
        self.ook_but.setObjectName(u"ook_but")
        self.ook_but.setMinimumSize(QSize(100, 25))
        self.ook_but.setMaximumSize(QSize(100, 25))
        self.ook_but.setFont(font1)

        self.verticalLayout_15.addWidget(self.ook_but)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.hex_str_but = QPushButton(self.file_tab)
        self.hex_str_but.setObjectName(u"hex_str_but")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(120)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.hex_str_but.sizePolicy().hasHeightForWidth())
        self.hex_str_but.setSizePolicy(sizePolicy2)
        self.hex_str_but.setMinimumSize(QSize(100, 25))
        self.hex_str_but.setMaximumSize(QSize(100, 25))
        self.hex_str_but.setSizeIncrement(QSize(120, 0))
        self.hex_str_but.setFont(font1)
#if QT_CONFIG(tooltip)
        self.hex_str_but.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.hex_str_but.setAutoExclusive(False)

        self.verticalLayout_17.addWidget(self.hex_str_but)

        self.zhalan_but = QPushButton(self.file_tab)
        self.zhalan_but.setObjectName(u"zhalan_but")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(120)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.zhalan_but.sizePolicy().hasHeightForWidth())
        self.zhalan_but.setSizePolicy(sizePolicy3)
        self.zhalan_but.setMinimumSize(QSize(100, 25))
        self.zhalan_but.setMaximumSize(QSize(100, 25))
        self.zhalan_but.setFont(font1)

        self.verticalLayout_17.addWidget(self.zhalan_but)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.hex_str = QPushButton(self.file_tab)
        self.hex_str.setObjectName(u"hex_str")
        self.hex_str.setMinimumSize(QSize(100, 25))
        self.hex_str.setMaximumSize(QSize(100, 25))
        self.hex_str.setFont(font1)

        self.verticalLayout_18.addWidget(self.hex_str)

        self.hexin_but = QPushButton(self.file_tab)
        self.hexin_but.setObjectName(u"hexin_but")
        self.hexin_but.setMinimumSize(QSize(100, 25))
        self.hexin_but.setMaximumSize(QSize(100, 25))
        self.hexin_but.setFont(font1)

        self.verticalLayout_18.addWidget(self.hexin_but)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_18)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)

        self.label_11 = QLabel(self.file_tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.exif_but = QPushButton(self.file_tab)
        self.exif_but.setObjectName(u"exif_but")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(120)
        sizePolicy4.setVerticalStretch(30)
        sizePolicy4.setHeightForWidth(self.exif_but.sizePolicy().hasHeightForWidth())
        self.exif_but.setSizePolicy(sizePolicy4)
        self.exif_but.setMinimumSize(QSize(100, 25))
        self.exif_but.setMaximumSize(QSize(100, 25))
        self.exif_but.setFont(font1)

        self.verticalLayout_19.addWidget(self.exif_but)

        self.tu_re = QPushButton(self.file_tab)
        self.tu_re.setObjectName(u"tu_re")
        self.tu_re.setMinimumSize(QSize(100, 25))
        self.tu_re.setMaximumSize(QSize(100, 25))
        self.tu_re.setFont(font1)

        self.verticalLayout_19.addWidget(self.tu_re)

        self.jpg_high_but = QPushButton(self.file_tab)
        self.jpg_high_but.setObjectName(u"jpg_high_but")
        self.jpg_high_but.setMinimumSize(QSize(100, 25))
        self.jpg_high_but.setMaximumSize(QSize(100, 25))
        self.jpg_high_but.setFont(font1)

        self.verticalLayout_19.addWidget(self.jpg_high_but)

        self.png_high_but = QPushButton(self.file_tab)
        self.png_high_but.setObjectName(u"png_high_but")
        self.png_high_but.setMinimumSize(QSize(100, 25))
        self.png_high_but.setMaximumSize(QSize(100, 25))
        self.png_high_but.setFont(font1)

        self.verticalLayout_19.addWidget(self.png_high_but)

        self.gif_fenli_but = QPushButton(self.file_tab)
        self.gif_fenli_but.setObjectName(u"gif_fenli_but")
        self.gif_fenli_but.setMinimumSize(QSize(100, 25))
        self.gif_fenli_but.setMaximumSize(QSize(100, 25))
        self.gif_fenli_but.setFont(font1)

        self.verticalLayout_19.addWidget(self.gif_fenli_but)


        self.horizontalLayout_9.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.bin_image_but = QPushButton(self.file_tab)
        self.bin_image_but.setObjectName(u"bin_image_but")
        self.bin_image_but.setMinimumSize(QSize(100, 25))
        self.bin_image_but.setMaximumSize(QSize(100, 25))
        self.bin_image_but.setFont(font1)

        self.verticalLayout_20.addWidget(self.bin_image_but)

        self.heibai_but = QPushButton(self.file_tab)
        self.heibai_but.setObjectName(u"heibai_but")
        self.heibai_but.setMinimumSize(QSize(100, 25))
        self.heibai_but.setMaximumSize(QSize(100, 25))
        self.heibai_but.setFont(font1)

        self.verticalLayout_20.addWidget(self.heibai_but)

        self.jpg_block_but = QPushButton(self.file_tab)
        self.jpg_block_but.setObjectName(u"jpg_block_but")
        self.jpg_block_but.setMinimumSize(QSize(100, 25))
        self.jpg_block_but.setMaximumSize(QSize(100, 25))

        self.verticalLayout_20.addWidget(self.jpg_block_but)

        self.hide_str_but = QPushButton(self.file_tab)
        self.hide_str_but.setObjectName(u"hide_str_but")
        self.hide_str_but.setMinimumSize(QSize(100, 25))
        self.hide_str_but.setMaximumSize(QSize(100, 25))

        self.verticalLayout_20.addWidget(self.hide_str_but)

        self.gif_hebing = QPushButton(self.file_tab)
        self.gif_hebing.setObjectName(u"gif_hebing")
        self.gif_hebing.setMinimumSize(QSize(100, 25))
        self.gif_hebing.setMaximumSize(QSize(100, 25))
        self.gif_hebing.setFont(font1)

        self.verticalLayout_20.addWidget(self.gif_hebing)


        self.horizontalLayout_9.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.rgb2img_but = QPushButton(self.file_tab)
        self.rgb2img_but.setObjectName(u"rgb2img_but")
        sizePolicy4.setHeightForWidth(self.rgb2img_but.sizePolicy().hasHeightForWidth())
        self.rgb2img_but.setSizePolicy(sizePolicy4)
        self.rgb2img_but.setMinimumSize(QSize(100, 25))
        self.rgb2img_but.setMaximumSize(QSize(100, 25))
        self.rgb2img_but.setSizeIncrement(QSize(120, 30))
        self.rgb2img_but.setFont(font1)

        self.verticalLayout_21.addWidget(self.rgb2img_but)

        self.mangshuiyin_but = QPushButton(self.file_tab)
        self.mangshuiyin_but.setObjectName(u"mangshuiyin_but")
        sizePolicy.setHeightForWidth(self.mangshuiyin_but.sizePolicy().hasHeightForWidth())
        self.mangshuiyin_but.setSizePolicy(sizePolicy)
        self.mangshuiyin_but.setMinimumSize(QSize(100, 25))
        self.mangshuiyin_but.setMaximumSize(QSize(100, 25))
        self.mangshuiyin_but.setSizeIncrement(QSize(0, 0))
        self.mangshuiyin_but.setFont(font1)

        self.verticalLayout_21.addWidget(self.mangshuiyin_but)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_9)

        self.png_idat_but = QPushButton(self.file_tab)
        self.png_idat_but.setObjectName(u"png_idat_but")
        self.png_idat_but.setMinimumSize(QSize(100, 25))
        self.png_idat_but.setMaximumSize(QSize(100, 25))

        self.verticalLayout_21.addWidget(self.png_idat_but)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_10)


        self.horizontalLayout_9.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.coordinate_img = QPushButton(self.file_tab)
        self.coordinate_img.setObjectName(u"coordinate_img")
        self.coordinate_img.setMinimumSize(QSize(100, 25))
        self.coordinate_img.setMaximumSize(QSize(100, 25))

        self.verticalLayout_22.addWidget(self.coordinate_img)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_22)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 8, 0, 1, 2)

        self.label_12 = QLabel(self.file_tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.single_crc_but = QPushButton(self.file_tab)
        self.single_crc_but.setObjectName(u"single_crc_but")
        self.single_crc_but.setMinimumSize(QSize(100, 25))
        self.single_crc_but.setMaximumSize(QSize(100, 25))
        self.single_crc_but.setFont(font1)

        self.horizontalLayout_8.addWidget(self.single_crc_but)

        self.zip_wei_but = QPushButton(self.file_tab)
        self.zip_wei_but.setObjectName(u"zip_wei_but")
        self.zip_wei_but.setMinimumSize(QSize(100, 25))
        self.zip_wei_but.setMaximumSize(QSize(100, 25))
        self.zip_wei_but.setFont(font1)

        self.horizontalLayout_8.addWidget(self.zip_wei_but)

        self.more_crc_but = QPushButton(self.file_tab)
        self.more_crc_but.setObjectName(u"more_crc_but")
        self.more_crc_but.setMinimumSize(QSize(100, 25))
        self.more_crc_but.setMaximumSize(QSize(100, 25))
        self.more_crc_but.setFont(font1)

        self.horizontalLayout_8.addWidget(self.more_crc_but)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 10, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 335, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 11, 1, 1, 1)

        self.function_list.addTab(self.file_tab, "")
        self.pcap_tab = QWidget()
        self.pcap_tab.setObjectName(u"pcap_tab")
        self.verticalLayout = QVBoxLayout(self.pcap_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.flag_search_but_2 = QPushButton(self.pcap_tab)
        self.flag_search_but_2.setObjectName(u"flag_search_but_2")
        self.flag_search_but_2.setMinimumSize(QSize(100, 25))
        self.flag_search_but_2.setMaximumSize(QSize(100, 25))
        self.flag_search_but_2.setSizeIncrement(QSize(100, 30))
        self.flag_search_but_2.setBaseSize(QSize(100, 30))
        self.flag_search_but_2.setFont(font1)

        self.horizontalLayout_48.addWidget(self.flag_search_but_2)

        self.re_input_2 = QLineEdit(self.pcap_tab)
        self.re_input_2.setObjectName(u"re_input_2")

        self.horizontalLayout_48.addWidget(self.re_input_2)


        self.verticalLayout.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tiqu_but = QPushButton(self.pcap_tab)
        self.tiqu_but.setObjectName(u"tiqu_but")
        self.tiqu_but.setMinimumSize(QSize(100, 25))
        self.tiqu_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_6.addWidget(self.tiqu_but)

        self.ttl_but = QPushButton(self.pcap_tab)
        self.ttl_but.setObjectName(u"ttl_but")
        self.ttl_but.setMinimumSize(QSize(100, 25))
        self.ttl_but.setMaximumSize(QSize(100, 25))
        self.ttl_but.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.ttl_but)

        self.len_but = QPushButton(self.pcap_tab)
        self.len_but.setObjectName(u"len_but")
        self.len_but.setMinimumSize(QSize(100, 25))
        self.len_but.setMaximumSize(QSize(100, 25))
        self.len_but.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.len_but)

        self.telnet_but = QPushButton(self.pcap_tab)
        self.telnet_but.setObjectName(u"telnet_but")
        self.telnet_but.setMinimumSize(QSize(100, 25))
        self.telnet_but.setMaximumSize(QSize(100, 25))
        self.telnet_but.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.telnet_but)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mouse_but = QPushButton(self.pcap_tab)
        self.mouse_but.setObjectName(u"mouse_but")
        self.mouse_but.setMinimumSize(QSize(100, 25))
        self.mouse_but.setMaximumSize(QSize(100, 25))
        self.mouse_but.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.mouse_but)

        self.keyboard_but = QPushButton(self.pcap_tab)
        self.keyboard_but.setObjectName(u"keyboard_but")
        self.keyboard_but.setMinimumSize(QSize(100, 25))
        self.keyboard_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_7.addWidget(self.keyboard_but)

        self.Bluetooth_but = QPushButton(self.pcap_tab)
        self.Bluetooth_but.setObjectName(u"Bluetooth_but")
        self.Bluetooth_but.setMinimumSize(QSize(100, 25))
        self.Bluetooth_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_7.addWidget(self.Bluetooth_but)

        self.pushButton_6 = QPushButton(self.pcap_tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setMinimumSize(QSize(100, 25))
        self.pushButton_6.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sql_but = QPushButton(self.pcap_tab)
        self.sql_but.setObjectName(u"sql_but")
        self.sql_but.setMinimumSize(QSize(100, 25))
        self.sql_but.setMaximumSize(QSize(100, 25))
        self.sql_but.setSizeIncrement(QSize(90, 25))

        self.horizontalLayout_12.addWidget(self.sql_but)

        self.pushButton_7 = QPushButton(self.pcap_tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(100, 25))
        self.pushButton_7.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_7)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.file_extract_but = QPushButton(self.pcap_tab)
        self.file_extract_but.setObjectName(u"file_extract_but")
        self.file_extract_but.setMinimumSize(QSize(100, 25))
        self.file_extract_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_14.addWidget(self.file_extract_but)

        self.pushButton_3 = QPushButton(self.pcap_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 25))
        self.pushButton_3.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_14.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.pcap_tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_14.addWidget(self.pushButton)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.groupBox_2 = QGroupBox(self.pcap_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(430, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.shell_tab = QComboBox(self.groupBox_2)
        self.shell_tab.addItem("")
        self.shell_tab.addItem("")
        self.shell_tab.addItem("")
        self.shell_tab.addItem("")
        self.shell_tab.addItem("")
        self.shell_tab.addItem("")
        self.shell_tab.setObjectName(u"shell_tab")
        self.shell_tab.setMinimumSize(QSize(150, 25))
        self.shell_tab.setMaximumSize(QSize(110, 25))

        self.horizontalLayout_17.addWidget(self.shell_tab)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.req_box = QCheckBox(self.groupBox_2)
        self.req_box.setObjectName(u"req_box")
        self.req_box.setEnabled(False)
        self.req_box.setMinimumSize(QSize(80, 0))
        self.req_box.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_17.addWidget(self.req_box)

        self.res_box = QCheckBox(self.groupBox_2)
        self.res_box.setObjectName(u"res_box")
        self.res_box.setEnabled(False)
        self.res_box.setMinimumSize(QSize(80, 0))
        self.res_box.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_17.addWidget(self.res_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.shell_type = QComboBox(self.groupBox_2)
        self.shell_type.setObjectName(u"shell_type")
        self.shell_type.setMinimumSize(QSize(110, 25))
        self.shell_type.setMaximumSize(QSize(110, 25))

        self.horizontalLayout_18.addWidget(self.shell_type)

        self.shell_manner = QComboBox(self.groupBox_2)
        self.shell_manner.setObjectName(u"shell_manner")
        self.shell_manner.setMinimumSize(QSize(0, 25))
        self.shell_manner.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_18.addWidget(self.shell_manner)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 25))
        self.label_4.setMaximumSize(QSize(100, 25))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_4)

        self.input_key = QLineEdit(self.groupBox_2)
        self.input_key.setObjectName(u"input_key")
        self.input_key.setEnabled(False)
        self.input_key.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_19.addWidget(self.input_key)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 9)

        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 25))
        self.label_13.setMaximumSize(QSize(100, 25))
        self.label_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_13)

        self.input_pass = QLineEdit(self.groupBox_2)
        self.input_pass.setObjectName(u"input_pass")
        self.input_pass.setEnabled(False)
        self.input_pass.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_20.addWidget(self.input_pass)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 9)

        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.input_srt = QTextBrowser(self.groupBox_2)
        self.input_srt.setObjectName(u"input_srt")
        self.input_srt.setEnabled(False)
        self.input_srt.setMinimumSize(QSize(0, 200))
        self.input_srt.setMaximumSize(QSize(16777215, 16777215))
        self.input_srt.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.input_srt)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.find_key = QPushButton(self.groupBox_2)
        self.find_key.setObjectName(u"find_key")
        self.find_key.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.find_key)

        self.sd_but = QPushButton(self.groupBox_2)
        self.sd_but.setObjectName(u"sd_but")
        self.sd_but.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.sd_but)

        self.auto_but = QPushButton(self.groupBox_2)
        self.auto_but.setObjectName(u"auto_but")
        self.auto_but.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.auto_but)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_4 = QSpacerItem(20, 513, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.function_list.addTab(self.pcap_tab, "")
        self.vol_tab = QWidget()
        self.vol_tab.setObjectName(u"vol_tab")
        self.verticalLayout_23 = QVBoxLayout(self.vol_tab)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.set_vol = QPushButton(self.vol_tab)
        self.set_vol.setObjectName(u"set_vol")
        self.set_vol.setMinimumSize(QSize(100, 25))
        self.set_vol.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_47.addWidget(self.set_vol)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_32)

        self.vol3_but = QPushButton(self.vol_tab)
        self.vol3_but.setObjectName(u"vol3_but")
        self.vol3_but.setMinimumSize(QSize(100, 25))
        self.vol3_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_47.addWidget(self.vol3_but)

        self.vol2_but = QPushButton(self.vol_tab)
        self.vol2_but.setObjectName(u"vol2_but")
        self.vol2_but.setMinimumSize(QSize(100, 25))
        self.vol2_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_47.addWidget(self.vol2_but)


        self.verticalLayout_23.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.vol_input = QLineEdit(self.vol_tab)
        self.vol_input.setObjectName(u"vol_input")

        self.horizontalLayout_31.addWidget(self.vol_input)

        self.vol3_start_but = QPushButton(self.vol_tab)
        self.vol3_start_but.setObjectName(u"vol3_start_but")
        self.vol3_start_but.setMinimumSize(QSize(100, 25))
        self.vol3_start_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_31.addWidget(self.vol3_start_but)


        self.verticalLayout_23.addLayout(self.horizontalLayout_31)

        self.tabWidget = QTabWidget(self.vol_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_16.setFont(font3)

        self.horizontalLayout_35.addWidget(self.label_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_8)

        self.help = QCheckBox(self.tab_2)
        self.help.setObjectName(u"help")
        self.help.setMinimumSize(QSize(50, 0))
        self.help.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_35.addWidget(self.help)


        self.verticalLayout_12.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.v3w_info = QPushButton(self.tab_2)
        self.v3w_info.setObjectName(u"v3w_info")
        self.v3w_info.setMinimumSize(QSize(90, 25))
        self.v3w_info.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_22.addWidget(self.v3w_info)

        self.v3w_hashdump = QPushButton(self.tab_2)
        self.v3w_hashdump.setObjectName(u"v3w_hashdump")
        self.v3w_hashdump.setMinimumSize(QSize(90, 25))
        self.v3w_hashdump.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_22.addWidget(self.v3w_hashdump)

        self.v3w_netstat = QPushButton(self.tab_2)
        self.v3w_netstat.setObjectName(u"v3w_netstat")
        self.v3w_netstat.setMinimumSize(QSize(90, 25))
        self.v3w_netstat.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_22.addWidget(self.v3w_netstat)

        self.v3w_cmdscan = QPushButton(self.tab_2)
        self.v3w_cmdscan.setObjectName(u"v3w_cmdscan")
        self.v3w_cmdscan.setMinimumSize(QSize(90, 25))
        self.v3w_cmdscan.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_22.addWidget(self.v3w_cmdscan)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.v3w_amcache = QPushButton(self.tab_2)
        self.v3w_amcache.setObjectName(u"v3w_amcache")
        self.v3w_amcache.setMinimumSize(QSize(90, 25))
        self.v3w_amcache.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_49.addWidget(self.v3w_amcache)

        self.v3w_shimcache = QPushButton(self.tab_2)
        self.v3w_shimcache.setObjectName(u"v3w_shimcache")
        self.v3w_shimcache.setMinimumSize(QSize(90, 25))
        self.v3w_shimcache.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_49.addWidget(self.v3w_shimcache)

        self.v3w_scheduled_tasks = QPushButton(self.tab_2)
        self.v3w_scheduled_tasks.setObjectName(u"v3w_scheduled_tasks")
        self.v3w_scheduled_tasks.setMinimumSize(QSize(90, 25))
        self.v3w_scheduled_tasks.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_49.addWidget(self.v3w_scheduled_tasks)

        self.v3w_psxview = QPushButton(self.tab_2)
        self.v3w_psxview.setObjectName(u"v3w_psxview")
        self.v3w_psxview.setMinimumSize(QSize(90, 25))
        self.v3w_psxview.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_49.addWidget(self.v3w_psxview)


        self.verticalLayout_12.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.v3w_timeliner = QPushButton(self.tab_2)
        self.v3w_timeliner.setObjectName(u"v3w_timeliner")
        self.v3w_timeliner.setMinimumSize(QSize(90, 25))
        self.v3w_timeliner.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_50.addWidget(self.v3w_timeliner)

        self.v3w_certificates = QPushButton(self.tab_2)
        self.v3w_certificates.setObjectName(u"v3w_certificates")
        self.v3w_certificates.setMinimumSize(QSize(90, 25))
        self.v3w_certificates.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_50.addWidget(self.v3w_certificates)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_7)

        self.v3w_file_but = QCheckBox(self.tab_2)
        self.v3w_file_but.setObjectName(u"v3w_file_but")

        self.horizontalLayout_50.addWidget(self.v3w_file_but)


        self.verticalLayout_12.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.v3w_pid = QLineEdit(self.tab_2)
        self.v3w_pid.setObjectName(u"v3w_pid")
        self.v3w_pid.setEnabled(False)
        self.v3w_pid.setMinimumSize(QSize(90, 30))
        self.v3w_pid.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_33.addWidget(self.v3w_pid)

        self.v3w_physaddr = QLineEdit(self.tab_2)
        self.v3w_physaddr.setObjectName(u"v3w_physaddr")
        self.v3w_physaddr.setEnabled(False)
        self.v3w_physaddr.setMinimumSize(QSize(90, 30))
        self.v3w_physaddr.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_33.addWidget(self.v3w_physaddr)

        self.v3w_filter = QLineEdit(self.tab_2)
        self.v3w_filter.setObjectName(u"v3w_filter")
        self.v3w_filter.setEnabled(False)
        self.v3w_filter.setMinimumSize(QSize(90, 30))
        self.v3w_filter.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_33.addWidget(self.v3w_filter)

        self.v3w_str = QLineEdit(self.tab_2)
        self.v3w_str.setObjectName(u"v3w_str")
        self.v3w_str.setEnabled(False)
        self.v3w_str.setMinimumSize(QSize(90, 30))
        self.v3w_str.setMaximumSize(QSize(90, 30))

        self.horizontalLayout_33.addWidget(self.v3w_str)


        self.verticalLayout_12.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.v3w_filescan = QPushButton(self.tab_2)
        self.v3w_filescan.setObjectName(u"v3w_filescan")
        self.v3w_filescan.setMinimumSize(QSize(90, 25))
        self.v3w_filescan.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_34.addWidget(self.v3w_filescan)

        self.v3w_strings = QPushButton(self.tab_2)
        self.v3w_strings.setObjectName(u"v3w_strings")
        self.v3w_strings.setMinimumSize(QSize(90, 25))
        self.v3w_strings.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_34.addWidget(self.v3w_strings)

        self.v3w_dumpfiles = QPushButton(self.tab_2)
        self.v3w_dumpfiles.setObjectName(u"v3w_dumpfiles")

        self.horizontalLayout_34.addWidget(self.v3w_dumpfiles)

        self.v3w_dump = QCheckBox(self.tab_2)
        self.v3w_dump.setObjectName(u"v3w_dump")
        self.v3w_dump.setEnabled(False)
        self.v3w_dump.setMinimumSize(QSize(90, 30))
        self.v3w_dump.setMaximumSize(QSize(90, 30))

        self.horizontalLayout_34.addWidget(self.v3w_dump)


        self.verticalLayout_12.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.v3w_registry_hive = QLineEdit(self.tab_2)
        self.v3w_registry_hive.setObjectName(u"v3w_registry_hive")
        self.v3w_registry_hive.setEnabled(False)
        self.v3w_registry_hive.setMinimumSize(QSize(90, 30))
        self.v3w_registry_hive.setMaximumSize(QSize(90, 30))

        self.horizontalLayout_10.addWidget(self.v3w_registry_hive)

        self.v3w_registry_key = QLineEdit(self.tab_2)
        self.v3w_registry_key.setObjectName(u"v3w_registry_key")
        self.v3w_registry_key.setEnabled(False)
        self.v3w_registry_key.setMinimumSize(QSize(90, 30))
        self.v3w_registry_key.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.v3w_registry_key)

        self.v3w_recurse = QCheckBox(self.tab_2)
        self.v3w_recurse.setObjectName(u"v3w_recurse")
        self.v3w_recurse.setEnabled(False)
        self.v3w_recurse.setMinimumSize(QSize(90, 30))
        self.v3w_recurse.setMaximumSize(QSize(90, 30))

        self.horizontalLayout_10.addWidget(self.v3w_recurse)

        self.v3w_printkey = QPushButton(self.tab_2)
        self.v3w_printkey.setObjectName(u"v3w_printkey")
        self.v3w_printkey.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.v3w_printkey)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_17)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.v3w_fun_list = QComboBox(self.tab_2)
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.addItem("")
        self.v3w_fun_list.setObjectName(u"v3w_fun_list")
        self.v3w_fun_list.setMinimumSize(QSize(200, 25))
        self.v3w_fun_list.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_27.addWidget(self.v3w_fun_list)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_2)

        self.v3w_fun_but = QPushButton(self.tab_2)
        self.v3w_fun_but.setObjectName(u"v3w_fun_but")
        self.v3w_fun_but.setMinimumSize(QSize(100, 25))
        self.v3w_fun_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_27.addWidget(self.v3w_fun_but)


        self.verticalLayout_12.addLayout(self.horizontalLayout_27)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_18)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.v3l_fun_list = QComboBox(self.tab_2)
        self.v3l_fun_list.setObjectName(u"v3l_fun_list")
        self.v3l_fun_list.setMinimumSize(QSize(200, 25))
        self.v3l_fun_list.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_28.addWidget(self.v3l_fun_list)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_3)

        self.v3l_fun_but = QPushButton(self.tab_2)
        self.v3l_fun_but.setObjectName(u"v3l_fun_but")
        self.v3l_fun_but.setMinimumSize(QSize(100, 25))
        self.v3l_fun_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_28.addWidget(self.v3l_fun_but)


        self.verticalLayout_12.addLayout(self.horizontalLayout_28)

        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_19)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.v3m_fun_list = QComboBox(self.tab_2)
        self.v3m_fun_list.setObjectName(u"v3m_fun_list")
        self.v3m_fun_list.setMinimumSize(QSize(200, 25))
        self.v3m_fun_list.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_32.addWidget(self.v3m_fun_list)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_6)

        self.v3m_fun_but = QPushButton(self.tab_2)
        self.v3m_fun_but.setObjectName(u"v3m_fun_but")
        self.v3m_fun_but.setMinimumSize(QSize(100, 25))
        self.v3m_fun_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_32.addWidget(self.v3m_fun_but)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_12 = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_16 = QVBoxLayout(self.tab_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_16.addWidget(self.pushButton_4)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_23.addWidget(self.tabWidget)

        self.function_list.addTab(self.vol_tab, "")
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.verticalLayout_10 = QVBoxLayout(self.data_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_2 = QLabel(self.data_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_13.addWidget(self.label_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.db_clear = QPushButton(self.data_tab)
        self.db_clear.setObjectName(u"db_clear")
        self.db_clear.setEnabled(True)
        self.db_clear.setMinimumSize(QSize(100, 25))
        self.db_clear.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_37.addWidget(self.db_clear)

        self.list_clear = QPushButton(self.data_tab)
        self.list_clear.setObjectName(u"list_clear")
        self.list_clear.setEnabled(False)
        self.list_clear.setMinimumSize(QSize(100, 25))
        self.list_clear.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_37.addWidget(self.list_clear)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_28)

        self.start_db_but = QPushButton(self.data_tab)
        self.start_db_but.setObjectName(u"start_db_but")
        self.start_db_but.setMinimumSize(QSize(100, 25))
        self.start_db_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_37.addWidget(self.start_db_but)


        self.verticalLayout_10.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)

        self.read_db = QPushButton(self.data_tab)
        self.read_db.setObjectName(u"read_db")
        self.read_db.setMinimumSize(QSize(100, 25))
        self.read_db.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_15.addWidget(self.read_db)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.label_22 = QLabel(self.data_tab)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_10.addWidget(self.label_22)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.txt_csv = QPushButton(self.data_tab)
        self.txt_csv.setObjectName(u"txt_csv")
        self.txt_csv.setMinimumSize(QSize(100, 25))
        self.txt_csv.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_16.addWidget(self.txt_csv)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_33)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_34)


        self.verticalLayout_10.addLayout(self.horizontalLayout_40)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.data_tab)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.db_str = QLineEdit(self.data_tab)
        self.db_str.setObjectName(u"db_str")

        self.verticalLayout_9.addWidget(self.db_str)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.select_yufa = QPushButton(self.data_tab)
        self.select_yufa.setObjectName(u"select_yufa")
        self.select_yufa.setEnabled(True)
        self.select_yufa.setMinimumSize(QSize(100, 25))
        self.select_yufa.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_23.addWidget(self.select_yufa)

        self.revise_column_name = QPushButton(self.data_tab)
        self.revise_column_name.setObjectName(u"revise_column_name")
        self.revise_column_name.setEnabled(False)
        self.revise_column_name.setMinimumSize(QSize(100, 25))
        self.revise_column_name.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_23.addWidget(self.revise_column_name)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_31)

        self.db_select_but = QPushButton(self.data_tab)
        self.db_select_but.setObjectName(u"db_select_but")
        self.db_select_but.setEnabled(False)
        self.db_select_but.setMinimumSize(QSize(100, 25))
        self.db_select_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_23.addWidget(self.db_select_but)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_21)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_22)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_15 = QLabel(self.data_tab)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_30.addWidget(self.label_15)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_23)


        self.verticalLayout_2.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.select_one_up = QPushButton(self.data_tab)
        self.select_one_up.setObjectName(u"select_one_up")
        self.select_one_up.setEnabled(False)
        self.select_one_up.setMinimumSize(QSize(100, 25))
        self.select_one_up.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_38.addWidget(self.select_one_up)

        self.select_one_down = QPushButton(self.data_tab)
        self.select_one_down.setObjectName(u"select_one_down")
        self.select_one_down.setEnabled(False)
        self.select_one_down.setMinimumSize(QSize(100, 25))
        self.select_one_down.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_38.addWidget(self.select_one_down)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_18)

        self.show_guanxi = QPushButton(self.data_tab)
        self.show_guanxi.setObjectName(u"show_guanxi")
        self.show_guanxi.setEnabled(False)
        self.show_guanxi.setMinimumSize(QSize(100, 25))
        self.show_guanxi.setMaximumSize(QSize(100, 25))
        self.show_guanxi.setAutoDefault(False)
        self.show_guanxi.setFlat(False)

        self.horizontalLayout_38.addWidget(self.show_guanxi)


        self.verticalLayout_2.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_29)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_30)


        self.verticalLayout_2.addLayout(self.horizontalLayout_39)


        self.verticalLayout_10.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 196, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.function_list.addTab(self.data_tab, "")
        self.misc_tab = QWidget()
        self.misc_tab.setObjectName(u"misc_tab")
        self.verticalLayout_4 = QVBoxLayout(self.misc_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.misc_tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.plist_but = QPushButton(self.misc_tab)
        self.plist_but.setObjectName(u"plist_but")
        self.plist_but.setMinimumSize(QSize(100, 25))
        self.plist_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_44.addWidget(self.plist_but)

        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_78)

        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_79)


        self.verticalLayout_4.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_80 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_80)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_81)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_82)


        self.verticalLayout_4.addLayout(self.horizontalLayout_45)

        self.label_6 = QLabel(self.misc_tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_2 = QPushButton(self.misc_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 25))
        self.pushButton_2.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_42.addWidget(self.pushButton_2)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_72)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_73)


        self.verticalLayout_4.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_20 = QLabel(self.misc_tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(50, 25))
        self.label_20.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_46.addWidget(self.label_20)

        self.hook_name = QLineEdit(self.misc_tab)
        self.hook_name.setObjectName(u"hook_name")
        self.hook_name.setMinimumSize(QSize(80, 0))
        self.hook_name.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_46.addWidget(self.hook_name)

        self.hook_fun = QComboBox(self.misc_tab)
        self.hook_fun.addItem("")
        self.hook_fun.addItem("")
        self.hook_fun.addItem("")
        self.hook_fun.addItem("")
        self.hook_fun.addItem("")
        self.hook_fun.setObjectName(u"hook_fun")

        self.horizontalLayout_46.addWidget(self.hook_fun)

        self.hook_but = QPushButton(self.misc_tab)
        self.hook_but.setObjectName(u"hook_but")
        self.hook_but.setMinimumSize(QSize(80, 25))
        self.hook_but.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_46.addWidget(self.hook_but)


        self.verticalLayout_4.addLayout(self.horizontalLayout_46)

        self.label_21 = QLabel(self.misc_tab)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_4.addWidget(self.label_21)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pyc_but = QPushButton(self.misc_tab)
        self.pyc_but.setObjectName(u"pyc_but")
        self.pyc_but.setMinimumSize(QSize(100, 25))
        self.pyc_but.setMaximumSize(QSize(100, 25))
        font4 = QFont()
        font4.setFamilies([u"\u6977\u4f53"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.pyc_but.setFont(font4)

        self.horizontalLayout_24.addWidget(self.pyc_but)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.label_8 = QLabel(self.misc_tab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.facefusion_but = QPushButton(self.misc_tab)
        self.facefusion_but.setObjectName(u"facefusion_but")
        self.facefusion_but.setMinimumSize(QSize(100, 25))
        self.facefusion_but.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_36.addWidget(self.facefusion_but)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_24)


        self.verticalLayout_4.addLayout(self.horizontalLayout_36)

        self.label_7 = QLabel(self.misc_tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.mod_but = QPushButton(self.misc_tab)
        self.mod_but.setObjectName(u"mod_but")
        self.mod_but.setMinimumSize(QSize(100, 25))
        self.mod_but.setMaximumSize(QSize(100, 25))
        font5 = QFont()
        font5.setFamilies([u"\u6977\u4f53"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.mod_but.setFont(font5)

        self.horizontalLayout_29.addWidget(self.mod_but)

        self.time_zhuan = QPushButton(self.misc_tab)
        self.time_zhuan.setObjectName(u"time_zhuan")
        self.time_zhuan.setMinimumSize(QSize(100, 25))
        self.time_zhuan.setMaximumSize(QSize(100, 25))
        self.time_zhuan.setFont(font5)

        self.horizontalLayout_29.addWidget(self.time_zhuan)

        self.rsa_public = QPushButton(self.misc_tab)
        self.rsa_public.setObjectName(u"rsa_public")
        self.rsa_public.setMinimumSize(QSize(100, 25))
        self.rsa_public.setMaximumSize(QSize(100, 25))
        self.rsa_public.setFont(font5)

        self.horizontalLayout_29.addWidget(self.rsa_public)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_25)


        self.verticalLayout_4.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.ceshi111_but = QPushButton(self.misc_tab)
        self.ceshi111_but.setObjectName(u"ceshi111_but")
        self.ceshi111_but.setMinimumSize(QSize(100, 25))
        self.ceshi111_but.setMaximumSize(QSize(100, 25))
        self.ceshi111_but.setFont(font5)

        self.horizontalLayout_41.addWidget(self.ceshi111_but)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_70)


        self.verticalLayout_4.addLayout(self.horizontalLayout_41)

        self.verticalSpacer_6 = QSpacerItem(17, 203, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.function_list.addTab(self.misc_tab, "")

        self.horizontalLayout_11.addWidget(self.function_list)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(zhu_windows)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setPointSize(12)
        self.label.setFont(font6)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.silu_but = QPushButton(zhu_windows)
        self.silu_but.setObjectName(u"silu_but")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.silu_but.setFont(font7)

        self.horizontalLayout.addWidget(self.silu_but)

        self.clear_but = QPushButton(zhu_windows)
        self.clear_but.setObjectName(u"clear_but")
        self.clear_but.setFont(font6)

        self.horizontalLayout.addWidget(self.clear_but)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.text_echo = QTextEdit(zhu_windows)
        self.text_echo.setObjectName(u"text_echo")
        self.text_echo.setMinimumSize(QSize(0, 0))
        self.text_echo.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Microsoft YaHei UI"])
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        self.text_echo.setFont(font8)
        self.text_echo.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        self.text_echo.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.text_echo)

        self.table_echo = QTableView(zhu_windows)
        self.table_echo.setObjectName(u"table_echo")
        self.table_echo.setMaximumSize(QSize(16777215, 0))

        self.verticalLayout_5.addWidget(self.table_echo)

        self.verticalLayout_5.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)


        self.retranslateUi(zhu_windows)

        self.function_list.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.show_guanxi.setDefault(False)


        QMetaObject.connectSlotsByName(zhu_windows)
    # setupUi

    def retranslateUi(self, zhu_windows):
        zhu_windows.setWindowTitle(QCoreApplication.translate("zhu_windows", u"SQM\u7684MISC\u5de5\u5177\u96c6", None))
        self.label_3.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u8f93\u5165", None))
        self.input_file.setText(QCoreApplication.translate("zhu_windows", u"\u62d6\u62fd\u8f93\u5165\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.flag_search_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u6570\u636e\u4e2d\u641c\u7d22\u6307\u5b9a\u7684ascii\u5b57\u7b26\u4e32,\u9700\u6307\u5b9a\u6587\u4ef6\u548c\u5b57\u7b26\u4e32", None))
#endif // QT_CONFIG(tooltip)
        self.flag_search_but.setText(QCoreApplication.translate("zhu_windows", u"\u6b63\u5219\u641c\u7d22\u5b57\u7b26\u4e32", None))
        self.re_ipnut.setText(QCoreApplication.translate("zhu_windows", u"\u53ef\u8f93\u5165\u6b63\u5219\uff0c\u9ed8\u8ba4\u4e3aflag", None))
        self.label_9.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6", None))
        self.shibie_but.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u4e8c\u8fdb\u5236", None))
        self.print_str_but.setText(QCoreApplication.translate("zhu_windows", u"\u663e\u793a\u53ef\u6253\u5370\u5b57\u7b26", None))
#if QT_CONFIG(tooltip)
        self.fenli_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u9700\u6307\u5b9a\u6587\u4ef6,\u8c03\u7528binwalk\u8fdb\u884c\u5206\u79bb", None))
#endif // QT_CONFIG(tooltip)
        self.fenli_but.setText(QCoreApplication.translate("zhu_windows", u"binwalk\u5206\u79bb", None))
        self.for_but.setText(QCoreApplication.translate("zhu_windows", u"format\u5206\u79bb", None))
        self.str_down_but.setText(QCoreApplication.translate("zhu_windows", u"\u5b57\u7b26\u4e32\u53cd\u8f6c", None))
        self.zipin_but.setText(QCoreApplication.translate("zhu_windows", u"\u5b57\u9891\u5206\u6790", None))
#if QT_CONFIG(tooltip)
        self.cipin_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6253\u5f00\u6587\u4ef6\u6216\u4f7f\u7528\u8f93\u5165\u6846\u6dfb\u52a0\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.cipin_but.setText(QCoreApplication.translate("zhu_windows", u"\u8bcd\u9891\u5206\u6790", None))
        self.zero_str_but.setText(QCoreApplication.translate("zhu_windows", u"\u96f6\u5bbd\u5b57\u7b26\u9690\u5199", None))
        self.label_10.setText(QCoreApplication.translate("zhu_windows", u"\u5e38\u7528\u7f16\u89e3\u7801", None))
        self.input_text.setMarkdown("")
        self.input_text.setHtml(QCoreApplication.translate("zhu_windows", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.html_but.setText(QCoreApplication.translate("zhu_windows", u"HTML\u89e3\u7801", None))
        self.base_but.setText(QCoreApplication.translate("zhu_windows", u"\u5168base\u8f6c\u7801", None))
        self.fuck_but.setText(QCoreApplication.translate("zhu_windows", u"brainfuck\u89e3\u7801", None))
        self.url_but.setText(QCoreApplication.translate("zhu_windows", u"URL\u89e3\u7801", None))
        self.kaisa_but.setText(QCoreApplication.translate("zhu_windows", u"\u51ef\u6492\u5bc6\u7801", None))
        self.ook_but.setText(QCoreApplication.translate("zhu_windows", u"OOK\u89e3\u7801", None))
        self.hex_str_but.setText(QCoreApplication.translate("zhu_windows", u"hex\u89e3\u7801", None))
        self.zhalan_but.setText(QCoreApplication.translate("zhu_windows", u"\u6805\u680f\u5bc6\u7801", None))
        self.hex_str.setText(QCoreApplication.translate("zhu_windows", u"hex\u89e3\u7801\u5e26\u504f\u79fb", None))
        self.hexin_but.setText(QCoreApplication.translate("zhu_windows", u"\u6838\u5fc3\u4ef7\u503c\u89c2\u89e3\u7801", None))
        self.label_11.setText(QCoreApplication.translate("zhu_windows", u"\u56fe\u7247\u5904\u7406", None))
        self.exif_but.setText(QCoreApplication.translate("zhu_windows", u"\u56fe\u7247exif\u4fe1\u606f", None))
        self.tu_re.setText(QCoreApplication.translate("zhu_windows", u"\u56fe\u7247\u9006\u5e8f", None))
#if QT_CONFIG(tooltip)
        self.jpg_high_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6307\u5b9a\u6587\u4ef6,\u81ea\u52a8\u8ba1\u7b97crc\u5e76\u663e\u793a\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.jpg_high_but.setText(QCoreApplication.translate("zhu_windows", u"JPG\u5bbd\u9ad8\u4fee\u6b63", None))
#if QT_CONFIG(tooltip)
        self.png_high_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6307\u5b9a\u6587\u4ef6,\u81ea\u52a8\u8ba1\u7b97crc\u5e76\u663e\u793a\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.png_high_but.setText(QCoreApplication.translate("zhu_windows", u"PNG\u9ad8\u5bbd\u7206\u7834", None))
        self.gif_fenli_but.setText(QCoreApplication.translate("zhu_windows", u"GIF\u5206\u79bb", None))
#if QT_CONFIG(tooltip)
        self.bin_image_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6307\u5b9a\u4e8c\u8fdb\u5236\u6587\u672c\u6587\u4ef6,\u590d\u539f\u4e3a\u56fe\u7247,\u81ea\u52a8\u8ba1\u7b97\u5bbd\u9ad8", None))
#endif // QT_CONFIG(tooltip)
        self.bin_image_but.setText(QCoreApplication.translate("zhu_windows", u"\u4e8c\u8fdb\u5236\u8f6c\u56fe\u7247", None))
        self.heibai_but.setText(QCoreApplication.translate("zhu_windows", u"\u9ed1\u767d\u56fe\u8f6c\u56fe\u7247", None))
        self.jpg_block_but.setText(QCoreApplication.translate("zhu_windows", u"JPG\u5757\u9690\u85cf", None))
        self.hide_str_but.setText(QCoreApplication.translate("zhu_windows", u"PNG\u89e3\u7801hide", None))
        self.gif_hebing.setText(QCoreApplication.translate("zhu_windows", u"GIF\u5408\u5e76", None))
        self.rgb2img_but.setText(QCoreApplication.translate("zhu_windows", u"RGB\u8f6c\u56fe\u7247", None))
        self.mangshuiyin_but.setText(QCoreApplication.translate("zhu_windows", u"\u529f\u80fd\u672a\u5b9e\u73b0", None))
        self.png_idat_but.setText(QCoreApplication.translate("zhu_windows", u"PNG\u5206\u6790IDAT", None))
        self.coordinate_img.setText(QCoreApplication.translate("zhu_windows", u"\u5750\u6807\u8f6c\u56fe\u7247", None))
        self.label_12.setText(QCoreApplication.translate("zhu_windows", u"\u538b\u7f29\u5305\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.single_crc_but.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6307\u5b9a\u6587\u4ef6\u5939,\u5bf9zip\u76844\u5b57\u8282\u6587\u4ef6\u8fdb\u884cCRC\u7206\u7834", None))
#endif // QT_CONFIG(tooltip)
        self.single_crc_but.setText(QCoreApplication.translate("zhu_windows", u"\u5355\u6587\u4ef6CRC\u7206\u7834", None))
        self.zip_wei_but.setText(QCoreApplication.translate("zhu_windows", u"\u4f2a\u52a0\u5bc6\u7834\u89e3", None))
        self.more_crc_but.setText(QCoreApplication.translate("zhu_windows", u"\u591a\u6587\u4ef6CRC\u7206\u7834", None))
        self.function_list.setTabText(self.function_list.indexOf(self.file_tab), QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.flag_search_but_2.setToolTip(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u6570\u636e\u4e2d\u641c\u7d22\u6307\u5b9a\u7684ascii\u5b57\u7b26\u4e32,\u9700\u6307\u5b9a\u6587\u4ef6\u548c\u5b57\u7b26\u4e32", None))
#endif // QT_CONFIG(tooltip)
        self.flag_search_but_2.setText(QCoreApplication.translate("zhu_windows", u"\u6b63\u5219\u641c\u7d22\u5b57\u7b26\u4e32", None))
        self.re_input_2.setText(QCoreApplication.translate("zhu_windows", u"\u53ef\u8f93\u5165\u6b63\u5219\uff0c\u9ed8\u8ba4\u4e3aflag", None))
        self.tiqu_but.setText(QCoreApplication.translate("zhu_windows", u"\u8bfb\u53d6\u5168\u90e8URL", None))
        self.ttl_but.setText(QCoreApplication.translate("zhu_windows", u"\u8bfb\u53d6TLL\u957f\u5ea6", None))
        self.len_but.setText(QCoreApplication.translate("zhu_windows", u"\u8bfb\u53d6len\u957f\u5ea6", None))
        self.telnet_but.setText(QCoreApplication.translate("zhu_windows", u"\u8bfb\u53d6TELNET", None))
        self.mouse_but.setText(QCoreApplication.translate("zhu_windows", u"\u9f20\u6807\u6d41\u91cf\u5206\u6790", None))
        self.keyboard_but.setText(QCoreApplication.translate("zhu_windows", u"\u952e\u76d8\u6d41\u91cf\u5206\u6790", None))
        self.Bluetooth_but.setText(QCoreApplication.translate("zhu_windows", u"\u84dd\u7259\u6d41\u91cf\u5206\u6790", None))
        self.pushButton_6.setText(QCoreApplication.translate("zhu_windows", u"\u7a7a", None))
        self.sql_but.setText(QCoreApplication.translate("zhu_windows", u"SQL\u76f2\u6ce8\u5206\u6790", None))
        self.pushButton_7.setText(QCoreApplication.translate("zhu_windows", u"\u7a7a", None))
        self.file_extract_but.setText(QCoreApplication.translate("zhu_windows", u"\u7a7a", None))
        self.pushButton_3.setText(QCoreApplication.translate("zhu_windows", u"\u7a7a", None))
        self.pushButton.setText(QCoreApplication.translate("zhu_windows", u"\u7a7a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("zhu_windows", u"webshell\u5206\u6790\u533a", None))
        self.shell_tab.setItemText(0, QCoreApplication.translate("zhu_windows", u"\u8bf7\u9009\u62e9shell\u5de5\u5177", None))
        self.shell_tab.setItemText(1, QCoreApplication.translate("zhu_windows", u"\u83dc\u5200", None))
        self.shell_tab.setItemText(2, QCoreApplication.translate("zhu_windows", u"\u8681\u5251", None))
        self.shell_tab.setItemText(3, QCoreApplication.translate("zhu_windows", u"\u54e5\u65af\u62c9", None))
        self.shell_tab.setItemText(4, QCoreApplication.translate("zhu_windows", u"\u51b0\u874e3", None))
        self.shell_tab.setItemText(5, QCoreApplication.translate("zhu_windows", u"\u51b0\u874e4", None))

        self.req_box.setText(QCoreApplication.translate("zhu_windows", u"\u8bf7\u6c42", None))
        self.res_box.setText(QCoreApplication.translate("zhu_windows", u"\u54cd\u5e94", None))
        self.label_4.setText(QCoreApplication.translate("zhu_windows", u"\u8bf7\u8f93\u5165  key", None))
        self.label_13.setText(QCoreApplication.translate("zhu_windows", u"\u8bf7\u8f93\u5165 pass", None))
        self.input_srt.setHtml(QCoreApplication.translate("zhu_windows", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u624b\u52a8\u5355\u6761\u89e3\u5bc6\u8bf7\u8f93\u5165</span></p></body></html>", None))
        self.find_key.setText(QCoreApplication.translate("zhu_windows", u"\u641c\u7d22KEY", None))
        self.sd_but.setText(QCoreApplication.translate("zhu_windows", u"\u624b\u52a8\u6570\u636e\u5206\u6790", None))
        self.auto_but.setText(QCoreApplication.translate("zhu_windows", u"\u81ea\u52a8\u5206\u6790", None))
        self.function_list.setTabText(self.function_list.indexOf(self.pcap_tab), QCoreApplication.translate("zhu_windows", u"\u6d41\u91cf\u5206\u6790", None))
        self.set_vol.setText(QCoreApplication.translate("zhu_windows", u"\u9009\u62e9vol\u76ee\u5f55", None))
        self.vol3_but.setText(QCoreApplication.translate("zhu_windows", u"vol3\u8bf4\u660e\u4e66", None))
        self.vol2_but.setText(QCoreApplication.translate("zhu_windows", u"vol2\u8bf4\u660e\u4e66", None))
        self.vol3_start_but.setText(QCoreApplication.translate("zhu_windows", u"\u624b\u52a8\u6267\u884c", None))
        self.label_16.setText(QCoreApplication.translate("zhu_windows", u"windows\u5e38\u7528\u67e5\u8be2", None))
        self.help.setText(QCoreApplication.translate("zhu_windows", u"\u547d\u4ee4\u5e2e\u52a9", None))
#if QT_CONFIG(tooltip)
        self.v3w_info.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.info</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u663e\u793a\u5185\u5b58\u955c\u50cf\u7684\u57fa\u672c\u7cfb\u7edf\u4fe1\u606f\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple"
                        "-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/>1.</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u63d0\u4f9b\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u3001\u6784\u5efa\u53f7\u3001\u7cfb\u7edf\u65f6\u95f4\u7b49\u57fa\u672c\u4fe1\u606f<br/>2.\u663e\u793a\u5185\u5b58\u5e03\u5c40\u548c\u5173\u952e\u5730\u5740<br/>3.\u9a8c\u8bc1\u5185\u5b58\u955c\u50cf\u662f\u5426\u88ab\u6b63\u786e\u89e3\u6790</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_info.setText(QCoreApplication.translate("zhu_windows", u"\u57fa\u672c\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.v3w_hashdump.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.hashdump</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u63d0\u53d6\u672c\u5730\u8d26\u6237\u7684\u5bc6\u7801\u54c8\u5e0c\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','"
                        "system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a<br/>1.\u83b7\u53d6SAM\u6570\u636e\u5e93\u4e2d\u7684\u7528\u6237\u5bc6\u7801\u54c8\u5e0c(NTLM)<br/>2.\u53ef\u7528\u4e8e\u79bb\u7ebf\u5bc6\u7801\u7834\u89e3<br/>3.\u9700\u8981\u7cfb\u7edf\u6743\u9650\u624d\u80fd\u83b7\u53d6\u8fd9\u4e9b\u54c8\u5e0c</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_hashdump.setText(QCoreApplication.translate("zhu_windows", u"\u5bc6\u7801hash", None))
#if QT_CONFIG(tooltip)
        self.v3w_netstat.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.netscan</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u626b\u63cf\u5185\u5b58\u4e2d\u7684\u7f51\u7edc\u8fde\u63a5\u548c\u5957\u63a5\u5b57\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui"
                        "','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/>1.</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u663e\u793aTCP/UDP\u8fde\u63a5\u5217\u8868<br/>2.\u5305\u62ec\u672c\u5730/\u8fdc\u7a0bIP\u548c\u7aef\u53e3<br/>3.\u8bc6\u522b\u5f02\u5e38\u7f51\u7edc\u8fde\u63a5(\u5982C2\u901a\u4fe1)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_netstat.setText(QCoreApplication.translate("zhu_windows", u"\u7f51\u7edc\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.v3w_cmdscan.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:medium; font-weight:700; color:#404040;\">windows.consoles.Consoles</span></h4><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a\u63d0\u53d6\u5185\u5b58\u4e2d\u7684\u547d\u4ee4\u884c\u63a7\u5236\u53f0\uff08cmd.exe\uff09\u5386\u53f2\u8bb0\u5f55<br/></span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFo"
                        "nt','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u7528\u6cd5</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a</span><span style=\" font-family:'Courier New'; color:#404040;\">vol.py -f memory.dump windows.consoles</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\"><br/></span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" fo"
                        "nt-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u6062\u590d\u653b\u51fb\u8005\u6267\u884c\u7684\u547d\u4ee4\u5386\u53f2\uff0c\u663e\u793a\u8f93\u5165/\u8f93\u51fa\u7f13\u51b2\u533a\u5185\u5bb9\uff0c\u5305\u542b\u8fdb\u7a0bID\u548c\u65f6\u95f4\u6233</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\"><br/></span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFon"
                        "t','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u53d6\u8bc1\u4ef7\u503c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a\u91cd\u73b0\u653b\u51fb\u8005\u64cd\u4f5c\u6d41\u7a0b\uff0c\u83b7\u53d6\u5173\u952e\u547d\u4ee4\u8bc1\u636e</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_cmdscan.setText(QCoreApplication.translate("zhu_windows", u"cmd\u5386\u53f2\u547d\u4ee4", None))
#if QT_CONFIG(tooltip)
        self.v3w_amcache.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.amcache</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u89e3\u6790Windows AmCache.hve\u4e2d\u7684\u7a0b\u5e8f\u6267\u884c\u5386\u53f2\u8bb0\u5f55\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','sy"
                        "stem-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/>1.</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u663e\u793a\u7cfb\u7edf\u4e0a\u66fe\u7ecf\u6267\u884c\u8fc7\u7684\u7a0b\u5e8f\u4fe1\u606f<br/>2.\u5305\u542b\u6587\u4ef6\u8def\u5f84\u3001\u521b\u5efa\u65f6\u95f4\u3001\u4fee\u6539\u65f6\u95f4\u7b49<br/>3.\u5bf9\u8c03\u67e5\u6076\u610f\u8f6f\u4ef6\u6267\u884c\u5386\u53f2\u7279\u522b\u6709\u7528</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_amcache.setText(QCoreApplication.translate("zhu_windows", u"\u7a0b\u5e8f\u6267\u884c\u8bb0\u5f55", None))
#if QT_CONFIG(tooltip)
        self.v3w_shimcache.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.shimcache</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u63d0\u53d6\u5e94\u7528\u7a0b\u5e8f\u517c\u5bb9\u6027\u7f13\u5b58(ShimCache)\u6570\u636e\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','sy"
                        "stem-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/>1.</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u663e\u793a\u7cfb\u7edf\u4e0a\u66fe\u7ecf\u8fd0\u884c\u8fc7\u7684\u53ef\u6267\u884c\u6587\u4ef6\u5217\u8868<br/>2.\u5373\u4f7f\u6587\u4ef6\u5df2\u88ab\u5220\u9664\u4e5f\u80fd\u63d0\u4f9b\u5386\u53f2\u8bb0\u5f55<br/>3.\u53d6\u8bc1\u8c03\u67e5\u4e2d\u7528\u4e8e\u786e\u5b9a\u53ef\u7591\u6587\u4ef6\u6267\u884c</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_shimcache.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u6267\u884c\u8bb0\u5f55", None))
#if QT_CONFIG(tooltip)
        self.v3w_scheduled_tasks.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.scheduled_tasks</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u679a\u4e3e\u5185\u5b58\u4e2d\u7684\u8ba1\u5212\u4efb\u52a1\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system"
                        "','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/></span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">1.\u663e\u793a\u5df2\u6ce8\u518c\u7684\u8ba1\u5212\u4efb\u52a1<br/>2.\u8bc6\u522b\u6076\u610f\u6301\u4e45\u5316\u673a\u5236<br/>3.\u5305\u542b\u4efb\u52a1\u540d\u79f0\u3001\u89e6\u53d1\u5668\u3001\u64cd\u4f5c\u7a0b\u5e8f\u7b49\u4fe1\u606f</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_scheduled_tasks.setText(QCoreApplication.translate("zhu_windows", u"\u8ba1\u5212\u4efb\u52a1", None))
#if QT_CONFIG(tooltip)
        self.v3w_psxview.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.psxview</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u901a\u8fc7\u591a\u79cd\u65b9\u6cd5\u679a\u4e3e\u8fdb\u7a0b\uff0c\u6bd4\u8f83\u7ed3\u679c\u4ee5\u53d1\u73b0\u9690\u85cf\u8fdb\u7a0b\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" fon"
                        "t-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/>1.</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u4f7f\u75285\u79cd\u4e0d\u540c\u65b9\u6cd5\u4ea4\u53c9\u9a8c\u8bc1\u8fdb\u7a0b\u5217\u8868<br/>2.\u9ad8\u4eae\u663e\u793a\u4e0d\u4e00\u81f4\u7684\u6761\u76ee(\u53ef\u80fd\u88ab\u9690\u85cf)<br/>3.\u6700\u5168\u9762\u7684\u8fdb\u7a0b\u68c0\u6d4b\u65b9\u6cd5\u4e4b\u4e00</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_psxview.setText(QCoreApplication.translate("zhu_windows", u"\u5168\u8fdb\u7a0b\u626b\u63cf", None))
#if QT_CONFIG(tooltip)
        self.v3w_timeliner.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.timeliner</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u521b\u5efa\u7cfb\u7edf\u6d3b\u52a8\u7684\u65f6\u95f4\u7ebf\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','Bli"
                        "nkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u6574\u5408\u591a\u4e2a\u6765\u6e90\u7684\u65f6\u95f4\u6233\u6570\u636e\uff0c\u751f\u6210\u7cfb\u7edf\u6d3b\u52a8\u7684\u7efc\u5408\u65f6\u95f4\u7ebf\uff0c\u5bf9\u4e8b\u4ef6\u91cd\u5efa\u548c\u8c03\u67e5\u975e\u5e38\u6709\u7528</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_timeliner.setText(QCoreApplication.translate("zhu_windows", u"\u68b3\u7406\u65f6\u95f4\u7ebf", None))
#if QT_CONFIG(tooltip)
        self.v3w_certificates.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p>windows.registry.certificates</p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\uff1a\u63d0\u53d6\u5185\u5b58\u4e2d\u7684\u8bc1\u4e66\u4fe1\u606f\u3002</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-weight:700; color:#404040;\">\u6548\u679c</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-"
                        "system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040;\">\uff1a<br/>1.</span><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">\u663e\u793a\u7cfb\u7edf\u5b58\u50a8\u7684\u8bc1\u4e66<br/>2.\u8bc6\u522b\u6076\u610f\u6216\u53ef\u7591\u8bc1\u4e66</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; color:#404040; background-color:#ffffff;\">3.\u5305\u542b\u8bc1\u4e66\u6307\u7eb9\u3001\u9881\u53d1\u8005\u7b49\u4fe1\u606f</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_certificates.setText(QCoreApplication.translate("zhu_windows", u"cer\u8bc1\u4e66\u626b\u63cf", None))
        self.v3w_file_but.setText(QCoreApplication.translate("zhu_windows", u"\u5f00\u542f\u6587\u4ef6\u64cd\u4f5c", None))
        self.v3w_pid.setText(QCoreApplication.translate("zhu_windows", u"PID", None))
        self.v3w_physaddr.setText(QCoreApplication.translate("zhu_windows", u"\u7269\u7406\u5730\u5740", None))
        self.v3w_filter.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u540d", None))
        self.v3w_str.setText(QCoreApplication.translate("zhu_windows", u"\u683c\u5f0f: \\.docx", None))
#if QT_CONFIG(tooltip)
        self.v3w_filescan.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p><span style=\" font-size:12pt;\">windows.filescan</span></p><p><span style=\" font-size:12pt;\">\u529f\u80fd\uff1a\u626b\u63cf\u5185\u5b58\u4e2d\u7684\u6587\u4ef6\u5bf9\u8c61\uff0c\u5217\u51fa\u6240\u6709\u5728\u5185\u5b58\u4e2d\u7f13\u5b58\u6216\u6253\u5f00\u7684\u6587\u4ef6\u3002</span></p><p><br/></p><p><span style=\" font-size:12pt;\">\u53c2\u6570\u8bf4\u660e\uff1a</span></p><p><span style=\" font-size:12pt;\">--name-filter &lt;pattern&gt;	\u6309\u6587\u4ef6\u540d\u8fc7\u6ee4\uff08\u5982 *.docx\uff09</span></p><p><span style=\" font-size:12pt;\">--physaddr &lt;\u5730\u5740&gt;	\u76f4\u63a5\u8f6c\u50a8\u6307\u5b9a\u7269\u7406\u5730\u5740\u7684\u6587\u4ef6</span></p><p><span style=\" font-size:12pt;\">--output-dir &lt;dir&gt;	\u5c06\u6587\u4ef6\u5bfc\u51fa\u5230\u6307\u5b9a\u76ee\u5f55</span></p><p><br/></p><p><span style=\" font-size:12pt;\">\u6548\u679c\uff1a</span></p><p><span style=\" font-size:12pt;\">1.\u663e\u793a\u6587\u4ef6\u540d\u3001\u6587\u4ef6\u5bf9\u8c61\u5730\u5740\u3001\u5927"
                        "\u5c0f\u3001\u8bbf\u95ee\u65f6\u95f4\u7b49\u4fe1\u606f</span></p><p><span style=\" font-size:12pt;\">2.\u53ef\u7528\u4e8e\u53d1\u73b0\u6076\u610f\u6587\u4ef6\u3001\u9690\u85cf\u6587\u4ef6\u6216\u5f02\u5e38\u6587\u4ef6\u8bbf\u95ee</span></p><p><span style=\" font-size:12pt;\">3.\u80fd\u6062\u590d\u5df2\u5220\u9664\u4f46\u4ecd\u5b58\u5728\u4e8e\u5185\u5b58\u4e2d\u7684\u6587\u4ef6\u5f15\u7528</span></p><p><br/></p><p><span style=\" font-size:12pt;\">\u4f7f\u7528\uff1a</span></p><p><span style=\" font-size:12pt;\">python vol.py -f memory.dmp windows.filescan --name-filter &quot;*.docx&quot;</span></p><p><span style=\" font-size:12pt;\">python vol.py -f memory.dmp windows.filescan | findstr .docx | .pdf | .zip</span></p><p><span style=\" font-size:12pt;\"># \u83b7\u53d6\u7269\u7406\u5730\u5740\u540e\uff0c\u4f7f\u7528 dumpfiles \u5bfc\u51fa</span></p><p><span style=\" font-size:12pt;\">python vol.py -f memory.dmp windows.dumpfiles --physaddr 0x3e1b000 --output-dir extracted_files</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_filescan.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u626b\u63cf", None))
#if QT_CONFIG(tooltip)
        self.v3w_strings.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p><span style=\" font-size:12pt; background-color:#ffffff;\">windows.strings.Strings</span></p><p><span style=\" font-size:12pt; font-weight:700; background-color:#ffffff;\">\u529f\u80fd</span><span style=\" font-size:12pt; background-color:#ffffff;\">\uff1a\u63d0\u53d6\u5185\u5b58\u4e2d\u7684ASCII/Unicode\u5b57\u7b26\u4e32</span></p><p><span style=\" font-size:12pt; font-weight:700; background-color:#ffffff;\">\u53c2\u6570\u8bf4\u660e</span></p><p><span style=\" font-size:12pt; background-color:#ffffff;\">--pid &lt;PID&gt; \u4ec5\u63d0\u53d6\u6307\u5b9a\u8fdb\u7a0b\u7684\u5b57\u7b26\u4e32</span></p><p><span style=\" font-size:12pt; background-color:#ffffff;\">--min-length &lt;N&gt; \u8fc7\u6ee4\u6700\u5c0f\u957f\u5ea6\u7684\u5b57\u7b26\u4e32\uff08\u9ed8\u8ba4 3\uff09</span></p><p><span style=\" font-size:12pt; background-color:#ffffff;\">--encoding &lt;ascii/unicode&gt; \u6307\u5b9a\u5b57\u7b26\u4e32\u7f16\u7801\u7c7b\u578b</span></p><p><span style=\" font-size:12pt; background-color:#ffff"
                        "ff;\">--output-file &lt;path&gt; \u5c06\u7ed3\u679c\u4fdd\u5b58\u5230\u6587\u4ef6</span></p><p><span style=\" font-size:12pt; font-weight:700; background-color:#ffffff;\">\u7528\u6cd5\uff1a</span></p><p><span style=\" font-size:12pt; background-color:#ffffff;\">vol.py -f memory.dump windows.strings --pid &lt;PID&gt; --offset 0x100000 | findstr &quot;http://|https://|.exe|.dll|password&quot;</span></p><p><span style=\" font-size:12pt; font-weight:700; background-color:#ffffff;\">\u7b56\u7565\uff1a</span><span style=\" font-size:12pt; background-color:#ffffff;\">\u7ed3\u5408grep \u6216 findstr \u641c\u7d22\u6307\u5b9a\u5b57\u7b26\u4e32</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_strings.setText(QCoreApplication.translate("zhu_windows", u"\u5b57\u7b26\u4e32\u641c\u7d22", None))
#if QT_CONFIG(tooltip)
        self.v3w_dumpfiles.setToolTip(QCoreApplication.translate("zhu_windows", u"<html><head/><body><p><span style=\" font-size:12pt;\">windows.dumpfiles</span></p><p><span style=\" font-size:12pt; font-weight:700;\">\u529f\u80fd:</span><span style=\" font-size:12pt;\">\u4ece\u5185\u5b58\u4e2d\u63d0\u53d6\u6587\u4ef6\u5185\u5bb9\uff0c\u652f\u6301\u7269\u7406\u5730\u5740\u6216\u865a\u62df\u5730\u5740\u5b9a\u4f4d\u3002\u7528\u4e8e\u6062\u590d \u5df2\u5220\u9664\u6587\u4ef6\u3001\u5bfc\u51fa\u6076\u610f\u8f6f\u4ef6\u6837\u672c\u6216\u5206\u6790\u5185\u5b58\u7f13\u5b58\u7684\u6587\u4ef6\u3002</span></p><p><br/></p><p><span style=\" font-size:12pt; font-weight:700;\">\u53c2\u6570\u8bf4\u660e\uff1a</span><span style=\" font-size:12pt;\"/></p><p><span style=\" font-size:12pt;\">--pid &lt;PID&gt;</span></p><p><span style=\" font-size:12pt;\">--virtaddr   &lt;\u865a\u62df\u5730\u5740&gt;</span></p><p><span style=\" font-size:12pt;\">--physaddr &lt;\u7269\u7406\u5730\u5740&gt;</span></p><p><span style=\" font-size:12pt;\">--filter FILTER &lt;\u6587\u4ef6\u540d&gt;</span></p><p><span style=\" font-si"
                        "ze:12pt;\">--ignore-case   \u5ffd\u7565\u5927\u5c0f\u5199</span></p><p><span style=\" font-size:12pt;\">--output-dir &lt;\u8f93\u51fa\u8def\u5f84&gt;</span></p><p><br/></p><p><span style=\" font-size:12pt; font-weight:700;\">\u4f7f\u7528\u65b9\u5f0f\uff1a</span><span style=\" font-size:12pt;\">\u9700\u5148\u901a\u8fc7 filescan \u83b7\u53d6\u5730\u5740</span></p><p><span style=\" font-size:12pt;\">python vol.py -f memory.dmp windows.dumpfiles --physaddr 0x3e1b000 --output-dir &lt;\u8f93\u51fa\u8def\u5f84&gt;</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.v3w_dumpfiles.setText(QCoreApplication.translate("zhu_windows", u"\u8f6c\u50a8\u6587\u4ef6", None))
        self.v3w_dump.setText(QCoreApplication.translate("zhu_windows", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.v3w_registry_hive.setText(QCoreApplication.translate("zhu_windows", u"Hive", None))
        self.v3w_registry_key.setText(QCoreApplication.translate("zhu_windows", u"key", None))
        self.v3w_recurse.setText(QCoreApplication.translate("zhu_windows", u"key\u9012\u5f52", None))
        self.v3w_printkey.setText(QCoreApplication.translate("zhu_windows", u"\u63d0\u53d6\u6ce8\u518c\u8868", None))
        self.label_17.setText(QCoreApplication.translate("zhu_windows", u"windows\u67e5\u8be2", None))
        self.v3w_fun_list.setItemText(0, QCoreApplication.translate("zhu_windows", u"\u5df2\u6267\u884c\u7684\u7a0b\u5e8f\u4fe1\u606f", None))
        self.v3w_fun_list.setItemText(1, QCoreApplication.translate("zhu_windows", u"\u83b7\u53d6\u7cfb\u7edf\u7f13\u5b58\u7684\u5bc6\u7801\u54c8\u5e0c", None))
        self.v3w_fun_list.setItemText(2, QCoreApplication.translate("zhu_windows", u"\u67e5\u770bcmd\u542f\u52a8\u547d\u4ee4", None))
        self.v3w_fun_list.setItemText(3, QCoreApplication.translate("zhu_windows", u"\u626b\u63cfcmd\u5386\u53f2\u8bb0\u5f55", None))
        self.v3w_fun_list.setItemText(4, QCoreApplication.translate("zhu_windows", u"\u63d0\u53d6cmd\u4f1a\u8bdd\u8bb0\u5f55", None))
        self.v3w_fun_list.setItemText(5, QCoreApplication.translate("zhu_windows", u"\u5206\u6790Windows\u5d29\u6e83\u8f6c\u50a8", None))
        self.v3w_fun_list.setItemText(6, QCoreApplication.translate("zhu_windows", u"\u5217\u51fa\u9a71\u52a8\u7a0b\u5e8f\u548c\u5173\u8054\u8bbe\u5907\u6811", None))
        self.v3w_fun_list.setItemText(7, QCoreApplication.translate("zhu_windows", u"\u5217\u51fa\u8fdb\u7a0b\u52a0\u8f7d\u7684DLL\u6a21\u5757", None))
        self.v3w_fun_list.setItemText(8, QCoreApplication.translate("zhu_windows", u"\u68c0\u6d4b\u9690\u85cf\u7684\u9a71\u52a8\u6a21\u5757", None))
        self.v3w_fun_list.setItemText(9, QCoreApplication.translate("zhu_windows", u"\u9690\u85cf\u9a71\u52a8\u626b\u63cf", None))
        self.v3w_fun_list.setItemText(10, QCoreApplication.translate("zhu_windows", u"\u73af\u5883\u53d8\u91cf\u4fe1\u606f", None))
        self.v3w_fun_list.setItemText(11, QCoreApplication.translate("zhu_windows", u"\u83b7\u53d6\u670d\u52a1ids", None))
        self.v3w_fun_list.setItemText(12, QCoreApplication.translate("zhu_windows", u"\u663e\u793a\u8fdb\u7a0b\u6240\u5c5e\u7684 SID", None))
        self.v3w_fun_list.setItemText(13, QCoreApplication.translate("zhu_windows", u"\u5217\u51fa\u8fdb\u7a0b\u6253\u5f00\u7684\u53e5\u67c4", None))
        self.v3w_fun_list.setItemText(14, QCoreApplication.translate("zhu_windows", u"\u4ece\u5185\u5b58\u4e2d\u8f6c\u50a8\u5404\u79cd\u51ed\u636e", None))
        self.v3w_fun_list.setItemText(15, QCoreApplication.translate("zhu_windows", u"\u68c0\u6d4b\u8fdb\u7a0b\u4e2d\u6f5c\u5728\u7684\u5185\u5b58\u6ce8\u5165\u4ee3\u7801", None))
        self.v3w_fun_list.setItemText(16, QCoreApplication.translate("zhu_windows", u"\u626b\u63cf\u4e3b\u5f15\u5bfc\u8bb0\u5f55MBR", None))
        self.v3w_fun_list.setItemText(17, QCoreApplication.translate("zhu_windows", u"\u626b\u63cfMFT\u6587\u4ef6\u5bf9\u8c61", None))
        self.v3w_fun_list.setItemText(18, QCoreApplication.translate("zhu_windows", u"\u626b\u63cf\u7f51\u7edc\u8fde\u63a5\u5bf9\u8c61", None))
        self.v3w_fun_list.setItemText(19, QCoreApplication.translate("zhu_windows", u"\u5217\u51fa\u5185\u5b58\u4e2d\u7684\u8fdb\u7a0b", None))
        self.v3w_fun_list.setItemText(20, QCoreApplication.translate("zhu_windows", u"\u626b\u63cf\u5185\u5b58\u4e2d\u7684\u8fdb\u7a0b", None))
        self.v3w_fun_list.setItemText(21, QCoreApplication.translate("zhu_windows", u"\u4ee5\u6811\u72b6\u7ed3\u6784\u663e\u793a\u8fdb\u7a0b\u7236\u5b50\u5173\u7cfb", None))
        self.v3w_fun_list.setItemText(22, QCoreApplication.translate("zhu_windows", u"\u68c0\u6d4b\u6ce8\u518c\u8868\u914d\u7f6e\u5355\u5143", None))
        self.v3w_fun_list.setItemText(23, QCoreApplication.translate("zhu_windows", u"\u6ce8\u518c\u8868\u914d\u7f6e\u4fe1\u606f", None))
        self.v3w_fun_list.setItemText(24, QCoreApplication.translate("zhu_windows", u"\u626b\u63cf\u5185\u5b58\u4e2d\u7684\u6ce8\u518c\u8868\u914d\u7f6e\u5355\u5143", None))
        self.v3w_fun_list.setItemText(25, QCoreApplication.translate("zhu_windows", u"\u5217\u51fa\u6ce8\u518c\u8868\u952e\u503c", None))
        self.v3w_fun_list.setItemText(26, QCoreApplication.translate("zhu_windows", u"\u63d0\u53d6\u8bb0\u5f55\u7528\u6237\u6267\u884c\u7a0b\u5e8f\u7684\u5386\u53f2", None))
        self.v3w_fun_list.setItemText(27, QCoreApplication.translate("zhu_windows", u"\u8ba1\u5212\u4efb\u52a1\u4fe1\u606f", None))
        self.v3w_fun_list.setItemText(28, QCoreApplication.translate("zhu_windows", u"sessions\u4f1a\u8bdd\u8bb0\u5f55", None))
        self.v3w_fun_list.setItemText(29, QCoreApplication.translate("zhu_windows", u"\u83b7\u53d6\u5386\u53f2\u6267\u884c\u8bb0\u5f55", None))
        self.v3w_fun_list.setItemText(30, QCoreApplication.translate("zhu_windows", u"\u6076\u610fSkeleton\u68c0\u6d4b", None))
        self.v3w_fun_list.setItemText(31, QCoreApplication.translate("zhu_windows", u"\u9690\u85cf\u670d\u52a1\u68c0\u6d4b", None))
        self.v3w_fun_list.setItemText(32, QCoreApplication.translate("zhu_windows", u"\u626b\u63cf\u5185\u5b58\u4e2d\u7684Windows\u670d\u52a1", None))
        self.v3w_fun_list.setItemText(33, QCoreApplication.translate("zhu_windows", u"\u68c0\u6d4b\u7cfb\u7edf\u4e2d\u5b58\u5728\u7684\u7b26\u53f7\u94fe\u63a5", None))
        self.v3w_fun_list.setItemText(34, QCoreApplication.translate("zhu_windows", u"\u67e5\u627eTrueCrypt\u7f13\u5b58\u7684\u5bc6\u7801", None))
        self.v3w_fun_list.setItemText(35, QCoreApplication.translate("zhu_windows", u"\u5217\u51fa\u8fdb\u7a0b\u7684\u865a\u62df\u5730\u5740\u63cf\u8ff0\u7b26", None))
        self.v3w_fun_list.setItemText(36, QCoreApplication.translate("zhu_windows", u"\u63d0\u53d6 PE \u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f", None))
        self.v3w_fun_list.setItemText(37, QCoreApplication.translate("zhu_windows", u"\u4f7f\u7528 YARA \u89c4\u5219\u626b\u63cf\u5185\u6838\u5185\u5b58", None))

        self.v3w_fun_but.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2", None))
        self.label_18.setText(QCoreApplication.translate("zhu_windows", u"linux\u67e5\u8be2", None))
        self.v3l_fun_but.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2", None))
        self.label_19.setText(QCoreApplication.translate("zhu_windows", u"macos\u67e5\u8be2", None))
        self.v3m_fun_but.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("zhu_windows", u"VOL3", None))
        self.pushButton_4.setText(QCoreApplication.translate("zhu_windows", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("zhu_windows", u"VOL2", None))
        self.function_list.setTabText(self.function_list.indexOf(self.vol_tab), QCoreApplication.translate("zhu_windows", u"\u5185\u5b58\u5206\u6790", None))
        self.label_2.setText(QCoreApplication.translate("zhu_windows", u"\u6570\u636e\u8f93\u5165\u533a", None))
        self.db_clear.setText(QCoreApplication.translate("zhu_windows", u"\u5220\u9664\u6570\u636e\u5e93", None))
        self.list_clear.setText(QCoreApplication.translate("zhu_windows", u"\u8868\u683c\u6e05\u7406", None))
        self.start_db_but.setText(QCoreApplication.translate("zhu_windows", u"\u6570\u636e\u5165\u5e93", None))
        self.read_db.setText(QCoreApplication.translate("zhu_windows", u"\u8bfb\u53d6\u6570\u636e\u5e93", None))
        self.label_22.setText(QCoreApplication.translate("zhu_windows", u"\u6587\u4ef6\u8f6c\u6362", None))
        self.txt_csv.setText(QCoreApplication.translate("zhu_windows", u"TXT\u8f6cCSV", None))
        self.label_14.setText(QCoreApplication.translate("zhu_windows", u"SQL\u6570\u636e\u67e5\u8be2", None))
        self.select_yufa.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2\u8bed\u6cd5", None))
        self.revise_column_name.setText(QCoreApplication.translate("zhu_windows", u"\u4fee\u6539\u6570\u636e\u5e93\u5217\u540d", None))
        self.db_select_but.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2", None))
        self.label_15.setText(QCoreApplication.translate("zhu_windows", u"\u6570\u636e\u5206\u6790\u533a", None))
        self.select_one_up.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2\u4e2a\u4eba\u4e0a\u7ebf", None))
        self.select_one_down.setText(QCoreApplication.translate("zhu_windows", u"\u67e5\u8be2\u4e2a\u4eba\u4e0b\u7ebf", None))
        self.show_guanxi.setText(QCoreApplication.translate("zhu_windows", u"\u5c42\u7ea7\u6811\u72b6\u56fe", None))
        self.function_list.setTabText(self.function_list.indexOf(self.data_tab), QCoreApplication.translate("zhu_windows", u"\u6570\u636e\u5206\u6790", None))
        self.label_5.setText(QCoreApplication.translate("zhu_windows", u"IOS\u5206\u6790", None))
        self.plist_but.setText(QCoreApplication.translate("zhu_windows", u"plist\u89e3\u6790", None))
        self.label_6.setText(QCoreApplication.translate("zhu_windows", u"android\u5206\u6790", None))
        self.pushButton_2.setText(QCoreApplication.translate("zhu_windows", u"\u65e0\u529f\u80fd", None))
        self.label_20.setText(QCoreApplication.translate("zhu_windows", u"HOOK\u5de5\u5177", None))
        self.hook_name.setText(QCoreApplication.translate("zhu_windows", u"\u8f93\u5165\u5305\u540d", None))
        self.hook_fun.setItemText(0, QCoreApplication.translate("zhu_windows", u"\u83b7\u53d6\u5168\u90e8\u5b57\u7b26\u4e32", None))
        self.hook_fun.setItemText(1, QCoreApplication.translate("zhu_windows", u"\u83b7\u53d6\u5b57\u7b26\u4e32", None))
        self.hook_fun.setItemText(2, QCoreApplication.translate("zhu_windows", u"\u83b7\u53d6AES\u52a0\u5bc6", None))
        self.hook_fun.setItemText(3, QCoreApplication.translate("zhu_windows", u"\u53cd\u8c03\u8bd5", None))
        self.hook_fun.setItemText(4, QCoreApplication.translate("zhu_windows", u"\u7ed5\u8fc7frida\u68c0\u6d4b", None))

        self.hook_but.setText(QCoreApplication.translate("zhu_windows", u"HOOK\u6267\u884c", None))
        self.label_21.setText(QCoreApplication.translate("zhu_windows", u"python\u53cd\u7f16\u8bd1", None))
        self.pyc_but.setText(QCoreApplication.translate("zhu_windows", u"pyc\u53cd\u7f16\u8bd1", None))
        self.label_8.setText(QCoreApplication.translate("zhu_windows", u"\u4eba\u5de5\u667a\u80fd\u8f6f\u4ef6", None))
        self.facefusion_but.setText(QCoreApplication.translate("zhu_windows", u"facefusion", None))
        self.label_7.setText(QCoreApplication.translate("zhu_windows", u"\u5176\u4ed6\u5de5\u5177", None))
        self.mod_but.setText(QCoreApplication.translate("zhu_windows", u"\u5404\u79cd\u5c0f\u811a\u672c", None))
        self.time_zhuan.setText(QCoreApplication.translate("zhu_windows", u"\u65f6\u95f4\u6233\u8f6c\u6362", None))
        self.rsa_public.setText(QCoreApplication.translate("zhu_windows", u"RSA\u516c\u94a5\u5206\u89e3", None))
        self.ceshi111_but.setText(QCoreApplication.translate("zhu_windows", u"\u6d4b\u8bd5\u6309\u94ae", None))
        self.function_list.setTabText(self.function_list.indexOf(self.misc_tab), QCoreApplication.translate("zhu_windows", u"\u9006\u5411\u5206\u6790", None))
        self.label.setText(QCoreApplication.translate("zhu_windows", u"\u56de\u663e\u8f93\u51fa", None))
        self.silu_but.setText(QCoreApplication.translate("zhu_windows", u"\u8bf4\u660e\u6587\u6863", None))
        self.clear_but.setText(QCoreApplication.translate("zhu_windows", u"\u6e05\u7406\u56de\u663e", None))
        self.text_echo.setHtml(QCoreApplication.translate("zhu_windows", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u6977\u4f53'; font-weight:700;\">\u8f93\u51fa\u6846</span></p></body></html>", None))
    # retranslateUi

