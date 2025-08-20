from odoo import models, fields, api

class Exam(models.Model):
    _name = 'exam.exam'
    _description = 'Exam'
    _rec_name = 'name'

    name = fields.Char(string='Exam Name', required=True)
    course_id = fields.Many2one('course.course', string='Course', required=True)
    exam_date = fields.Date(string='Exam Date', required=True)
    max_score = fields.Float(string='Maximum Score', required=True)
    grade_ids = fields.One2many('student.grade', 'exam_id', string='Grades')
    student_ids = fields.Many2many('student.student', string='Students')
