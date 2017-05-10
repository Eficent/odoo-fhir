# -*- coding: utf-8 -*-

from odoo import models, fields


class Dosage(models.Model):
    _name = "hc.dosage"
    _description = "Dosage"

    sequence = fields.Integer(
        string="Sequence",
        help="The order of the dosage instruction.")
    text = fields.Text(
        string="Text",
        help="Free text dosage instruction e.g. SIG.")
    additional_instruction_ids = fields.Many2many(
        comodel_name="hc.vs.additional.instruction.code",
        relation="dosage_instruction_additional_instruction_rel",
        string="Additional Instruction",
        help='Supplemental instruction - e.g. "with meals".')
    patient_instruction = fields.Text(
        string="Patient Instruction",
        help="Patient or consumer oriented instructions.")
    timing_id = fields.Many2one(
        comodel_name="hc.dosage.timing",
        string="Timing",
        help="When medication should be administered.")
    as_needed_type = fields.Selection(
        string="As Needed Type",
        selection=[
            ("boolean", "Boolean"),
            ("code", "Code")],
        help='Type of take "as needed" (for x).')
    as_needed_name = fields.Char(
        string="As Needed",
        compute="_compute_as_needed_name",
        store="True",
        help='Take "as needed" (for x).')
    as_needed = fields.Boolean(
        string="As Needed",
        help='Numerator value of take "as needed" (for x).')
    as_needed_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.as.needed.reason",
        string="As Needed Code",
        help='Code of take "as needed" (for x).')
    site_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code",
        string="Site",
        help="Body site to administer to.")
    route_id = fields.Many2one(
        comodel_name="hc.vs.route.code",
        string="Route",
        help="How drug should enter body.")
    method_id = fields.Many2one(
        comodel_name="hc.vs.administration.method.code",
        string="Method",
        help="Technique for administering medication.")
    dose_type = fields.Selection(
        string="Dose Type",
        selection=[
            ("range", "Range"),
            ("quantity", "Quantity")],
        help="Type of amount of medication per dose.")
    dose_name = fields.Char(
        string="Dose",
        compute="_compute_dose_name",
        store="True",
        help="Amount of medication per dose.")
    dose_range_low = fields.Float(
        string="Dose Range Low",
        help="Low limit of amount of medication per dose.")
    dose_range_high = fields.Float(
        string="Dose Range High",
        help="High limit of amount of medication per dose.")
    dose_range_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Dose Range UOM",
        help="Dose range unit of measure.")
    dose_quantity = fields.Float(
        string="Dose Quantity",
        help="Amount of medication per dose.")
    dose_quantity_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Dose Quantity UOM",
        help="Dose quantity unit of measure.")
    max_dose_per_period_numerator = fields.Float(
        string="Max Dose Per Period Numerator",
        help="Numerator value of upper limit on medication per unit of time.")
    max_dose_per_period_numerator_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Max Dose Per Period Numerator UOM",
        help="Max Dose Per Period Numerator unit of measure.")
    max_dose_per_period_denominator = fields.Float(
        string="Max Dose Per Period Denominator",
        help="Denominator value of upper limit on medication per unit of time.")
    max_dose_per_period_denominator_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Max Dose Per Period Denominator UOM",
        help="Max Dose Per Period Denominator unit of measure.")
    max_dose_per_period_ratio = fields.Float(
        string="Max Dose Per Period Ratio",
        compute="_compute_max_dose_per_period_ratio",
        store="True",
        help="Ratio of upper limit on medication per unit of time.")
    max_dose_per_period_ratio_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Max Dose Per Period Ratio UOM",
        help="Max Dose Per Period Ratio unit of measure.")
    max_dose_per_administration = fields.Float(
        string="Max Dose Per Administration",
        help="Upper limit on medication per administration")
    max_dose_per_administration_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Max Dose Per Administration UOM",
        help="Max Dose Per Administration unit of measure.")
    max_dose_per_lifetime = fields.Float(
        string="Max Dose Per Lifetime",
        help="Upper limit on medication per lifetime of the patient")
    max_dose_per_lifetime_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Max Dose Per Lifetime UOM",
        help="Max Dose Per Lifetime unit of measure.")
    rate_type = fields.Selection(
        string="Rate Type",
        selection=[
            ("ratio", "Ratio"),
            ("range", "Range"),
            ("quantity", "Quantity")],
        help="Type of amount of medication per unit of time.")
    rate_name = fields.Char(
        string="Rate",
        compute="_compute_rate_name",
        store="True",
        help="Amount of medication per unit of time.")
    rate_numerator = fields.Float(
        string="Rate Numerator",
        help="Numerator value of amount of medication per unit of time.")
    rate_numerator_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Rate Numerator UOM",
        help="Rate Numerator unit of measure.")
    rate_denominator = fields.Float(
        string="Rate Denominator",
        help="Denominator value of amount of medication per unit of time.")
    rate_denominator_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Rate Denominator UOM",
        help="Rate Denominator unit of measure.")
    rate_ratio = fields.Float(
        string="Rate Ratio",
        compute="_compute_rate_ratio",
        store="True",
        help="Ratio of amount of medication per unit of time.")
    rate_ratio_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Rate Ratio UOM",
        help="Rate Ratio unit of measure.")
    rate_range_low = fields.Float(
        string="Rate Range Low",
        help="Low limit of amount of medication per unit of time.")
    rate_range_high = fields.Float(
        string="Rate Range High",
        help="High limit of amount of medication per unit of time.")
    rate_range_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Rate Range UOM",
        help="Rate Range unit of measure.")
    rate_quantity = fields.Float(
        string="Rate Quantity",
        help="Amount of medication per unit of time.")
    rate_uom_id = fields.Many2one(
        comodel_name="product.uom",
        string="Rate Quantity UOM",
        help="Rate Quantity unit of measure.")


class DosageTiming(models.Model):
    _name = "hc.dosage.timing"
    _description = "Dosage Timing"
    _inherit = ["hc.basic.association", "hc.timing"]


class AdditionalInstructionCode(models.Model):
    _name = "hc.vs.additional.instruction.code"
    _description = "Additional Instruction Code"
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name",
        help="Name of this additional instruction code.")
    code = fields.Char(
        string="Code",
        help="Code of this additional instruction code.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.additional.instruction.code",
        string="Parent",
        help="Parent additional instruction code.")
