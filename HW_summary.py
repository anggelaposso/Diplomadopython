# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 08:33:12 2022

@author: Angela Posso
"""
"""correo: angela.posso@upb.edu.co
identificación: 502224
"""

# Importamos librerias
# libreria utilizada para el preprocesamiento de los datos.

# Funcion para escalar los datos
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn import linear_model
import matplotlib.pyplot as plt
scale = StandardScaler()

# ----------------PUNTO #1----------------
# Leemos los archivos csv con pandas y creamos df
#cars2_df = pd.read_csv (r'C:\Users\Angela Posso\My_python\DiplomadoUpb\cars2.csv', sheet_name = 'cars2')
cars_df = pd.read_csv('cars2.csv')
#netflix_pd = pd.read_csv('netflix_titles.csv')
#student_pd = pd.read_csv('student_data.csv')

# Definimos variables dependientes para datos cars
X = cars_df[['Weight', 'Volume']]

# Definimos variable independiente para datos cars
y = cars_df[['CO2']]

# -------------PUNTO #2--------------------
# Realice una estandarización de todos los valores
# dentro del DataFrame.

scale_cars  = StandardScaler()
# Aplicando el escalado.
scale_cars  = (cars_df["Weight"]-cars_df["Weight"].mean())/cars_df["Weight"].std()
# Teniendo en cuenta la media y desviación.

# Se muestran los valores escalados.
print(scale_cars )

#Train / Test
X_train_cars = scale_cars[:28]
y_train_cars = y[:28]

X_test_cars = scale_cars[28:]
y_test_cars = y[28:]

# Grafica de variables
plt.scatter(X_train_cars,y_train_cars)
plt.show()

plt.scatter(X_test_cars, y)
plt.show()

# Modelo de regresion para las variables dependientes e independientes.
poli_cars =  np.poly1d(np.polyfit(X_train_cars,y,4))
# se ajusta el modelo a los datos escalados
myline = np.linspace(0,2,100)
poli_new_y = poli_cars(myline)

poli_cars =  np.poly1d(np.polyfit(X_train_cars,y_train_cars,4))
myline = np.linspace(0,2,100)
poli_new_y = poli_cars(myline)

# -------------PUNTO #3--------------------
# Evidencie el diagrama de dispersión
# (si es posible) para los datos.
plt.scatter(X_train_cars,y)
plt.plot(myline,poli_new_y )
plt.show()


# -------------PUNTO #4--------------------
# Haga una división entre los datos, teniendo en cuenta
# los porcentajes 80%-20% para train/test respectivamente.
poli_cars =  np.poly1d(np.polyfit(X_train_cars, y,4))
myline = np.linspace(0,2,100)
poli_new_y = poli_cars(myline)

# -------------PUNTO #5,6--------------------
# Proceda a mostrar sus conjuntos de datos train/test
# en sus respectivos scatters plots.
plt.scatter(X_train_cars,y)
plt.plot(myline,poli_new_y )
plt.show()

# -------------PUNTO #7--------------------
# Determine el valor de r de relación para evidenciar
# el funcionamiento optimo o no del modelo.
r2_train = r2_score(y, poli_cars(X_train_cars))
print(r2_train)

r2_test = r2_score(y, poli_cars(X_test_cars))
print(r2_test)


# -------------PUNTO #8--------------------
# Predecir el comportamiento de la variable dependiente
# Usando valores estandarizados.
print(poli_cars(0.1))



# ----------------PUNTO #1,2----------------
# Leemos los archivos csv con pandas y creamos df
netflix_df["duracion"] = pd.to_numeric(netflix_df['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')

condiciones2 = [
    (netflix_df["duration"].str.contains("Season").astype(np.bool_)),
    (netflix_df["duration"].str.contains("min").astype(np.bool_))
    ]
selecciones2 = [1.0, 2.0]
netflix_df["duration_type"] =  np.select(condiciones2, selecciones2, default='Not Specified')

# Definimos variables dependientes para datos netflix
y = netflix_df["duracion"][:2000] 

# Definimos variable independiente para datos netflix
X = netflix_df[["Cod_type","duration_type"]][:2000]    

# -------------PUNTO #3,4,5--------------------
# Realice una estandarización de todos los valores
# dentro del DataFrame.
scale_netflix = StandardScaler()
scale_netflix_df =scale_netflix.fit_transform(X)


#Train / Test
train_netflix = scale_netflix[:1600]
train_netflix = y[:1600]

test_netflix = scale_netflix[1600:]
test_netflix = y[1600:]

# -------------PUNTO #6--------------------
# A partir de los valores independientes seleccionados
# cree el modelo de regresión para ajustar los datos.
# Modelo de regresion para las variables dependientes e independientes.
modelo_netflix = linear_model.LinearRegression()
modelo_netflix.fit(train_netflix,y)


# -------------PUNTO #7--------------------
# Determine el valor de r de relación para evidenciar
# el funcionamiento optimo o no del modelo.
r2_train = r2_score(y, modelo_netflix.predict(train_netflix))
print(r2_train)

r2_test = r2_score(y, modelo_netflix.predict(test_netflix))
print(r2_test)


# -------------PUNTO #8--------------------
# Predecir el comportamiento de la variable dependiente
# Usando valores estandarizados.
#Prediccion del modelo
pred_scale_netflix = modelo_netflix.predict([test_netflix[0]])
print(pred_scale_netflix)


# ----------------PUNTO #1,2----------------
# Leemos los archivos csv con pandas y creamos df
student_pd = pd.read_csv('student_data.csv')

# Definimos variables dependientes para datos student
y = student_df["health"]

# Definimos variable independiente para datos student
X = student_df[["age","freetime"]]     

# -------------PUNTO #3,4,5--------------------
# Realice una estandarización de todos los valores
# dentro del DataFrame.
scale_student = StandardScaler()
scale_student =scale_student.fit_transform(X)


#Train / Test
train_student = scale_student[:519]
train_student = y[:519]

test_student = scale_student[519:]
test_student = y[519:]

# -------------PUNTO #6--------------------
# A partir de los valores independientes seleccionados
# cree el modelo de regresión para ajustar los datos.
# Modelo de regresion para las variables dependientes e independientes.
modelo_student = linear_model.LinearRegression()
modelo_student.fit(train_student,y)


# -------------PUNTO #7--------------------
# Determine el valor de r de relación para evidenciar
# el funcionamiento optimo o no del modelo.
r2_train = r2_score(train_student, modelo_student.predict(train_student))
print(r2_train)

r2_test = r2_score(y, modelo_student.predict(test_student))
print(r2_test)

# -------------PUNTO #8--------------------
# Predecir el comportamiento de la variable dependiente
# Usando valores estandarizados.
#Prediccion del modelo
pred_scale_student = modelo_student.predict([test_student[0]])
print(pred_scale_student)