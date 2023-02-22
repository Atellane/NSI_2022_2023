import requests
import os

# URL de la source d'images gratuites
url = 'https://picsum.photos'

# Nombre d'images à télécharger
num_images = 20

# Créer le dossier pour enregistrer les images
if not os.path.exists('images'):
    os.makedirs('images')

# Télécharger les images
for i in range(num_images):
    # Générer une URL aléatoire pour une image de taille 500x500 pixels
    image_url = f'{url}/500/500/?random'
    # Envoyer une requête pour télécharger l'image
    response = requests.get(image_url)
    # Enregistrer l'image dans le dossier 'images'
    with open(f'images/image_{i+1}.jpg', 'wb') as f:
        f.write(response.content)

print('Téléchargement terminé.')