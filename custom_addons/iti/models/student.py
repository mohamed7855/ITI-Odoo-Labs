from odoo import models,fields

class Student(models.Model):
    _name = 'iti2.student'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('male', 'male'), ('female', 'female')])
    info = fields.Text()
    selary = fields.Integer()
    cv = fields.Html()
    dob = fields.Date()