from odoo import models, api

class BoardInherit(models.Model):
    _inherit = 'board.board'

    @api.model
    def get_student_dashboard_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Dashboard',
            'res_model': 'board.board',
            'view_mode': 'form',
            'usage': 'menu',
            'view_id': self.env.ref('student_management.student_dashboard_form').id,
            'context': {
                'action_student': self.env.ref('student_management.action_student').id,
                'action_course': self.env.ref('student_management.action_course').id,
                'action_teacher': self.env.ref('student_management.action_teacher').id,
                'action_course_registration_wizard': self.env.ref('student_management.action_course_registration_wizard').id,
            },
        }
