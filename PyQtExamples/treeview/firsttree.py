from PyQt5.QtWidgets import *
import sys

class FirstTree(QWidget):
    """
    Пример создания простого QTreeWidget
    """
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)

        champs = [["Тон Сейбрандс", "1972"],
                  ["Харм Вирсма", "1976"],
                  ["Анатолий Гантварг", "1978"],
                  ["Александр Дыбман", "1986"],
                  ["Алексей Чижов", "1988"]]

        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderLabels(["ФИО", "Год"])

        for item in champs:
            champ = QTreeWidgetItem(item)
            self.treeWidget.addTopLevelItem(champ)
        
        self.treeWidget.resizeColumnToContents(0)

        layout.addWidget(self.treeWidget)



app = QApplication(sys.argv)

screen = FirstTree()
screen.show()

sys.exit(app.exec_())



