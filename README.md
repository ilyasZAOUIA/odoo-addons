# odoo-addons

Repo des modules Odoo custom de l'entreprise.

## Structure

```
odoo-addons/
├── .github/workflows/         # GitHub Actions (CI, sync, notifications)
├── .mergify.yml              # Règles Mergify pour les merges vers staging
├── hello_module/             # Module de test pour valider le workflow
└── (autres modules à venir)
```

## Workflow de développement

### Créer une nouvelle feature

```bash
# Récupérer la dernière version de staging
git checkout staging
git pull

# Créer une branche à partir de staging
git checkout -b feature-ma-nouvelle-fonction

# ... développer, commit, push régulièrement ...

# Push
git push origin feature-ma-nouvelle-fonction
```

### Merger vers staging

1. Ouvrir une Pull Request depuis GitHub UI (base : `staging`)
2. Vérifier que la CI `tests` passe (vert)
3. Ajouter le label `ready-to-merge`
4. Mergify va :
   - Vérifier qu'il n'y a pas de conflit
   - Vérifier que la branche est à jour avec staging
   - Si les deux OK → merger automatiquement
   - Si conflit → commenter avec les commandes pour rebase

### Branches permanentes

- `main` — reflète l'état de la production
- `staging` — reflète l'état de staging
- `dev-<nom>` — branche personnelle de chaque développeur, synchronisée avec son sandbox
- `preprod` — reflète l'état de preprod

## Sandboxes de test

Chaque branche `dev-*`, `staging`, `preprod` est synchronisée automatiquement avec un sandbox sur la VM. Voir le repo `odoo-cicd-test` pour l'infrastructure.

URLs des sandboxes :

- https://dev1.odoo.local
- https://dev2.odoo.local
- https://staging.odoo.local
- https://preprod.odoo.local
