from odoo import api, fields , models

class CompanyBranch(models.Model):
    _name='company.hrm.branch'
    _description = 'Company HRM'

    name = fields.Char(string="Company Name",required=True)
    branches = fields.Char(string="Branches")
    company_ids = fields.Many2one('company.hrm',string="Company Name")

    
    



    