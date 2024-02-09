from odoo import models,fields

class Doctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = 'FirstName'

    FirstName = fields.Char(string='First Name')
    LastName = fields.Char(string='Last Name')
    Image = fields.Binary(string='Image')