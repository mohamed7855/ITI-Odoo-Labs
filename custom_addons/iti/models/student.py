from odoo import models,fields,api

class Student(models.Model):
    _name = 'iti2.student'

    name = fields.Char(required=True)
    age = fields.Integer()
    gender = fields.Selection([('male', 'male'), ('female', 'female')])
    info = fields.Text()
    selary = fields.Integer()
    cv = fields.Html()
    dob = fields.Date()

    is_working = fields.Boolean(default=False)
    summery = fields.Text()

    track = fields.Many2one(comodel_name='iti2.track')
    trackCapacity = fields.Integer(related='track.capacity')

    state = fields.Selection([('level1', 'Prep'), ('level2', 'Sec'), ('level3', 'Graduate')])

    log = fields.One2many(comodel_name='iti2.log', inverse_name='student')
    logDescription = fields.Char(related='log.description')


    def ChangeState(self):
        if self.state == 'level1':
            self.state = 'level2'
        elif self.state == 'level2':
            self.state = 'level3'
        else:
            self.state = 'level1'

    @api.onchange('is_working')
    def set_summery(self):
        for rec in self:    
            if rec.summery == False:
                rec.summery = 'This Student is working'
            else:
                pass
    
    @api.onchange('state')
    def warn_user(self):
        for rec in self:    
            return {
                'warning':{
                    'title':'State Change Warning',
                    'message': 'State Change To %s'%rec.state
                }
            }
    
    @api.onchange('state')
    def log_state(self):
        for rec in self: 
            rec.env['iti2.log'].create({
                'description': 'State Change To %s'%rec.state,
                'student': rec.id
            })

    