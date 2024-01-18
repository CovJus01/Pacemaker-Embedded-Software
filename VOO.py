import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd
import csv

global parametersList_VOO
parametersList_VOO = [0]*21

class VOO():
    def __init__(self, name, LRL, URL, VA, VPW): #parameters
        self.name = name#name of user
        self.LRL = LRL #ppm
        self.URL = URL #ppm
        self.VA = VA #Volts
        self.VPW = VPW
        parametersList_VOO[1] = 1
        parametersList_VOO[2] = LRL
        parametersList_VOO[3] = URL
        parametersList_VOO[5] = VA*10
        parametersList_VOO[7] = VPW*100
        parametersList_VOO[19] = 16
        parametersList_VOO[20] = 55

        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self): #Obtains values from 2nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = df.loc[1, "P1"]
        self.URL = df.loc[1, "P2"]
        self.VA = df.loc[1, "P3"]
        self.VPW = df.loc[1, "P4"]
        parametersList_VOO[1] = 1
        parametersList_VOO[2] = self.LRL
        parametersList_VOO[3] = self.URL
        parametersList_VOO[5] = self.VA*10
        parametersList_VOO[7] = self.VPW*100
        parametersList_VOO[19] = 16
        parametersList_VOO[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of VOO")],
            [sg.Text("",key="status")],
            [sg.Text('LRL: ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL: ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('VA: ' + str(self.VA) + "V",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('VPW: ' + str(self.VA) + "ms",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Button('Quit')]
            ]
        # Create the window
        window = sg.Window('VOO', layout, font=('Helvetica',20), element_justification='c', size=(450,400))
        # Display and interact with the Window using an Event Loop
        while True:
            event, values = window.read()
            window['status'].update('')
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            # Output a message to the window
            if event == "B1+":
                if(((self.LRL) >= 30) and ((self.LRL) < 50)) or ((self.LRL>= 90) and (self.LRL < 175)):
                    self.LRL = self.LRL + 5
                elif((self.LRL) >= 50) and ((self.LRL) < 90):
                    self.LRL = self.LRL + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B1-":
                if(((self.LRL) > 30) and ((self.LRL) <= 50)) or ((self.LRL> 90) and (self.LRL <= 175)):
                    self.LRL = self.LRL - 5
                elif((self.LRL) > 50) and ((self.LRL) <= 90):
                    self.LRL = self.LRL - 1
                else:
                    window['status'].update('Value cannot decrease further')
               
            if event == "B2+":
                if((self.URL >= 50) and (self.URL < 175)):
                    self.URL = self.URL + 5
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B2-":
                if((self.URL> 50) and (self.URL <= 175)):
                    self.URL = self.URL - 5
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B3+":
                if(((self.VA) >= 0.5) and ((self.VA) < 3.2)):
                    self.VA = round(self.VA + 0.1, 5)
                elif((self.VA) == 3.2):
                    self.VA = round(3.5, 1)
                elif((self.VA) >= 3.5) and ((self.VA) < 7.0):
                    self.VA = round(self.VA + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if(((self.VA) > 0.5) and ((self.VA) <= 3.2)):
                    self.VA = round(self.VA - 0.1, 5)
                elif((self.VA) == 3.5):
                    self.VA = round(3.2, 1)
                elif((self.VA) > 3.5) and ((self.VA) <= 7.0):
                    self.VA = round(self.VA - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B4+":
                if((self.VPW) == 0.05):
                    self.VPW = round(0.1, 1)
                elif((self.VPW) >= 0.1) and ((self.VPW) < 1.9):
                    self.VPW = round(self.VPW + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if((self.VPW) == 0.1):
                    self.VPW = round(0.05, 2)
                elif((self.VPW) > 0.1) and ((self.VPW) <= 1.9):
                    self.VPW = round(self.VPW - 0.1, 1)
                else:
                    window['status'].update('Value cannot decrease further')

            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('VA: ' + str(self.VA) + "V")
            window['t4'].update('VPW: ' + str(self.VPW) + "ms")
       
            parametersList_VOO[1] = 1
            parametersList_VOO[2] = self.LRL
            parametersList_VOO[3] = self.URL
            parametersList_VOO[5] = self.VA*10
            parametersList_VOO[7] = self.VPW*100
            parametersList_VOO[19] = 16
            parametersList_VOO[20] = 55

        # Finish up by removing from the screen
        window.close()



