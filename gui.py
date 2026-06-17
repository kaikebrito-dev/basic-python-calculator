import sys
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QWidget, QPushButton,
                              QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit)    
                    
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.resize(300, 400)

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        grid = QGridLayout()
        main_layout.addLayout(grid)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 12px;")
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            grid.addWidget(button, row, col)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def on_button_click(self, text):
        if text == "C":
            self.display.clear()
            return
        elif text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText("Erro")
        else:
            current = self.display.text()
            self.display.setText(current + text)


app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
