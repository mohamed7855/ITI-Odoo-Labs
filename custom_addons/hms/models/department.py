from odoo import models,fields

class Department(models.Model):
    _name = 'hms.department'
    _rec_name = 'Name'

    Name = fields.Char(string='Name')
    Capacity = fields.Integer()
    Is_opened = fields.Boolean()
    Patients = fields.One2many(comodel_name='hms.patient', inverse_name='department')