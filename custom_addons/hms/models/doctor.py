from odoo import models,fields

class Doctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = 'FirstName'

    FirstName = fields.Char(string='First Name')
    LastName = fields.Char(string='Last Name')
    Image = fields.Binary(string='Image')

    patients = fields.Many2many(comodel_name='hms.patient', string='Patients')