# -*- coding: utf-8 -*-
{
    'name': "Selenium Automate",

    'summary': """
        The tool to display a unique identifier for each lead""",

    'description': """
        basic odoo does not display the id of each record.
        but with this module, you have the opportunity to see it, it allows you to find it easily and simply, with a unique identifier

        The tool is compatible with both Odoo Enterprise and Odoo Community.
    """,

    'author': "Eufonie",
    'website': "https://www.eufonie.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        "static/description/icon.png"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
