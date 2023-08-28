import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.echo_expander import echo_expander
import hydralit_components as hc
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth



"""
    The above code defines three functions that display navigation bars with different menu options for users who are not
    logged in, logged in, and admin users.
    :return: The functions `show_navbarusr_notlog()`, `show_navbarusr_log(usr)`, and `show_navbar_admin(usr)` all return the
    `menu_id` value.
"""

def show_navbarusr_notlog():
    """
    The function `show_navbarusr_notlog()` displays a navigation bar with menu options for a user who is not logged in.
    :return: the `menu_id` variable.
    """
    user = 'Login'
    menu_data = [
    {'icon': "far fa-copy", 'label':"Docs"},
    {'id':'About','icon':"❓",'label':"FAQ"},
    {'id':'contact','icon':"📩",'label':"Contacto"},
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
    return  menu_id


def show_navbarusr_log(usr):
    """
    The function `show_navbarusr_log` displays a navigation bar with various menu options and returns the ID of the selected
    menu item.

    :param usr: The `usr` parameter is a string that represents the username of the logged-in user. It will be displayed in
    the navbar as the login name
    :return: The function `show_navbarusr_log` returns the `menu_id` value.
    """
    user = 'Login'
    menu_data = [
    {'icon': "fa-solid fa-radar",'label':"Problemas", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Basicos"},{'id':'subid12','icon': "fa fa-database", 'label':"Intermedios"},{'id':'subid13','icon': "💀", 'label':"Avanzados"}]},
    {'id':'contest','icon': "🏆", 'label':"Concursos"},
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
        login_name=usr,
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=False, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )
    return menu_id


def show_navbar_admin(usr):
    """
    The function `show_navbar_admin` displays a navigation bar with various menu options for an admin user.

    :param usr: The `usr` parameter is the username of the logged-in user. It is used to display the username in the navbar
    :return: the menu_id.
    """
    user = 'Login'
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
        login_name=usr,
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=False, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )
    return menu_id
