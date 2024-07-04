from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError, UserError


class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description = 'Bus schedule information'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name')
    date_of_issue = fields.Datetime(string="Date of Issue", default=lambda self: datetime.today(), readonly=True, tracking=1)
    payment_method = fields.Selection(
        [
            ("cash","Cash"),
            ("transfer","Transfer")
        ], string='Payment', tracking=1)
    departure = fields.Datetime(string="Departure", tracking=1)
    arrival = fields.Datetime(string="Arrival", tracking=1)
    bus_id = fields.Many2one(comodel_name='res.bus', string="Bus", tracking=1)
    route_id = fields.Many2one(comodel_name='bus.route', string="Bus Route")
    baggage_ids = fields.One2many(comodel_name='baggage.baggage', inverse_name='schedule_id', string='Baggage')
    passenger_ids = fields.Many2many('res.passenger', string='Passenger')
    capacity = fields.Integer(string="Capacity", related="bus_id.capacity")
    driver_id = fields.Many2one(comodel_name='hr.employee', string='Driver ', domain=[("is_driver", "=", True)], tracking=1)
    driver_name = fields.Char(related='driver_id.name', string='Driver Name')
    driver_license = fields.Char(related='driver_id.driver_license', string='Driver License')
    driver_license_expired_date = fields.Date(related='driver_id.driver_license_expired_date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('on_going', 'On Going'),
        ('done', 'Done'),
    ], string='Status', default='draft', copy=False)
    
    @api.constrains('arrival', 'departure')
    def _check_arrival_time(self):
        for record in self:
            if record.arrival and record.arrival < record.departure:
                raise UserError("Arrival time cannot be earlier than Departure time..")
            
    @api.constrains('passenger_ids', 'capacity')
    def _check_capacity(self):
        for record in self:
            if record.capacity and len(record.passenger_ids) > record.capacity:
                raise ValidationError("The bus is at maximum capacity..")
            
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('bus.schedule.seq')
        return super(BusSchedule, self).create(vals)
    
    def bus_schedule_submit_button(self):
        self.state = 'submitted'
        
    def bus_schedule_run_button(self):
        self.state = 'on_going'
        
    def bus_schedule_done_button(self):
        self.state = 'done'
    
