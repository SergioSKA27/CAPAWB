import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.echo_expander import echo_expander
import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

#--------------------------------------------- page config ---------------------------------------------
#basic configuration
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

#balloons :)
st.balloons()
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
        st.write('## Club de Algoritmia en Python Avanzado' )
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
#------------------------------------- Navbar ---------------------------------------------------------


#st.write(st.session_state)

if 'name' in st.session_state:
  user = st.session_state['name']

if 'authentication_status' not in st.session_state :
    st.session_state['authentication_status'] = None


with open('secrets/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)



authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#st.write(authenticator)
if 'authenticator' not in st.session_state:
    st.session_state['authenticator'] = authenticator


#navbar items
if 'username' not in st.session_state or st.session_state['username'] is None:
#navbar items for not logged in users

    user = 'Login'
    menu_data = [
    {'icon': "far fa-copy", 'label':"Docs"},
    {'id':'About','icon':"❓",'label':"FAQ"},
    {'id':'contact','icon':"📩",'label':"Contacto"},
    ]
else:
    menu_data = [
    {'icon': "fa-solid fa-radar",'label':"Problemas", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Basicos"},{'id':'subid12','icon': "fa fa-database", 'label':"Intermedios"},{'id':'subid13','icon': "💀", 'label':"Avanzados"}]},
    {'id':'contest','icon': "🏆", 'label':"Concursos"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    {'icon': "far fa-copy", 'label':"Docs"},
    {'icon': "fa-solid fa-radar",'label':"Tests", 'submenu':[{'label':"Basicos", 'icon': "🐛"},{'icon':'🐍','label':"Intermedios"},{'icon':'🐉','label':"Avanzados",}]},
    {'id':'About','icon':"❓",'label':"FAQ"},
    {'id':'contact','icon':"📩",'label':"Contacto"},
    {'id':'logout','icon': "🚪", 'label':"Logout"},#no tooltip message

    ]



over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#002B7A'}
menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Inicio',
        login_name=user,
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=False, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )

    #get the id of the menu item clicked
#st.write(f"{menu_id}")

if menu_id == 'Login':
    switch_page('login')

if menu_id == 'Inicio':
    switch_page('Main')


if menu_id == 'About':
    switch_page('faq')

if menu_id == 'logout' and 'authenticator' in st.session_state:
    st.session_state['authenticator'].logout('Logout', 'main')
    st.session_state['name'] = None
    del st.session_state['authentication_status']

#------------------------------------- Body ---------------------------------------------------------

clases_basicas = [int, str, list, dict, tuple, bool, float]

for clase in clases_basicas:
    with st.expander(r'''# **'''+str(clase.__name__)+'** '):
        st.write(type(clase),key=clase.__name__)


components.html('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .container {
    text-align: center;
  }

  .link {
    font-size: 24px;
    color: #0073e6;
    text-decoration: none;
    transition: color 0.3s;
  }

  .link:hover {
    color: #0057b3;
  }
</style>
<title>Documentación de Python</title>
</head>
<body>
  <div class="container">
    <p> Documentación de Python</p>
    <a class="link" href="https://docs.python.org/3/" target="_blank">Ir a la documentación</a>
  </div>
</body>
</html>


''')

#------------------------------------- Footer ---------------------------------------------------------

with open('frontend/footer.html') as foo:
  st.markdown(foo.read(), unsafe_allow_html=True)
