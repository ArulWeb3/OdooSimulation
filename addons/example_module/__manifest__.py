{
    'name': 'Example Module',
    'version': '1.0',
    'category': 'Technical',
    'summary': 'Example module demonstrating best practices',
    'description': """
        This module serves as a template and demonstration of best practices
        for Odoo module development in the simulation environment.
    """,
    'author': 'Your Company',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/example_views.xml',
    ],
    'demo': [
        'demo/example_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}