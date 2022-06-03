# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:49:46 2022

@author: Angela Posso
"""
"""
correo: angela.posso@upb.edu.co
Id: 502224
"""

importar  pandas  como  pd

mis_datos  =  pd . read_csv ( 'netflix_titles.csv' )

imprimir ( mis_datos . cabeza ())
imprimir ( mis_datos . cola ())


imprimir ( mis_datos . dtypes )

mis_datos . to_excel ( "Netflix_list.xlsx" , sheet_name  =  "títulos" , index = False )


nuevadata  =  mis_datos [[ 'tipo' , 'duración' , 'descripción' , 'país' ]]


mis_datos [ "duracion" ] =  pd . to_numeric ( my_data [ 'duración' ]. reemplazar ( '([^0-9]*)' , '' , regex = True ), errores = 'coaccionar' )
dum  =  mis_datos [ mis_datos [ 'duracion' ] >  100   ]
imprimir _ _ _

filtv  =  mis_datos [( mis_datos [ 'tipo' ] ==  'Programa de TV' ) & ( mis_datos [ 'duración' ] >  '3 Temporadas' )]

newopeli  =  mis_datos [[ 'título' , 'descripción' ]]

mis_datos . iloc [: 6 , 8 ] =  'ninguno'
imprimir ( mis_datos . cabeza ())

mis_datos . loc [: 2 , 'país' ] =  'nan'
imprimir ( mis_datos . cabeza ())


mis_datos . iloc [: 5 , 0 ] =  's5'
mis_datos . loc [: 8801 , 'mostrar id' ] =  'nan'
mis_datos . iloc [: 1 , 9 ] =  '1 Hora 30 min'


                
importar  numpy  como  np

mis_datos [ "Visto" ] =  np . al azar randint ( 0 , 2 , mis_datos . forma [ 0 ])