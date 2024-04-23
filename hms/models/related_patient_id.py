from odoo import fields, models, api
from odoo import exceptions

class Customer(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(comodel_name='hms_patient_2', string="Patient Id")
    vat = fields.Char(required=True)

    @api.constrains('related_patient_id')
    def _check_unique_patient(self):
        for customer in self:
            if customer.related_patient_id:
                existing_customer = self.env['res.partner'].search([
                    ('related_patient_id', '=', customer.related_patient_id.id),
                    ('id', '!=', customer.id),
                    ('related_patient_id', '!=', False)  
                ])
                if existing_customer:
                    raise exceptions.ValidationError('This Patient is already assigned to a different customer.')
