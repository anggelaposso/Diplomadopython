# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:35:45 2022

@author: Angela Posso
"""
"""
correo: angela.posso@upb.edu.co
identificación: 502224
"""
"""
A partir de los valores independientes 
(volumen, peso y producción de CO2) predecir el comportamiento 
de la variable dependiente (marca del carro.)
"""
#Importamos librerias
import pandas as pd
from sklearn import linear_model

#Leemos archivo csv con pandas y creamos df
cars_df = pd.read_csv("cars.csv")

#Variables independientes
x = cars_df[["Weight", "Volume", "CO2"]]

#Creamos función
def funcion_car(marca_c):
      if marca_c == "Audi":
        return 1

      elif marca_c == "BMW":
        return 2
  
      elif marca_c == "Fiat":
        return 3
 
      elif marca_c == "Ford":
       return 4
 
      elif marca_c == "Honda":
       return 5

      elif marca_c == "Hundai":
       return 6

      elif marca_c == "Mazda":
       return 7

      elif marca_c == "Mercedes":
       return 8

      elif marca_c == "Mini":
       return 9

      elif marca_c == "Mitsubishi":
       return 10

      elif marca_c == "Opel":
       return 11

      elif marca_c == "Skoda":
       return 12

      elif marca_c == "Suzuki":
       return 13

      elif marca_c == "Toyoty":
       return 14

      elif marca_c == "VW":
       return 15

      elif marca_c == "Volvo":
       return 16

      elif marca_c == "Hyundai":
       return 17
   
#Valores de la variable dependiente
y = cars_df ["Car"].apply(funcion_car)
   
#Regresión 
reg_mod = linear_model.LinearRegression()
reg_mod.fit(x, y)

#Predicción
predic_co2 = reg_mod.predict([[765, 900, 90]])
print(predic_co2)

