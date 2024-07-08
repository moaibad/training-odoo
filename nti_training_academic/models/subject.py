from odoo import models, fields, api


class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'Subject'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    lecturer_id = fields.Many2one(
        comodel_name='res.partner',
        string="Lecturer",
        domain=[("is_lecturer", "=", True)]
    )