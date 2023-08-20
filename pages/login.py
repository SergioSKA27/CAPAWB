import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import base64
import struct
import math
from streamlit_extras.echo_expander import echo_expander
from code_editor import code_editor
import subprocess
import time
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
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
if  "session_state"  in st.session_state and "authentication_status" in st.session_state and st.session_state["authentication_status"] != None:
    switch_page('Main')

#--------------------------------------------- Header ---------------------------------------------
def pythonlogo():
    """
    The `pythonlogo` function displays the Python logo using SVG code and a CSS file.
    """
    with open('frontend/mainpage/stylepythonlogo.css') as f:
        container1 = st.empty()
        columns1,col2,col3 = st.columns(3)
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        with columns1:
            container1.markdown(
    '''<svg width="25%" height="25%" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" id="python-logo">
    <path d="m116 296c0-30.328125 24.671875-55 55-55h170c13.785156 0 25-11.214844 25-25v-141c0-41.355469-33.644531-75-75-75h-70c-41.355469 0-75 33.644531-75 75v41h110c8.285156 0 15 6.714844 15 15s-6.714844 15-15 15h-181c-41.355469 0-75 33.644531-75 75v70c0 41.355469 33.644531 75 75 75h41zm105-220c-8.285156 0-15-6.714844-15-15s6.714844-15 15-15 15 6.714844 15 15-6.714844 15-15 15zm0 0" />
    <path d="m437 146h-41v70c0 30.328125-24.671875 55-55 55h-170c-13.785156 0-25 11.214844-25 25v141c0 41.355469 33.644531 75 75 75h70c41.355469 0 75-33.644531 75-75v-41h-110c-8.285156 0-15-6.714844-15-15s6.714844-15 15-15h181c41.355469 0 75-33.644531 75-75v-70c0-41.355469-33.644531-75-75-75zm-146 290c8.285156 0 15 6.714844 15 15s-6.714844 15-15 15-15-6.714844-15-15 6.714844-15 15-15zm0 0" />
    </svg>''',unsafe_allow_html=True
            )


def show_logos():
    """
    The `show_logos` function displays the Python logo and the name of a Python club using SVG code and a CSS file.
    """


    columns1,col2,col3 = st.columns(3)

    with col2:
        st.markdown('<h1 class="happy-font">Club de Algoritmia en Python Avanzado</h1>',unsafe_allow_html=True )
    with columns1:
        file_ = open("frontend/imageedit_2_6501036184.png",'rb')
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
                f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="logo-fes-mac"></div>',
                unsafe_allow_html=True,
                )
    with col3:
        pythonlogo()


show_logos()



#style for header
tetx = r'''
<style>
.big-font {
    font-size:100px !important;
    text-shadow:
    1px 1px 1px red,
    2px 2px 1px red;
}



@import url(https://fonts.googleapis.com/css?family=Signika:700,300,600);

html, body { height: 100%; }
body { display: flex; justify-content: center; align-items: center; margin:20px 0; text-align:center; background:beige; overflow:hidden; }

.happy-font {
 font-size:5em;
 font:bold 2.5vw/1.6 'Signika', sans-serif;
 user-select:none;
}

.happy-font span { display:inline-block; animation:float .2s ease-in-out infinite; }
 @keyframes float {
  0%,100%{ transform:none; }
  33%{ transform:translateY(-1px) rotate(-2deg); }
  66%{ transform:translateY(1px) rotate(2deg); }
}
body:hover span { animation:bounce .6s; }
@keyframes bounce {
  0%,100%{ transform:translate(0); }
  25%{ transform:rotateX(20deg) translateY(2px) rotate(-3deg); }
  50%{ transform:translateY(-20px) rotate(3deg) scale(1.1);  }
}

span:nth-child(4n) { color:hsl(50, 75%, 55%); text-shadow:1px 1px hsl(50, 75%, 45%), 2px 2px hsl(50, 45%, 45%), 3px 3px hsl(50, 45%, 45%), 4px 4px hsl(50, 75%, 45%); }
span:nth-child(4n-1) { color:hsl(135, 35%, 55%); text-shadow:1px 1px hsl(135, 35%, 45%), 2px 2px hsl(135, 35%, 45%), 3px 3px hsl(135, 35%, 45%), 4px 4px hsl(135, 35%, 45%); }
span:nth-child(4n-2) { color:hsl(155, 35%, 60%); text-shadow:1px 1px hsl(155, 25%, 50%), 2px 2px hsl(155, 25%, 50%), 3px 3px hsl(155, 25%, 50%), 4px 4px hsl(140, 25%, 50%); }
span:nth-child(4n-3) { color:hsl(30, 65%, 60%); text-shadow:1px 1px hsl(30, 45%, 50%), 2px 2px hsl(30, 45%, 50%), 3px 3px hsl(30, 45%, 50%), 4px 4px hsl(30, 45%, 50%); }

.happy-font span:nth-child(2){ animation-delay:.05s; }
.happy-font span:nth-child(3){ animation-delay:.1s; }
.happy-font span:nth-child(4){ animation-delay:.15s; }
.happy-font span:nth-child(5){ animation-delay:.2s; }
.happy-font span:nth-child(6){ animation-delay:.25s; }
.happy-font span:nth-child(7){ animation-delay:.3s; }
.happy-font span:nth-child(8){ animation-delay:.35s; }
.happy-font span:nth-child(9){ animation-delay:.4s; }
.happy-font span:nth-child(10){ animation-delay:.45s; }
.happy-font span:nth-child(11){ animation-delay:.5s; }
.happy-font span:nth-child(12){ animation-delay:.55s; }
.happy-font span:nth-child(13){ animation-delay:.6s; }
.happy-font span:nth-child(14){ animation-delay:.65s; }


.big-font2 {
    font:bold 2.5vw/1.6 'Signika', sans-serif;
}
.big-font3 {
    font:bold 1.5vw/1.6 'Signika', sans-serif;
}
</style>

'''

st.markdown(tetx, unsafe_allow_html=True)

#------------------------------------- Navbar ---------------------------------------------------------


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



#-------------------------------------- Login ---------------------------------------------------------
with open('secrets/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)



authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


if 'authenticator' not in st.session_state:
    st.session_state['authenticator'] = authenticator

name, authentication_status, username = authenticator.login('Login', 'main')



#st.write(name, authentication_status, username)
if authentication_status:
    #authenticator.logout('Logout', 'main')
    st.session_state['name'] = username
    st.session_state['authentication_status'] = authentication_status
    st.toast(f'Welcome *{name}*', icon='🎉')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')



if st.button('Registrarse'):
    switch_page('singup')


#------------------------------------- Footer ---------------------------------------------------------

with open('frontend/footer.html') as foo:
  st.markdown(foo.read(), unsafe_allow_html=True)


