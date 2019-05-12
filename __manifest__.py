# -*- coding: utf-8 -*-
{
    'name': "thuani",

    'summary': """
        Reliable Business Website""",

    'description': """
        thuani.com is the place for Small Business Owners to get their business website.
    """,

    'author': "Zawro",
    'website': "https://thuani.com/developer/zawro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        'views/blog.xml',
        'views/base.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}