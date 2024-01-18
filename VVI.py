import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd
import csv

global parametersList_VVI
parametersList_VVI = [0]*21

class VVI():
    def __init__(self, name, LRL, URL, VA, VPW, VS, VRP): #parameters
        self.name = name#name of user
        self.LRL = LRL 
        self.URL = URL 
        self.VA = VA 
        self.VPW = VPW
        self.VS = VS
        self.VRP = VRP
        parametersList_VVI[1] = 1
        parametersList_VVI[2] = LRL
        parametersList_VVI[3] = URL
        parametersList_VVI[5] = VA*10
        parametersList_VVI[7] = VPW*100
        parametersList_VVI[9] = 1
        parametersList_VVI[10] = VS*10
        parametersList_VVI[11] = VRP
        parametersList_VVI[19] = 16
        parametersList_VVI[20] = 55

        #User must write their input into the Input space and then press the corresponding button to load the value
    def set_from_csv(self): #Obtains values from 3nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = int(df.loc[3, "P1"])
        self.URL = int(df.loc[3, "P2"])
        self.VA = float(df.loc[3, "P3"])
        self.VPW = float(df.loc[3, "P4"])
        self.VS = float(df.loc[3, "P5"])
        self.VRP = float(df.loc[3, "P6"])
        parametersList_VVI[1] = 1
        parametersList_VVI[2] = self.LRL
        parametersList_VVI[3] = self.URL
        parametersList_VVI[5] = self.VA*10
        parametersList_VVI[7] = self.VPW*100
        parametersList_VVI[9] = 1
        parametersList_VVI[10] = self.VS*10
        parametersList_VVI[11] = self.VRP
        parametersList_VVI[19] = 16
        parametersList_VVI[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of VVI")],
            [sg.Text("",key="status")],
            [sg.Text('LRL:  ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL:  ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('VA:   ' + str(self.VA) + "V",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('VPW:  ' + str(self.VPW) + "ms",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Text('VS:   ' + str(self.VS) + "mV",key="t5"), sg.Button('+', key="B5+"), sg.Button('-', key="B5-")],
            [sg.Text('VRP:  ' + str(self.VRP) + "ms",key="t6"), sg.Button('+', key="B6+"), sg.Button('-', key="B6-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('VAI', layout, font=('Helvetica',20), element_justification='c', size=(450,600))

        # Display and interact with the Window using an Event Loop
        while True:
            event, values = window.read()
            window['status'].update('')
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            # Output a message to the window
            if event == "B1+":
                if((int(self.LRL) >= 30) and (int(self.LRL) < 50)) or (int(self.LRL>= 90) and (int(self.LRL) < 175)):
                    self.LRL = self.LRL + 5
                elif(int(self.LRL) >= 50) and (int(self.LRL) < 90):
                    self.LRL = self.LRL + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B1-":
                if((int(self.LRL) > 30) and (int(self.LRL) <= 50)) or (int(self.LRL> 90) and (int(self.LRL) <= 175)):
                    self.LRL = self.LRL - 5
                elif(int(self.LRL) > 50) and (int(self.LRL) <= 90):
                    self.LRL = self.LRL - 1
                else:
                    window['status'].update('Value cannot decrease further')
               
            if event == "B2+":
                if((int(self.URL) >= 50) and (int(self.URL) < 175)):
                    self.URL = self.URL + 5
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B2-":
                if((int(self.URL)> 50) and (int(self.URL) <= 175)):
                    self.URL = self.URL - 5
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B3+":
                if((float(self.VA) >= 0.5) and (float(self.VA) < 3.2)):
                    self.VA = round(self.VA + 0.1, 5)
                elif(float(self.VA) == 3.2):
                    self.VA = round(3.5, 1)
                elif((float(self.VA) >= 3.5) and (float(self.VA) < 7.0)):
                    self.VA = round(self.VA + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if((float(self.VA) > 0.5) and (float(self.VA) <= 3.2)):
                    self.VA = round(float(self.VA) - 0.1, 5)
                elif(float(self.VA) == 3.5):
                    self.VA = round(3.2, 1)
                elif(float(self.VA) > 3.5) and (float(self.VA) <= 7.0):
                    self.VA = round(self.VA - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B4+":
                if(float(self.VPW) == 0.05):
                    self.VPW = round(0.1, 1)
                elif(float(self.VPW) >= 0.1) and (float(self.VPW) < 1.9):
                    self.VPW = round(self.VPW + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if(float(self.VPW) == 0.1):
                    self.VPW = round(0.05, 2)
                elif(float(self.VPW) > 0.1) and (float(self.VPW) <= 1.9):
                    self.VPW = round(self.VPW - 0.1, 1)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B5+":
                if(float(self.VS) >= 0.25) and (float(self.VS) < 1.0):
                    self.VS = round(self.VS + 0.25, 5)
                elif(float(self.VS) >= 1.0) and (float(self.VS) < 10):
                    self.VS = round(self.VS + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B5-":
                if(float(self.VS) > 0.25) and (float(self.VS) <= 1.0):
                    self.VS = round(self.VS - 0.25, 5)
                elif(float(self.VS) > 1.0) and (float(self.VS) <= 10):
                    self.VS = round(self.VS - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')     

            if event == "B6+":
                if(float(self.VRP) >= 150) and (float(self.VRP)  < 500):
                    self.VRP = self.VRP + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B6-":
                if(float(self.VRP) > 150) and (float(self.VRP) <= 500):
                    self.VRP = self.VRP - 10
                else:
                    window['status'].update('Value cannot decrease further')        
                    
            if event == "B7+":
                if(float(self.PVVRP) >= 150) and (float(self.PVVRP) < 500):
                    self.PVVRP = self.PVVRP + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B7-":
                if(float(self.PVVRP) > 150) and (float(self.PVVRP) <= 500):
                    self.PVVRP = self.PVVRP - 10
                else:
                    window['status'].update('Value cannot decrease further')
            
            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('VA: ' + str(self.VA) + "V")
            window['t4'].update('VPW: ' + str(self.VPW) + "ms")
            window['t5'].update('VS: ' + str(self.VS) + "mV")
            window['t6'].update('VRP: ' + str(self.VRP) + "ms")

            parametersList_VVI[1] = 1
            parametersList_VVI[2] = self.LRL
            parametersList_VVI[3] = self.URL
            parametersList_VVI[5] = self.VA*10
            parametersList_VVI[7] = self.VPW*100
            parametersList_VVI[9] = 1
            parametersList_VVI[10] = self.VS*10
            parametersList_VVI[11] = self.VRP
            parametersList_VVI[19] = 16
            parametersList_VVI[20] = 55

        # Finish up by removing from the screen
        window.close()



