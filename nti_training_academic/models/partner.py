from odoo import models, fields, api
from datetime import datetime

class Partner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age', store=False)
    is_lecturer = fields.Boolean(string='Is Lecturer')
    subject_line_ids = fields.One2many('subject.subject', 'lecturer_id', string='Subjects')
    
    
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                today = datetime.today()
                birthday = fields.Date.from_string(record.birthday)
                age = today.year - birthday.year                
                record.age = age
            else:
                record.age = 0
             
    def show_subject_list(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Subject List',
            'view_type': 'tree',
            'view_mode': 'tree',
            'domain' : [('lecturer_id', '=', self.id)],
            'res_model': 'subject.subject',
            'target' : 'new'
        }