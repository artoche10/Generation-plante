from random import random

import numpy as np

from GiveSecAxis import GiveSecAxis
from ReadImageParam import ReadImageParam
from GiveSecRootDiametre import GiveRootSecDiametre

def TraceSecRoots(Matrice, MatriceLog, nbRacinesSec):
    tailleimage = ReadImageParam()[0]


    for i in range(nbRacinesSec):
        indiceLigne = 1000 + round(i * random() * 1500)
        if indiceLigne<tailleimage:

            AxeLigne1 = int(MatriceLog[indiceLigne][0])
            AxeColonne = int(MatriceLog[indiceLigne][1])
            largeur = MatriceLog[indiceLigne][3]-MatriceLog[indiceLigne][2]

            Matrice,MatriceLogSec = GiveSecAxis(AxeLigne1,AxeColonne,Matrice,MatriceLog)
            Matrice = GiveRootSecDiametre(Matrice,MatriceLogSec,largeur)

    return Matrice
