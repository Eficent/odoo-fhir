# -*- coding: utf-8 -*-

# Version 9

from odoo import models, fields


class ProductUom(models.Model):
    _inherit = 'product.uom'

    code = fields.Char('Code',
                       help="Code of this unit of measure. Case sensitive.")
    source_id = fields.Many2one('res.partner', 'Source',
                                help="The source of the definition of the unit of measure.")
    sequence = fields.Integer('Sequence',
                              help="The ascending order of the unit of measure within a category.")


class ProductUomCategory(models.Model):
    _inherit = 'product.uom.categ'

    code = fields.Char('Code',
                       help="Code of this unit of measure category. Case sensitive.")
    source_id = fields.Many2one('res.partner', 'Source',
                                help="The source of the definition of the unit of measure category.")
