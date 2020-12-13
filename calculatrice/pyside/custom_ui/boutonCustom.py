from PySide import QtGui

CUSTOM_FONT = QtGui.QFont()
CUSTOM_FONT.setPointSize(14)

class BoutonCustom(QtGui.QPushButton):

	def __init__(self, texte):
		super(BoutonCustom, self).__init__(texte)

		self.setFont(CUSTOM_FONT)
		self.setStyleSheet('QPushButton:hover {color: rgb(100, 200, 130);}')

