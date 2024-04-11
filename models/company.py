from odoo import api, fields , models

class Company(models.Model):
    _name='company.hrm'
    _description = 'Company HRM'

    name = fields.Char(string="Company Name",required=True)
    contact = fields.Char(string="Contact")
    address =  fields.Char(string="Address")
    tax_id = fields.Char(string="Tax")
    city = fields.Char(string=" ")
    state = fields.Char(string=" ")
    zip = fields.Char(string=" ")
    country = fields.Selection(
        [('country','Country'),('us','US'),('uk','UK'),('vn','Vietnamease')],
        string=" ",default='country')
    company_id = fields.Char(string="Company ID")
    currency = fields.Char(string="Currency")

    phone = fields.Char(string="Phone") 
    mobile = fields.Char(string="Mobile") 
    email = fields.Char(string="Email") 
    website = fields.Char(string="Wensite") 
    parent_company = fields.Char(string="Parent Company") 
    email_domain = fields.Char(string="Email Domain") 
    color = fields.Char(string="Color") 
    branch_ids = fields.One2many("company.hrm.branch","company_ids",string="Branches")

    def action_send_msg(self):
        print("Check Send Msg")

    def action_log_note(self):
        print("Check Log Note")

    