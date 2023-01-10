############################## LIBRERIAS ################################

import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import plotly_express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from IPython.display import IFrame
import streamlit.components.v1 as components

####################### CONFIGURACION PAGINA #####################

st.set_page_config(page_title='Trabajo Titanic ', layout='centered', page_icon='⛵️')


################ #COSAS QUE PODEMOS USAR EN NUESTRA APP ########################

df = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/TrabajosClase/main/titanic.csv')

######################## EMPIEZA APP #########################

st.title('Trabajo sobre Titanic 🌊⛵️🌊')
st.image('https://cdn.pixabay.com/photo/2021/03/04/16/32/ship-6068668__340.png', width = 550)
st.text('Trabajo sobre titanic ')

st.text('Este proyecto va sobre DATOS interesantes sobre sucesos del TITANIC')


################################### COLUMNAS ###############################

col1, col2 = st.columns(2)
with col1:

##################################### ABORDANTES TITANIC SEGUN GENERO  /// GRAFICO DONUT ###################################

    labels = ['Hombres', 'Mujeres']
    contador = df['Sex'].value_counts() # Cuenta la cantidad de personas
    colors = ['deepblue', 'pink'] # Colores del grafico 
    grafico = go.Figure(data=[go.Pie(labels=labels, values=contador , hole=0.3, marker_colors = colors, pull =[0,0.1], textfont_size=15,)]) # CODIGO GRAFICO
    grafico.update_traces(textinfo='value') # Muestra el valor en vez de el porciento
    grafico.update_layout(title_text='Abordantes en el TITANIC segun su genero') # Titulo del grafico 
    st.plotly_chart(grafico) # Muestra el grafico


with col2:

    ##################################### SUPERVIVIENTES TITANIC SEGUN GENERO  /// GRAFICO PASTEL ###################################
  
    labels = ['Mujeres', 'Hombres'] # Titulos 
    sobrevivientes = df['Survived'].value_counts() # Contador 
    colors = ['#9d1a6b', '#3359FF'] # Colores para el grafico 
    gsobre = go.Figure(data=[go.Pie(labels=labels, values=sobrevivientes, marker_colors = colors, pull=[0, 0.2], textfont_size=15,
    marker_line_width = 0, marker_line_color = 'white')]) # Color el el contorno
    #gsobre.update_traces(textinfo='value') # Muestra el valor en vez de el porciento
    gsobre.update_layout(title_text='Sobrevivientes TITANIC segun su genero') # Titulo del grafico 
    st.plotly_chart(gsobre)


# STORY TELLING

st.write(''' ___________________________________________________________________________________________________
            Como podemos observar en los graficos, aunque si hubieron mas pasajeros masculinos que femeninos   
            la tasa de superviviencia es mas elevada en las mujeres que en los hombres como podemos ver en el  
            grafico de la derecha, el porque, es, que la mayoria de los hombres, dieron prioridad a los ninos, 
            mujeres y a los hombres de la clase alta. La conclusion que podemos sacar es de que, la mayoria    
            de tripulantes se quedaron en el barco ayudando a dichos pasajeros para ayudar en la supervivencia.
            ''')


#################################### RELACION EDAD A PRECIO DEL BILLETE  /// GRAFICO SCATTER ########################################
precios = px.scatter(df, x='Age', y='Fare', color='Age', size='Fare', hover_data=['Age'], title='Relacion edad a precio del billete',
labels={
                     "Age": "Edad de los tripulantes",
                     "Fare": "Precio del billete",
                 })

precios.update_layout(
    # font_family="Courier New",
    font_color="#05a3ff",
    # title_font_family="Times New Roman",
    title_font_color="white",
    legend_title_font_color="#828282")
st.plotly_chart(precios)

################################### COLUMNAS ###############################

col1, col2 = st.columns(2)
with col1:
    if st.button('Billete mas caro'):
        st.text('El billete mas caro costaba 512.32$')
with col2:
   if st.button('Billete mas barato'):
        st.text('El billete mas barato costaba 0')


# SIDEBAR

st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.image("https://images.twinkl.co.uk/tr/image/upload/t_illustration/illustation/Titanic-KS2.png", width=150)
st.sidebar.title("Trabajo Titanic")
st.sidebar.write("---")
st.sidebar.audio('http://www.sonidosmp3gratis.com/sounds/ringtones-titanic-flute.mp3')
st.sidebar.download_button('Descarga el CSV', 'https://raw.githubusercontent.com/HerculesCastro/TrabajosClase/main/titanic.csv')

if st.sidebar.button("Mostrar Tablas 🌊"):
    st.dataframe(df)

######################## TIPOS DE CLASES ############################

clase = df.groupby("Pclass")["Survived"].value_counts().unstack()
grafico1 = px.bar(clase, title='Supervivientes segun clase social', template = 'plotly_dark', color_discrete_sequence = ['#1a849d', '#e57b62'], height=500, labels={'index':'Clase', 'value':'Supervivientes', 'Survived': 'Supervivientes', 'Pclass' : 'Clase de cabina'})
series_names1 = ["Fallecidos", "Supervivientes"]
for idx, name in enumerate(series_names1):

        grafico1.data[idx].name = name

        grafico1.data[idx].hovertemplate = name
st.plotly_chart(grafico1)

st.text('''Las conclusiones que podemos sacar viendo esta grafica,
 es de que tanto en primera como segunda clase, sobrevivieron muchas
mas que en los de la tercera clase, sobre todo, podemos ver, 
que en la primera clase, es la unica clase en la que el porcentaje
de supervivientes es mayor que el de fallecidos''')

############################ DATOS INTERESANTES ############################
col1, col2, col3= st.columns(3)
with col1:
    if st.button('Edad de la persona mas mayor'):
        st.text('80 Anos')
with col2:
   if st.button('Edad de la persona mas joven'):
        st.text('4 a 5 meses')
with col3:
    if st.button('Edad promedia de los pasajeros'):
        st.text('29 anos')

###################### GRAFICO DEL MAPA ####################

# table_path = '/Users/ivor/Desktop/Upgrade/Pagina_Web_Titanic/file.html'
# table_path = open(table_path, 'r').read()
# st.write(table_path, unsafe_allow_html=True)



html = open("/Users/ivor/Desktop/Upgrade/Pagina_Web_Titanic/file.html", "r").read()
st.components.v1.html(html,height=400)
