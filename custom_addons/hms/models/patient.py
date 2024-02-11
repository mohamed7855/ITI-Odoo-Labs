from odoo import models,fields,api

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
    age = fields.Integer(string='Age')

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