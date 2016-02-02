# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2015 GRIMMETTE,LLC <info@grimmette.com>

from openerp.osv import fields, osv


class res_currency(osv.osv):
    _name = 'res.currency'
    _inherit = 'res.currency'
    _columns = {
        'code': fields.integer("Code"),
        'full_name': fields.char("Full name", translate=True),
    }


