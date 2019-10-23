# -*- coding: utf-8 -*-
import time

import requests
from imapclient import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(840, 600)
        Main_Window.setStyleSheet("QToolTip\n"
                                  "{\n"
                                  "     border: 1px solid black;\n"
                                  "     background-color: #ffa02f;\n"
                                  "     padding: 1px;\n"
                                  "     border-radius: 3px;\n"
                                  "     opacity: 100;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget\n"
                                  "{\n"
                                  "    color: #b1b1b1;\n"
                                  "    background-color: #323232;\n"
                                  "}\n"
                                  "\n"
                                  "QTreeView, QListView\n"
                                  "{\n"
                                  "    background-color: silver;\n"
                                  "    margin-left: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget:item:hover\n"
                                  "{\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
                                  "    color: #000000;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget:item:selected\n"
                                  "{\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                  "}\n"
                                  "\n"
                                  "QMenuBar::item\n"
                                  "{\n"
                                  "    background: transparent;\n"
                                  "}\n"
                                  "\n"
                                  "QMenuBar::item:selected\n"
                                  "{\n"
                                  "    background: transparent;\n"
                                  "    border: 1px solid #ffaa00;\n"
                                  "}\n"
                                  "\n"
                                  "QMenuBar::item:pressed\n"
                                  "{\n"
                                  "    background: #444;\n"
                                  "    border: 1px solid #000;\n"
                                  "    background-color: QLinearGradient(\n"
                                  "        x1:0, y1:0,\n"
                                  "        x2:0, y2:1,\n"
                                  "        stop:1 #212121,\n"
                                  "        stop:0.4 #343434/*,\n"
                                  "        stop:0.2 #343434,\n"
                                  "        stop:0.1 #ffaa00*/\n"
                                  "    );\n"
                                  "    margin-bottom:-1px;\n"
                                  "    padding-bottom:1px;\n"
                                  "}\n"
                                  "\n"
                                  "QMenu\n"
                                  "{\n"
                                  "    border: 1px solid #000;\n"
                                  "}\n"
                                  "\n"
                                  "QMenu::item\n"
                                  "{\n"
                                  "    padding: 2px 20px 2px 20px;\n"
                                  "}\n"
                                  "\n"
                                  "QMenu::item:selected\n"
                                  "{\n"
                                  "    color: #000000;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget:disabled\n"
                                  "{\n"
                                  "    color: #808080;\n"
                                  "    background-color: #323232;\n"
                                  "}\n"
                                  "\n"
                                  "QAbstractItemView\n"
                                  "{\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
                                  "}\n"
                                  "\n"
                                  "QWidget:focus\n"
                                  "{\n"
                                  "    /*border: 1px solid darkgray;*/\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit\n"
                                  "{\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                                  "    padding: 1px;\n"
                                  "    border-style: solid;\n"
                                  "    border: 1px solid #1e1e1e;\n"
                                  "    border-radius: 5;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton\n"
                                  "{\n"
                                  "    color: #b1b1b1;\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                  "    border-width: 1px;\n"
                                  "    border-color: #1e1e1e;\n"
                                  "    border-style: solid;\n"
                                  "    border-radius: 6;\n"
                                  "    padding: 3px;\n"
                                  "    font-size: 12px;\n"
                                  "    padding-left: 5px;\n"
                                  "    padding-right: 5px;\n"
                                  "    min-width: 40px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed\n"
                                  "{\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox\n"
                                  "{\n"
                                  "    selection-background-color: #ffaa00;\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                  "    border-style: solid;\n"
                                  "    border: 1px solid #1e1e1e;\n"
                                  "    border-radius: 5;\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox:hover,QPushButton:hover\n"
                                  "{\n"
                                  "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "QComboBox:on\n"
                                  "{\n"
                                  "    padding-top: 3px;\n"
                                  "    padding-left: 4px;\n"
                                  "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                  "    selection-background-color: #ffaa00;\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox QAbstractItemView\n"
                                  "{\n"
                                  "    border: 2px solid darkgray;\n"
                                  "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox::drop-down\n"
                                  "{\n"
                                  "     subcontrol-origin: padding;\n"
                                  "     subcontrol-position: top right;\n"
                                  "     width: 15px;\n"
                                  "\n"
                                  "     border-left-width: 0px;\n"
                                  "     border-left-color: darkgray;\n"
                                  "     border-left-style: solid; /* just a single line */\n"
                                  "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                  "     border-bottom-right-radius: 3px;\n"
                                  " }\n"
                                  "\n"
                                  "QComboBox::down-arrow\n"
                                  "{\n"
                                  "     image: url(:/dark_orange/img/down_arrow.png);\n"
                                  "}\n"
                                  "\n"
                                  "QGroupBox\n"
                                  "{\n"
                                  "    border: 1px solid darkgray;\n"
                                  "    margin-top: 10px;\n"
                                  "}\n"
                                  "\n"
                                  "QGroupBox:focus\n"
                                  "{\n"
                                  "    border: 1px solid darkgray;\n"
                                  "}\n"
                                  "\n"
                                  "QTextEdit:focus\n"
                                  "{\n"
                                  "    border: 1px solid darkgray;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar:horizontal {\n"
                                  "     border: 1px solid #222222;\n"
                                  "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                  "     height: 7px;\n"
                                  "     margin: 0px 16px 0 16px;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::handle:horizontal\n"
                                  "{\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                  "      min-height: 20px;\n"
                                  "      border-radius: 2px;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::add-line:horizontal {\n"
                                  "      border: 1px solid #1b1b19;\n"
                                  "      border-radius: 2px;\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                  "      width: 14px;\n"
                                  "      subcontrol-position: right;\n"
                                  "      subcontrol-origin: margin;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::sub-line:horizontal {\n"
                                  "      border: 1px solid #1b1b19;\n"
                                  "      border-radius: 2px;\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                  "      width: 14px;\n"
                                  "     subcontrol-position: left;\n"
                                  "     subcontrol-origin: margin;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
                                  "{\n"
                                  "      border: 1px solid black;\n"
                                  "      width: 1px;\n"
                                  "      height: 1px;\n"
                                  "      background: white;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                  "{\n"
                                  "      background: none;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar:vertical\n"
                                  "{\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                  "      width: 7px;\n"
                                  "      margin: 16px 0 16px 0;\n"
                                  "      border: 1px solid #222222;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::handle:vertical\n"
                                  "{\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                  "      min-height: 20px;\n"
                                  "      border-radius: 2px;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::add-line:vertical\n"
                                  "{\n"
                                  "      border: 1px solid #1b1b19;\n"
                                  "      border-radius: 2px;\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                  "      height: 14px;\n"
                                  "      subcontrol-position: bottom;\n"
                                  "      subcontrol-origin: margin;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::sub-line:vertical\n"
                                  "{\n"
                                  "      border: 1px solid #1b1b19;\n"
                                  "      border-radius: 2px;\n"
                                  "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
                                  "      height: 14px;\n"
                                  "      subcontrol-position: top;\n"
                                  "      subcontrol-origin: margin;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                  "{\n"
                                  "      border: 1px solid black;\n"
                                  "      width: 1px;\n"
                                  "      height: 1px;\n"
                                  "      background: white;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                  "{\n"
                                  "      background: none;\n"
                                  "}\n"
                                  "\n"
                                  "QTextEdit\n"
                                  "{\n"
                                  "    background-color: #242424;\n"
                                  "}\n"
                                  "\n"
                                  "QPlainTextEdit\n"
                                  "{\n"
                                  "    background-color: #242424;\n"
                                  "}\n"
                                  "\n"
                                  "QHeaderView::section\n"
                                  "{\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
                                  "    color: white;\n"
                                  "    padding-left: 4px;\n"
                                  "    border: 1px solid #6c6c6c;\n"
                                  "}\n"
                                  "\n"
                                  "QCheckBox:disabled\n"
                                  "{\n"
                                  "color: #414141;\n"
                                  "}\n"
                                  "\n"
                                  "QDockWidget::title\n"
                                  "{\n"
                                  "    text-align: center;\n"
                                  "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                  "}\n"
                                  "\n"
                                  "QDockWidget::close-button, QDockWidget::float-button\n"
                                  "{\n"
                                  "    text-align: center;\n"
                                  "    spacing: 1px; /* spacing between items in the tool bar */\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                  "}\n"
                                  "\n"
                                  "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
                                  "{\n"
                                  "    background: #242424;\n"
                                  "}\n"
                                  "\n"
                                  "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
                                  "{\n"
                                  "    padding: 1px -1px -1px 1px;\n"
                                  "}\n"
                                  "\n"
                                  "QMainWindow::separator\n"
                                  "{\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                  "    color: white;\n"
                                  "    padding-left: 4px;\n"
                                  "    border: 1px solid #4c4c4c;\n"
                                  "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                  "}\n"
                                  "\n"
                                  "QMainWindow::separator:hover\n"
                                  "{\n"
                                  "\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
                                  "    color: white;\n"
                                  "    padding-left: 4px;\n"
                                  "    border: 1px solid #6c6c6c;\n"
                                  "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                  "}\n"
                                  "\n"
                                  "QToolBar::handle\n"
                                  "{\n"
                                  "     spacing: 3px; /* spacing between items in the tool bar */\n"
                                  "     background: url(:/dark_orange/img/handle.png);\n"
                                  "}\n"
                                  "\n"
                                  "QMenu::separator\n"
                                  "{\n"
                                  "    height: 2px;\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                  "    color: white;\n"
                                  "    padding-left: 4px;\n"
                                  "    margin-left: 10px;\n"
                                  "    margin-right: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QProgressBar\n"
                                  "{\n"
                                  "    border: 2px solid grey;\n"
                                  "    border-radius: 5px;\n"
                                  "    text-align: center;\n"
                                  "}\n"
                                  "\n"
                                  "QProgressBar::chunk\n"
                                  "{\n"
                                  "    background-color: #d7801a;\n"
                                  "    width: 2.15px;\n"
                                  "    margin: 0.5px;\n"
                                  "}\n"
                                  "\n"
                                  "QTabBar::tab {\n"
                                  "    color: #b1b1b1;\n"
                                  "    border: 1px solid #444;\n"
                                  "    border-bottom-style: none;\n"
                                  "    background-color: #323232;\n"
                                  "    padding-left: 10px;\n"
                                  "    padding-right: 10px;\n"
                                  "    padding-top: 3px;\n"
                                  "    padding-bottom: 2px;\n"
                                  "    margin-right: -1px;\n"
                                  "}\n"
                                  "\n"
                                  "QTabWidget::pane {\n"
                                  "    border: 1px solid #444;\n"
                                  "    top: 1px;\n"
                                  "}\n"
                                  "\n"
                                  "QTabBar::tab:last\n"
                                  "{\n"
                                  "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                  "    border-top-right-radius: 3px;\n"
                                  "}\n"
                                  "\n"
                                  "QTabBar::tab:first:!selected\n"
                                  "{\n"
                                  " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
                                  "\n"
                                  "\n"
                                  "    border-top-left-radius: 3px;\n"
                                  "}\n"
                                  "\n"
                                  "QTabBar::tab:!selected\n"
                                  "{\n"
                                  "    color: #b1b1b1;\n"
                                  "    border-bottom-style: solid;\n"
                                  "    margin-top: 3px;\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
                                  "}\n"
                                  "\n"
                                  "QTabBar::tab:selected\n"
                                  "{\n"
                                  "    border-top-left-radius: 3px;\n"
                                  "    border-top-right-radius: 3px;\n"
                                  "    margin-bottom: 0px;\n"
                                  "}\n"
                                  "\n"
                                  "QTabBar::tab:!selected:hover\n"
                                  "{\n"
                                  "    /*border-top: 2px solid #ffaa00;\n"
                                  "    padding-bottom: 3px;*/\n"
                                  "    border-top-left-radius: 3px;\n"
                                  "    border-top-right-radius: 3px;\n"
                                  "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                                  "    color: #b1b1b1;\n"
                                  "    background-color: #323232;\n"
                                  "    border: 1px solid #b1b1b1;\n"
                                  "    border-radius: 6px;\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator:checked\n"
                                  "{\n"
                                  "    background-color: qradialgradient(\n"
                                  "        cx: 0.5, cy: 0.5,\n"
                                  "        fx: 0.5, fy: 0.5,\n"
                                  "        radius: 1.0,\n"
                                  "        stop: 0.25 #ffaa00,\n"
                                  "        stop: 0.3 #323232\n"
                                  "    );\n"
                                  "}\n"
                                  "\n"
                                  "QCheckBox::indicator{\n"
                                  "    color: #b1b1b1;\n"
                                  "    background-color: #323232;\n"
                                  "    border: 1px solid #b1b1b1;\n"
                                  "    width: 9px;\n"
                                  "    height: 9px;\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator\n"
                                  "{\n"
                                  "    border-radius: 6px;\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                                  "{\n"
                                  "    border: 1px solid #ffaa00;\n"
                                  "}\n"
                                  "\n"
                                  "QCheckBox::indicator:checked\n"
                                  "{\n"
                                  "    image:url(:/dark_orange/img/checkbox.png);\n"
                                  "}\n"
                                  "\n"
                                  "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
                                  "{\n"
                                  "    border: 1px solid #444;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "QSlider::groove:horizontal {\n"
                                  "    border: 1px solid #3A3939;\n"
                                  "    height: 8px;\n"
                                  "    background: #201F1F;\n"
                                  "    margin: 2px 0;\n"
                                  "    border-radius: 2px;\n"
                                  "}\n"
                                  "\n"
                                  "QSlider::handle:horizontal {\n"
                                  "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                  "      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                  "    border: 1px solid #3A3939;\n"
                                  "    width: 14px;\n"
                                  "    height: 14px;\n"
                                  "    margin: -4px 0;\n"
                                  "    border-radius: 2px;\n"
                                  "}\n"
                                  "\n"
                                  "QSlider::groove:vertical {\n"
                                  "    border: 1px solid #3A3939;\n"
                                  "    width: 8px;\n"
                                  "    background: #201F1F;\n"
                                  "    margin: 0 0px;\n"
                                  "    border-radius: 2px;\n"
                                  "}\n"
                                  "\n"
                                  "QSlider::handle:vertical {\n"
                                  "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
                                  "      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                  "    border: 1px solid #3A3939;\n"
                                  "    width: 14px;\n"
                                  "    height: 14px;\n"
                                  "    margin: 0 -4px;\n"
                                  "    border-radius: 2px;\n"
                                  "}\n"
                                  "\n"
                                  "QAbstractSpinBox {\n"
                                  "    padding-top: 2px;\n"
                                  "    padding-bottom: 2px;\n"
                                  "    border: 1px solid darkgray;\n"
                                  "\n"
                                  "    border-radius: 2px;\n"
                                  "    min-width: 50px;\n"
                                  "}")

        self.centralwidget = QtWidgets.QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 821, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # ============================================= LABELS ===================================================
        self.label_email = QtWidgets.QLabel(self.frame)
        self.label_email.setGeometry(QtCore.QRect(50, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")

        self.label_password = QtWidgets.QLabel(self.frame)
        self.label_password.setGeometry(QtCore.QRect(340, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.label_mailer = QtWidgets.QLabel(self.frame)
        self.label_mailer.setGeometry(QtCore.QRect(50, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mailer.setFont(font)
        self.label_mailer.setObjectName("label_mailer")

        self.label_emailslistname = QtWidgets.QLabel(self.frame)
        self.label_emailslistname.setGeometry(QtCore.QRect(60, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_emailslistname.setFont(font)
        self.label_emailslistname.setObjectName("label_emailslistname")

        self.label_mailinfo = QtWidgets.QLabel(self.frame)
        self.label_mailinfo.setGeometry(QtCore.QRect(640, 200, 141, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mailinfo.setFont(font)
        self.label_mailinfo.setAutoFillBackground(False)
        self.label_mailinfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_mailinfo.setScaledContents(False)
        self.label_mailinfo.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_mailinfo.setWordWrap(True)
        self.label_mailinfo.setObjectName("label_mailinfo")

        self.label_emailconfirmed = QtWidgets.QLabel(self.frame)
        self.label_emailconfirmed.setGeometry(QtCore.QRect(640, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_emailconfirmed.setFont(font)
        self.label_emailconfirmed.setObjectName("label_emailconfirmed")

        self.label_progress = QtWidgets.QLabel(self.frame)
        self.label_progress.setGeometry(QtCore.QRect(60, 460, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")

        # ============================================= LINE EDIT ===================================================
        self.lineedit_mailer = QtWidgets.QLineEdit(self.frame)
        self.lineedit_mailer.setGeometry(QtCore.QRect(50, 120, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineedit_mailer.setFont(font)
        self.lineedit_mailer.setObjectName("lineedit_mailer")

        self.lineedit_mailer.setText("noreply@medium.com")
        # self.lineedit_mailer.setPlaceholderText("Enter email you wish delete it's messages")
        self.lineedit_mailer.setDisabled(True)

        self.lineedit_password = QtWidgets.QLineEdit(self.frame)
        self.lineedit_password.setGeometry(QtCore.QRect(340, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineedit_password.setFont(font)
        self.lineedit_password.setObjectName("lineedit_password")
        self.lineedit_password.setText("a0535184509")
        # self.lineedit_password.setPlaceholderText("Enter your mail password")

        self.lineedit_yourmail = QtWidgets.QLineEdit(self.frame)
        self.lineedit_yourmail.setGeometry(QtCore.QRect(50, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineedit_yourmail.setFont(font)
        self.lineedit_yourmail.setObjectName("lineedit_yourmail")
        self.lineedit_yourmail.setText("ahmedsayed551991@gmail.com")
        # self.lineedit_yourmail.setPlaceholderText("Enter your email")

        # ============================================= BUTTON ===================================================
        self.button_addmail = QtWidgets.QPushButton(self.frame)
        self.button_addmail.setGeometry(QtCore.QRect(510, 120, 101, 31))
        self.button_addmail.setObjectName("button_addmail")
        self.button_addmail.clicked.connect(self.add_mail)
        self.button_addmail.setDisabled(True)

        self.button_exit = QtWidgets.QPushButton(self.frame)
        self.button_exit.setGeometry(QtCore.QRect(290, 540, 101, 31))
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(self.close_app_exit)

        self.button_delete = QtWidgets.QPushButton(self.frame)
        self.button_delete.setGeometry(QtCore.QRect(640, 430, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.button_delete.setFont(font)
        self.button_delete.setObjectName("button_delete")
        self.button_delete.clicked.connect(self.delete_messages)
        self.button_delete.setDisabled(True)

        self.button_login = QtWidgets.QPushButton(self.frame)
        self.button_login.setGeometry(QtCore.QRect(550, 40, 61, 31))
        self.button_login.setObjectName("button_login")
        self.button_login.clicked.connect(self.login)

        # ========================================== PROGRESS BAR =================================================
        self.progressbar = QtWidgets.QProgressBar(self.frame)
        self.progressbar.setGeometry(QtCore.QRect(60, 490, 561, 23))
        self.progressbar.setMinimum(1)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setObjectName("progressbar")

        # ============================================= TEXT BROWSER =================================================
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(55, 201, 561, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

        self.deleted_mailes = []
        print("deleted_mailes list", self.deleted_mailes)

        imaplib._MAXLINE = 1000000

    # ============================================= FUNCTIONS =================================================
    # TODO: ADD CLEAR TEXT BROWSE BUTTON & BUTTONS ICONS

    #  --------------------New--------------------
    def auto_detect_mail(self):
        # auto detect mail type (yahoo, Gmail, hotmail)
        # while loop
        if '@yahoo.com' in self.lineedit_yourmail.text():
            # print("auto_detect_mail(self): yahoo mail")
            return 'yahoo'

        elif '@gmail.com' in self.lineedit_yourmail.text():
            print("auto_detect_mail(self): Gmail")
            return 'gmail'

        elif '@hotmail.com' in self.lineedit_yourmail.text():
            # print("auto_detect_mail(self): hotmail")
            return "hotmail"
        else:
            return False

    #  --------------------New--------------------
    def internet_connection(self):
        # check internet connection
        url = 'http://www.google.com/'
        timeout = 5

        try:
            requests.get(url, timeout=timeout)
            return True

        except requests.ConnectionError:
            self.label_emailconfirmed.setText("No internet")
            return False

    #  --------------------New--------------------
    def login(self):
        try:
            self.lineedit_mailer.setDisabled(True)
            self.button_addmail.setDisabled(True)
            self.button_delete.setDisabled(True)

            # login email using address and password
            # yahoo mail
            if self.internet_connection() and self.auto_detect_mail() is 'yahoo':
                self.label_mailinfo.setText("please unprotect your email goto link yahoo imap activate")
                self.yahoo_e_mail = self.lineedit_yourmail.text()
                self.yahoo_password = self.lineedit_password.text()
                self.yahoo_imap_Object = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True, port="993")
                self.yahoo_imap_Object.login(self.yahoo_e_mail, self.yahoo_password)
                self.label_emailconfirmed.setText("yahoo connected")
                print("you have internet connection and yahoo register")

                self.lineedit_mailer.setDisabled(False)
                self.button_addmail.setDisabled(False)
                self.button_delete.setDisabled(False)
                return True

            # Gmail
            elif self.internet_connection() and self.auto_detect_mail() is 'gmail':
                self.label_mailinfo.setText("please unprotect your email goto link gmail imap activate")
                self.gmail_e_mail = self.lineedit_yourmail.text()
                self.gmail_password = self.lineedit_password.text()
                self.gmail_imap_Object = imapclient.IMAPClient('imap.gmail.com', ssl=True)
                self.gmail_imap_Object.login(self.gmail_e_mail, self.gmail_password)
                self.label_emailconfirmed.setText("Gmail connected")
                print("you have internet connection and 'gmail' register")

                self.lineedit_mailer.setDisabled(False)
                self.button_addmail.setDisabled(False)
                self.button_delete.setDisabled(False)
                return True

            # Hotmail
            elif self.internet_connection() and self.auto_detect_mail() is 'hotmail':
                self.label_mailinfo.setText("please unprotect your email goto link hotmail imap activate")
                self.hotmail = self.lineedit_yourmail.text()
                self.hotmail_password = self.lineedit_password.text()

                Server_name = "outlook.office365.com"
                self.hotmail_imap_Object = imapclient.IMAPClient(Server_name, ssl=True, port=993)
                self.hotmail_imap_Object.login(self.hotmail, self.hotmail_password)
                self.label_emailconfirmed.setText("hotmail connected")
                print("you have internet connection and hotmail register")

                self.lineedit_mailer.setDisabled(False)
                self.button_addmail.setDisabled(False)
                self.button_delete.setDisabled(False)
                return True

            else:
                if self.internet_connection():
                    print("Unknown email Or wrong email")
                    return False

        except:
            self.label_mailinfo.setText("Wrong mail or password")
            self.label_emailconfirmed.setText("Error")
            print("Unknown email")

    #  --------------------New--------------------
    def add_mail(self):  # so complicated
        # check if the mail have record messages if it haven't don't add

        # take the all messages from sender and store it in dictionary {key(sender): value(count)}.
        if self.lineedit_mailer.text() not in self.deleted_mailes and "@" in self.lineedit_mailer.text():
            self.deleted_mailes.append(self.lineedit_mailer.text())
            self.lineedit_mailer.clear()
        else:
            self.label_mailinfo.setText("Repeated Mail or wrong mailer")
            return False
        try:
            # login email using address and password
            # yahoo mail
            if self.internet_connection() and self.auto_detect_mail() is 'yahoo':

                self.yahoo_imap_Object.select_folder('INBOX', readonly=False)
                for link in self.deleted_mailes:
                    search_address = f"FROM {link}"
                    self.yahoo_UIDs = self.yahoo_imap_Object.search(search_address)
                    print(self.yahoo_UIDs)
                    index = len(self.deleted_mailes) - (len(self.deleted_mailes) + 1)

                    for i in self.yahoo_UIDs:
                        self.content = f"mail from: {self.deleted_mailes[index]}, messages count = {len(self.yahoo_UIDs)}"
                        print(self.content)

                self.textBrowser.append(str(self.content))

            # Gmail
            elif self.internet_connection() and self.auto_detect_mail() is 'gmail':    # CONFIRMED FUNCTION
                self.gmail_imap_Object.select_folder('INBOX', readonly=False)
                for link in self.deleted_mailes:
                    search = "FROM {}".format(link)
                    self.gmail_UIDs = self.gmail_imap_Object.search(search)
                    for i in self.gmail_UIDs:
                        self.content = f"FROM: {self.deleted_mailes[-1]},  MESSAGES = {len(self.gmail_UIDs)}"

                self.textBrowser.append(str(self.content))

            # Hotmail
            elif self.internet_connection() and self.auto_detect_mail() is 'hotmail':

                self.hotmail_imap_Object.select_folder('INBOX', readonly=False)
                for link in self.deleted_mailes:
                    search = "FROM {}".format(link)
                    self.hotmail_UIDs = self.hotmail_imap_Object.search(search)
                    print(self.hotmail_UIDs)

                    for i in self.hotmail_UIDs:
                        self.content = f"FROM: {self.deleted_mailes[-1]},  MESSAGES = {len(self.hotmail_UIDs)}"

                print(self.deleted_mailes)
                self.textBrowser.append(str(self.content))

            else:
                if self.internet_connection():
                    self.label_mailinfo.setText("Write Valid Mail")
                    print("Unknown email Or wrong email")

        except:
            # self.label_mailinfo.setText("please select\nyour email type")
            # self.label_emailconfirmed.setText("choose mail")
            print("Unknown email")
            return False

    #  --------------------New--------------------
    def delete_messages(self):  # take mails in the list and delete it if it isn't empty
        # connect progressbar to delete messages and delete all messages stored in textBrowser
        if len(self.deleted_mailes) > 0:
            if self.auto_detect_mail() is 'gmail':
                for link in self.deleted_mailes:
                    from_search = "FROM {}".format(link)
                    self.after_gmail_UIDs = self.gmail_imap_Object.search(from_search)
                    for i in self.after_gmail_UIDs:
                        self.gmail_imap_Object.delete_messages(i)
                self.label_mailinfo.setText("Process Finished")
                return True

            elif self.auto_detect_mail() is 'yahoo':
                for link in self.deleted_mailes:
                    from_search = "FROM {}".format(link)
                    self.after_yahoo_UIDs = self.yahoo_imap_Object.search(from_search)
                    for i in self.after_yahoo_UIDs:
                        self.yahoo_imap_Object.delete_messages(i)
                self.label_mailinfo.setText("Process Finished")
                return True

            elif self.auto_detect_mail() is 'hotmail':
                for link in self.deleted_mailes:
                    from_search = "FROM {}".format(link)
                    self.after_hotmail_UIDs = self.hotmail_imap_Object.search(from_search)
                    for i in self.after_hotmail_UIDs:
                        self.hotmail_imap_Object.delete_messages(i)
                self.label_mailinfo.setText("Process Finished")
                return True

        else:
            # NOTHING TO DELETE
            return False

    # TODO: LOGOUT BEFORE YOY CLOSE THE APP
    def close_app_exit(self):
        # try to logout Before EXIT
        # ---------------

        # EXIT
        self.button_exit.clicked.connect(sys.exit(0))

    # TODO: TRY TO ADD ARABIC EDITION , SELECT LANGUAGE
    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "Mail Cleaner"))
        self.label_mailer.setText(_translate("Main_Window", "E-mail From"))
        self.button_addmail.setText(_translate("Main_Window", "Add mail to list"))
        self.label_emailslistname.setText(_translate("Main_Window", "Emails You will delete"))
        self.label_progress.setText(_translate("Main_Window", "Progress"))
        self.button_exit.setText(_translate("Main_Window", "EXIT"))
        self.button_delete.setText(_translate("Main_Window", "Delete"))
        self.label_email.setText(_translate("Main_Window", "Your Mail"))
        self.label_password.setText(_translate("Main_Window", "Your PassWord"))
        self.label_mailinfo.setText(_translate("Main_Window", "information about activate mail"))
        self.label_emailconfirmed.setText(_translate("Main_Window", "Please Login"))
        self.button_login.setText(_translate("Main_Window", "Login"))
        self.textBrowser.setHtml(_translate("Main_Window",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())
