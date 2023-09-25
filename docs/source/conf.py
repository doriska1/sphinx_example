# docs/source/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('../../app'))  # Dodaj katalog app do sys.path

# Ustaw nazwę projektu i autora
project = 'Moja Dokumentacja Sphinx'
author = 'Twoje Imię i Nazwisko'

# Ustaw ścieżki do źródeł
source_suffix = '.rst'
master_doc = 'index'

# Ustaw moduły Pythona, które mają być uwzględnione w dokumentacji
extensions = [
    'sphinx.ext.autodoc',
]

# Ustaw automatyczne generowanie dokumentacji z docstringów
autodoc_mock_imports = []  # Usuń wszelkie wcześniejsze wpisy, jeśli były

# Ustaw wyjściowy format dokumentacji
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'MojaDokumentacjaSphinx'

# Dodaj rozszerzenia lub konfiguracje własne tutaj
