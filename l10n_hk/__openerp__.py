# -*- encoding: utf-8 -*-

# Copyright (C) 2015 GRIMMETTE,LLC <info@grimmette.com>

{
    'name': 'Hong Kong - Accounting',
    'version': '1.1',
    'summary': 'Hong Kong - Accounting',
    'category': 'Localization/Account Charts',
    "license": "LGPL-3",     
    'description': """
This is the base module to manage the Chart of Accounts for Hong Kong in Odoo.
==============================================================================

    - Chart of Accounts
    
    """,
    'author': 'GRIMMETTE,LLC',
    'website': 'http://www.grimmette.com',
    'support': 'info@grimmette.com',
    'images': ['static/description/icon.png'],
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'data/account_chart_template.xml',
        'data/account_l10n_hk.xml',
        'data/account_tax_template.xml',
        'data/account_chart_template.yml',	
        'security/ir.model.access.csv'
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
}