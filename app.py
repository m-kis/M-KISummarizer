from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement du fichier .env
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    response = requests.get(url, verify=False)
    
    # Extraire et nettoyer le contenu de la page web
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join(p.get_text() for p in paragraphs)
    # Extraire les URL des images
    images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]

    # Utiliser un prompt spécifique
    prompt = f"Veuillez fournir un résumé concis en énumérant les points clés et les idées principales du texte suivant: {text}"
    
   # Utiliser l'API d'OpenAI pour résumer le texte
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    
    # Formater le résumé
    summary = response.choices[0].text.strip()

    # Renvoyer les résultats et les URL des images à la page
    return render_template('index.html', summary=summary, images=images)

if __name__ == '__main__':
    app.run(debug=True)