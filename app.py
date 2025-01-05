# app.py : Script Streamlit pour la détection du type de cheveux

# Importation des bibliothèques nécessaires
import streamlit as st  # Bibliothèque pour créer l'interface web
from tensorflow.keras.models import load_model  # Charger le modèle de deep learning
from PIL import Image  # Pour ouvrir et traiter des images
import numpy as np  # Bibliothèque pour manipuler des tableaux de données

# Charger le modèle pré-entraîné
model_path = "/content/drive/MyDrive/model_mobilenet.h5"  # Chemin vers le fichier du modèle
model = load_model(model_path)  # Charger le modèle depuis le fichier
class_names = ['Straight', 'Wavy', 'Curly', 'Dreadlocks', 'Kinky']  # Noms des classes de prédiction

# Interface utilisateur Streamlit
st.title("Application de Détection du Type de Cheveux")  # Titre de la page web
st.write("Importez une image pour connaître le type de cheveux.")  # Texte descriptif

# Zone pour uploader une image
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])

# Fonction pour prétraiter l'image et faire la prédiction
def preprocess_and_predict(image_file, model):
    # Charger et transformer l'image
    img = Image.open(image_file).convert("RGB")  # Ouvrir l'image en mode RGB
    img = img.resize((224, 224))  # Redimensionner à la taille compatible avec le modèle
    img_array = np.array(img) / 255.0  # Normalisation des pixels entre 0 et 1
    img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension batch

    # Faire la prédiction
    prediction = model.predict(img_array)  # Prédire la classe de l'image
    class_index = np.argmax(prediction)  # Trouver l'indice de la classe avec la plus haute probabilité
    confidence = np.max(prediction)  # Extraire la confiance associée à la classe prédite
    class_name = class_names[class_index]  # Trouver le nom de la classe prédite

    return class_name, confidence  # Retourner le nom de la classe et la confiance

# Affichage du résultat si une image a été uploadée
if uploaded_file is not None:
    class_name, confidence = preprocess_and_predict(uploaded_file, model)  # Faire la prédiction
    st.image(uploaded_file, caption=f"Type de cheveux : {class_name}\nConfiance : {confidence:.2f}")  # Afficher l'image avec la prédiction
    st.write(f"**Type de cheveux détecté : {class_name}**")  # Afficher le résultat
    st.write(f"**Confiance du modèle : {confidence:.2f}**")  # Afficher la confiance du modèle
