{
    'name': 'Base Cascada MFH',
    'version' : '1.2',
    'summary': 'Módulo base con los cambios',
    'sequence': 10,
    'description': """
Father (TOTP)
================================
Allows users to configure
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.marlonfalcon.com',
    'depends': ['base', 'crm', 'base_bim_2'],
    'category': 'Extra Tools',
    'auto_install': False,
    'data': [
        'views/view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'base_cascada/static/src/chatter/chatter.xml',
        ],
    },
    'license': 'LGPL-3',
}