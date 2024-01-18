#from PIL import Image (don't require this module every time)
import PySimpleGUI as sg
import pandas as pd
import csv
import time
import os 

#setting theme of gui
sg.theme('Dark Teal 5')

#Defines each mode
from AOO import *
from VOO import *
from AAI import * 
from VVI import *
from AAIR import *
from VVIR import *
from AOOR import *
from VOOR import *
from DOO import *
from DOOR import *
from serialComm import *
from graphing import *

global parametersList

#Default Values
atriNone = AOO("",0,0,0,0)
ventriNone = VOO("",0,0,0,0)
atriInhi = AAI("",0,0,0,0,0,0,0)
ventriInhi = VVI("",0,0,0,0,0,0)
dualNone = DOO("",0,0,0,0,0,0,0)
dualRate = DOOR("",0,0,0,0,0,0,0,0,"",0,0,0)
atriNoneNoneRate = AOOR("",0,0,0,0,0,"",0,0,0)
atriAtriInhiRate = AAIR("",0,0,0,0,0,0,0,0,"",0,0,0)
ventriNoneNoneRate = VOOR("",0,0,0,0,0,"",0,0,0)
ventriVentriInhiRate = VVIR("",0,0,0,0,0,0,0,"",0,0,0)
def get_WD(file_directory):
    pwd = os.getcwd()
    pwd = pwd + '/' + file_directory + '/'
    return pwd

def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key, visible=False))

def dcm_UpdateParam(username):  #updates paramters
    df = pd.DataFrame({'P1':[atriNone.LRL,ventriNone.LRL,atriInhi.LRL,ventriInhi.LRL,dualNone.LRL,dualRate.LRL,atriNoneNoneRate.LRL,atriAtriInhiRate.LRL,ventriNoneNoneRate.LRL,ventriVentriInhiRate.LRL],  #First column
                       'P2':[atriNone.URL,ventriNone.URL,atriInhi.URL,ventriInhi.URL,dualNone.URL,dualRate.URL,atriNoneNoneRate.URL,atriAtriInhiRate.URL,ventriNoneNoneRate.URL,ventriVentriInhiRate.URL],  #Second column
                       'P3':[atriNone.AA,ventriNone.VA,atriInhi.AA,ventriInhi.VA,dualNone.FAVD,dualRate.FAVD,atriNoneNoneRate.AA,atriAtriInhiRate.AA,ventriNoneNoneRate.VA,ventriVentriInhiRate.VA],      #and so on
                       'P4':[atriNone.APW,ventriNone.VPW, atriInhi.APW, ventriInhi.VPW,dualNone.AA,dualRate.AA,atriNoneNoneRate.APW,atriAtriInhiRate.APW,ventriNoneNoneRate.VPW,ventriVentriInhiRate.VPW],
                       'P5':[" "," ",atriInhi.AS, ventriInhi.VS,dualNone.VA,dualRate.VA,atriNoneNoneRate.MSR,atriAtriInhiRate.AS,ventriNoneNoneRate.MSR,ventriVentriInhiRate.VS],
                       'P6':[" "," ",atriInhi.ARP,ventriInhi.VRP,dualNone.APW, dualRate.APW,atriNoneNoneRate.AT,atriAtriInhiRate.ARP,ventriNoneNoneRate.AT,ventriVentriInhiRate.VRP],
                       'P7':[" "," ",atriInhi.PVARP," ",dualNone.VPW, dualRate.VPW,atriNoneNoneRate.ReaT,atriAtriInhiRate.PVARP,ventriNoneNoneRate.ReaT,ventriVentriInhiRate.MSR],
                       'P8':[" "," "," "," "," ", dualRate.MSR,atriNoneNoneRate.ResF,atriAtriInhiRate.MSR,ventriNoneNoneRate.ResF,ventriVentriInhiRate.AT],
                       'P9':[" "," "," "," "," ", dualRate.AT,atriNoneNoneRate.RecT,atriAtriInhiRate.AT,ventriNoneNoneRate.RecT,ventriVentriInhiRate.ReaT],
                       'P10':[" "," "," "," "," ", dualRate.ReaT," ",atriAtriInhiRate.ReaT," ",ventriVentriInhiRate.ResF],
                       'P11':[" "," "," "," "," ", dualRate.ResF," ",atriAtriInhiRate.ResF," ",ventriVentriInhiRate.RecT],
                       'P12':[" "," "," "," "," ", dualRate.RecT," ",atriAtriInhiRate.RecT," "," "],
   })
    #first row is AOO
    #second row is VOO
    #third row is AAI
    #fourth row is VVI
    #fifth row is DOO
    #sixth row is DOOR
    #seventh row is AOOR
    #eight row is AAIR
    #ninth row is VOOR
    #tenth row is VVIR

    df.to_csv("Database_CSV/" + str(username) + ".csv", index=False)#updates the csv file

def dcm_pacingModeDir():
    #symbol for collapsable gui
    SYMBOL_UP =    '▲'
    SYMBOL_DOWN =  '▼'
    index  = 0 #Used to determine which state we are in
    #The following set_from_csv functions are used to obtian values from the user's file for each mode
    atriNone.set_from_csv()
    ventriNone.set_from_csv()
    atriInhi.set_from_csv()
    ventriInhi.set_from_csv()
    dualNone.set_from_csv()
    dualRate.set_from_csv()
    atriNoneNoneRate.set_from_csv()
    atriAtriInhiRate.set_from_csv()
    ventriNoneNoneRate.set_from_csv()
    ventriVentriInhiRate.set_from_csv()
   
    dropdown_section = [[sg.Text(size=(40,1), key='out1')],                 #Output lines for each pacing mode
        [sg.Text(size=(40,1), key='out2')],
        [sg.Text(size=(40,1), key='out3')],
        [sg.Text(size=(40,1), key='out4')],
        [sg.Text(size=(40,1), key='out5')],
        [sg.Text(size=(40,1), key='out6')],
        [sg.Text(size=(40,1), key='out7')],
        [sg.Text(size=(40,1), key='out8')],
        [sg.Text(size=(40,1), key='out9')],
        [sg.Text(size=(40,1), key='out10')],
        [sg.Text(size=(40,1), key='out11')],
        [sg.Text(size=(40,1), key='out12')],
        [sg.Text(size=(40,1), key='out13')]]
   
   
    layout = [
        [sg.Text("Please choose your state")],
        [sg.Button('AOO'), sg.Button('VOO'), sg.Button('AAI'), sg.Button('VVI'), sg.Button('DOO'), sg.Button('DOOR'), sg.Button('AOOR'), sg.Button('AAIR'), sg.Button('VOOR'), sg.Button('VVIR')], #These are used to change Pacing mode
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), sg.T('Parameters', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
        [collapse(dropdown_section, '-SEC1-')],
        [sg.Button('Generate_EGRAM'),sg.Button('Change_Values'), sg.Button('Quit')]     #Used to change values and quit
        ]
    window = sg.Window("Pacing Modes", layout,font=('Helvetica',14), element_justification = 'c')
    opened_dropdown = False
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event.startswith('-OPEN SEC1-'):
            opened_dropdown = not opened_dropdown
            window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
            window['-SEC1-'].update(visible=opened_dropdown)

        if event == "AOO":  #Displays mode AOO
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing AOO')
            window['out2'].update('LRL is ' + str(atriNone.LRL) + " ppm")
            window['out3'].update('URL is ' + str(atriNone.URL) + " ppm")
            window['out4'].update('Amplitude is ' + str(atriNone.AA) + " V")
            window['out5'].update('Pulse Width is ' + str(atriNone.APW) + " ms")
            window['out6'].update('')
            window['out7'].update('')
            window['out8'].update('')

            window['out9'].update('')
            window['out10'].update('')
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')
            index = 1
            pacemaker_serial_comm(parametersList_AOO)
            
        if event == "VOO":  #Displays mode VOO
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing VOO')
            window['out2'].update('LRL is ' + str(ventriNone.LRL) + " ppm")
            window['out3'].update('URL is ' + str(ventriNone.URL) + " ppm")
            window['out4'].update('Amplitude is ' + str(ventriNone.VA) + " V")
            window['out5'].update('Pulse Width is ' + str(ventriNone.VPW) + " ms")
            window['out6'].update('')
            window['out7'].update('')
            window['out8'].update('')
            
            window['out9'].update('')
            window['out10'].update('')
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')
            index = 2
            pacemaker_serial_comm(parametersList_VOO)

        if event == "AAI":  #Displays mode AAI
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing AAI')
            window['out2'].update('LRL is ' + str(atriInhi.LRL) + " ppm")
            window['out3'].update('URL is ' + str(atriInhi.URL) + " ppm")
            window['out4'].update('Amplitude is ' + str(atriInhi.AA) + " V")
            window['out5'].update('Pulse Width is ' + str(atriInhi.APW) + " ms")
            window['out6'].update('Sensitivity is ' + str(atriInhi.AS) + " mV")
            window['out7'].update('Refactory Period is ' + str(atriInhi.ARP) + " ms")
            window['out8'].update('PVARP is ' + str(atriInhi.PVARP) + " ms")
            
            window['out9'].update('')
            window['out10'].update('')
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')
            index = 3
            pacemaker_serial_comm(parametersList_AAI)

        if event == "VVI":  #Displays mode VVI
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing VVI')
            window['out2'].update('LRL is ' + str(ventriInhi.LRL) + " ppm")
            window['out3'].update('URL is ' + str(ventriInhi.URL) + " ppm")
            window['out4'].update('Amplitude is ' + str(ventriInhi.VA) + " V")
            window['out5'].update('Pulse Width is ' + str(ventriInhi.VPW) + " ms")
            window['out6'].update('Sensitivity is ' + str(ventriInhi.VS) + " mV")
            window['out7'].update('Refactory Period is ' + str(ventriInhi.VRP) + " ms")
            window['out8'].update('')
            
            window['out9'].update('')
            window['out10'].update('')
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')
            index = 4
            pacemaker_serial_comm(parametersList_VVI)

        if event == "DOO":  #Displays mode DOO
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing DOO')
            window['out2'].update('LRL is ' + str(dualNone.LRL) + " ppm")
            window['out3'].update('URL is ' + str(dualNone.URL) + " ppm")
            window['out4'].update('Fixed AV Delay is ' + str(dualNone.FAVD) + " ms")
            window['out5'].update('Atrial Amplitude is ' + str(dualNone.AA) + " V")
            window['out6'].update('Ventricular Amplitude is ' + str(dualNone.VA) + " V")
            window['out7'].update('Atrial Pulse Width is ' + str(dualNone.APW) + " ms")
            window['out8'].update('Ventricular Pulse Width is ' + str(dualNone.VPW) + " ms")
            
            window['out9'].update('')
            window['out10'].update('')
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')
            index = 5
            pacemaker_serial_comm(parametersList_DOO)

        if event == "DOOR":  #Displays mode DOOR
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing DOOR')
            window['out2'].update('LRL is ' + str(dualRate.LRL) + " ppm")
            window['out3'].update('URL is ' + str(dualRate.URL) + " ppm")
            window['out4'].update('Fixed AV Delay is ' + str(dualRate.FAVD) + " ms")
            window['out5'].update('Atrial Amplitude is ' + str(dualRate.AA) + " V")
            window['out6'].update('Ventricular Amplitude is ' + str(dualRate.VA) + " V")
            window['out7'].update('Atrial Pulse Width is ' + str(dualRate.APW) + " ms")
            window['out8'].update('Ventricular Pulse Width is ' + str(dualRate.VPW) + " ms")

            window['out9'].update('Maximum Sensor Rate is ' + str(dualRate.MSR) + " ppm")
            window['out10'].update('Activity Threshold is ' + str(dualRate.AT))
            window['out11'].update('Reaction Time is ' + str(dualRate.ReaT) + "s")
            window['out12'].update('Response Factor is ' + str(dualRate.ResF))
            window['out13'].update('Recovery Time is ' + str(dualRate.RecT) + "min")
            index = 6
            pacemaker_serial_comm(parametersList_DOOR)

        if event == "AOOR":  #Displays mode AOOR
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing AOOR')
            window['out2'].update('LRL is ' + str(atriNoneNoneRate.LRL) + " ppm")
            window['out3'].update('URL is ' + str(atriNoneNoneRate.URL) + " ppm")
            window['out4'].update('Atrial Amplitude is ' + str(atriNoneNoneRate.AA) + " V")
            window['out5'].update('Atrial Pulse Width is ' + str(atriNoneNoneRate.APW) + " ms")

            window['out6'].update('Maximum Sensor Rate is ' + str(atriNoneNoneRate.MSR) + " ppm")
            window['out7'].update('Activity Threshold is ' + str(atriNoneNoneRate.AT))
            window['out8'].update('Reaction Time is ' + str(atriNoneNoneRate.ReaT) + "s")
            window['out9'].update('Response Factor is ' + str(atriNoneNoneRate.ResF))
            window['out10'].update('Recovery Time is ' + str(atriNoneNoneRate.RecT) + "min")
            
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')
            index = 7
            pacemaker_serial_comm(parametersList_AOOR)

        if event == "AAIR":  #Displays mode AAIR
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing AAIR')
            window['out2'].update('LRL is ' + str(atriAtriInhiRate.LRL) + " ppm")
            window['out3'].update('URL is ' + str(atriAtriInhiRate.URL) + " ppm")
            window['out4'].update('Atrial Amplitude is ' + str(atriAtriInhiRate.AA) + " V")
            window['out5'].update('Atrial Pulse Width is ' + str(atriAtriInhiRate.APW) + " ms")

            window['out6'].update('Sensitivity is ' + str(atriAtriInhiRate.AS) + " mV")
            window['out7'].update('Refactory Period is ' + str(atriAtriInhiRate.ARP) + " ms")
            window['out8'].update('PVARP is ' + str(atriAtriInhiRate.PVARP) + " ms")

            window['out9'].update('Maximum Sensor Rate is ' + str(atriAtriInhiRate.MSR) + " ppm")
            window['out10'].update('Activity Threshold is ' + str(atriAtriInhiRate.AT))
            window['out11'].update('Reaction Time is ' + str(atriAtriInhiRate.ReaT) + "s")
            window['out12'].update('Response Factor is ' + str(atriAtriInhiRate.ResF))
            window['out13'].update('Recovery Time is ' + str(atriAtriInhiRate.RecT) + "min")
            index = 8
            pacemaker_serial_comm(parametersList_AAIR)

        if event == "VOOR":  #Displays mode VOOR
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing VOOR')
            window['out2'].update('LRL is ' + str(ventriNoneNoneRate.LRL) + " ppm")
            window['out3'].update('URL is ' + str(ventriNoneNoneRate.URL) + " ppm")
            window['out4'].update('Ventricular Amplitude is ' + str(ventriNoneNoneRate.VA) + " V")
            window['out5'].update('Ventricular Pulse Width is ' + str(ventriNoneNoneRate.VPW) + " ms")
            window['out6'].update('Maximum Sensor Rate is ' + str(ventriNoneNoneRate.MSR) + " ppm")
            window['out7'].update('Activity Threshold is ' + str(ventriNoneNoneRate.AT))
            window['out8'].update('Reaction Time is ' + str(ventriNoneNoneRate.ReaT) + "s")
            window['out9'].update('Response Factor is ' + str(ventriNoneNoneRate.ResF))
            window['out10'].update('Recovery Time is ' + str(ventriNoneNoneRate.RecT) + "min")
            window['out11'].update('')
            window['out12'].update('')
            window['out13'].update('')            
            index = 9
            pacemaker_serial_comm(parametersList_VOOR)

        if event == "VVIR":  #Displays mode VVIR
            if(opened_dropdown != True):
                opened_dropdown = not opened_dropdown
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened_dropdown else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened_dropdown)
            window['out1'].update('Viewing VVIR')
            window['out2'].update('LRL is ' + str(ventriVentriInhiRate.LRL) + " ppm")
            window['out3'].update('URL is ' + str(ventriVentriInhiRate.URL) + " ppm")
            window['out4'].update('Ventricular Amplitude is ' + str(ventriVentriInhiRate.VA) + " V")
            window['out5'].update('Ventricular Pulse Width is ' + str(ventriVentriInhiRate.VPW) + " ms")
            
            window['out6'].update('Sensitivity is ' + str(ventriVentriInhiRate.VS) + " mV")
            window['out7'].update('Refactory Period is ' + str(ventriVentriInhiRate.VRP) + " ms")

            window['out8'].update('Maximum Sensor Rate is ' + str(ventriVentriInhiRate.MSR) + " ppm")
            window['out9'].update('Activity Threshold is ' + str(ventriVentriInhiRate.AT))
            window['out10'].update('Reaction Time is ' + str(ventriVentriInhiRate.ReaT) + "s")
            window['out11'].update('Response Factor is ' + str(ventriVentriInhiRate.ResF))
            window['out12'].update('Recovery Time is ' + str(ventriVentriInhiRate.RecT) + "min")

            window['out13'].update('')
            index = 10
            pacemaker_serial_comm(parametersList_VVIR)

        #grab_data()
        if event == "Generate_EGRAM":
            print("generating egram")
            egram()

        if event == "Change_Values":    #Allows the user to change depending on the state they are in
            if index == 1:              #In order to change the values of a mode the user must be first
                atriNone.change()       #in that mode
                dcm_UpdateParam(atriNone.name)          #Update Parameters are called after each change
            if index == 2:
                ventriNone.change()
                dcm_UpdateParam(ventriNone.name)
            if index == 3:
                atriInhi.change()
                dcm_UpdateParam(atriInhi.name)
            if index == 4:
                ventriInhi.change()
                dcm_UpdateParam(ventriInhi.name)
            if index == 5:
                dualNone.change()
                dcm_UpdateParam(dualNone.name)
            if index == 6:
                dualRate.change()
                dcm_UpdateParam(dualRate.name)
            if index == 7:
                atriNoneNoneRate.change()
                dcm_UpdateParam(atriNoneNoneRate.name)
            if index == 8:
                atriAtriInhiRate.change()
                dcm_UpdateParam(atriAtriInhiRate.name)
            if index == 9:
                ventriNoneNoneRate.change()
                dcm_UpdateParam(ventriNoneNoneRate.name)
            if index == 10:
                ventriVentriInhiRate.change()
                dcm_UpdateParam(ventriVentriInhiRate.name)
    window.close()

#Store Programming Parameters into CSV file for later use

def register(username,password):
    
    pwd = get_WD('Database_CSV')+'/'
    #check for common-username 
    with open(pwd+"users.csv",mode="r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        f.seek(0)
        for row in reader:
            if row[0] == username:
                return 0
                
    #check for how many registered users there are
    f = open(pwd+"users.csv")
    f.seek(0)
    reader = csv.reader(f)
    lines= len(list(reader))
    f.close()
    if(lines == 10):
        return 1
   
    with open(pwd+"users.csv",mode="a", newline="") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([username,password])
        f.close()
    with open(pwd+str(username) +".csv",mode="a", newline="") as f: #Creates csv file for each user after register
        writer = csv.writer(f,delimiter=",")
        writer.writerow(["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12"]) #Parameters, used to label columns
        writer.writerow([60,120,3.5,0.4]) #AOO      parameters are filled with the lowest possible value
        writer.writerow([60,120,3.5,0.4]) #VOO
        writer.writerow([60,120,3.5,0.4,0.75,250,250]) #AAI
        writer.writerow([60,120,3.5,0.4,2.5,320]) #VVI
        writer.writerow([60,120,150,3.5,3.5,0.4,0.4]) #DOO
        writer.writerow([60,120,150,3.5,3.5,0.4,0.4,120,'Med',30,8,5]) #DOOR
        writer.writerow([60,120,3.5,0.4,120,'Med',30,8,5]) #AOOR
        writer.writerow([60,120,3.5,0.4,0.75,250,250,120,'Med',30,8,5]) #AAIR
        writer.writerow([60,120,3.5,0.4,120,'Med',30,8,5]) #VOOR
        writer.writerow([60,120,3.5,0.4,2.5,320,120,'Med',30,8,5]) #VVIR

        f.close()
    
    return 2

def login(username,password):
    pwd = get_WD('Database_CSV')+'/'
    
    with open(pwd+"users.csv",mode="r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        f.seek(0)
        for row in reader:
            if row == [username,password]:
                f.close()
                return True
            
        f.close()
        return False

def dcm_status():
    #putting place holder values for dcm_active
    dcm_active = True #this will change when we acc integrate DCM
    #putting place hold value for the current DCM "running"
    current_dcm = 'DCM1' #this will change in realtime as we integerate DCM.
    pwd = get_WD('Database_CSV')+'/'

    if (dcm_active == True):
        with open(pwd+"DCMs.csv",mode="a+", newline='') as f:    
            reader = csv.reader(f) #\r\n ??
            f.seek(0)
            try:
                intial_row = next(reader)  # gets the first line
                if intial_row[0] == current_dcm: #legacy DCM is current DCM
                    f.close()
                    return True, 'Current DCM is the same one that was connected previously'
            except: #if code reaches this position, this means that Current DCM is different to Previous DCM
               pass
            f.seek(0)
            writer = csv.writer(f)
            f.truncate()
            writer.writerow([current_dcm])
            f.close()
            return True, 'Current DCM is different to the one that was connected previously'


    else:
        return False,'Idle'



# Defining the login page contents
def register_window(): 
    elements_to_be_centered = [[sg.Button('Register', key="register"),sg.Button('Cancel', key="cancel")],]
    layout = [ [sg.Text("New Username:")],
            [sg.Input()],
            [sg.Text("New Password:")],
            [sg.Input()],
            [sg.Column(elements_to_be_centered, justification='centre')]]
    window = sg.Window("registration page", layout,font=('Helvetica',20))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: 
            quit()
        if event == "cancel":
            window.close()
            main()
        if event == "register":
                registration_status = register(values[0],values[1])
                if registration_status == 1:
                    popup_layout_1 = [[sg.Text("10 Users Already Registered")],[sg.OK()]]
                    popup_window_1 = sg.Window('Failed',popup_layout_1,font=('Helvetica',15),element_justification='c',size=(280,100))
                    while True:
                        event1,value1 = popup_window_1.read()
                        if event1 == 'OK':
                            break
                        elif event1 ==  sg.WIN_CLOSED:
                            break
                    popup_window_1.close()
                elif registration_status == 0: 
                    popup_layout_2 = [[sg.Text("Username Already Exists")],[sg.OK()]]
                    popup_window_2 = sg.Window('Failed',popup_layout_2,font=('Helvetica',15),element_justification='c',size=(280,100))
                    while True:
                        event2,value2 = popup_window_2.read()
                        if event2 == 'OK':
                            break
                        elif event2 ==  sg.WIN_CLOSED:
                            break
                    popup_window_2.close()
                else:
                    popup_layout_3 = [[sg.Text("Registration Succesful!")],[sg.OK()]]
                    popup_window_3 = sg.Window('Failed',popup_layout_3,font=('Helvetica',15),element_justification='c',size=(280,100))
                    while True:
                        event3,value3 = popup_window_3.read()
                        if event3 == 'OK':
                            break
                        elif event3 ==  sg.WIN_CLOSED:
                            break
                    popup_window_3.close()
                window.close()
                main()
            
    window.close()

def dcm_paratemers(): #place holders for 1,2,3,4,7
    dcm_connection, dcm_telemetry = dcm_status()
    pwd = get_WD('Program_Items')+'/'
    temp_file_name = "Red-Circle.png"
    temp_file_text = "Connection Not Active"
    colour = 'maroon'
    if dcm_connection == True:
        temp_file_name = "Green-Circle.png"
        temp_file_text = "Connection Active"
        colour = 'green'
    layout = [ [sg.Button('Pacing Modes', key="pace",font=('Helvetica',20))],
               [sg.Image(filename=pwd+temp_file_name,key="circle", size=(80,80)),sg.Text(temp_file_text, font=('Helvetica',20))],
               [sg.Text(dcm_telemetry, text_color=colour, font=('Helvetica',14))],
               [sg.Button("Quit", key="quit", font=('Helvetica',20))] ]

    window = sg.Window("DCM Parameters", layout, size=(550,250), finalize=True, element_justification='c')


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            quit()
        if event == "quit": 
            window.close()
            main()
        if event == "pace":
            dcm_pacingModeDir()

    #print('dcm_parameters')

def main(): #creating the main login page.
    
    elements_to_be_centered = [[sg.Button('Login', key="login"),sg.Button('Register', key="register"),sg.Button("Quit", key="quit")],]
    #[sg.Button('Login', key="login"),sg.Button('Register', key="register"),sg.Button("Quit", key="quit")]
    layout = [ [sg.Text("Username:")],
            [sg.Input(do_not_clear=False)],
            [sg.Text("Password:")],
            [sg.Input(do_not_clear=False)],
            [sg.Column(elements_to_be_centered, justification='centre')]]
    
    window = sg.Window("DCM Interface", layout,font=('Helvetica',20))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "quit":
            quit()
        else:
            if event == "login": #compare with our text file database.
                login_status = login(values[0],values[1])
                if login_status != True:
                    popup_layout_f = [[sg.Text("Invalid login. Try again")],[sg.OK()]]
                    popup_window_f = sg.Window('Failed', popup_layout_f, font=('Helvetica',15),element_justification='c',size=(280,100))
                    while True:
                        event2, values2 = popup_window_f.read()
                        if event2 == 'OK':
                            break
                        elif event2 ==  sg.WIN_CLOSED:
                            break
                    popup_window_f.close()
                    window.close()
                    main()
                popup_layout = [[sg.Text("Login Succesful!")],[sg.OK()]]
                popup_window = sg.Window('Success', popup_layout, font=('Helvetica',15),element_justification='c',size=(280,100))
                while True:
                    event1, values1 = popup_window.read()
                    if event1 == 'OK':
                        break
                    elif event1 ==  sg.WIN_CLOSED:
                        break
                atriNone.name = values[0]
                ventriNone.name = values[0]
                atriInhi.name = values[0]
                ventriInhi.name = values[0]
                dualNone.name = values[0]
                dualRate.name = values[0]
                atriNoneNoneRate.name = values[0]
                atriAtriInhiRate.name = values[0]
                ventriNoneNoneRate.name = values[0]
                ventriVentriInhiRate.name = values[0]
                popup_window.close()
                window.close()
                dcm_paratemers()        
            elif event == "register":
                window.close()
                register_window()
            window.close()
        

if __name__ == "__main__":
    main()

