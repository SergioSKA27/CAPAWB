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
#Autor: Sergio Lopez



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
        sticky_nav=False, #at the top or not
        sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
        first_select=20
    )

    #get the id of the menu item clicked
#st.write(f"{menu_id}")

if menu_id == 'Inicio':
    switch_page('Main')

#------------------------------------- body ---------------------------------------------------------
st.header('Tests Editor')

st.text(st.session_state)
test =st.text_input('Ingrese el nombre del test','Test uno')
t = test_e.test(test)
if 'test' not in st.session_state:
    st.session_state['test']= t
else:
    if st.session_state['test'].test_name != test:
        st.session_state['test'].test_name = test

if 'test_edit' not in st.session_state:
  st.session_state['test_edit'] = None


if 'qnum' not in st.session_state:
  st.session_state['qnum'] = 0

if 'questions_data' not in st.session_state:
  st.session_state['questions_data'] = {}
else:
    st.write(len(st.session_state['questions_data']))



cols = st.columns([.7,.3],gap='large')

t = st.selectbox('Seleccione el tipo de pregunta que desea agregar',('opcion multiple','selccion multiple','entrada libre','codigo','ordenacion'),key='s'+str(st.session_state['qnum']))

if t == 'opcion multiple':
  st.write('## Ingrese el texto de la pregunta '+str(st.session_state['qnum']+1))
  question_text = st.text_area('Texto de la pregunta','Pregunta?', height=100,key='text'+str(st.session_state['qnum']))
  col =st.columns(3)
  answ_num = col[0].number_input('**Ingrese el numero de respuestas**', min_value=1, max_value=5,key='num'+str(st.session_state['qnum']))
  ans = []
  correct_ans = 0
  for i in range(answ_num):
    st.write('Ingrese el texto de la respuesta '+str(i+1))
    correcta = st_toggle_switch('Respuesta correcta',key='ans'+str(i)+str(st.session_state['qnum']))
    if correcta:
      correct_ans = i
    answer_text = st.text_area('Texto de la respuesta','Respuesta '+str(i+1), height=50,key='answ'+str(i)+str(st.session_state['qnum']))
    ans.append(answer_text)
  st.session_state['questions_data'][st.session_state['qnum']] = {
    'question_text':question_text,
    'answers':np.random.permutation(np.array(ans)),
    'correct_answer':correct_ans,
    'qtype': 'multiple'
    }


if t == 'selccion multiple':
  st.write('## Ingrese el texto de la pregunta '+str(st.session_state['qnum']))
  question_text = st.text_area('Texto de la pregunta','Pregunta?', height=100,key='text'+str(st.session_state['qnum']))
  col =st.columns(3)
  answ_num = col[0].number_input('**Ingrese el numero de respuestas**', min_value=1, max_value=5,key='num'+str(st.session_state['qnum']))
  ans = []
  correct_ans = []
  for i in range(answ_num):
    st.write('Ingrese el texto de la respuesta '+str(i+1))
    correcta = st_toggle_switch('Respuesta correcta',key='ans'+str(i)+str(st.session_state['qnum']))
    if correcta:
      correct_ans.append(i)
    answer_text = st.text_area('Texto de la respuesta','Respuesta '+str(i+1), height=50,key='answ'+str(i)+str(st.session_state['qnum']))
    ans.append(answer_text)
  st.session_state['questions_data'][st.session_state['qnum']] = {
    'question_text':question_text,
    'answers':ans,
    'correct_answer':correct_ans,
    'qtype': 'checkbox'
    }

if t == 'ordenacion':
  st.write('## Ingrese el texto de la pregunta '+str(st.session_state['qnum']))
  question_text = st.text_area('Texto de la pregunta','Pregunta?', height=100,key='text'+str(st.session_state['qnum']))
  col =st.columns(3)
  answ_num = col[0].number_input('**Ingrese el numero de respuestas**', min_value=1, max_value=100,key='num'+str(st.session_state['qnum']))
  ans = []
  correct_ans = []
  st.write('Ingrese las repuestas en orden ')
  for i in range(answ_num):
    st.write('Ingrese el texto de la respuesta '+str(i+1))
    answer_text = st.text_area('Texto de la respuesta','Respuesta '+str(i+1), height=50,key='answ'+str(i)+str(st.session_state['qnum']))
    ans.append(answer_text)
  st.session_state['questions_data'][st.session_state['qnum']] = {
    'question_text':question_text,
    'answers':ans,
    'correct_answer':ans,
    'qtype': 'order'
    }

if t == 'entrada libre':
  st.write('## Ingrese el texto de la pregunta '+str(st.session_state['qnum']))
  question_text = st.text_area('Texto de la pregunta','Pregunta?', height=100,key='text'+str(st.session_state['qnum']))
  col =st.columns(3)
  leftoev = st.checkbox('Dejar para evaluar')
  answ = st.text_area('Ingresa la respuesta exacta(o una expresion regular)',r'\b{palabra|python}\b', height=100,key='text'+str(st.session_state['qnum']+1))

  if leftoev:
    st.session_state['questions_data'][st.session_state['qnum']] = {
    'question_text':question_text,
    'answers':'',
    'correct_answer':'left to evalute',
    'qtype': 'text'
    }
  else:
    st.session_state['questions_data'][st.session_state['qnum']] = {
    'question_text':question_text,
    'answers':answ,
    'correct_answer':answ,
    'qtype': 'text'
    }

if st.button('Añadir pregunta'):
    st.session_state['qnum'] += 1
    st.experimental_rerun()

st.write('# Preview')
for i in range(st.session_state['qnum']):
    st.write('## Pregunta ' +str(i+1))
    st.write(st.session_state['questions_data'][i]['question_text'])
    if st.session_state['questions_data'][i]['qtype'] == 'multiple':
        st.write('Selecciona la respuesta correcta')
        st.radio('**Respuesta correcta**',options=st.session_state['questions_data'][i]['answers'],label_visibility='collapsed',key='radio'+str(i))
        st.write('Respuesta correcta: ', st.session_state['questions_data'][i]['correct_answer'])
    if st.session_state['questions_data'][i]['qtype'] == 'checkbox':
        st.write('Selecciona la respuesta correcta')
        chcks = []
        for t in range(len(st.session_state['questions_data'][i]['answers'])):
            chcks.append(st.checkbox(st.session_state['questions_data'][i]['answers'][t],key='chck'+str(t)+str(i)))
        st.write('Respuestas correctas: ', st.session_state['questions_data'][i]['correct_answer'])

    if st.session_state['questions_data'][i]['qtype'] == 'text':
        st.write('Ingresa la respuesta')
        st.text_area('Respuesta', height=50,key='text'+str(i))
        st.write('Respuestas correctas: ', st.session_state['questions_data'][i]['correct_answer'])

    if st.session_state['questions_data'][i]['qtype'] == 'order':
        st.write('Ingresa las respuestas en orden')
        st.multiselect('Respuestas',options=st.session_state['questions_data'][i]['answers'],key='mult'+str(i))
        st.write('Respuestas correctas(en orden): ', st.session_state['questions_data'][i]['correct_answer'])





#------------------------------------- Footer ---------------------------------------------------------

with open('frontend/footer.html') as foo:
  st.markdown(foo.read(), unsafe_allow_html=True)
