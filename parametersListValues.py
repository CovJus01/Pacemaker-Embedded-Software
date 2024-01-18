from AOO import *
from VOO import *
from AAI import * 
from VVI import *
from DOO import *
from DOOR import *
from AOOR import * 
from VOOR import *
from AAIR import *
from VVIR import *
from serialComm import *

global parametersList
parametersList = [0]*21
parametersList[19] = 16
parametersList[20] = 55

def updateParamsList_AOO(self):         #sandy
    parametersList[0] = True
    parametersList[2] = self.LRL
    parametersList[3] = self.URL
    parametersList[4] = self.AA
    parametersList[6] = self.APW

def updateParamsList_VOO(self):
    parametersList[1] = True
    parametersList[2] = self.LRL
    parametersList[3] = self.URL
    parametersList[5] = self.VA
    parametersList[7] = self.VPW

def updateParamsList_AAI(self):         #sandy
    parametersList[0] = True
    parametersList[2] = self.LRL
    parametersList[3] = self.URL
    parametersList[4] = self.AA
    parametersList[6] = self.APW
    parametersList[8] = True
    parametersList[10] = self.AS
    parametersList[11] = self.ARP

def updateParamsList_VVI(self):
    parametersList[1] = True
    parametersList[2] = self.LRL
    parametersList[3] = self.URL
    parametersList[5] = self.VA
    parametersList[7] = self.VPW
    parametersList[9] = True
    parametersList[10] = self.VS
    parametersList[11] = self.VRP

def updateParamsList_DOO(self):
    parametersList[0] = True
    parametersList[1] = True
    parametersList[2] = self.LRL   
    parametersList[3] = self.URL
    parametersList[4] = self.AA
    parametersList[5] = self.VA
    parametersList[6] = self.APW
    parametersList[7] = self.VPW
    parametersList[12] = self.FAVD
    
def updateParamsList_DOOR(self):
    parametersList[0] = True
    parametersList[1] = True
    parametersList[2] = self.LRL   
    parametersList[3] = self.URL
    parametersList[4] = self.AA
    parametersList[5] = self.VA
    parametersList[6] = self.APW
    parametersList[7] = VPW
    parametersList[12] = FAVD
    parametersList[13] = MSR
    parametersList[14] = AT
    parametersList[15] = ReaT
    parametersList[16] = ResF
    parametersList[17] = RecT

def updateParamsList_AAIR(self):
    parametersList[0] = True
    parametersList[2] = LRL   
    parametersList[3] = URL
    parametersList[4] = AA
    parametersList[6] = APW
    parametersList[8] = True
    parametersList[10] = AS
    parametersList[11] = ARP
    #parametersList[0] = PVARP add PVARP to list!
    parametersList[13] = MSR
    parametersList[14] = AT
    parametersList[15] = ReaT
    parametersList[16] = ResF
    parametersList[17] = RecT