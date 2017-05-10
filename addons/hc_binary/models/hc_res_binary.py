# -*- coding: utf-8 -*-

from odoo import models, fields


class Binary(models.Model):
    _name = "hc.res.binary"
    _description = "Binary"

    content_type_id = fields.Many2one(
        comodel_name="hc.vs.mime.type",
        string="Content Type",
        required="True",
        help="MimeType of the binary content.")
    content = fields.Binary(
        string="Content",
        required="True",
        help="The actual content.")
