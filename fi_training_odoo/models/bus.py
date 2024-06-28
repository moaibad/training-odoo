from odoo import models, fields, api


class Bus(models.Model):
    _name = 'res.bus'
    _description = 'Bus information'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity')
    image = fields.Image(string='Image')