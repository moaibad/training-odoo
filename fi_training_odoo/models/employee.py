from odoo import models, fields, api

class Employee(models.Model):
 _inherit = 'hr.employee'

 is_driver = fields.Boolean(string='Is Driver')