from odoo import models, fields, api

class StudentPayment(models.Model):
    _name = 'student.payment'
    _description = 'Student Payment'
    _rec_name = 'name'

    name = fields.Char(string='Payment Number', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('student.payment'))
    student_id = fields.Many2one('student.student', string='Student', required=True)
    invoice_id = fields.Many2one('student.invoice', string='Invoice')
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True, default=fields.Date.context_today)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank Transfer'),
        ('card', 'Credit/Debit Card'),
    ], string='Payment Method', default='cash')

    def create(self, vals):
        payment = super(StudentPayment, self).create(vals)
        if payment.invoice_id:
            if payment.invoice_id.amount == payment.amount:
                payment.invoice_id.state = 'paid'
        return payment
