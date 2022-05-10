# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Manufacturing Order',
    'version': '1.0',
    'category': 'Manufacturing/Manufacturing',
    'sequence': 55,
    'summary': 'Manufacturing Custom',
    'depends': ['mrp', 'mrp_account', 'sale', 'base'],
    'description': "",
    'data': [
        # 'security/mrp_security.xml',
        # 'security/ir.model.access.csv',
        # 'views/mrp_bom_views.xml',
        'views/menu.xml',
        'views/mo_view.xml'
    ],
    'qweb': [],
    'demo': [
    
    ],
    'test': [],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
