from odoo import models, fields, api


class Bus(models.Model):
    _name = 'res.bus'
    _description = 'Bus information'
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique!')
    ]

    name = fields.Char(string='Name')
    code = fields.Char(string='Code', required=True)
    capacity = fields.Integer(string='Capacity')
    image = fields.Image(string='Image')