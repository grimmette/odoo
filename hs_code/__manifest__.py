# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'HS Code',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Add field HS Code',
    'license': "AGPL-3",
    'description': """
Add field HS Code.
==============================================================

""",
    'author': 'GRIMMETTE,LLC',
    'support': 'info@grimmette.com',
    'depends': ['product'],
    'images': ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    'installable': True,
    
}
