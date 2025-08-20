from odoo import models, fields, api

class StudentGrade(models.Model):
    _name = 'student.grade'
    _description = 'Student Grade'
    _rec_name = 'name'

    name = fields.Char(string='Grade Name', compute='_compute_name', store=True)
    student_id = fields.Many2one('student.student', string='Student', required=True)
    exam_id = fields.Many2one('exam.exam', string='Exam', required=True)
    score = fields.Float(string='Score', required=True)
    grade = fields.Char(string='Grade', compute='_compute_grade', store=True)

    @api.depends('student_id.name', 'exam_id.name')
    def _compute_name(self):
        for record in self:
            record.name = f'{record.student_id.name} - {record.exam_id.name}'

    @api.depends('score', 'exam_id.max_score')
    def _compute_grade(self):
        for record in self:
            if record.exam_id.max_score > 0:
                percentage = (record.score / record.exam_id.max_score) * 100
                if percentage >= 90:
                    record.grade = 'A'
                elif percentage >= 80:
                    record.grade = 'B'
                elif percentage >= 70:
                    record.grade = 'C'
                elif percentage >= 60:
                    record.grade = 'D'
                else:
                    record.grade = 'F'
            else:
                record.grade = 'N/A'
