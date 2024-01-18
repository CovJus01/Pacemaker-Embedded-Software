##add rate adaptive on index 18 to this file!
import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd 
import csv

global parametersList_VOOR
parametersList_VOOR = [0]*21

class VOOR():
    
    def __init__(self, name, LRL, URL, VA, VPW, MSR, AT, ReaT, ResF, RecT): #parameters
        self.name = name#name of user
        self.LRL = LRL   
        self.URL = URL  
        self.VA = VA
        self.VPW = VPW
        self.MSR = MSR
        self.AT = AT
        self.ReaT = ReaT
        self.ResF = ResF
        self.RecT = RecT
        parametersList_VOOR[1] = 1
        parametersList_VOOR[2] = LRL
        parametersList_VOOR[3] = URL
        parametersList_VOOR[5] = VA*10
        parametersList_VOOR[7] = VPW*100
        parametersList_VOOR[13] = MSR
        parametersList_VOOR[14] = AT
        parametersList_VOOR[15] = ReaT
        parametersList_VOOR[16] = ResF
        parametersList_VOOR[17] = RecT
        parametersList_VOOR[18] = 1
        parametersList_VOOR[19] = 16
        parametersList_VOOR[20] = 55

        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self):#Obtains values from 1nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7","P8","P9"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = df.loc[8, "P1"]   
        self.URL = df.loc[8, "P2"]

        self.VA = df.loc[8, "P3"]
        self.VPW = df.loc[8, "P4"]

        self.MSR = df.loc[8, "P5"] #might have to swap positions 
        self.AT = df.loc[8, "P6"]
        self.ReaT = df.loc[8, "P7"]
        self.ResF = df.loc[8, "P8"]
        self.RecT = df.loc[8, "P9"]
        parametersList_VOOR[1] = 1
        parametersList_VOOR[2] = self.LRL
        parametersList_VOOR[3] = self.URL
        parametersList_VOOR[5] = self.VA*10
        parametersList_VOOR[7] = self.VPW*100
        parametersList_VOOR[13] = self.MSR
        parametersList_VOOR[14] = self.AT
        parametersList_VOOR[15] = self.ReaT
        parametersList_VOOR[16] = self.ResF
        parametersList_VOOR[17] = self.RecT
        parametersList_VOOR[18] = 1
        parametersList_VOOR[19] = 16
        parametersList_VOOR[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of VOOR")],
            [sg.Text("",key="status")],
            [sg.Text('LRL: ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL: ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('VA: ' + str(self.VA) + "ms",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('VPW: ' + str(self.VPW) + "V",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            #Rate adaptive variables
            [sg.Text('MSR: ' + str(self.MSR) + "ppm",key="t5"), sg.Button('+', key="B5+"), sg.Button('-', key="B5-")],
            [sg.Text('AT: ' + str(self.AT),key="t6"), sg.Button('V-Low', key="B6VL"), sg.Button('Low', key="B6L")], 
            [sg.Button('Med-Low', key="B6ML"), sg.Button('Med', key="B6M")], 
            [sg.Button('Med-High', key="B6MH"), sg.Button('High', key="B6H"), sg.Button('V-High', key="B6VH")],
            [sg.Text('ReaT: ' + str(self.ReaT) + "sec",key="t7"), sg.Button('+', key="B7+"), sg.Button('-', key="B7-")],
            [sg.Text('ResF: ' + str(self.ResF),key="t8"), sg.Button('+', key="B8+"), sg.Button('-', key="B8-")],
            [sg.Text('RecT: ' + str(self.RecT) + "min",key="t9"), sg.Button('+', key="B9+"), sg.Button('-', key="B9-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('DOOR', layout, font=('Helvetica',14), element_justification='c', size=(450,800))

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
                if((float(self.VA) >= 0.5) and (float(self.VA) < 3.2)):
                    self.VA = round(float(self.VA) + 0.1, 5)
                elif(float(self.VA) == 3.2):
                    self.VA = round(3.5, 1)
                elif(float(self.VA) >= 3.5) and (float(self.VA) < 7.0):
                    self.VA = round(float(self.VA) + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if((float(self.VA) > 0.5) and (float(self.VA) <= 3.2)):
                    self.VA = round(float(self.VA) - 0.1, 5)
                elif(float(self.VA) == 3.5):
                    self.VA = round(3.2, 1)
                elif(float(self.VA) > 3.5) and (float(self.VA) <= 7.0):
                    self.VA = round(float(self.VA) - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B4+":
                if(float(self.VPW) == 0.05):
                    self.VPW = round(0.1, 1)
                elif(float(self.VPW) >= 0.1) and (float(self.VPW) < 1.9):
                    self.VPW = round(float(self.VPW) + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if(float(self.VPW) == 0.1):
                    self.VPW = round(0.05, 2)
                elif(float(self.VPW) > 0.1) and (float(self.VPW) <= 1.9):
                    self.VPW = round(float(self.VPW)- 0.1, 1)
                else:
                    window['status'].update('Value cannot decrease further')
#RATE ADAPTIVE MODES:
            if event == "B5+":
                if((float(self.MSR) >= 50) and (float(self.MSR) < 175)):
                    self.MSR = float(self.MSR) + 5
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B5-":
                if (float(self.MSR) - 5 <= float(self.URL)):
                    window['status'].update('MSR cannot be lower than URL')
                elif((float(self.MSR) > 50) and (float(self.MSR) <= 175)):
                    self.MSR = float(self.MSR) - 5
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B6VL":
                self.AT = "V-Low";
            if event == "B6L":
                self.AT = "Low";
            if event == "B6ML":
                self.AT = "Med-Low";
            if event == "B6M":
                self.AT = "Med";
            if event == "B6M":
                self.AT = "Med-High";
            if event == "B6H":
                self.AT = "High";
            if event == "B6VH":
                self.AT = "V-High";

            if event == "B7+":
                if(int(float(self.ReaT)) >= 10) and ((int(float(self.ReaT))  < 50)):
                    self.ReaT = float(self.ReaT) + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B7-":
                if((int(float(self.ReaT))  > 10) and (int(float(self.ReaT))  <= 50)):
                    self.ReaT = float(self.ReaT) - 10
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B8+":
                if((int(float(self.ResF))  >= 1) and (int(float(self.ResF))  < 16)):
                    self.ResF = float(self.ResF) + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B8-":
                if((int(float(self.ResF))  > 1) and (int(float(self.ResF)) <= 16)):
                    self.ResF = int(float(self.ResF)) - 1
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B9+":
                if((float(self.RecT) >= 2) and (float(self.RecT) < 16)):
                    self.RecT = float(self.RecT) + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B9-":
                if((float(self.RecT) > 2) and (float(self.RecT) <= 16)):
                    self.RecT = float(self.RecT) - 1
                else:
                    window['status'].update('Value cannot decrease further')

            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('VA: ' + str(self.VA) + "V")
            window['t4'].update('VPW: ' + str(self.VPW) + "ms")
#RATE ADAPTIVE MODES:
            window['t5'].update('MSR: ' + str(self.MSR) + "ppm")
            window['t6'].update('AT: ' + str(self.AT))
            window['t7'].update('ReaT: ' + str(self.ReaT) + "sec")
            window['t8'].update('ResF: ' + str(self.ResF))
            window['t9'].update('RecT: ' + str(self.RecT) + "min")
        # Finish up by removing from the screen
        parametersList_VOOR[1] = 1
        parametersList_VOOR[2] = self.LRL
        parametersList_VOOR[3] = self.URL
        parametersList_VOOR[5] = self.VA*10
        parametersList_VOOR[7] = self.VPW*100
        parametersList_VOOR[13] = self.MSR
        parametersList_VOOR[14] = self.AT
        parametersList_VOOR[15] = self.ReaT
        parametersList_VOOR[16] = self.ResF
        parametersList_VOOR[17] = self.RecT
        parametersList_VOOR[18] = 1
        parametersList_VOOR[19] = 16
        parametersList_VOOR[20] = 55

        window.close()