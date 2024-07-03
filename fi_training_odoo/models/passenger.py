from odoo import models, fields, api
from datetime import datetime

class Passenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger information'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age', store=False)
    
    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = datetime.today()
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year                
                record.age = age
            else:
                record.age = 0
