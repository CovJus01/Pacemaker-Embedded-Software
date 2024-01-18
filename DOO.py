import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd 
import csv

global parametersList_DOO
parametersList_DOO = [0]*21

class DOO():
    
    def __init__(self, name, LRL, URL, FAVD, AA, VA, APW, VPW): #parameters
        self.name = name#name of user
        self.LRL = LRL   
        self.URL = URL
        self.FAVD = FAVD
        self.VA = VA
        self.AA = AA
        self.APW = APW
        self.VPW = VPW
        parametersList_DOO[0] = 1
        parametersList_DOO[1] = 1
        parametersList_DOO[2] = LRL   
        parametersList_DOO[3] = URL
        parametersList_DOO[4] = AA*10
        parametersList_DOO[5] = VA*10
        parametersList_DOO[6] = APW*100
        parametersList_DOO[7] = VPW*100
        parametersList_DOO[12] = FAVD
        parametersList_DOO[19] = 16
        parametersList_DOO[20] = 55

        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self):#Obtains values from 1nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = int(df.loc[4, "P1"])
        self.URL = int(df.loc[4, "P2"])
        self.FAVD = float(df.loc[4, "P3"])
        self.AA = float(df.loc[4, "P4"])
        self.VA = float(df.loc[4, "P5"])
        self.APW = float(df.loc[4, "P6"])
        self.VPW = float(df.loc[4, "P7"])
        parametersList_DOO[0] = 1
        parametersList_DOO[1] = 1
        parametersList_DOO[2] = self.LRL   
        parametersList_DOO[3] = self.URL
        parametersList_DOO[4] = self.AA*10
        parametersList_DOO[5] = self.VA*10
        parametersList_DOO[6] = self.APW*100
        parametersList_DOO[7] = self.VPW*100
        parametersList_DOO[12] = self.FAVD
        parametersList_DOO[19] = 16
        parametersList_DOO[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of DOO")],
            [sg.Text("",key="status")],
            [sg.Text('LRL: ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL: ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('FAVD: ' + str(self.FAVD) + "ms",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('AA: ' + str(self.AA) + "V",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Text('VA: ' + str(self.VA) + "V",key="t5"), sg.Button('+', key="B5+"), sg.Button('-', key="B5-")],
            [sg.Text('APW: ' + str(self.APW) + "ms",key="t6"), sg.Button('+', key="B6+"), sg.Button('-', key="B6-")],
            [sg.Text('VPW: ' + str(self.VPW) + "ms",key="t7"), sg.Button('+', key="B7+"), sg.Button('-', key="B7-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('DOO', layout, font=('Helvetica',20), element_justification='c', size=(450,600))

        # Display and interact with the Window using an Event Loop
        while True:
            event, values = window.read()
            window['status'].update('')
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            # Output a message to the window
            if event == "B1+":
                if (int(self.LRL) + 5 >= int(self.URL)):
                    window['status'].update('LRL cannot be larger than URL')
                elif(((self.LRL) >= 30) and ((self.LRL) < 50)) or ((self.LRL>= 90) and (self.LRL < 175)):
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
                if (int(self.URL) - 5 <= int(self.LRL)):
                    window['status'].update('URL cannot be lower than LRL')
                elif((self.URL> 50) and (self.URL <= 175)):
                    self.URL = self.URL - 5
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B3+":
                if((self.FAVD) >= 70) and ((self.FAVD) < 300):
                    self.FAVD = self.FAVD + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if((self.FAVD) > 70) and ((self.FAVD) <= 300):
                    self.FAVD = self.FAVD - 10
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B4+":
                if((float(self.AA) >= 0.5) and (float(self.AA) < 3.2)):
                    self.AA = round(float(self.AA) + 0.1, 5)
                elif(float(self.AA) == 3.2):
                    self.AA = round(3.5, 1)
                elif(float(self.AA) >= 3.5) and (float(self.AA) < 7.0):
                    self.AA = round(float(self.AA) + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if((float(self.AA) > 0.5) and (float(self.AA) <= 3.2)):
                    self.AA = round(float(self.AA) - 0.1, 5)
                elif(float(self.AA) == 3.5):
                    self.AA = round(3.2, 1)
                elif(float(self.AA) > 3.5) and (float(self.AA) <= 7.0):
                    self.AA = round(float(self.AA) - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B5+":
                if((float(self.VA) >= 0.5) and (float(self.VA) < 3.2)):
                    self.VA = round(float(self.VA) + 0.1, 5)
                elif(float(self.VA) == 3.2):
                    self.VA = round(3.5, 1)
                elif(float(self.VA) >= 3.5) and (float(self.VA) < 7.0):
                    self.VA = round(float(self.VA) + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B5-":
                if((float(self.VA) > 0.5) and (float(self.VA) <= 3.2)):
                    self.VA = round(self.VA - 0.1, 5)
                elif(float(self.VA) == 3.5):
                    self.VA = round(3.2, 1)
                elif(float(self.VA) > 3.5) and (float(self.VA) <= 7.0):
                    self.VA = round(self.VA - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B6+":
                if(float(self.APW) == 0.05):
                    self.APW = round(0.1, 1)
                elif(float(self.APW) >= 0.1) and (float(self.APW) < 1.9):
                    self.APW = round(float(self.APW) + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B6-":
                if(float(self.APW) == 0.1):
                    self.APW = round(0.05, 2)
                elif(float(self.APW) > 0.1) and (float(self.APW) <= 1.9):
                    self.APW = round(float(self.APW)- 0.1, 1)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B7+":
                if(float(self.VPW) == 0.05):
                    self.VPW = round(0.1, 1)
                elif(float(self.VPW) >= 0.1) and (float(self.VPW) < 1.9):
                    self.VPW = round(float(self.VPW) + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B7-":
                if(float(self.VPW) == 0.1):
                    self.VPW = round(0.05, 2)
                elif(float(self.VPW) > 0.1) and (float(self.VPW) <= 1.9):
                    self.VPW = round(float(self.VPW) - 0.1, 1)
                else:
                    window['status'].update('Value cannot decrease further')

            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('FAVD: ' + str(self.FAVD) + "ms")
            window['t4'].update('AA: ' + str(self.AA) + "V")
            window['t5'].update('VA: ' + str(self.VA) + "V")
            window['t6'].update('APW: ' + str(self.APW) + "ms")
            window['t7'].update('VPW: ' + str(self.VPW) + "ms")

            parametersList_DOO[0] = 1
            parametersList_DOO[1] = 1
            parametersList_DOO[2] = self.LRL   
            parametersList_DOO[3] = self.URL
            parametersList_DOO[4] = self.AA*10
            parametersList_DOO[5] = self.VA*10
            parametersList_DOO[6] = self.APW*100
            parametersList_DOO[7] = self.VPW*100
            parametersList_DOO[12] = self.FAVD
            parametersList_DOO[19] = 16
            parametersList_DOO[20] = 55

        # Finish up by removing from the screen
        window.close()
