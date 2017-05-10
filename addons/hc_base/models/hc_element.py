# -*- coding: utf-8 -*-

from odoo import models, fields


class ElementElement(models.Model):
    _name = "hc.element"
    _description = "Element"

    extension_ids = fields.One2many(
        comodel_name="hc.element.extension",
        inverse_name="element_id",
        string="Extensions",
        help="Additional Content defined by implementations.")


class ElementExtension(models.Model):
    _name = "hc.element.extension"
    _description = "Element Extension"
    _inherit = ["hc.basic.association", "hc.extension"]

    element_id = fields.Many2one(
        comodel_name="hc.element",
        string="Element",
        help="Element associated with this Element Extension.")


class Extension(models.Model):
    _inherit = ["hc.element"]


class Narrative(models.Model):
    _inherit = ["hc.element"]


class Reference(models.Model):
    _inherit = ["hc.element"]
