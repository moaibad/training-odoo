from odoo import models, fields

class ReportBusProblem(models.TransientModel):
    _name = 'report.bus.problem.wizard'
    _description = 'Report Bus Problem Wizard'
    
    bus_id = fields.Many2one(
        comodel_name='res.bus',
        string="Bus",
    )
    reason = fields.Text(string='Reason')
    
    def report_problem(self):
        for rec in self:
            err_message = "There's a problem with the bus with the reason : " + str(rec.reason)
            rec.bus_id.state = 'maintenance'
            rec.bus_id.message_post(body=err_message)
        
