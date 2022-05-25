from MainHandle.InMainGUI import *
class SCode_01(InMainGUI):
    def __init__(self,GUI):
        super().__init__(GUI)
        self.Main_Button_Test.setClickEvent(lambda : self.Click())
        pass

    def Click(self):
        print("버튼클릭")



