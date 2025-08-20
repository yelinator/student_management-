from odoo import models, fields

class Course(models.Model):
    _name = 'course.course'
    _description = 'Course'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    credits = fields.Float(string='Credits')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    student_ids = fields.Many2many('student.student', string='Students')
