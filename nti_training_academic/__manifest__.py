# -*- coding: utf-8 -*-
{
    'name': "nti_training_academic",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menuitem.xml',
        'views/res_partner_view.xml',
        'views/class_view.xml',
        'views/subject_view.xml',
        'views/show_subject_list_view.xml',
        'report/class_class_template.xml',
        'report/class_class_reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
