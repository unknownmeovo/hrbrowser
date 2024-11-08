import sys 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *
import os #this module is very dangerous 😂😂😂


class MainWindow(QMainWindow):  #create a window for browser
    def __init__(self): 
        super(MainWindow, self).__init__() 
        self.browser = QWebEngineView() 
        self.browser.setUrl(QUrl.fromLocalFile(os.path.abspath("hrbrowser.html")))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        self.setWindowIcon(QIcon("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5txJu_m76YGWYHN-ZO78YDIfgxSgAJhRubg&s"))

        #navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #back button
        backBtn = QAction('Back', self)
        backBtn.triggered.connect(self.browser.back)
        navbar.addAction(backBtn)

        #forward button
        forwardBtn = QAction('Forward', self)
        forwardBtn.triggered.connect(self.browser.back)
        navbar.addAction(forwardBtn)

        #refresh button
        refreshBtn = QAction('Refresh', self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #home button
        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.navigate_home)
        navbar.addAction(homeBtn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.url_update)

    def navigate_home(self):
        self.browser.setUrl(QUrl.fromLocalFile(os.path.abspath("hrbrowser.html")))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def url_update(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationDisplayName('HR Browser')
window = MainWindow()
app.exec_() #app will execute here.