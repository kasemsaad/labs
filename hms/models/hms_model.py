from odoo import models , fields , api
from odoo.exceptions import ValidationError

class Hms_model_LevelLog(models.Model):
    _name = 'db.hms.log'
    description = fields.Text()
    pationt_id = fields.Many2one('db.hms')


class Hms_model(models.Model):
    _name = 'db.hms'
    _rec_name = 'first_name'
    first_name = fields.Char()
    lirst_name = fields.Char()
    date_birth = fields.Date()
    history =fields.Html()
    cr_ratio =fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ])
    PCR = fields.Boolean()
    Image = fields.Image()
    Address = fields.Text()
    age = fields.Integer()
    email = fields.Char(required=True)

    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'Email must be unique!')
    ]

    @api.constrains('email')
    def _check_unique_email(self):
        for record in self:
            if record.email:
                check = self.env['db.hms'].search([('email', '=', record.email), ('id', '!=', record.id)])
                if check:
                    raise ValidationError("email already exists!")





    doctor_id=fields.Many2many('db.doctors')
    department_id=fields.Many2one('db.departments')
    level_logs=fields.One2many('db.hms.log','pationt_id')

    @api.onchange('age')
    def _onchange_pcr(self):
        if(self.age < 30):
            self.PCR = True
            return{
                'warning':{
                    'title':'warning',
                    'message':'PCR has checked'
                }
            }
        else:
            self.PCR = False
            return{
                'warning':{
                    'title':'warning',
                    'message':'PCR has not checked'
                }
            }
        


    @api.onchange('level')
    def create_level_log(self):
        if self.level:
            vals = {
                'description' : 'Level change to %s'(self.level),
                'pationt_id' :self.id
            }
            self.env['db.hms.log'].create(vals)
