# Dossier 3 — Automatisation IHM (Selenium WebDriver)

Suite de tests Selenium pour la plateforme **Restful-Booker**
(`https://automationintesting.online/`).

---

## Architecture — Page Object Model (POM)

```
Dossier3/
├── conftest.py                  # Fixtures pytest (WebDriver)
├── pytest.ini                   # Configuration pytest + marqueurs
├── requirements.txt             # Dépendances Python
│
├── data/
│   └── test_data.py             # Jeu de données de test (aucune donnée en dur dans les pages)
│
├── pages/                       # Couche POM — localisateurs + actions
│   ├── base_page.py             # Classe mère : helpers WebDriverWait exclusivement
│   ├── home_page.py             # Page principale (formulaire contact + réservation)
│   ├── admin_login_page.py      # Page de connexion admin
│   └── admin_dashboard_page.py  # Tableau de bord admin (gestion des chambres)
│
├── tests/                       # Scripts de test pytest
│   ├── test_contact_form.py     # Happy & Negative path — formulaire de contact
│   ├── test_admin_login.py      # Happy & Negative path — authentification admin
│   ├── test_admin_rooms.py      # Happy & Negative path — gestion des chambres
│   └── test_room_booking.py     # Happy & Negative path — réservation en ligne
│
├── utils/
│   └── driver_factory.py        # Instanciation du WebDriver (Chrome / Firefox)
│
└── reports/                     # Généré automatiquement par pytest-html
```

### Principes respectés

| Exigence | Implémentation |
|---|---|
| Pattern POM | `pages/` contient localisateurs + actions ; `tests/` contient uniquement les assertions |
| Attentes explicites uniquement | `BasePage` expose `wait_for_visible`, `wait_for_clickable`, etc. — `implicitly_wait(0)` forcé |
| Aucune donnée en dur dans les méthodes | Toutes les valeurs de test sont dans `data/test_data.py` |
| Happy Path + Negative Path | Chaque module de test couvre les deux scénarios |

---

## Installation de l'environnement virtuel

```bash
cd Dossier3

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Exécution des tests

### Tous les tests (navigateur visible)
```bash
pytest
```

### En mode headless
```bash
HEADLESS=1 pytest
```

### Un seul fichier de test
```bash
pytest tests/test_admin_login.py
```

### Générer le rapport HTML
Le rapport est automatiquement produit dans `reports/report.html`