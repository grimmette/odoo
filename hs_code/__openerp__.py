# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'HS Code',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Add field HS Code',
    'description': """
Add field HS Code.
==============================================================

""",
    'author': 'GRIMMETTE,LLC',
    'website': 'http://www.grimmette.com',
    'support': 'info@grimmette.com',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    'installable': True,
}
