from odoo import models, fields, api

class StudentInvoice(models.Model):
    _name = 'student.invoice'
    _description = 'Student Invoice'
    _rec_name = 'name'

    name = fields.Char(string='Invoice Number', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('student.invoice'))
    student_id = fields.Many2one('student.student', string='Student', required=True)
    amount = fields.Float(string='Amount', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')
    registration_ids = fields.Many2many('student.course.registration', string='Registrations')

    def action_confirm(self):
        self.state = 'open'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'
        
    def action_register_payment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Register Payment',
            'res_model': 'student.payment',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_student_id': self.student_id.id,
                'default_invoice_id': self.id,
                'default_amount': self.amount,
            }
        }
