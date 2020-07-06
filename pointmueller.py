from nuueomueller import Mueller ,Luchiman
import numpy as np

sample = Mueller()

muellermatrix = sample.mueller()
lc = Luchiman(muellermatrix)

D_value = lc.diattenuation('D_value')
P_value = lc.diattenuation('P_value')
diattenuationMatrix = lc.diattenuation('matrix')

Delta_value = lc.depolarization('Delta_value')
depolarizationMatrix = lc.depolarization('matrix')
retardanceMatrix = lc.retardance('matrix')
R_value = lc.retardancevalue('R_value')
linear_value = lc.retardancevalue('linear')
opticalactivity_value = lc.retardancevalue('opticalactivity')
theta_value = lc.retardancevalue('theta')

print('穆勒矩陣: \n',np.array(muellermatrix,dtype=int))
print('衰減矩陣: \n',np.array(diattenuationMatrix,dtype=int))
print('去極化矩陣: \n',np.array(depolarizationMatrix,dtype=int))
print('相位延遲矩陣: \n',np.array(retardanceMatrix,dtype=int))
print('衰減能力: \n',int(D_value))
print('極化能力: \n',int(P_value))
print('去極化能力: \n',int(Delta_value))
print('相位延遲量 \n',R_value,'°')
print('線性延遲量: \n',linear_value,'°')
print('旋光性: \n',opticalactivity_value,'°')
print('方位角: \n',theta_value,'°')


