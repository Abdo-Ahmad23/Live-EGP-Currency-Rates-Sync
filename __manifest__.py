{
    'name': 'Advanced Live EGP Currency Rates Sync',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Sync daily EGP exchange rates via ExchangeRate-API with UI configuration',
    'author': 'Abdelrahman ',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_data.xml',
        'views/config_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}