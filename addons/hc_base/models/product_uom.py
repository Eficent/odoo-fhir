# -*- coding: utf-8 -*-

# Version 9

from openerp.osv import osv, fields, expression

class product_uom(osv.osv):
    _inherit = 'product.uom'

    _columns = {
        'code': fields.char('Code', 
            help="Code of this unit of measure. Case sensitive."),
        'source_id': fields.many2one('res.partner', 'Source',
            help="The source of the definition of the unit of measure."),
        'sequence': fields.integer('Sequence',
        	help="The ascending order of the unit of measure within a category.")
    }

class product_uom_categ(osv.osv):
    _inherit = 'product.uom.categ'

    _columns = {
        'code': fields.char('Code', 
            help="Code of this unit of measure category. Case sensitive."),
        'source_id': fields.many2one('res.partner', 'Source',
            help="The source of the definition of the unit of measure category."),
    }

# Version 10

# from openerp import models, fields, api

# class ProductUoM(models.Model):
#     _inherit = "product.uom"

#     code = fields.Char(
#         string="Code", 
#         help="Code of this unit of measure. Case sensitive.")
#     source_id = fields.Many2one(
#         comodel_name="res.partner", 
#         string="Source",
#         help="The source of the definition of the unit of measure.")