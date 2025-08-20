from odoo import models, fields

class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'Teacher'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    course_ids = fields.One2many('course.course', 'teacher_id', string='Courses')
