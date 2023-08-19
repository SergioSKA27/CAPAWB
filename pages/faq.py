import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.echo_expander import echo_expander
import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page

#--------------------------------------------- page config ---------------------------------------------
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


#navbar items
menu_data = [
    {'id':'About','icon':"❓",'label':"FAQ"},
    {'icon': "fa-solid fa-radar",'label':"Problemas", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
    {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
    {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    {'icon': "far fa-copy", 'label':"Right End"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
    ]

over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#002B7A'}
menu_id = hc.nav_bar(
        menu_definition=[{'id':'s','label':""},],
        override_theme=over_theme,
        home_name='Inicio',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=False, #at the top or not
        sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
        first_select=20
    )

    #get the id of the menu item clicked
#st.write(f"{menu_id}")

if menu_id == 'Inicio':
    switch_page('Main')







#------------------------------------- Body ---------------------------------------------------------



txt = r'''
# PREGUNTAS FRECUENTES

## ¿Que es CAPA?

CAPA es un espacio diseñado para todos aquellos apasionados por la resolución de problemas algorítmicos y la programación en Python. Aquí, nos sumergiremos en el fascinante mundo de los algoritmos, desde los más fundamentales hasta los más complejos. Nuestro objetivo es desarrollar habilidades sólidas en resolución de problemas y algoritmos, lo que te brindará una ventaja en tus estudios y en tu carrera.

## ¿Qué esperar?


**Sesiones de Aprendizaje** : Participarás en sesiones prácticas donde exploraremos diferentes algoritmos y técnicas de resolución de problemas. ¡Prepárate para desafíos emocionantes y soluciones creativas!

**Colaboración**: Trabajaremos juntos en proyectos y desafíos grupales. La colaboración es fundamental para el aprendizaje efectivo de la programación y los algoritmos.

**Crecimiento Personal**: A medida que enfrentes desafíos algorítmicos y resuelvas problemas complejos, tu pensamiento analítico y habilidades de programación mejorarán significativamente.


## Únete a nosotros

¡No importa si eres un principiante o un experto en programación! CAPA está abierto para todos aquellos interesados en mejorar sus habilidades algorítmicas. Únete a nuestras sesiones y actividades para sumergirte en el emocionante mundo de la resolución de problemas y los algoritmos en Python.

'''



st.markdown(txt, unsafe_allow_html=True)




#------------------------------------- Footer ---------------------------------------------------------

with open('frontend/footer.html') as foo:
  st.markdown(foo.read(), unsafe_allow_html=True)
