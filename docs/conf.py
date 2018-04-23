
# The master toctree document.
master_doc = 'index'

templates_path = ['_templates']

project = u'Smile'
#copyright = u'2018, Inomial Pty Ltd'
copyright = '2018-{}, Inomial Pty Ltd & contributors'

#html_logo = 'logo.png'
#html_static_path = ['_static']

#html_theme_path = ['_themes']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = 'logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
