# -*- coding: utf-8 -*-

from openerp import models, fields, api

class HealthcareService(models.Model):  
    _name = "hc.res.healthcare.service" 
    _description = "Healthcare Service"

    identifier_ids = fields.One2many(
        comodel_name="hc.healthcare.service.identifier", 
        inverse_name="healthcare_service_id", 
        string="Identifiers", 
        help="External Identifiers for this item.")       
    is_active = fields.Boolean(
        string="Active", 
        help="Whether this healthcare service is in active use.")
    provided_by_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Provided By", 
        help="The organization that provides this Healthcare Service.")      
    service_category_id = fields.Many2one(
        comodel_name="hc.vs.service.category", 
        string="Category", 
        help="Identifies the broad category of service being performed or delivered. Selecting a Service Category then determines the list of relevant service types that can be selected in the Primary Service Type.")        
    service_type_ids = fields.Many2many(
        comodel_name="hc.vs.service.type", 
        string="Service Types", 
        help="Type of service that may be delivered or performed.")
    specialty_ids = fields.Many2many(
        comodel_name="hc.vs.c80.practice.code", 
        string="Specialties", 
        help="Collection of Specialties handled by the Service Site. This is more of a Medical Term.")
    location_ids = fields.One2many(
        comodel_name="hc.healthcare.service.location", 
        inverse_name="healthcare_service_id", 
        string="Location", 
        help="Location(s) where service may be provided.")        
    service_name = fields.Char(
        string="Service Name", 
        help="Further description of the service as it would be presented to a consumer while searching.")        
    comment = fields.Text(
        string="Comment", 
        help="Any additional description of the service and/or any specific issues not covered by the other attributes, which can be displayed as further detail under the serviceName.")       
    extra_details = fields.Text(
        string="Extra Details", 
        help="Extra details about the service that can't be placed in the other fields.")       
    photo_ids = fields.One2many(
        comodel_name="hc.healthcare.service.photo", 
        inverse_name="healthcare_service_id", 
        string="Photo", 
        help="If there is a photo/symbol associated with this Healthcare Service, it may be included here to facilitate quick identification of the service in a list.")       
    telecom_ids = fields.One2many(
        comodel_name="hc.healthcare.service.telecom", 
        inverse_name="healthcare_service_id", 
        string="Telecoms", 
        help="List of contacts related to this specific healthcare service. If this is empty, then refer to the location's contacts.")     
    coverage_area_ids = fields.One2many(
        comodel_name="hc.healthcare.service.coverage.area", 
        inverse_name="healthcare_service_id", 
        string="Coverage Areas", 
        help="The location(s) that this service is available to (not where the service is provided).")       
    service_provision_code_ids = fields.Many2many(
        comodel_name="hc.vs.service.provision.condition", 
        string="Service Provision Codes", 
        help="The code(s) that detail the conditions under which the healthcare service is available/offered.")
    eligibility_id = fields.Many2one(
        comodel_name="hc.vs.service.eligibility", 
        string="Eligibility", 
        help="Does this service have specific eligibility requirements that need to be met in order to use the service.")      
    eligibility_note = fields.Text(
        string="Eligibility Note", 
        help="Describes the eligibility conditions for the service.")     
    program_name_ids = fields.One2many(
        comodel_name="hc.healthcare.service.program.name", 
        inverse_name="healthcare_service_id", 
        string="Program Names", 
        help="Program Names that can be used to categorize the service.")       
    characteristic_ids = fields.Many2many(
        comodel_name="hc.vs.service.characteristic", 
        string="Characteristics", 
        help="Collection of Characteristics (attributes).")      
    referral_method_ids = fields.Many2many(
        comodel_name="hc.vs.service.referral.method", 
        string="Referral Methods", 
        help="Ways that the service accepts referrals.")       
    public_key = fields.Char(
        string="Public Key", 
        help="The public part of the 'keys' allocated to an Organization by an accredited body to support secure exchange of data over the internet. To be provided by the Organization, where available.")       
    is_appointment_required = fields.Boolean(
        string="Appointment Required", 
        help="Indicates if an appointment is required for access to this service.")     
    availability_exceptions = fields.Text(
        string="Availability Exceptions", 
        help="A description of Site availability exceptions, e.g., public holiday availability. Succinctly describing all possible exceptions to normal Site availability as details in the Available Times and Not Available Times.")      
    available_time_ids = fields.One2many(
        comodel_name="hc.healthcare.service.available.time", 
        inverse_name="healthcare_service_id", 
        string="Available Times", 
        help="A Collection of times that the Service Site is available.")
    not_available_ids = fields.One2many(
        comodel_name="hc.healthcare.service.not.available.time", 
        inverse_name="healthcare_service_id", 
        string="Not Available Times", 
        help="The Healthcare Service is not available during this period of time due to the provided reason.")

class HealthcareServiceAvailableTime(models.Model): 
    _name = "hc.healthcare.service.available.time"  
    _description = "Healthcare Service Available Time"      
    _inherit = ["hc.available.time"]    

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare Service available during this period of time.")                 

class HealthcareServiceNotAvailableTime(models.Model):  
    _name = "hc.healthcare.service.not.available.time"  
    _description = "Healthcare Service Not Available Time"      
    _inherit = ["hc.not.available.time"]

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare Service not available during this period of time.")                 

class HealthcareServiceIdentifier(models.Model):    
    _name = "hc.healthcare.service.identifier"  
    _description = "Healthcare Service Identifier"      
    _inherit = ["hc.basic.association", "hc.identifier"]

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service associated with this Healthcare Service Identifier.")                                                  

class HealthcareServicePhoto(models.Model): 
    _name = "hc.healthcare.service.photo"   
    _description = "Healthcare Service Photo"       
    _inherit = ["hc.basic.association", "hc.attachment"]    

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service associated with this Healthcare Service Photo.")                  

class HealthcareServiceTelecom(models.Model):   
    _name = "hc.healthcare.service.telecom" 
    _description = "Healthcare Service Telecom"     
    _inherit = ["hc.contact.point.use"] 
    _inherits = {"hc.contact.point": "telecom_id"}  

    telecom_id = fields.Many2one(
        comodel_name="hc.contact.point", 
        string="Telecom", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this Healthcare Service Telecom.")                      
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare Service associated with this Healthcare Service Telecom.")                                  

class HealthcareServiceProgramName(models.Model):
    _name = "hc.healthcare.service.program.name"    
    _description = "Healthcare Service Program Name"
    _inherit = ["hc.basic.association"]            

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare Service associated with this Healthcare Service Program Name.")                   
    program_name = fields.Char(
        string="Program Name", 
        help="Program Name associated with this Healthcare Service Program Name.")                 

class HealthcareServiceLocation(models.Model):  
    _name = "hc.healthcare.service.location"    
    _description = "Healthcare Service Location"        
    _inherit = ["hc.basic.association"] 
    _inherits = {"hc.res.location": "location_id"}

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location",
        required="True", 
        ondelete="restrict", 
        help="Location associated with this Healthcare Service Location.")                    
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare Service associated with this Healthcare Service Location.")                               

class HealthcareServiceCoverageArea(models.Model):   
    _name = "hc.healthcare.service.coverage.area"    
    _description = "Healthcare Service Coverage Area"        
    _inherit = ["hc.basic.association"] 
    _inherits = {"hc.res.location": "location_id"}

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location",
        required="True", 
        ondelete="restrict", 
        help="Coverage Area associated with this Healthcare Service Coverage Area.") 
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare Service associated with this Healthcare Service Coverage Area.")                   

class ServiceType(models.Model):    
    _name = "hc.vs.service.type"    
    _description = "Service Type"       
    _inherit = ["hc.value.set.contains"]        

class ServiceProvisionCondition(models.Model): 
    _name = "hc.vs.service.provision.condition"    
    _description = "Service Provision Condition"       
    _inherit = ["hc.value.set.contains"]    

class ServiceCategory(models.Model):    
    _name = "hc.vs.service.category"    
    _description = "Service Category"       
    _inherit = ["hc.value.set.contains"]    

class ServiceEligibility(models.Model): 
    _name = "hc.vs.service.eligibility" 
    _description = "Service Eligibility"        
    _inherit = ["hc.value.set.contains"]    

class ServiceReferralMethod(models.Model):  
    _name = "hc.vs.service.referral.method" 
    _description = "Service Referral Method"        
    _inherit = ["hc.value.set.contains"]    

class ServiceCharacteristic(models.Model):  
    _name = "hc.vs.service.characteristic"  
    _description = "Service Characteristic"     
    _inherit = ["hc.value.set.contains"]    
                  
