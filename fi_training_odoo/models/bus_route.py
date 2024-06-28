from odoo import models, fields, api


class BusRoute(models.Model):
    _name = 'bus.route'
    _description = 'Bus route information'

    name = fields.Char(string='Name')