from re import search
from odoo import models, fields, api
from datetime import date


class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True, help="Student's name")
    student_id = fields.Char(string="Student ID", required=True, copy=False)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        string="Gender",
        default="other",
    )
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Text(string="Address")
    image = fields.Image(string="Image")
    course_ids = fields.Many2many("course.course", string="Courses")
    registration_ids = fields.One2many(
        "student.course.registration", "student_id", string="Registrations"
    )
    grade_ids = fields.One2many('student.grade', 'student_id', string='Grades')
    state = fields.Selection(
        [
            ("new", "New"),
            ("enrolled", "Enrolled"),
            ("graduated", "Graduated"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="new",
    )
    _sql_constraints = [
        ("student_id_unique", "unique(student_id)", "Student ID must be unique"),
        ("email_unique", "unique(email)", "Email must be unique"),
    ]

    def action_create_invoice(self):
        invoice_vals = {
            "student_id": self.id,
            "amount": sum(self.course_ids.mapped("fee")),
            "due_date": fields.Date.today(),
            "registration_ids": [(6, 0, self.registration_ids.ids)],
        }
        invoice = self.env["student.invoice"].create(invoice_vals)
        return {
            "type": "ir.actions.act_window",
            "name": "Invoice",
            "res_model": "student.invoice",
            "view_mode": "form",
            "res_id": invoice.id,
            "target": "current",
        }

    @api.depends("date_of_birth")
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                record.age = (
                    today.year
                    - record.date_of_birth.year
                    - (
                        (today.month, today.day)
                        < (record.date_of_birth.month, record.date_of_birth.day)
                    )
                )
            else:
                record.age = 0


class StudentCourseRegistration(models.Model):
    _name = "student.course.registration"
    _description = "Student Course Registration"
    _rec_name = 'name'

    name = fields.Char(string='Name', compute='_compute_name', store=True)
    student_id = fields.Many2one("student.student", string="Student", required=True)
    course_id = fields.Many2one("course.course", string="Course", required=True)
    registration_date = fields.Date(
        string="Registration Date", default=fields.Date.context_today
    )
    fee = fields.Float(
        string="Fee", related="course_id.credits", store=True, readonly=False
    )

    @api.depends('student_id.name', 'course_id.name')
    def _compute_name(self):
        for record in self:
            record.name = f'{record.student_id.name} - {record.course_id.name}'
