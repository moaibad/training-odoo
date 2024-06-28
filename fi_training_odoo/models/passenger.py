from odoo import models, fields, api


class Passenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger information'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    birth_date = fields.Date(string='Birth Date')