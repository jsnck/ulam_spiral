from math import sqrt
import wx 
 
###############################
########### ulam spiral #######
###############################

app = wx.App() 

#####size of window#####
#get size of display
width, height = wx.GetDisplaySize()
#set window size
windowWidth = width*0.6
windowHeight = height*0.6

#####variables#####
#fix
direction = 0 #0=start, 1=rigth, 2=up, 3=left, 4=down
curPosX = (windowWidth/2)
curPosY = (windowHeight/2)
stepCounter = 1
tmpCounter = 0
iteration = 0

#change here number of steps and range
numberRange = 100000
step = (windowWidth/numberRange) + 1

#####application#####
#create window
window = wx.Frame(None, title = "wxPython Frame", size = (windowWidth,windowHeight))
panel = wx.Panel(window)

#function to check if current number is prime
def check_Prime(i):
    if(i > 1):
        for j in range(2, i-1):
            if i % j == 0:
                 return False
        return True
    return False


#print spiral
for i in range (1, numberRange+1):
    
    if direction == 1: #rigth
        curPosX = curPosX + step
    elif direction == 2: #up
        curPosY = curPosY - step
    elif direction == 3: #left
        curPosX = curPosX - step
    elif direction == 4: #down
        curPosY = curPosY + step
    
    #print current number if its prime
    if(check_Prime(i) == True):
        label = wx.StaticText(panel, label = ".", pos = (curPosX,curPosY))
    
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


#to-do
    #performance
    #change variables in application (step number, number of values, displayed char)
    #as new project in git
    #zoom?
    #
            
#main loop 
window.Show(True) 
app.MainLoop()