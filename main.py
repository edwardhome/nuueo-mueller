import numpy as np
import os
from nuueomueller import Luchiman, Mueller, Differential
from tool import  initial, imageread,im_show, export

initial()
data = imageread('tif')
pixel =data[0].shape[0]
muellerimage = np.empty([4*pixel,4*pixel],dtype=float)
diattenuationMatriximage = np.empty([4*pixel,4*pixel],dtype=float)
depolarizationMatriximage  = np.empty([4*pixel,4*pixel],dtype=float)
retardanceMatriximage = np.empty([4*pixel,4*pixel],dtype=float)

differentialMatriximage= np.empty([4*pixel,4*pixel],dtype=float)
lorentz_mMatriximage= np.empty([4*pixel,4*pixel],dtype=float)
lorentz_uMatriximage= np.empty([4*pixel,4*pixel],dtype=float)

D_value_image = np.empty([pixel,pixel],dtype=float)
P_value_image= np.empty([pixel,pixel],dtype=float)
Delta_value_image= np.empty([pixel,pixel],dtype=float)
R_value_image= np.empty([pixel,pixel],dtype=float)
linear_value_image= np.empty([pixel,pixel],dtype=float)
opticalactivity_value_image= np.empty([pixel,pixel],dtype=float)
theta_value_image= np.empty([pixel,pixel],dtype=float)

diattenuatuon_image= np.empty([pixel,pixel],dtype=float)
depolarization_image= np.empty([pixel,pixel],dtype=float)
Retardance_image= np.empty([pixel,pixel],dtype=float)
LinearRetardance_image= np.empty([pixel,pixel],dtype=float)
opticalactivity2_value_image= np.empty([pixel,pixel],dtype=float)
theta2_value_image= np.empty([pixel,pixel],dtype=float)

X = pixel
for m in range(pixel):
    for n in range(pixel):
        sample = Mueller()
        muellermatrix = sample.mueller(data[1][m,n],data[2][m,n],data[3][m,n],data[4][m,n],data[5][m,n],data[6][m,n],data[7][m,n],data[8][m,n],data[9][m,n],data[10][m,n],data[11][m,n],data[12][m,n],data[13][m,n],data[14][m,n],data[15][m,n],data[16][m,n])
        lc = Luchiman(muellermatrix)
        df = Differential(muellermatrix)
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
        differential = df.differential('differentialmatrix')
        lorentz_mMatrix = df.differential('Lorentz_m')
        lorentz_uMatrix = df.differential('Lorentz_u')
        diattenuatuon = df.diattenuatuon('D')
        depolarization = df.depolarization('Delta')
        Retardance = df.retardance('R')
        LinearRetardance = df.retardance('delta')
        opticalactivity2_value = df.retardance('Psi')
        theta2_value = df.retardance('theta')

        i =0
        j = 0
        for i in range(4):
            for j in range(4):
                muellerimage[m+pixel*i,n+pixel*j] = muellermatrix[i,j]
                diattenuationMatriximage[m+pixel*i,n+pixel*j]=diattenuationMatrix[i,j]
                depolarizationMatriximage[m+pixel*i,n+pixel*j]=depolarizationMatrix[i,j]
                retardanceMatriximage[m+pixel*i,n+pixel*j] = retardanceMatrix[i,j]
                differentialMatriximage[m+pixel*i,n+pixel*j]=differential[i,j]
                lorentz_mMatriximage[m+pixel*i,n+pixel*j]=lorentz_mMatrix[i,j]
                lorentz_uMatriximage[m+pixel*i,n+pixel*j]=lorentz_uMatrix[i,j]
        D_value_image[m,n]=D_value
        P_value_image[m,n]=P_value
        R_value_image[m,n]=R_value
        Delta_value_image[m,n]=Delta_value
        linear_value_image[m,n]=linear_value
        opticalactivity_value_image[m,n]=opticalactivity_value
        theta_value_image[m,n]=theta_value
        diattenuatuon_image[m,n]= diattenuatuon
        depolarization_image[m,n]=depolarization
        Retardance_image[m,n]=Retardance
        LinearRetardance_image[m,n]=LinearRetardance
        opticalactivity2_value_image[m,n]=opticalactivity2_value
        theta2_value_image[m,n]=theta2_value
    os.system('cls' if os.name == 'nt' else 'clear')
    print('目前進度：',round(m/X*100,2),'%','='*int(m/X*100),'>')

export(-1,muellerimage,'Mueller Matrix','polar_decomposition')
export(-1,diattenuationMatriximage,'Diattenuation Matrix','polar_decomposition')
export(-1,depolarizationMatriximage,'Depolarization Matrix','polar_decomposition')
export(-1,retardanceMatriximage,'Retardance Matrix','polar_decomposition')
export(0,D_value_image,'Diattenuatuon','polar_decomposition')
export(0,P_value_image,'Polarizance','polar_decomposition')
export(0,Delta_value_image,'Depolarization','polar_decomposition')
export(180,R_value_image,'Retardance','polar_decomposition')
export(180,linear_value_image,'Linear Retardance','polar_decomposition')
export(90,opticalactivity_value_image,'Optical activity','polar_decomposition')
export(90,theta_value_image,'Orientation','polar_decomposition')
export(-1,muellerimage,'Mueller Matrix','differential_decomposition')
export(-1,differentialMatriximage,'Differential Matrix','differential_decomposition')
export(-1,lorentz_mMatriximage,'Lorentz_m Matrix','differential_decomposition')
export(-1,lorentz_uMatriximage,'Lorentz_u Matrix','differential_decomposition')
export(0,diattenuatuon_image,'Diattenuatuon','differential_decomposition')
export(0,depolarization_image,'Depolarization','differential_decomposition')
export(180,Retardance_image,'Retardance','differential_decomposition')
export(180,LinearRetardance_image,'Linear Retardance','differential_decomposition')
export(90,opticalactivity2_value_image,'Optical activity','differential_decomposition')
export(90,theta2_value_image,'Orientation','differential_decomposition')

os.system('cls' if os.name == 'nt' else 'clear')
print('完成')