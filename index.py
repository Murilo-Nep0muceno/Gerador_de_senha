from PyQt5 import uic,QtWidgets
import mysql.connector
import random


def funcao_principal():
  linha=formulario.lineEdit.text()
  linha2=formulario.lineEdit_2.text()
  min="abcdefghijklmnopqrstuvwxyz"
  mai="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  num="1234567890"
  symbols="!@#$%&*?\/"
  use = mai + min + num + symbols
  password="".join(random.sample(use, int(linha)))
  formulario.label_4.setText(linha2)
  formulario.label_5.setText(password + "fdsafdsafsd:" )

  print(linha2, ":" , password)



app= QtWidgets.QApplication([])
formulario=uic.loadUi("tela_1.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
