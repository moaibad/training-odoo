from odoo import models, fields, api


class Class(models.Model):
    _name = 'class.class'
    _description = 'Class'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
    )
    student_ids = fields.Many2many('res.partner', domain=[("is_lecturer", "=", False)], string='Students')
    subject_line_ids = fields.One2many('subject.line', 'class_id', string='Subject Lines')