##add PVARP to this file!
import PySimpleGUI as sg
from decimal import Decimal
import pandas as pd 
import csv

global parametersList_AAIR
parametersList_AAIR = [0]*21

class AAIR():
    
    def __init__(self, name, LRL, URL, AA, APW, AS, ARP, PVARP, MSR, AT, ReaT, ResF, RecT): #parameters
        self.name = name#name of user
        self.LRL = LRL   
        self.URL = URL
        self.AA = AA
        self.APW = APW
        self.AS = AS
        self.ARP = ARP
        self.PVARP = PVARP
        self.MSR = MSR
        self.AT = AT
        self.ReaT = ReaT
        self.ResF = ResF
        self.RecT = RecT
        parametersList_AAIR[0] = 1
        parametersList_AAIR[2] = LRL   
        parametersList_AAIR[3] = URL
        parametersList_AAIR[4] = AA*10
        parametersList_AAIR[6] = APW*100
        parametersList_AAIR[8] = 1
        parametersList_AAIR[10] = AS*10
        parametersList_AAIR[11] = ARP
        #parametersList_AAIR[0] = PVARP add PVARP to list!
        parametersList_AAIR[13] = MSR
        parametersList_AAIR[14] = AT
        parametersList_AAIR[15] = ReaT
        parametersList_AAIR[16] = ResF
        parametersList_AAIR[17] = RecT
        parametersList_AAIR[19] = 16
        parametersList_AAIR[20] = 55

        #User must write their input into the Input space and then press the corresponding button to load the value

    def set_from_csv(self):#Obtains values from 1nd row in the users CSV file
        col_list = ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12"]
        df = pd.read_csv("Database_CSV/" + str(self.name) + ".csv", usecols=col_list)
        self.LRL = int(df.loc[7, "P1"])
        self.URL = int(df.loc[7, "P2"])
        self.AA = float(df.loc[7, "P3"])
        self.APW = float(df.loc[7, "P4"])
        self.AS = float(df.loc[7, "P5"])
        self.ARP = float(df.loc[7, "P6"])
        self.PVARP = float(df.loc[7, "P7"])
        self.MSR = float(df.loc[7, "P8"])
        self.AT = str(df.loc[7, "P9"])
        self.ReaT = float(df.loc[7, "P10"])
        self.ResF = float(df.loc[7, "P11"])
        self.RecT = float(df.loc[7, "P12"])
        parametersList_AAIR[0] = 1
        parametersList_AAIR[2] = self.LRL   
        parametersList_AAIR[3] = self.URL
        parametersList_AAIR[4] = self.AA*10
        parametersList_AAIR[6] = self.APW*100
        parametersList_AAIR[8] = 1
        parametersList_AAIR[10] = self.AS*10
        parametersList_AAIR[11] = self.ARP
        #parametersList_AAIR[0] = self.PVARP add PVARP to list!
        parametersList_AAIR[13] = self.MSR
        parametersList_AAIR[14] = self.AT
        parametersList_AAIR[15] = self.ReaT
        parametersList_AAIR[16] = self.ResF
        parametersList_AAIR[17] = self.RecT
        parametersList_AAIR[19] = 16
        parametersList_AAIR[20] = 55

    def change(self):
        layout = [
            [sg.Text("Changing values of AAIR")],
            [sg.Text("",key="status")],
            [sg.Text('LRL: ' + str(self.LRL) + "ppm",key="t1"), sg.Button('+', key="B1+"), sg.Button('-', key="B1-")],
            [sg.Text('URL: ' + str(self.URL) + "ppm",key="t2"), sg.Button('+', key="B2+"), sg.Button('-', key="B2-")],
            [sg.Text('AA: ' + str(self.AA) + "V",key="t3"), sg.Button('+', key="B3+"), sg.Button('-', key="B3-")],
            [sg.Text('APW: ' + str(self.APW) + "ms",key="t4"), sg.Button('+', key="B4+"), sg.Button('-', key="B4-")],
            [sg.Text('AS: ' + str(self.AS) + "ms",key="t5"), sg.Button('+', key="B5+"), sg.Button('-', key="B5-")],
            [sg.Text('ARP: ' + str(self.ARP) + "ms",key="t6"), sg.Button('+', key="B6+"), sg.Button('-', key="B6-")],
            [sg.Text('PVARP: ' + str(self.PVARP) + "ms",key="t7"), sg.Button('+', key="B7+"), sg.Button('-', key="B7-")],            
            #Rate adaptive variables
            [sg.Text('MSR: ' + str(self.MSR) + "ppm",key="t8"), sg.Button('+', key="B8+"), sg.Button('-', key="B8-")],
            [sg.Text('AT: ' + str(self.AT),key="t9"), sg.Button('V-Low', key="B9VL"), sg.Button('Low', key="B9L")], 
            [sg.Button('Med-Low', key="B9ML"), sg.Button('Med', key="B9M")], 
            [sg.Button('Med-High', key="B9MH"), sg.Button('High', key="B9H"), sg.Button('V-High', key="B9VH")],
            [sg.Text('ReaT: ' + str(self.ReaT) + "sec",key="t10"), sg.Button('+', key="B10+"), sg.Button('-', key="B10-")],
            [sg.Text('ResF: ' + str(self.ResF),key="t11"), sg.Button('+', key="B11+"), sg.Button('-', key="B11-")],
            [sg.Text('RecT: ' + str(self.RecT) + "min",key="t12"), sg.Button('+', key="B12+"), sg.Button('-', key="B12-")],
            [sg.Button('Quit')]
            ]

        # Create the window
        window = sg.Window('AAIR', layout, font=('Helvetica',14), element_justification='c', size=(450,800))

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
                if((float(self.AA) >= 0.5) and (float(self.AA) < 3.2)):
                    self.AA = round(float(self.AA) + 0.1, 5)
                elif(float(self.AA) == 3.2):
                    self.AA = round(3.5, 1)
                elif(float(self.AA) >= 3.5) and (float(self.AA) < 7.0):
                    self.AA = round(float(self.AA) + 0.5, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B3-":
                if((float(self.AA) > 0.5) and (float(self.AA) <= 3.2)):
                    self.AA = round(float(self.AA) - 0.1, 5)
                elif(float(self.AA) == 3.5):
                    self.AA = round(3.2, 1)
                elif(float(self.AA) > 3.5) and (float(self.AA) <= 7.0):
                    self.AA = round(float(self.AA) - 0.5, 5)
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B4+":
                if(float(self.APW) == 0.05):
                    self.APW = round(0.1, 1)
                elif(float(self.APW) >= 0.1) and (float(self.APW) < 1.9):
                    self.APW = round(float(self.APW) + 0.1, 5)
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B4-":
                if(float(self.APW) == 0.1):
                    self.APW = round(0.05, 2)
                elif(float(self.APW) > 0.1) and (float(self.APW) <= 1.9):
                    self.APW = round(float(self.APW)- 0.1, 1)
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
#RATE ADAPTIVE MODES:
            if event == "B8+":
                if((float(self.MSR) >= 50) and (float(self.MSR) < 175)):
                    self.MSR = float(self.MSR) + 5
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B8-":
                if (float(self.MSR) - 5 <= float(self.URL)):
                    window['status'].update('MSR cannot be lower than URL')
                elif((float(self.MSR) > 50) and (float(self.MSR) <= 175)):
                    self.MSR = float(self.MSR) - 5
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B9VL":
                self.AT = "V-Low";
            if event == "B9L":
                self.AT = "Low";
            if event == "B9ML":
                self.AT = "Med-Low";
            if event == "B9M":
                self.AT = "Med";
            if event == "B9M":
                self.AT = "Med-High";
            if event == "B9H":
                self.AT = "High";
            if event == "B9VH":
                self.AT = "V-High";

            if event == "B10+":
                if(int(float(self.ReaT)) >= 10) and ((int(float(self.ReaT))  < 50)):
                    self.ReaT = float(self.ReaT) + 10
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B10-":
                if((int(float(self.ReaT))  > 10) and (int(float(self.ReaT))  <= 50)):
                    self.ReaT = float(self.ReaT) - 10
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B11+":
                if((int(float(self.ResF))  >= 1) and (int(float(self.ResF))  < 16)):
                    self.ResF = float(self.ResF) + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B11-":
                if((int(float(self.ResF))  > 1) and (int(float(self.ResF)) <= 16)):
                    self.ResF = int(float(self.ResF)) - 1
                else:
                    window['status'].update('Value cannot decrease further')

            if event == "B12+":
                if((float(self.RecT) >= 2) and (float(self.RecT) < 16)):
                    self.RecT = float(self.RecT) + 1
                else:
                    window['status'].update('Value cannot increase further')
            if event == "B12-":
                if((float(self.RecT) > 2) and (float(self.RecT) <= 16)):
                    self.RecT = float(self.RecT) - 1
                else:
                    window['status'].update('Value cannot decrease further')

            window['t1'].update('LRL: ' + str(self.LRL) + "ppm")
            window['t2'].update('URL: ' + str(self.URL) + "ppm")
            window['t3'].update('AA: ' + str(self.AA) + "V")
            window['t4'].update('APW: ' + str(self.APW) + "ms")
            window['t5'].update('AS: ' + str(self.AS) + "V")
            window['t6'].update('ARP: ' + str(self.ARP) + "ms")
            window['t7'].update('PVARP: ' + str(self.PVARP) + "ms")
#RATE ADAPTIVE MODES:
            window['t8'].update('MSR: ' + str(self.MSR) + "ppm")
            window['t9'].update('AT: ' + str(self.AT))
            window['t10'].update('ReaT: ' + str(self.ReaT) + "sec")
            window['t11'].update('ResF: ' + str(self.ResF))
            window['t12'].update('RecT: ' + str(self.RecT) + "min")

            parametersList_AAIR[0] = 1
            parametersList_AAIR[2] = self.LRL   
            parametersList_AAIR[3] = self.URL
            parametersList_AAIR[4] = self.AA*10
            parametersList_AAIR[6] = self.APW*100
            parametersList_AAIR[8] = 1
            parametersList_AAIR[10] = self.AS*10
            parametersList_AAIR[11] = self.ARP
            #parametersList_AAIR[0] = self.PVARP add PVARP to list!
            parametersList_AAIR[13] = self.MSR
            parametersList_AAIR[14] = self.AT
            parametersList_AAIR[15] = self.ReaT
            parametersList_AAIR[16] = self.ResF
            parametersList_AAIR[17] = self.RecT
            parametersList_AAIR[19] = 16
            parametersList_AAIR[20] = 55
        # Finish up by removing from the screen
        window.close()
