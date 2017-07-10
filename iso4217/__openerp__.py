# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2015 GRIMMETTE,LLC <info@grimmette.com>

{
    'name': 'Codes and Full Names of Currencies ISO 4217',
    'version': '1.1',
    'summary': 'Codes and Full Names of Currencies ISO 4217',
    'category': 'Accounting & Finance',
    'description': """
Codes and full name of the currencies - ISO 4217.

    """,
    'author': 'GRIMMETTE,LLC',
    'website': 'http://www.grimmette.com',
    'support': 'info@grimmette.com',
    'depends': [
        'base',
    ],
    'data': [
        'iso4217_view.xml',
        'data/iso4217.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
}
