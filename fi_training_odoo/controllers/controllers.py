# -*- coding: utf-8 -*-
# from odoo import http


# class FiTrainingOdoo(http.Controller):
#     @http.route('/fi_training_odoo/fi_training_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fi_training_odoo/fi_training_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fi_training_odoo.listing', {
#             'root': '/fi_training_odoo/fi_training_odoo',
#             'objects': http.request.env['fi_training_odoo.fi_training_odoo'].search([]),
#         })

#     @http.route('/fi_training_odoo/fi_training_odoo/objects/<model("fi_training_odoo.fi_training_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fi_training_odoo.object', {
#             'object': obj
#         })
