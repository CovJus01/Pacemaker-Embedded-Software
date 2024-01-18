##add rate adaptive on index 18 to this file!
import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd 
import csv

global parametersList_VVIR
parametersList_VVIR = [0]*21

class VVIR():
    
    def __init__(self, name, LRL, URL, VA, VPW, VS, VRP, MSR, AT, ReaT, ResF, RecT): #parameters
        self.name = name#name of user
        self.LRL = LRL   
        self.URL = URL
        self.VA = VA
        self.VPW = VPW
        self.VS = VS
        self.VRP = VRP
        self.MSR = MSR
        self.AT = AT
        self.ReaT = ReaT
        self.ResF = ResF
        self.RecT = RecT
        parametersList_VVIR[1] = 1
        parametersList_VVIR[2] = LRL
        parametersList_VVIR[3] = URL
        parametersList_VVIR[5] = VA*10
        parametersList_VVIR[7] = VPW*100
        parametersList_VVIR[9] = 1
        parametersList_VVIR[10] = VS*10
        parametersList_VVIR[11] = VRP
        parametersList_VVIR[13] = MSR
        parametersList_VVIR[14] = AT
        parametersList_VVIR[15] = ReaT
        parametersList_VVIR[16] = ResF
        parametersList_VVIR[17] = RecT
        parametersList_VVIR[18] = 1
        parametersList_VVIR[19] = 16
        parametersList_VVIR[20] = 55
        #parametersList_VVIR[18] = 1
        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self):#Obtains values from 1nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = df.loc[9, "P1"]
        self.URL = df.loc[9, "P2"]
        self.VA = df.loc[9, "P3"]
        self.VPW = df.loc[9, "P4"]
        self.VS = df.loc[9, "P5"]
        self.VRP = df.loc[9, "P6"]
        self.MSR = df.loc[9, "P7"]
        self.AT = df.loc[9, "P8"]
        self.ReaT = df.loc[9, "P9"]
        self.ResF = df.loc[9, "P10"]
        self.RecT = df.loc[9, "P11"]
        parametersList_VVIR[1] = 1
        parametersList_VVIR[2] = self.LRL
        parametersList_VVIR[3] = self.URL
        parametersList_VVIR[5] = self.VA*10
        parametersList_VVIR[7] = self.VPW*100
        parametersList_VVIR[9] = 1
        parametersList_VVIR[10] = self.VS*10
        parametersList_VVIR[11] = self.VRP
        parametersList_VVIR[13] = self.MSR
        parametersList_VVIR[14] = self.AT
        parametersList_VVIR[15] = self.ReaT
        parametersList_VVIR[16] = self.ResF
        parametersList_VVIR[17] = self.RecT
        parametersList_VVIR[18] = 1
        parametersList_VVIR[19] = 16
        parametersList_VVIR[20] = 55
    def change(self):
        layout = [
            [sg.Text("Changing values of VVIR")],
            [sg.Text("",key="status")],
            [sg.Text('LRL: ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL: ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('VA: ' + str(self.VA) + "V",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('VPW: ' + str(self.VPW) + "ms",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Text('VS: ' + str(self.VS) + "ms",key="t5"), sg.Button('+', key="B5+"), sg.Button('-', key="B5-")],
            [sg.Text('VRP: ' + str(self.VRP) + "ms",key="t6"), sg.Button('+', key="B6+"), sg.Button('-', key="B6-")],          
            #Rate adaptive variables
            [sg.Text('MSR: ' + str(self.MSR) + "ppm",key="t7"), sg.Button('+', key="B7+"), sg.Button('-', key="B7-")],
            [sg.Text('AT: ' + str(self.AT),key="t8"), sg.Button('V-Low', key="B8VL"), sg.Button('Low', key="B8L")], 
            [sg.Button('Med-Low', key="B8ML"), sg.Button('Med', key="B8M")], 
            [sg.Button('Med-High', key="B8MH"), sg.Button('High', key="B8H"), sg.Button('V-High', key="B8VH")],
            [sg.Text('ReaT: ' + str(self.ReaT) + "sec",key="t9"), sg.Button('+', key="B9+"), sg.Button('-', key="B9-")],
            [sg.Text('ResF: ' + str(self.ResF),key="t10"), sg.Button('+', key="B10+"), sg.Button('-', key="B10-")],
            [sg.Text('RecT: ' + str(self.RecT) + "min",key="t11"), sg.Button('+', key="B11+"), sg.Button('-', key="B11-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('VVIR', layout, font=('Helvetica',14), element_justification='c', size=(450,800))

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
#RATE ADAPTIVE MODES:
            if event == "B7+":
                if((float(self.MSR) >= 50) and (float(self.MSR) < 175)):
                    self.MSR = float(self.MSR) + 5
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B7-":
                if (float(self.MSR) - 5 <= float(self.URL)):
                    window['status'].update('MSR cannot be lower than URL')
                elif((float(self.MSR) > 50) and (float(self.MSR) <= 175)):
                    self.MSR = float(self.MSR) - 5
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B8VL":
                self.AT = "V-Low";
            if event == "B8L":
                self.AT = "Low";
            if event == "B8ML":
                self.AT = "Med-Low";
            if event == "B8M":
                self.AT = "Med";
            if event == "B8M":
                self.AT = "Med-High";
            if event == "B8H":
                self.AT = "High";
            if event == "B8VH":
                self.AT = "V-High";

            if event == "B9+":
                if(int(float(self.ReaT)) >= 10) and ((int(float(self.ReaT))  < 50)):
                    self.ReaT = float(self.ReaT) + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B9-":
                if((int(float(self.ReaT))  > 10) and (int(float(self.ReaT))  <= 50)):
                    self.ReaT = float(self.ReaT) - 10
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B10+":
                if((int(float(self.ResF))  >= 1) and (int(float(self.ResF))  < 16)):
                    self.ResF = float(self.ResF) + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B10-":
                if((int(float(self.ResF))  > 1) and (int(float(self.ResF)) <= 16)):
                    self.ResF = int(float(self.ResF)) - 1
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B11+":
                if((float(self.RecT) >= 2) and (float(self.RecT) < 16)):
                    self.RecT = float(self.RecT) + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B11-":
                if((float(self.RecT) > 2) and (float(self.RecT) <= 16)):
                    self.RecT = float(self.RecT) - 1
                else:
                    window['status'].update('Value cannot decrease further')

            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('VA: ' + str(self.VA) + "V")
            window['t4'].update('VPW: ' + str(self.VPW) + "ms")
            window['t5'].update('VS: ' + str(self.VS) + "V")
            window['t6'].update('VRP: ' + str(self.VRP) + "ms")
#RATE ADAPTIVE MODES:
            window['t7'].update('MSR: ' + str(self.MSR) + "ppm")
            window['t8'].update('AT: ' + str(self.AT))
            window['t9'].update('ReaT: ' + str(self.ReaT) + "sec")
            window['t10'].update('ResF: ' + str(self.ResF))
            window['t11'].update('RecT: ' + str(self.RecT) + "min")
        # Finish up by removing from the screen
            parametersList_VVIR[1] = 1
            parametersList_VVIR[2] = self.LRL
            parametersList_VVIR[3] = self.URL
            parametersList_VVIR[5] = self.VA*10
            parametersList_VVIR[7] = self.VPW*100
            parametersList_VVIR[9] = 1
            parametersList_VVIR[10] = self.VS*10
            parametersList_VVIR[11] = self.VRP
            parametersList_VVIR[13] = self.MSR
            parametersList_VVIR[14] = self.AT
            parametersList_VVIR[15] = self.ReaT
            parametersList_VVIR[16] = self.ResF
            parametersList_VVIR[17] = self.RecT
            parametersList_VVIR[18] = 1
            parametersList_VVIR[19] = 16
            parametersList_VVIR[20] = 55
        window.close()