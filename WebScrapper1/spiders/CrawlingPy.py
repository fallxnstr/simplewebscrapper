from PyQt5 import QtCore, QtGui, QtWidgets
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os




class CrawlingSpider(CrawlSpider):
    name = "myCrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"),  callback="parse_item")

    )

    def parse_item(self, response):
        yield {
            "Title": response.css(".product_main h1::text").get(),
            "Price": response.css(".price_color::text").get(),
            "Availablity": response.css(".availability::text")[1].get().replace("\n", "").replace(" ", "").replace("Instock", "").replace("(", "").replace(")", " ").replace("available", "").strip(),
            "Rating": response.css(".star-rating::attr(class)").get().replace("star-rating", "").strip()

        }

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(120, 270, 260, 120))
        self.Start.clicked.connect(self.startClicked)
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Start.setFont(font)
        self.Start.setObjectName("Start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 500, 250))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Json = QtWidgets.QPushButton(self.centralwidget)
        self.Json.setGeometry(QtCore.QRect(430, 270, 260, 120))
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Json.setFont(font)
        self.Json.setObjectName("Json")
        self.Json.clicked.connect(self.jsonClicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def startClicked(self):
        os.system('cmd /c "cd.. & scrapy crawl myCrawler -o output.json"')
        self.label.setText("Done Scraping!")

    def jsonClicked(self):
        path = r'C:\Users\Fallxnstr\PycharmProjects\WebScrapper\WebScrapper1\WebScrapper1\output.json'
        path = os.path.realpath(path)
        os.startfile(path)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scrapper 2.0"))
        self.Start.setText(_translate("MainWindow", "Start Scrapping"))
        self.label.setText(_translate("MainWindow", "Welcome to the WebScrapper 2.0!"))
        self.Json.setText(_translate("MainWindow", "Open JSON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
