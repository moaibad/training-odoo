from odoo import models, fields, api


class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description = 'Bus schedule information'

    name = fields.Char(string='Name')
    schedule = fields.Datetime(string="Schedule")
    payment_method = fields.Selection(
        [
            ("cash","Cash"),
            ("transfer","Transfer")
        ], string='Payment')
    departure = fields.Datetime(string="Departure")
    arrival = fields.Datetime(string="Arrival")
    bus_id = fields.Many2one(comodel_name='res.bus', string="Bus")
    route_id = fields.Many2one(comodel_name='bus.route', string="Bus Route")
    baggage_ids = fields.One2many(comodel_name='baggage.baggage', inverse_name='schedule_id', string='Baggage')
