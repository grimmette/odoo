# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2015 GRIMMETTE,LLC <info@grimmette.com>

{
    'name': 'Russia - Accounting IFRS',
    'version': '1.1',
    'summary': 'IFRS Chart of Accounts for Russia',
    'category': 'Localization/Account Charts',
    "license": "LGPL-3",     
    'description': """
This is the base module to manage the IFRS Chart of Accounts for Russia in Odoo.
==============================================================================

This is the IFRS Chart of Accounts for Russia Odoo localization and consists of:
    - IFRS Chart of Accounts
    - VAT tax structure
    """,
    'author': 'GRIMMETTE,LLC',
    'website': 'http://www.grimmette.com',
    'depends': [
        'account',
        'base_vat',
        'l10n_multilang',
    ],
    'data': [
        'data/account_chart_template.xml',
        'data/account_ifrs_russian.xml',
        'data/account_tax_template.xml',
        'data/account_chart_template.yml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/l10n_ru_ifrs_demo.yml',
        '../account/demo/account_bank_statement.yml',
        '../account/demo/account_invoice_demo.yml',
    ],
    'test': [
    ],
    'installable': True,
}
