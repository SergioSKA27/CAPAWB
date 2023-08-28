import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.echo_expander import echo_expander
import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import pages.modules.test_edit as test_e
from streamlit_toggle import st_toggle_switch
import random
import numpy as np
import pandas as pd
import plotly.express as px


#--------------------------------------------- page config ---------------------------------------------
#basic page configuration
st.set_page_config(
    page_title='CAPA',
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': """# Web Site Club de Algoritmia Avanzada en Python.
                        Todos los derechos reservados 2023, CAPA."""
    }
)

#Disable sidebar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


#------------------------------------- Navbar ---------------------------------------------------------


over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#002B7A'}
menu_id = hc.nav_bar(
        menu_definition=[{'id':'s','label':""},],
        override_theme=over_theme,
        home_name='Inicio',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
        first_select=20
    )

    #get the id of the menu item clicked
#st.write(f"{menu_id}")

if menu_id == 'Inicio':
    switch_page('Main')

#------------------------------------- body ---------------------------------------------------------

st.header('Dashboard 🔎')
# Generar datos aleatorios
def generate_random_data(num_students):
    data = []
    for _ in range(num_students):
        student_id = random.randint(1000, 9999)
        name = f"Student_{student_id}"
        age = random.randint(18, 25)
        gender = random.choice(["Femenino", "Masculino"])
        programming_experience = random.choice(["Pricipiante", "Intermedio", "Avanzado"])
        midterm_exam = random.randint(50, 100)
        final_exam = random.randint(50, 100)
        assignments = [random.randint(0, 20) for _ in range(5)]
        data.append([student_id, name, age, gender, programming_experience, midterm_exam, final_exam] + assignments)
    return data

# Crear un DataFrame a partir de los datos generados
def create_dataframe(data):
    columns = ["Student ID", "Nombre", "Edad", "Genero", "Experiencia en Programacion", "Examen de Midterm", "Examen Final"]
    columns += [f"Tarea {i+1}" for i in range(5)]
    df = pd.DataFrame(data, columns=columns)
    return df

# Generar 20 estudiantes aleatorios
random_data = generate_random_data(20)
student_dataframe = create_dataframe(random_data)


st.dataframe(student_dataframe)



# Create plots using Plotly
fig1 = px.histogram(student_dataframe, x="Edad", title="Distribución de Edades")
fig2 = px.box(student_dataframe, x="Genero", y="Examen de Midterm", title="Boxplot del Examen de Midterm por Género")
fig3 = px.scatter(student_dataframe, x="Examen de Midterm", y="Examen Final", color="Experiencia en Programacion", title="Scatter Plot: Examen Midterm vs Examen Final")
fig4 = px.box(student_dataframe, x="Experiencia en Programacion", y="Examen Final", title="Boxplot del Examen Final por Experiencia en Programación")





st.plotly_chart(fig1, use_container_width=True)


st.plotly_chart(fig2,use_container_width=True)

st.plotly_chart(fig3,use_container_width=True)
st.plotly_chart(fig4,use_container_width=True)



#------------------------------------- Footer ---------------------------------------------------------

with open('frontend/footer.html') as foo:
  st.markdown(foo.read(), unsafe_allow_html=True)
