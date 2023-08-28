import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.echo_expander import echo_expander
import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from code_editor import code_editor
import subprocess
from time import perf_counter
#Autor: Sergio Lopez

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



code1 = r'''
#Ingresa tu propio código de python y  prueba tus conocimientos :D!
#¡Recuerda que todo lo que ingreses el editor se borrara una vez que cierres la pagina!
'''
bts = [
 {
   "name": "Copy",
   "feather": "Copy",
   "hasText": True,
   "alwaysOn": True,
   "commands": ["copyAll"],
   "style": {"top": "0.46rem", "right": "0.4rem"}
 },
 {
   "name": "Shortcuts",
   "feather": "Type",
   "class": "shortcuts-button",
   "hasText": True,
   "commands": ["toggleKeyboardShortcuts"],
   "style": {"bottom": "calc(50% + 1.75rem)", "right": "0.4rem"}
 },
 {
   "name": "Collapse",
   "feather": "Minimize2",
   "hasText": True,
   "commands": ["selectall",
                "toggleSplitSelectionIntoLines",
                "gotolinestart",
                "gotolinestart",
                "backspace"],
   "style": {"bottom": "calc(50% - 1.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Guardar",
   "feather": "Save",
   "hasText": True,
   "commands": ["save-state", ["response","saved"]],
   "response": "saved",
   "style": {"bottom": "calc(50% - 4.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Ejecutar",
   "feather": "Play",
   "primary": True,
   "hasText": True,
   "showWithIcon": True,
   "commands": ["submit"],
   "style": {"bottom": "0.44rem", "right": "0.4rem"}
 },
 {
   "name": "Comandos",
   "feather": "Terminal",
   "primary": True,
   "hasText": True,
   "commands": ["openCommandPallete"],
   "style": {"bottom": "3.5rem", "right": "0.4rem"}
 }
]

css_string = '''
background-color: #bee1e5;

body > #root .ace-streamlit-dark~& {
   background-color: #262830;
}

.ace-streamlit-dark~& span {
   color: #fff;
   opacity: 0.6;
}

span {
   color: #000;
   opacity: 0.5;
}

.code_editor-info.message {
   width: inherit;
   margin-right: 75px;
   order: 2;
   text-align: center;
   opacity: 0;
   transition: opacity 0.7s ease-out;
}

.code_editor-info.message.show {
   opacity: 0.6;
}

.ace-streamlit-dark~& .code_editor-info.message.show {
   opacity: 0.5;
}
'''
# create info bar dictionary
info_bar = {
  "name": "language info",
  "css": css_string,
  "style": {
            "order": "1",
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "center",
            "width": "100%",
            "height": "2.5rem",
            "padding": "0rem 0.75rem",
            "borderRadius": "8px 8px 0px 0px",
            "zIndex": "9993"
           },
  "info": [{
            "name": "python",
            "style": {"width": "100px"}
           }]
}
# CSS string for Code Editor
css_string2 = '''
font-weight: 600;
&.streamlit_code-editor .ace-streamlit-dark.ace_editor {
  background-color: #111827;
  color: rgb(255, 255, 255);
}
&.streamlit_code-editor .ace-streamlit-light.ace_editor {
        background-color: #eeeeee;
        color: rgb(0, 0, 0);
}
'''
# style dict for Ace Editor
ace_style = {"borderRadius": "0px 0px 8px 8px"}

# style dict for Code Editor
code_style = {"width": "100%"}
editor0 = code_editor(code1,theme="contrast",buttons=bts,lang='python',height=[15, 70],focus=True,info=info_bar,props={"style": ace_style}, component_props={"style": code_style, "css": css_string2})


if editor0['type'] == "submit" and len(editor0['text']) != 0:
# Run the Python code and capture the output
    start = perf_counter()
    result = subprocess.run(['python', '-c', editor0['text']], capture_output=True, text=True)
    cpu_time = perf_counter() - start
    output = result.stdout
    error = result.stderr
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(output, error)
        st.write(f"CPU Time: {cpu_time}")

if editor0['type'] == "saved" and len(editor0['text']) != 0:
    filename = st.text_input('Ingrese el nombre del archivo sin la extension .py','example')
    st.download_button(
        label="Descargar",
        data=editor0['text'],
        file_name=filename+'.py',
        mime='text/python',)

