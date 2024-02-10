from odoo import models,fields

class StateLog(models.Model):
    _name = 'iti2.log'

    description = fields.Char()

    student = fields.Many2one(comodel_name='iti2.student')
