import sys

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("PySide6 no Codespaces")
janela.resize(300, 150)

layout = QVBoxLayout()
rotulo = QLabel("Olá do GitHub Codespaces!")
botao = QPushButton("Clique Aqui")
botao.clicked.connect(lambda: rotulo.setText("PySide6 funcionando!"))

layout.addWidget(rotulo)
layout.addWidget(botao)
janela.setLayout(layout)

janela.show()
sys.exit(app.exec())