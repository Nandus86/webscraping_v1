# -*- coding: utf-8 -*-

{
    'name': 'Web Scraping V1',
    'version': '16.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'A web scraping module with text field and webhook integration',
    'description': """
        This module adds:
        * Text field input
        * List view of entries
        * Webhook integration for data sending
    """,
    'author': 'Fernando Dias - v.1.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/webscraping_view.xml',
        'data/config_parameter.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['requests'],
    },
}