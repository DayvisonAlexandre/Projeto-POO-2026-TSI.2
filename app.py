import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Demonstração PySide6")

    janela = QWidget()
    janela.setWindowTitle("PySide6 no GitHub Codespaces")
    janela.resize(420, 200)
    janela.setMinimumSize(360, 160)

    rotulo = QLabel("Olá do GitHub Codespaces!")
    rotulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

    botao = QPushButton("Clique Aqui")
    botao.setMinimumHeight(36)

    botao.clicked.connect(
        lambda: rotulo.setText("PySide6 funcionando!\nSinal e slot executados com sucesso.")
    )

    layout = QVBoxLayout()
    layout.setContentsMargins(24, 24, 24, 24)
    layout.setSpacing(18)
    layout.addWidget(rotulo)
    layout.addWidget(botao)
    janela.setLayout(layout)

    janela.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())