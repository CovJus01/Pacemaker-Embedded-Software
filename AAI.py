##add PVARP to this file!
import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd
import csv

global parametersList_AAI
parametersList_AAI = [0]*21

class AAI:
    def __init__(self, name, LRL, URL, AA, APW, AS, ARP, PVARP): #parameters
        self.name = name#name of user
        self.LRL = LRL
        self.URL = URL
        self.AA = AA
        self.APW = APW
        self.AS = AS
        self.ARP = ARP
        self.PVARP = PVARP
        parametersList_AAI[0] = 1
        parametersList_AAI[2] = LRL
        parametersList_AAI[3] = URL
        parametersList_AAI[4] = AA*10
        parametersList_AAI[6] = APW*100
        parametersList_AAI[8] = 1
        parametersList_AAI[10] = AS*10
        parametersList_AAI[11] = ARP
        parametersList_AAI[19] = 16
        parametersList_AAI[20] = 55

        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self): #Obtains values from 3nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = int(df.loc[2, "P1"])
        self.URL = int(df.loc[2, "P2"])
        self.AA = float(df.loc[2, "P3"])
        self.APW = float(df.loc[2, "P4"])
        self.AS = float(df.loc[2, "P5"])
        self.ARP = float(df.loc[2, "P6"])
        self.PVARP = float(df.loc[2, "P7"])
        parametersList_AAI[0] = 1
        parametersList_AAI[2] = self.LRL
        parametersList_AAI[3] = self.URL
        parametersList_AAI[4] = self.AA*10
        parametersList_AAI[6] = self.APW*100
        parametersList_AAI[8] = 1
        parametersList_AAI[10] = self.AS*10
        parametersList_AAI[11] = self.ARP
        parametersList_AAI[19] = 16
        parametersList_AAI[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of AAI")],
            [sg.Text("",key="status")],
            [sg.Text('LRL:  ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL:  ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('AA:   ' + str(self.AA) + "V",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('APW:  ' + str(self.APW) + "ms",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Text('AS:   ' + str(self.AS) + "mV",key="t5"), sg.Button('+', key="B5+"), sg.Button('-', key="B5-")],
            [sg.Text('ARP:  ' + str(self.ARP) + "ms",key="t6"), sg.Button('+', key="B6+"), sg.Button('-', key="B6-")],
            [sg.Text('PVARP:' + str(self.PVARP) + "ms",key="t7"), sg.Button('+', key="B7+"), sg.Button('-', key="B7-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('AAI', layout, font=('Helvetica',20), element_justification='c', size=(450,600))

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
                if((float(self.AA) >= 0.5) and (float(self.AA) < 3.2)):
                    self.AA = round(self.AA + 0.1, 5)
                elif(float(self.AA) == 3.2):
                    self.AA = round(3.5, 1)
                elif((float(self.AA) >= 3.5) and (float(self.AA) < 7.0)):
                    self.AA = round(self.AA + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if((float(self.AA) > 0.5) and (float(self.AA) <= 3.2)):
                    self.AA = round(float(self.AA) - 0.1, 5)
                elif(float(self.AA) == 3.5):
                    self.AA = round(3.2, 1)
                elif(float(self.AA) > 3.5) and (float(self.AA) <= 7.0):
                    self.AA = round(self.AA - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B4+":
                if(float(self.APW) == 0.05):
                    self.APW = round(0.1, 1)
                elif(float(self.APW) >= 0.1) and (float(self.APW) < 1.9):
                    self.APW = round(self.APW + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if(float(self.APW) == 0.1):
                    self.APW = round(0.05, 2)
                elif(float(self.APW) > 0.1) and (float(self.APW) <= 1.9):
                    self.APW = round(self.APW - 0.1, 1)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B5+":
                if(float(self.AS) >= 0.25) and (float(self.AS) < 1.0):
                    self.AS = round(self.AS + 0.25, 5)
                elif(float(self.AS) >= 1.0) and (float(self.AS) < 10):
                    self.AS = round(self.AS + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B5-":
                if(float(self.AS) > 0.25) and (float(self.AS) <= 1.0):
                    self.AS = round(self.AS - 0.25, 5)
                elif(float(self.AS) > 1.0) and (float(self.AS) <= 10):
                    self.AS = round(self.AS - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')     

            if event == "B6+":
                if(float(self.ARP) >= 150) and (float(self.ARP)  < 500):
                    self.ARP = self.ARP + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B6-":
                if(float(self.ARP) > 150) and (float(self.ARP) <= 500):
                    self.ARP = self.ARP - 10
                else:
                    window['status'].update('Value cannot decrease further')        
                    
            if event == "B7+":
                if(float(self.PVARP) >= 150) and (float(self.PVARP) < 500):
                    self.PVARP = self.PVARP + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B7-":
                if(float(self.PVARP) > 150) and (float(self.PVARP) <= 500):
                    self.PVARP = self.PVARP - 10
                else:
                    window['status'].update('Value cannot decrease further')
   
            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('AA: ' + str(self.AA) + "V")
            window['t4'].update('APW: ' + str(self.APW) + "ms")
            window['t5'].update('AS: ' + str(self.AS) + "mV")
            window['t6'].update('ARP: ' + str(self.ARP) + "ms")
            window['t7'].update('PVARP: ' + str(self.PVARP) + "ms")

            parametersList_AAI[0] = 1
            parametersList_AAI[2] = self.LRL
            parametersList_AAI[3] = self.URL
            parametersList_AAI[4] = self.AA*10
            parametersList_AAI[6] = self.APW*100
            parametersList_AAI[8] = 1
            parametersList_AAI[10] = self.AS*10
            parametersList_AAI[11] = self.ARP
            parametersList_AAI[19] = 16
            parametersList_AAI[20] = 55


        # Finish up by removing from the screen
        window.close()