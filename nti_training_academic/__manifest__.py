# -*- coding: utf-8 -*-
{
    'name': "Academic Management",

    'summary': """
        A module to manage academic activities at the university, 
        including subjects, lecturers, students, and classes.""",


    'description': """
        This module helps in managing university academics by providing 
        features to manage subjects, lecturers, students, and class schedules.
    """,

    'author': "Neural Technologies Indonesia",
    'website': "http://www.nti.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
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
