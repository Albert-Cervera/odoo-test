# -*- coding: utf-8 -*-
{
    'name': "Twitter Odoo Love",

    'summary': """
        Custom module that allows you to write and publish real tweets.""",

    'description': """
        Tweet, tweet, tweet, as a little birdie.
    """,

    'author': "Albert Cervera",
    'website': "http://www.twitter.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
