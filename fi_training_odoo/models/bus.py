from odoo import models, fields, api


class Bus(models.Model):
    _name = 'res.bus'
    _description = 'Bus information'
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique!')
    ]
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name')
    code = fields.Char(string='Code', required=True)
    capacity = fields.Integer(string='Capacity')
    image = fields.Image(string='Image')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('maintenance', 'Maintenance'),
        ('departure', 'Departure'),
    ], string='Status', default='draft', copy=False)
    
    def report_bus_problem(self):
        return {
            'name':'Bus Problem',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'report.bus.problem.wizard',
            'type': 'ir.actions.act_window',
            'context': {
                'default_bus_id': self.id
            },
            'target': 'new'
        }