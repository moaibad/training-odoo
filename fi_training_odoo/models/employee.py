from odoo import models, fields, api

class Employee(models.Model):
 _inherit = 'hr.employee'

 is_driver = fields.Boolean(string='Is Driver')
 driver_license = fields.Char(string='Driver License')
 driver_license_expired_date = fields.Date(string='Driver License Expired Date')