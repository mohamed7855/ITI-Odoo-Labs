from odoo import models,fields

class Track(models.Model):
    _name = 'iti2.track'
    _rec_name = 'name'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean(default=False)

    students = fields.One2many(comodel_name= 'iti2.student', inverse_name= 'track')