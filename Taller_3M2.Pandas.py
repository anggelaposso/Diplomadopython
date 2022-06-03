# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 17:04:32 2022

@author: Angela Posso
"""
"""
correo: angela.posso@upb.edu.co
Identificación: 502224
"""

importar  pandas  como  pd

mis_datos  =  pd . read_excel ( r'C:\Users\Angela Posso \my_python\Spyder\Estudiantes.xlsx' , sheet_name = 'Estudiantes' )

       
mis_datos [ "imc" ] =  round ( mis_datos [ 'peso (kg)' ] / ( mis_datos [ 'altura' ] ** 2 ))


n_imc  =  len ( mis_datos [ 'imc' ])
n_nombre  =  len ( mis_datos [ 'Nombre' ])
índice  =  0

mientras que  índice  <  n_imc :
    print ( "Indice de masa corporal: "  +  str ( my_data [ 'imc' ][ index ]) +  " "  +  my_data [ 'Nombre' ][ index ])
    índice  +=  1
    
imprimir ( " " )



capital_final  =  mis_datos [ 'Dinero a invertir' ] * (( mis_datos [ 'Interes anual' ] / 100 + 1 ) ** mis_datos [ 'Años de inversión' ])
print ( "El final de la capital es: " )
imprimir ( capital_final )
imprimir ( " " )




precio_pan  =  15000

def  calcular_descuento ( tiempo ):
    
    si el  tiempo  <=  6 :
        volver  0.1
    
    elif ( tiempo  >  6 ) & ( tiempo  <=  12 ):
        volver  0.2
    
    elif ( tiempo  >  12 ) & ( tiempo  <= 18 ):
        volver  0.3
    
    más :
        volver  0.4
    
mis_datos [ "Descuento" ] =  mis_datos [ 'HoraCompra (h)' ]. aplicar ( calcular_descuento )
mis_datos [ "Precio_final" ] =  precio_pan  -  mis_datos [ 'Descuento' ]    
    

def  funcion_extension ( sexo ):
    if  sexo  ==  "Masculino" :
        volver  11
    
    elif  sexo  ==  "Femenino" :
        volver  10
mis_datos [ "Extension_Num" ] =  mis_datos [ 'Sexo' ]. aplicar ( funcion_extension )    


n_numext  =  len ( my_data [ 'Extension_Num' ])
auxiliar  =  0
    
while  aux  <  n_numext :
    print ( "+ "  +  mis_datos [ 'Numero telefonico' ][ aux ] +  " - "  +  str ( mis_datos [ 'Extension_Num' ][ aux ]))
    auxiliar +=  1