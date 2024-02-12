from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(comodel_name='hms.patient')


    email = fields.Char(required=True)
    vat = fields.Char(required=True)
    

    _sql_constraints = [
        ('unique_email_patient', 'UNIQUE(email, related_patient_id)',
         'The email is already assigned to a different patient.'),
    ]

    

    @api.constrains('related_patient_id', 'email')
    def check(self):
        for rec in self:
            if rec.related_patient_id:
                check_patient = self.env['res.partner'].search([('related_patient_id', '=', rec.related_patient_id.id), ('id', '!=', rec.id)])
                if check_patient:
                    raise ValidationError("The patient is linked to another customer")

    
            if rec.email:
                        check_email = self.env['res.partner'].search([('email', '=', rec.email), ('id', '!=', rec.id)])
                        if check_email:
                            raise ValidationError("The Email '%s' Already Exists." % rec.email)
                        
    
    # @api.constrains('related_patient_id')
    # def check_linked_patient_on_delete(self):
    #     for customer in self:
    #         if customer.related_patient_id:
    #             raise ValidationError("Cannot delete a customer linked to a patient.")