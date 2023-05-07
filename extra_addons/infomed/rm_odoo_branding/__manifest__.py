# -*- coding: utf-8 -*-
{
    'name': "Remove Odoo Branding",
    'version': '15.0.0.1',
    'category': 'Website',
    'author': "Mihnea Grigore",
    'depends': [
        'website',
        'web',
    ],
    'data': [
        'views/no_powered_by_odoo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
