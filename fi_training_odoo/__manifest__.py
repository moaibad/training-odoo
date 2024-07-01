# -*- coding: utf-8 -*-
{
    'name': "Training Odoo (Ibad)",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohammad Fathul'ibad",
    'website': "https://moaibad.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bus_schedule_view.xml',
        'views/res_passenger_view.xml',
        'views/res_bus_view.xml',
        'views/hr_employee_view.xml',
        'views/menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
