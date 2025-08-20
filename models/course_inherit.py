from odoo import models, fields

class CourseInherit(models.Model):
    _inherit = 'course.course'

    fee = fields.Float(string='Fee')
