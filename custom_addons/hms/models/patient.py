from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re
from datetime import date


class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'first_name'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    history = fields.Html(string='History')
    cr_ratio = fields.Float(string='CR Ratio')
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ], string='Blood Type')
    pcr = fields.Boolean(string='PCR')
    image = fields.Binary(string='Image')
    address = fields.Text(string='Address')
    age = fields.Integer(string='Age', compute = 'calculate_age' , store = True)

    doctors = fields.Many2many(comodel_name='hms.doctor', string='Doctors')
    department = fields.Many2one(comodel_name='hms.department', string='Departments')
    departmentCapacity = fields.Integer(related='department.Capacity', string='Department Capacity')

    states = fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious'),
    ], string='States') 

    log = fields.One2many(comodel_name='hms.log', inverse_name='createdBy')
    
    email = fields.Char(validate='validate_email')
    _sql_constraints = [
        ('unique_patient_email', 'UNIQUE(email)', 'This Patient Email Already Exists Before'),
    ]

    @api.onchange('states')
    def log_state(self):
        for rec in self:
            if rec.states:
                rec.env['hms.log'].create({
                    'description': 'State Change To %s' % rec.states,
                    'createdBy': rec.id
                })

    @api.onchange('age')
    def pcr_check(self):
        for rec in self:
            if self.age and self.age < 30:
                self.pcr = True
                return {
                    'warning':{
                        'title': 'PCR Checked',
                        'message': 'PCR Checked To True'
                    }
                }
            else:
                self.pcr = False

    @api.constrains('email')
    def validate_email(self):
        for rec in self:
            if rec.email:
                regex_pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                if not re.match(regex_pattern, rec.email):
                    raise ValidationError('This Patient Email Not Valid')
                
    @api.depends('birth_date')
    def calculate_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 1
                