"""
Tkinter is used for the basic GUI
"""
from Tkinter import *
import  subprocess

import Tkinter
rootWindow = Tk()
rootWindow.title("GuiTesting")
rootWindow.geometry("600x400")#width = 600 height 400
#rootWindow.mainloop()

# This frame in which frame I want The new Frame to be in rootWindow Frame
# to give 3D effect use relief property
frObj = Frame(rootWindow, width=400, height=300, bg='yellow', relief=RAISED, borderwidth=5)
frObj.pack()# To add the frame to the window
frObj.pack_propagate(False) # Else the frame will grow or shrink

labelObj = Label(frObj, text="Welcome to Python training")
labelObj.pack()

userTextboxObj = Entry(frObj)
userTextboxObj.pack()
# After click the code to execute put it into a func

def buttonClick():
    print 'Button clicked' # This is printed in the console
    #msgObj = Message(frObj, text="You have submitted!") Uncomment this to just print this hardcoded text
    userInputText = userTextboxObj.get()
    msgObj = Message(frObj, text= "Hi " + userInputText + " !")
    msgObj.pack()

btnObj = Button(frObj, text="Submit", command=buttonClick) # after user click the btn then this func buttonClick() is called
btnObj.pack()


userTextboxIpObj = Entry(frObj)
userTextboxIpObj.pack()

def buttonClickPrintIP():
    print 'Button clicked'
    ipAddr = userTextboxIpObj.get()
    # Sending Ip Addr as input to the process
    #-c 3 implies print only 3 counts
    pingOutIpput = subprocess.check_output(['ping' ,ipAddr], shell=True)

    msgIPObj = Message(frObj, text= "Ip =  " + pingOutIpput + " !")
    msgIPObj.pack()


btnPingObj = Button(frObj, text="GetIP", command=buttonClickPrintIP)
btnPingObj.pack()





rootWindow.mainloop()






