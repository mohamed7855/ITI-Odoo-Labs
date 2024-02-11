from odoo import models,fields

class Log(models.Model):
    _name = 'hms.log'
    # _rec_name = 'FirstName'

    date = fields.Datetime(default=fields.Datetime.now, string='Date')
    description = fields.Char(string='Log')
    createdBy = fields.Many2one(comodel_name='hms.patient', string='Patient')