# -*- coding: utf-8 -*-
{
    'name': "convalidaciones",

    'summary': """
        Gestiona convalidaciones en un instituto""",

    'description': """
       Este modulo permite gestionar las convalidaciones de un centro educativo en Arequipa
    """,

    'author': "Tecsup",
    'website': "http://www.tecsup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded 
    'data': [
        # 'security/ir.model.access.csv',
        'views/alumnos.xml',
        'views/modulos.xml',
        'views/ciclos.xml',
        'views/convalidaciones.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #   'demo/demo.xml',
    #],
}