'''
Defines routes for this site
'''

from flask import render_template, Flask, request
from .constants import URL_GITHUB, URL_LINKEDIN, MAIL_ADDDRESS
from .localization import get_string, get_lang_strings

def init_routes(app: Flask):
    app.add_url_rule('/', 'splash', splash)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/about', 'about', about)

def splash():
    lang_strings = get_lang_strings(request.args)

    return render_template('splash.html',
        name=get_string('name', lang_strings.get('lang')),
        game_dev=get_string('game_developer', lang_strings.get('lang')).upper(),
        button_enter=get_string('enter', lang_strings.get('lang')).upper(),
        link_enter=request.url_root + 'index' + lang_strings.get('query_param'), 
        button_lang=get_string('other_lang', lang_strings.get('lang')).upper(),
        query_toggle_lang=lang_strings.get('query_param_toggle'),
        query_current_lang=lang_strings.get('query_param'),
        self_url=request.base_url
    )

def index():

    return render_template('index.html')
    
def about():
    lang_strings = get_lang_strings(request.args)
    
    return render_template('_about_me.html',
        page_title=get_string('about_me', lang_strings.get('lang')), 
        button_lang=get_string('other_lang', lang_strings.get('lang')).upper(),
        query_toggle_lang=lang_strings.get('query_param_toggle'),
        query_current_lang=lang_strings.get('query_param'),
        self_url=request.base_url,
        name=get_string('name', lang_strings.get('lang')),
        powered_by_flask=get_string('powered_by_flask', lang_strings.get('lang')),
        url_github=URL_GITHUB,
        url_linkedin=URL_LINKEDIN,
        email_address=MAIL_ADDDRESS
    )