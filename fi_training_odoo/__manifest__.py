# -*- coding: utf-8 -*-
{
    'name': "Training Odoo (Ibad)",

    'summary': """
        Modul untuk mengelola jadwal bus, rute, penumpang, dan integrasi dengan 
        HR untuk penugasan bus kepada karyawan.""",

    'description': """
        Modul ini dirancang untuk memudahkan pengelolaan operasional bus dalam sebuah organisasi. Modul ini menyediakan fitur untuk mengelola jadwal bus, rute, dan informasi penumpang. Selain itu, modul ini terintegrasi dengan modul HR untuk memungkinkan penugasan bus kepada karyawan, sehingga pengelolaan transportasi menjadi lebih efisien dan terorganisir.

        Fitur Utama:\n
        - Membuat dan mengelola jadwal dan rute bus
        - Memelihara database bus dan penumpang
        - Terintegrasi dengan modul HR untuk mengelola penugasan bus kepada karyawan
        - Tampilan dan menu yang mudah digunakan untuk navigasi dan operasi yang mudah
    """,

    'author': "Mohammad Fathul'ibad",
    'website': "https://moaibad.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Transportation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/bus_data.xml',
        'data/route_data.xml',
        'views/bus_schedule_view.xml',
        'views/bus_route_view.xml',
        'views/res_passenger_view.xml',
        'views/res_bus_view.xml',
        'views/baggage_view.xml',
        'views/hr_employee_view.xml',
        'views/menuitem.xml',
        'wizards/report_bus_problem_wizard_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
