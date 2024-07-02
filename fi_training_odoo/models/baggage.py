from odoo import models, fields, api


class Baggage(models.Model):
    _name = 'baggage.baggage'
    _description = 'Passenger\'s baggage'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    schedule_id = fields.Many2one(comodel_name='bus.schedule', string="Bus Schedule")
