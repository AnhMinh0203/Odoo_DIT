from odoo import api, fields , models

class Field(models.Model):
    _name='field.hrm'
    _description = 'Field HRM'

    field_name = fields.Char(string="Field Name",required=True)
    field_lable = fields.Char(string="Field Lable",required=True)
    field_model = fields.Char(string="Field Modle",required=True)
    field_type = fields.Char(string="Field Type",required=True)
    field_help= fields.Char(string="Field Help",required=True)
    require = fields.Boolean(string="Require",default=False)
    readonly = fields.Boolean(string="Readonly",default=False)
    stored = fields.Boolean(string="Stored",default=False)
    indexed  = fields.Boolean(string="Indexed",default=False)
    copied = fields.Boolean(string="Copied",default=False)



    