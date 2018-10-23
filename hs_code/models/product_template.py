# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    hs_code = fields.Char('HS Code')


