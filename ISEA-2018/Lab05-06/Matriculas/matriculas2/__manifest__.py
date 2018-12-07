# -*- coding: utf-8 -*-
{
    'name': "Matriculas2",

    'summary': """
        Modulo de Matriculas""",

    'description': """
        Este modulo gestiona Matriculas de diferentes Alumnos
    """,

    'author': "Daniela Aduviri",
    'website': "http://www.danielasac.com",

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
        'views/views.xml',
        'views/alumnos.xml',
        'views/area.xml',
        'views/matriculas.xml',
        'views/curso.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}