import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.echo_expander import echo_expander
import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import navbar




# The User class represents a user with an ID.
class User:
    user_type = 'user'

    def __init__(self,id_user):
        self.id_user = id_user



# The Admin class is a subclass of the User class and initializes with a user ID.
class Admin(User):
    user_type = 'admin'
    def __init__(self,id_user):
        #Validate the id
        super.__init__(id_user)





class Session:

    def __init__(self,session_id,user):
        self.session_id = session_id
        self.user = user









