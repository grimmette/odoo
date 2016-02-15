# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2015 GRIMMETTE,LLC <info@grimmette.ru>

import models
#import l10n_ru_ifrs
from openerp import SUPERUSER_ID


def load_translations(cr, registry):
    chart_template = registry['ir.model.data'].xmlid_to_object(cr, SUPERUSER_ID, 'l10nru_ifrs_chart_template')
    chart_template.process_coa_translations()