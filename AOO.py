import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd 
import csv

global parametersList_AOO
parametersList_AOO = [0]*21

class AOO():
    
    def __init__(self, name, LRL, URL, AA, APW): #parameters
        self.name = name#name of user
        self.LRL = LRL   
        self.URL = URL
        self.AA = AA*100
        self.APW = APW*1000
        parametersList_AOO[0] = 1
        parametersList_AOO[2] = LRL
        parametersList_AOO[3] = URL
        parametersList_AOO[4] = AA*100
        parametersList_AOO[6] = APW*1000
        parametersList_AOO[19] = 16
        parametersList_AOO[20] = 55
        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self):#Obtains values from 1nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7"]#,"P8","P9"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = df.loc[0, "P1"]
        self.URL = df.loc[0, "P2"]
        self.AA = df.loc[0, "P3"]
        self.APW = df.loc[0, "P4"]
        parametersList_AOO[0] = 1
        parametersList_AOO[2] = self.LRL
        parametersList_AOO[3] = self.URL
        parametersList_AOO[4] = self.AA*100
        parametersList_AOO[6] = self.APW*1000
        parametersList_AOO[19] = 16
        parametersList_AOO[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of AOO")],
            [sg.Text("",key="status")],
            [sg.Text('LRL: ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL: ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('AA: ' + str(self.AA) + "V",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('APW: ' + str(self.AA) + "ms",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('AOO', layout,font=('Helvetica',20), element_justification='c', size=(450,400))

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
                if(((self.AA) >= 0.5) and ((self.AA) < 3.2)):
                    self.AA = round(self.AA + 0.1,5)
                elif((self.AA) == 3.2):
                    self.AA = round(3.5,1)
                elif((self.AA) >= 3.5) and ((self.AA) < 7.0):
                    self.AA = round(self.AA + 0.5,5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if(((self.AA) > 0.5) and ((self.AA) <= 3.2)):
                    self.AA = round(self.AA - 0.10, 5)
                elif((self.AA) == 3.5):
                    self.AA = round(3.2,1)
                elif((self.AA) > 3.5) and ((self.AA) <= 7.0):
                    self.AA = round(self.AA - 0.5,1)
                else:
                    window['status'].update('Value cannot decrease further')


            if event == "B4+":
                if((self.APW) == 0.05):
                    self.APW = round(0.1, 1)
                elif((self.APW) >= 0.1) and ((self.APW) < 1.9):
                    self.APW = round(self.APW + 0.1,5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if((self.APW) == 0.1):
                    self.APW = round(0.05, 2)
                elif((self.APW) > 0.1) and ((self.APW) <= 1.9):
                    self.APW = round(self.APW - 0.1,1)
                else:
                    window['status'].update('Value cannot decrease further')


            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('AA: ' + str(self.AA) + "V")
            window['t4'].update('APW: ' + str(self.APW) + "ms")
            
            parametersList_AOO[0] = 1
            parametersList_AOO[2] = self.LRL
            parametersList_AOO[3] = self.URL
            parametersList_AOO[4] = self.AA*100
            parametersList_AOO[6] = self.APW*1000
            parametersList_AOO[19] = 16
            parametersList_AOO[20] = 55

        # Finish up by removing from the screen
        window.close()
