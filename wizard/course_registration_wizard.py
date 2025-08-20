from odoo import models, fields, api

class CourseRegistrationWizard(models.TransientModel):
    _name = 'student.course.registration.wizard'
    _description = 'Course Registration Wizard'

    student_id = fields.Many2one('student.student', string='Student', required=True)
    course_ids = fields.Many2many('course.course', string='Courses')

    def action_register_courses(self):
        for course in self.course_ids:
            self.env['student.course.registration'].create({
                'student_id': self.student_id.id,
                'course_id': course.id,
            })
        self.student_id.state = 'enrolled'
        return {'type': 'ir.actions.act_window_close'}
