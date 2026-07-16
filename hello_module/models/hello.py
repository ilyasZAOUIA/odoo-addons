# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Hello(models.Model):
    """
    Modèle de test très simple.

    Pour tester le hot-reload : modifie la valeur de `MESSAGE` ci-dessous,
    commit + push sur ta branche (dev-dev1 par exemple), et regarde ton
    sandbox se mettre à jour automatiquement.

    Pour tester un conflit : modifie la même ligne sur deux branches
    différentes, merge la première vers staging, puis essaie de merger la
    seconde. Mergify va bloquer et signaler le conflit.
    """

    _name = 'hello.message'
    _description = 'Hello Message'

    MESSAGE = "Bonjour tout le monde"

    name = fields.Char(string='Name', required=True)
    greeting = fields.Char(
        string='Greeting',
        compute='_compute_greeting',
        store=True,
    )

    @api.depends('name')
    def _compute_greeting(self):
        for record in self:
            record.greeting = f"{self.MESSAGE}, {record.name}!"
