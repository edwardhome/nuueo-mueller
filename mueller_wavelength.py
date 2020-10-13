import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from nuueomueller import Luchiman, Mueller


database = pd.read_excel('Lu_chipman.xlsx',sheet_name=0,header=0,index_col='wavelength')

wavelength = pd.Series.tolist(database.index)
element =  pd.Series.tolist(database.columns)

#將Database數據轉為變數陣列
for i in range(1,5):
    for j in range(1,5):
        element_str = str(f'M{i}{j}')
        exec(f'M{i}{j}'+ '=' + f'pd.Series.tolist(database.M{i}{j})')  

num = len(wavelength) #總運算次數
D_value = []
P_value = []
Delta_value =[]
R_value =[]
linear_value = []
opticalactivity_value = []
theta_value = []
for i in range(num):
    muellermatrix = np.array([[M11[i],M12[i],M13[i],M14[i]],
                             [M21[i],M22[i],M23[i],M24[i]],
                             [M31[i],M32[i],M33[i],M34[i]],
                             [M41[i],M42[i],M43[i],M44[i]]])

    lc = Luchiman(muellermatrix)
    D_value += [lc.diattenuation('D_value')]
    P_value += [lc.diattenuation('P_value')]
    Delta_value += [lc.depolarization('Delta_value')]
    #R_value += [lc.retardancevalue('R_value')]
    #linear_value += [lc.retardancevalue('linear')]
    #opticalactivity_value += [lc.retardancevalue('opticalactivity')]
    #theta_value += [lc.retardancevalue('theta')]

plt.plot(wavelength,D_value,'*')
plt.plot(wavelength,P_value,'-')
plt.plot(wavelength,Delta_value)
plt.legend(['Diattenuation','Polarizance','Delta_value'],loc='lower left')
plt.title('Diattenuation, polarizance and Depolarization')
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.ylim([-1,1])
plt.show()
