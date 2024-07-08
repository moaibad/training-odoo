# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nti_training_academic(models.Model):
#     _name = 'nti_training_academic.nti_training_academic'
#     _description = 'nti_training_academic.nti_training_academic'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
