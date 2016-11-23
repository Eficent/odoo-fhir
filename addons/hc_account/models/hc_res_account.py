# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Account(models.Model):    
    _name = "hc.res.account"    
    _description = "Account"            
    _inherits = {"account.account": "account_account_id"}

    account_account_id = fields.Many2one(
        comodel_name="account.account", 
        string="Account", 
        required="True", 
        ondelete="cascade", 
        help="Account associated with this Account.")                    
    identifier_ids = fields.One2many(
        comodel_name="hc.account.identifier", 
        inverse_name="account_id", 
        string="Identifiers", 
        help="Account number.")                    
    status = fields.Selection(string="Account Status", 
        selection=[
            ("active", "Active"), 
            ("inactive", "Inactive"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="State of the procedure.")                    
    active_start_date = fields.Datetime(
        string="Active Start Date", 
        help="Start of the time window that transactions may be posted to this account.")                    
    active_end_date = fields.Datetime(
        string="Active End Date", 
        help="End of the time window that transactions may be posted to this account.")                    
    coverage_ids = fields.One2many(
        comodel_name="hc.account.coverage", 
        inverse_name="account_id", 
        string="Coverages", 
        help="The party(s) that are responsible for covering the payment of this account.")                  
    coverage_period_start_date = fields.Datetime(
        string="Coverage Period Start Date", 
        help="Start of the transaction window.")                    
    coverage_period_end_date = fields.Datetime(
        string="Coverage Period End Date", 
        help="End of the transaction window.")                    
    subject_type = fields.Selection(
        string="Subject Type",
        selection=[
            ("Patient", "Patient"), 
            ("Device", "Device"), 
            ("Practitioner", "Practitioner"), 
            ("Location", "Location"), 
            ("Healthcare Service", "Healthcare Service"), 
            ("Organization", "Organization")], 
        help="Type of what is account tied to.")                   
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        help="What is account tied to.")                    
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient account tied to.")                    
    subject_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Subject Device", 
        help="Device account tied to.")                    
    subject_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Subject Practitioner", 
        help="Practitioner account tied to.")                    
    subject_location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Subject Location", 
        help="Location account tied to.")                    
    subject_healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Subject Healthcare Service", 
        help="Healthcare Service account tied to.")                    
    subject_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Subject Organization", 
        help="Organization account tied to")                    
    owner_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Owner", 
        help="Who is responsible?")                    
    description = fields.Char(
        string="Description", 
        help="Explanation of purpose/use.")                    

@api.multi          
def _compute_subject_name(self):            
    for hc_res_account in self:     
        if hc_res_account.subject_type == 'Patient':    
            hc_res_account.subject_name = hc_res_account.subject_patient_id.name
        elif hc_res_account.subject_type == 'Device':   
            hc_res_account.subject_name = hc_res_account.subject_device_id.name
        elif hc_res_account.subject_type == 'Practitioner': 
            hc_res_account.subject_name = hc_res_account.subject_practitioner_id.name
        elif hc_res_account.subject_type == 'Location': 
            hc_res_account.subject_name = hc_res_account.subject_location_id.name
        elif hc_res_account.subject_type == 'Healthcare Service':   
            hc_res_account.subject_name = hc_res_account.subject_healthcare_service_id.name
        elif hc_res_account.subject_type == 'Organization': 
            hc_res_account.subject_name = hc_res_account.subject_organization_id.name

class AccountIdentifier(models.Model):    
    _name = "hc.account.identifier"    
    _description = "Account Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    account_id = fields.Many2one(
        comodel_name="hc.res.account", 
        string="Account", 
        help="Account associated with this Account Identifier.")

class AccountCoverage(models.Model):    
    _name = "hc.account.coverage"   
    _description = "Account Coverage"       
    _inherit = ["hc.basic.association"]

    account_id = fields.Many2one(
        comodel_name="hc.res.account", 
        string="Account", 
        help="Account associated with this Account Coverage.")             
    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        help="Coverage associated with this Account Coverage.")             
