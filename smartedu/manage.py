#!/usr/bin/env python
import os
import sys

def main():
    """Point d'entrée principal pour les commandes de gestion Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartedu.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Assurez-vous qu'il est installé et "
            "accessible dans votre environnement."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
