# M-KIS Web Page Summarizer

M-KIS Web Page Summarizer est une application web qui utilise l'IA d'OpenAI pour résumer le contenu des pages web et en extraire les idées principales.

## Fonctionnalités

- Résumé automatique du contenu des pages web.
- Extraction des idées principales.
- Affichage des images de la page web résumée.

## Prérequis

- Python 3
- Un compte OpenAI avec une clé API

## Installation

1. Clonez ce dépôt ou téléchargez-le sur votre machine locale.

2. Naviguez vers le répertoire du projet et créez un environnement virtuel Python:

    ```
    python -m venv mkisenv
    ```

3. Activez l'environnement virtuel:

    - Sur Windows:
        ```
        .\mkisenv\Scripts\activate
        ```
    - Sur macOS et Linux:
        ```
        source mkisenv/bin/activate
        ```

4. Installez les dépendances nécessaires en utilisant le fichier `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

5. Créez un fichier `.env` dans le répertoire du projet et ajoutez votre clé API OpenAI:

    ```
    OPENAI_API_KEY=votre_clé_api
    ```

6. Exécutez l'application:

    ```
    python app.py
    ```

7. Ouvrez votre navigateur web et accédez à `http://127.0.0.1:5000/` pour utiliser l'application.

## Utilisation

1. Entrez l'URL de la page web que vous souhaitez résumer dans le champ de texte.

2. Cliquez sur le bouton "Summarize" pour obtenir un résumé de la page web.

3. Les résultats, y compris le résumé et les images de la page, seront affichés sur la page.

## Licence

Ce projet est sous licence [insérer le type de licence ici, si applicable].

## Auteur

M-KIS Athena

## Remerciements
Merci à OpenAI pour la mise à disposition de l'API GPT.
