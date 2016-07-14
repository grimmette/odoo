# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2015 GRIMMETTE,LLC <info@grimmette.ru>

from openerp import api, fields, models, _

class AccountTax(models.Model):
    _name = 'account.tax'
    _inherit = 'account.tax'

    description = fields.Char(string='Label on Invoices', translate=True)
    
