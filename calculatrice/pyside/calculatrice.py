from PySide import QtCore, QtGui
from functools import partial
from custom_ui.fenetrePrincipale import Ui_form_calculatrice

class Calculatrice(Ui_form_calculatrice, QtGui.QWidget):
	def __init__(self):
		super(Calculatrice, self).__init__()

		# Init Window

		self.setupUi(self)
		self.modificationSetupUi()
		self.setupConnections()
		self.setupRaccourcisClaviers()
		self.show()

	
	def modificationSetupUi(self):

		self.btns_nombres = []

		for i in range(self.gridLayout.count()):
			widget = self.gridLayout.itemAt(i).widget()

			if isinstance(widget, QtGui.QPushButton) and widget.text().isdigit():
				self.btns_nombres.append(widget)



	def setupConnections(self):
		for btn in self.btns_nombres:
			btn.clicked.connect(partial(self.btnNombrePressed, str(btn.text())))

		self.btn_moins.clicked.connect(partial(self.btnOperationPressed, str(self.btn_moins.text())))
		self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
		self.btn_mult.clicked.connect(partial(self.btnOperationPressed, str(self.btn_mult.text())))
		self.btn_div.clicked.connect(partial(self.btnOperationPressed, str(self.btn_div.text())))

		self.btn_egal.clicked.connect(self.calculOperation)
		self.btn_c.clicked.connect(self.supprimerResultat)


	def setupRaccourcisClaviers(self):
		# On fait une boucle de 0 a 9 pour passer a travers les boutons de nombres
		for btn in range(10):
			# On cree un shortcut pour chaque bouton
			QtGui.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.btnNombrePressed, str(btn)))

		# On cree plusieurs shortcuts pour les boutons d'operation
		QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_plus.text())), self, partial(self.btnOperationPressed, str(self.btn_plus.text())))
		QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_moins.text())), self, partial(self.btnOperationPressed, str(self.btn_moins.text())))
		QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_mult.text())), self, partial(self.btnOperationPressed, str(self.btn_mult.text())))
		QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_div.text())), self, partial(self.btnOperationPressed, str(self.btn_div.text())))
		
		# On cree d'autres shortcuts pour l'application en general
		QtGui.QShortcut(QtGui.QKeySequence('Enter'), self, self.calculOperation)
		QtGui.QShortcut(QtGui.QKeySequence('Del'), self, self.supprimerResultat)
		QtGui.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)


	def btnNombrePressed(self, bouton):
		"""Fonction activee quand l'utilisateur appuie sur un numero (0-9)"""

		# On recupere le texte dans le LineEdit resultat
		resultat = str(self.le_resultat.text())

		if resultat == '0':
			# Si le resultat est egal a 0 on met le nombre du bouton
			# que l'utilisateur a presse dans le LineEdit resultat
			self.le_resultat.setText(bouton)
		else:
			# Si le resultat contient autre chose que zero,
			# On ajoute le texte du bouton a celui dans le LineEdit resultat
			self.le_resultat.setText(resultat + bouton)

	def btnOperationPressed(self, operation):
		"""
		Fonction activee quand l'utilisateur appuie sur 
		une touche d'operation (+, -, /, *)
		"""

		# On recupere le texte dans le LineEdit operation
		operationText = str(self.le_operation.text())
		# On recupere le texte dans le LineEdit resultat
		resultat = str(self.le_resultat.text())

		# On additionne l'operation en cours avec le texte dans le resultat
		# et on ajoute a la fin le signe de l'operation qu'on a choisie
		self.le_operation.setText(operationText + resultat + operation)
		# On reset le texte du LineEdit resultat
		self.le_resultat.setText('0')

	def supprimerResultat(self):
		"""On reset le texte des deux LineEdit"""

		self.le_resultat.setText('0')
		self.le_operation.setText('')

	def calculOperation(self):
		"""On calcule le resultat de l'operation en cours (quand l'utilisateur appuie sur egal)"""

		# On recupere le texte dans le LineEdit resultat
		resultat = str(self.le_resultat.text())

		# On ajoute le nombre actuel dans le LineEdit resultat
		# au LineEdit operation
		self.le_operation.setText(self.le_operation.text() + resultat)
		
		# On evalue le resultat de l'operation
		resultatOperation = eval(str(self.le_operation.text()))
		
		# On met le resultat final dans le LineEdit resultat
		self.le_resultat.setText(str(resultatOperation))


app = QtGui.QApplication([])
fenetre = Calculatrice()
app.exec_()