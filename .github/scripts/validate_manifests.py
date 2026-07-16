#!/usr/bin/env python3
"""
Valide la structure de tous les modules Odoo dans le repo.

Un dossier est considéré comme un module Odoo s'il contient un __init__.py.
Dans ce cas, il DOIT aussi contenir un __manifest__.py qui doit être un dict
Python parseable.

Utilisé par le workflow tests.yml.
"""
import ast
import os
import sys

SKIP_DIRS = {'.github', '.git', 'docs'}


def validate_manifest(module_dir):
    """Retourne (True, msg) si le manifest est valide, sinon (False, msg)."""
    manifest_path = os.path.join(module_dir, '__manifest__.py')

    with open(manifest_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        return False, f'Syntax error dans le manifest : {e}'

    # Un manifest doit contenir une seule expression qui évalue un dict
    if len(tree.body) != 1:
        return False, 'Le manifest doit contenir une seule expression'

    node = tree.body[0]
    if not isinstance(node, ast.Expr):
        return False, 'Le manifest doit être une expression, pas une instruction'

    if not isinstance(node.value, ast.Dict):
        return False, 'Le manifest doit être un dict'

    return True, 'OK'


def main():
    errors = []
    modules_found = []

    for entry in sorted(os.listdir('.')):
        if not os.path.isdir(entry):
            continue
        if entry in SKIP_DIRS or entry.startswith('.'):
            continue

        has_init = os.path.isfile(os.path.join(entry, '__init__.py'))
        has_manifest = os.path.isfile(os.path.join(entry, '__manifest__.py'))

        # Un dossier avec __init__.py mais sans __manifest__.py = erreur
        if has_init and not has_manifest:
            errors.append(f'{entry}: contient __init__.py mais pas __manifest__.py')
            continue

        # Un dossier avec __manifest__.py = c'est un module, on valide
        if has_manifest:
            ok, msg = validate_manifest(entry)
            if ok:
                modules_found.append(entry)
                print(f'OK: {entry}')
            else:
                errors.append(f'{entry}: {msg}')

    print()
    if errors:
        print(f'ÉCHEC : {len(errors)} erreur(s) détectée(s)')
        for err in errors:
            print(f'  - {err}')
        sys.exit(1)

    print(f'SUCCÈS : {len(modules_found)} module(s) validé(s)')


if __name__ == '__main__':
    main()
