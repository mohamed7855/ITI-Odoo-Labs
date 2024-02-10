from odoo import models,fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    # _name = 'product.template2' # create new DB with all old fields and add next fields

    barcode2 = fields.Char()

    barcode = fields.Char(required=True)
