class Button:
    def __init__(self,GUI):
        self.GUI = GUI
    def setClickEvent(self,function):
        self.GUI.clicked.connect(function)
class Label:
    def __init__(self, GUI):
        self.GUI = GUI
    def setText(self,msg):
        self.GUI.setText(msg)
    def getText(self, msg):
        self.GUI.setText(msg)