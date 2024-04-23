from odoo import models , fields



class Department_model(models.Model):
    _name = 'db.departments'
    _rec_name = 'name'
    name = fields.Char()
    capacity = fields.Integer()
    Is_opened = fields.Boolean()
    pationts_ids = fields.One2many('db.hms','department_id')

    # patients = fields.Char()



