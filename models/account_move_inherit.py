from odoo import models, fields

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    student_id = fields.Many2one('student.student', string='Student')
