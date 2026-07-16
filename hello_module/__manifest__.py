# -*- coding: utf-8 -*-
{
    'name': 'Hello Module',
    'version': '17.0.1.0.0',
    'summary': 'Module de test pour valider le workflow CI/CD',
    'description': """
Module minimal Odoo pour tester le workflow CI/CD.
Sert de terrain de jeu pour :
- valider le hot reload après push
- provoquer des conflits Git contrôlés
- vérifier que Mergify bloque les merges avec conflit
    """,
    'author': 'ilyasZAOUIA',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
