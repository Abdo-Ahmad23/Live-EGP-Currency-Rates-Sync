{
    'name': 'Global Live Currency Rates Sync by Country',
    'version': '17.0.1.1.0',
    'category': 'Accounting',
    'summary': 'Automatically sync live exchange rates daily based on selected country via ExchangeRate-API',
    'description': """
        Advanced Odoo 17 module to automatically fetch and update live exchange rates for all active currencies.
        Instead of hardcoded currencies, users can select their target country from settings, 
        and the system dynamically updates all rates against that country's base currency via API.
    """,
    'author': 'Abdelrahman Abdelhameed',
    'website': 'https://www.linkedin.com/in/abdu-ahmad/',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_data.xml',
        'views/config_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}