#import
from math import sqrt
import wx 

#import functions
from check_prime import check_Prime
 
###############################
########### ulam spiral #######
###############################

class MainWindow(wx.Frame):

    def __init__(self, parent, title):

        ######size of window#####
        ##get size of display
        width, height = wx.GetDisplaySize()
        ##set window size
        self.windowWidth = width*0.6
        self.windowHeight = height*0.6

        #####variables#####
        ##change here number of steps and range
        self.numberRange = 10000
        self.curPosX = (self.windowWidth/2)
        self.curPosY = (self.windowHeight/2)
        self.step = (self.windowWidth/self.numberRange) + 1

        #create Window
        wx.Frame.__init__(self, None, title=title,size=(self.windowWidth,self.windowHeight))
        self.panel = wx.Panel(self) 
        
        #toolbar
        tb = wx.ToolBar( self, -1,) 
        self.ToolBar = tb

        #button to print the spiral
        self.print = wx.Button(tb,-1,"print the spiral", size =(self.windowWidth/3, 50))
        self.print.Bind(wx.EVT_BUTTON,self.getUserInput)

        #input fields
        self.spiralSize = wx.TextCtrl(tb, size=(150,50))
        self.spiralSize.SetHint('Set size of the spiral')

        #set char
        self.chooseChar = wx.Choice(tb, wx.ID_ANY, choices=[("."), ("'"), ("*")])
        self.chooseChar.SetSelection(0)

        #add controls to toolbar and show toolbar
        tb.AddControl(self.spiralSize)
        tb.AddControl(self.chooseChar)
        tb.AddControl(self.print) 
        #tb.SetToolBitmapSize(size =(60, 60))
        tb.Realize()  
        
        #show created frame
        self.Show()

    #get the user input of the spiral size and call the print function
    def getUserInput(self, event):
        self.numberRange = int(self.spiralSize.GetValue())
        self.chosenChar = self.chooseChar.GetString(self.chooseChar.GetSelection())
        self.resetSpiral(self)

    #delete the last drawn spiral and reset positions
    def resetSpiral(self, event):
        print("reset last drawn spiral")
        #reset position
        self.curPosX = (self.windowWidth/2)
        self.curPosY = (self.windowHeight/2)
        #delete old spiral

        #print new spiral
        self.printSpiral(self, self.chosenChar)

    def printSpiral(self, event, char):
        ###variables###
        #fix
        direction = 0 #0=start, 1=rigth, 2=up, 3=left, 4=down
        stepCounter = 1
        tmpCounter = 0
        iteration = 0

        ##print spiral
        for i in range (1, self.numberRange+1):
        
            if direction == 1: #rigth
                self.curPosX = self.curPosX + self.step
            elif direction == 2: #up
                self.curPosY = self.curPosY - self.step
            elif direction == 3: #left
                self.curPosX = self.curPosX - self.step
            elif direction == 4: #down
                self.curPosY = self.curPosY + self.step
            
            #print current number if its prime
            if(check_Prime(i) == True):
                label = wx.StaticText(self.panel, label = char, pos = (self.curPosX,self.curPosY))
            
            tmpCounter = tmpCounter + 1
            iteration = iteration + 1
        
            #check if all steps are made 
            if tmpCounter < stepCounter:
                tmpCounter = tmpCounter + 1
            #if all steps are made, change direction
            else:
                #change direction
                if direction == 0: direction = 1
                elif direction < 4: direction = direction + 1 
                else: direction = 1
                #check if second iteration is done
                if (iteration > 2): 
                    stepCounter = stepCounter + 1
                    tmpCounter = 0
                    iteration = 1

app = wx.App()
frame = MainWindow(None, "Ulam Spiral")
app.MainLoop()