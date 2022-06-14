# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:41:09 2022

@author: Angela Posso
"""
"""
correo: angela.posso@upb.edu.co
identificación: 502224
"""
#--------------------PUNTO 1,2--------------------------
#Importamos librerias
import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import pydotplus

#--------------------PUNTO 3----------------------------
#Creamos el df
carseats = sm.datasets.get_rdataset("Carseats", "ISLR")
datos = carseats.data
print(carseats.__doc__)

#-------------------PUNTO 4------------------------------
#Reemplazamos los valores NO númericos.
d= {'Yes':1, 'No':0}
d1= {'Bad':0, 'Medium':1, 'Good':2}
datos["Urban"] = datos["Urban"].map(d)
datos["US"] = datos["US"].map(d)
datos["ShelveLoc"] = datos["ShelveLoc"].map(d1)

#------------------PUNTO 5-------------------------------
datos['ventas_altas'] = np.where(datos.Sales > 8, 0, 1)
datos = datos.drop(columns = 'Sales')

features = ["CompPrice","Income","Advertising", "Population","Price","ShelveLoc","Age","Education","Urban","US"]

X = datos[features]
y = datos["ventas_altas"]

#------------------PUNTO 6,7-------------------------------
#------------CREAMOS ARBOL DE DESICIÓN-------------------
dtree = DecisionTreeClassifier()
dtree  = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file = None, feature_names= features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
img = pltimg.imread("mydecisiontree.png")
imgplot = plt.imshow(img)
plt.show()


