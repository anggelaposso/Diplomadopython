# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:21:43 2022

@author: Angela Posso
"""

#Import librerias
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy import stats

#Leemos archivo csv con pandas y creamos df
#aires_df = pd.excel("AirQualityUCI.xlsx")
aires_df  =  pd . read_excel ( r'C:\Users\Angela Posso\My_python\DiplomadoUpb\AirQualityUCI.xlsx' , sheet_name = 'AirQualityUCI' )

# Definimos las variables x, y 
# x NOx(GT)
# y NO2(GT)

#2. Seleccione las parejas x y del dataset para utilizarlos 
# en una regresión lineal y polinomial.
x = aires_df['NOx(GT)'][0: 8000]
y = aires_df['NO2(GT)'][0: 8000]
#5. Las variables escogidas son libres.

#PT08. S3 (óxido de tungsteno) 
#respuesta del sensor promediada por hora (nominalmente dirigida a NOx)
# PT08. S4 (óxido de tungsteno) 
#respuesta media del sensor por hora (nominalmente dirigida a NO2)

#Diagrama de disperción
#3. Grafique el diagrama de dispersión
plt.scatter(x, y)
plt.show
plt.xlabel('NOx')
plt.ylabel('NO2')
plt.title('PT08 S3 % PT08 S4')

#4. Verifique el r de relación
x = aires_df['NOx(GT)'][0: 8000]
y = aires_df['NO2(GT)'][0: 8000]

slope, intercept, r,p, std_err = stats.linregress(x,y)

print(r)

#Valores futuros
x = aires_df['NOx(GT)'][0: 8000]
y = aires_df['NO2(GT)'][0: 8000]
slope, intercept, r,p, std_err = stats.linregress(x,y)

def funcion(x):
    return slope * x + intercept

speed = funcion(10)

print(speed)










