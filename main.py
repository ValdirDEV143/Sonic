import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from sonic import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Sonic.clicked.connect(lambda: self.alterar_imagem("Sonic"))
        self.ui.pushButton_Tails.clicked.connect(lambda: self.alterar_imagem("Tails"))
        self.ui.pushButton_Knuckles.clicked.connect(lambda: self.alterar_imagem("Knuckles"))
        self.ui.pushButton_Amy.clicked.connect(lambda: self.alterar_imagem("Amy"))
        self.ui.pushButton_Eggman.clicked.connect(lambda: self.alterar_imagem("Eggman"))
        self.ui.pushButton_Shadow.clicked.connect(lambda: self.alterar_imagem("Shadow"))

    def alterar_imagem(self, nome_do_personagem):
        caminho_iamgem = {
            "Sonic": "Imagem/Sonic.png",
            "Tails": "Imagem/Tails.png",
            "Knuckles": "Imagem/Knuckles.png",
            "Amy": "Imagem/Amy.png",
            "Eggman": "Imagem/Eggman.webp",
            "Shadow": "Imagem/Shadow.png",
        }

        if nome_do_personagem in caminho_iamgem:
            pixmap = QPixmap(caminho_iamgem[nome_do_personagem])
            self.ui.label_PersonagemSelecionado.setPixmap(pixmap)
            self.ui.label_PersonagemSelecionado.setScaledContents(True)
        else:
            print(f"Imagem para {nome_do_personagem}")    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
