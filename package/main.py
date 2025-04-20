#!/usr/bin/env python

import markdown
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QFileDialog, QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView

def GetHTML(htmlFile):
    with open(htmlFile, "r") as f:
        markdown_text = f.read()

    html_content = markdown.markdown(
        markdown_text,
        extensions=["fenced_code", "codehilite"]
    )

    with open("style.css", "r") as f:
        html_content = "<style>" + f.read() + "</style>" + html_content

    return html_content

class InitialView(QWidget):
    def __init__(self, on_file_selected):
        super().__init__()
        layout = QVBoxLayout(self)

        self.button = QPushButton("Open File")
        self.button.clicked.connect(self.open_file)

        layout.addWidget(self.button)
        self.on_file_selected = on_file_selected

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select a file")
        if path:
            print("Selected file:", path)
            self.on_file_selected(path)

class HTMLView(QWebEngineView):
    def __init__(self, path):
        super().__init__()
        self.setHtml(GetHTML(path))

class MainWindow(QMainWindow):
    def __init__(self, arg):
        super().__init__()
        self.setWindowTitle("Markdown viewer")
        self.resize(800, 900)

        if  arg != None and arg != "":
            self.html_view = HTMLView(arg)
            self.setCentralWidget(self.html_view)
        else:
            self.initial_view = InitialView(self.show_html_view)
            self.setCentralWidget(self.initial_view)

    def show_html_view(self, file_path):
        self.html_view = HTMLView(file_path)
        self.setCentralWidget(self.html_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        window = MainWindow(sys.argv[1])
    else:
        window = MainWindow(None)
    
    window.show()
    sys.exit(app.exec())