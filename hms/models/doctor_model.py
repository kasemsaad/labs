from odoo import models , fields



class Doctor_model(models.Model):
    _name = 'db.doctors'
    _rec_name = 'first_name'
    first_name = fields.Char()
    last_name = fields.Char()
    Image = fields.Image()
    # pationts_ids = fields.Many2many('db.hms')


