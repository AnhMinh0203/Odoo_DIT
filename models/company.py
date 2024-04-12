from odoo import api, fields , models

class Company(models.Model):
    _name='company.hrm'
    _description = 'Company HRM'

    name = fields.Char(string="Company Name",required=True)
    contact = fields.Char(string="Contact")
    address =  fields.Char(string="Address")
    address_2 =  fields.Char(string=" ")
    tax_id = fields.Char(string="Tax")
    city = fields.Char(string=" ")
    state = fields.Selection(
        [('state_1','State 1'),('state_2','State 2'),('state_3','State 3')],
        string=" ",default='state_1')
    zip = fields.Char(string=" ")
    country = fields.Selection(
        [('country','Country'),('us','US'),('uk','UK'),('vn','Vietnamease')],
        string=" ",default='country')
    company_id = fields.Char(string="Company ID")
    currency = fields.Selection(
        [('currency_1','Currency 1'),('currency_2','Currency 2'),('currency_3','Currency 3')],
        string="Currency",default='currency_1')

    phone = fields.Char(string="Phone") 
    mobile = fields.Char(string="Mobile") 
    email = fields.Char(string="Email") 
    website = fields.Char(string="Wensite") 
    parent_company = fields.Selection(
        [('parent_company_1','Parent company 1'),('parent_company_2','Parent company 2'),('parent_company_3','Parent company 3')],
        string="Parent company",default='currency_1')
    email_domain = fields.Char(string="Email Domain") 
    color = fields.Selection(
        [('yeallow','Yellow'),('green','Green'),('red','Red')],
        string="Color",default='yeallow')
    branch_ids = fields.One2many("company.hrm.branch","company_ids",string="Branches")

    def action_send_msg(self):
        print("Check Send Msg")

    def action_log_note(self):
        print("Check Log Note")

    