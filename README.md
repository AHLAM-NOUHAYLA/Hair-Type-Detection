# Hair-Type-Detection

Créé par Ahlam EL ASRI et Nouhayla EL-BIYAALI - Université Paris-Est Créteil (UPEC)


## Description du Projet

Ce projet propose une application web interactive pour la *détection du type de cheveux* à partir d'images en utilisant un modèle de deep learning pré-entraîné avec *MobileNetV2*. Grâce à l'utilisation de *Streamlit*, l'application offre une interface simple et intuitive permettant aux utilisateurs de soumettre une image et d'obtenir des prédictions précises parmi plusieurs classes (Straight, Wavy, Curly, Dreadlocks, Kinky). Le projet met en avant l'importance de l'intelligence artificielle dans des domaines pratiques comme la beauté et la mode, tout en illustrant la puissance des réseaux de neurones convolutifs pour la reconnaissance d'images.

## Table des matières

1. [Description du Projet](#description-du-projet)
2. [Prérequis](#prérequis)
3. [Jeux de données](#jeux-de-données)
4. [Structure du Projet](#structure-du-projet)
5. [Déploiement](#déploiement)
6. [Améliorations possibles](#améliorations-possibles)

## Prérequis

Pour exécuter ce projet, assurez-vous d'avoir :

- Python 3.x : Langage de programmation utilisé pour le projet.
- Streamlit : Framework pour créer une interface utilisateur web interactive.
- TensorFlow & Keras : Bibliothèques pour charger le modèle de deep learning MobileNetV2 et effectuer des prédictions.
- MobileNetV2 pré-entraîné : Modèle de classification des images utilisé pour détecter le type de cheveux.
- Jeu de données classifié : Ensemble d'images annotées avec les classes Straight, Wavy, Curly, Dreadlocks, Kinky.
- Ngrok ou Localtunnel (optionnel) : Outils pour exposer l'application localement et obtenir une URL publique.
- Google Drive (optionnel) : Si vous utilisez Google Colab, montez votre Drive pour charger le modèle pré-enregistré.
  
Ces outils assurent un environnement complet pour exécuter l'application en local ou via Google Colab.

## Jeux de données

Les données utilisées pour ce projet proviennent du dataset public disponible sur Kaggle : Hair Type Dataset (https://www.kaggle.com/datasets/kavyasreeb/hair-type-dataset).

Ce jeu de données contient des images annotées selon cinq types de cheveux différents :

- Straight
- Wavy
- Curly
- Dreadlocks
- Kinky
  
Les données ont été téléchargées depuis Kaggle et pré-traitées pour être utilisées dans le modèle MobileNetV2.

Cette partie est un élément clé du projet pour entraîner et tester les performances du modèle sur des classes bien définies.

##  Structure du Projet

Le projet est organisé selon la structure suivante :

- Hair_Type_Detection.ipynb : Notebook pour traitement des données,entraînement du modèle et l'analyse des résultats.
- App_execution_streamlit.ipynb : Contient le notebook permettant d'exécuter et de tester l'application web Streamlit.
- README.md : Document de présentation du projet avec les instructions d'utilisation.
- app.py : Script contenant le code de l'application Streamlit pour la classification des types de cheveux.
- model_mobilenet.h5 : Fichier contenant le modèle MobileNetV2 sauvegardé après l'entraînement.
- test projet : Une base de données contenant des nouvelles images non vues auparavant .

##  Déploiement

Le déploiement de l'application Streamlit se fait via Google Colab en utilisant les étapes suivantes :

1. Lancer le notebook d'exécution :
     a. ouvrir le fichier App_execution_streamlit.ipynb dans Google Colab.
     b. S'assurer que les bibliothèques nécessaires sont installées (streamlit, pyngrok, localtunnel, tensorflow, etc.).

2. Montage du modèle pré-entraîné :
   
Le modèle model_mobilenet.h5 doit être importé depuis Google Drive ou directement dans l'environnement d'exécution.

3. Exécution de l'application :

     a. Lancer la commande suivante dans une cellule Colab pour démarrer l'application Streamlit : !streamlit run app.py & npx localtunnel --port 8501
     b. Cela génère une URL qui permet d’accéder à l'application depuis le web.
     c. Accéder à l'interface utilisateur :
     d. Une fois l'URL générée, cliquer sur le lien pour accéder à l'application de détection du type de cheveux.

## 4. Modèlisation

## 5. Entraînement du modèle

## 6. Evaluation

## 7. Test sur de nouvelles images

## 8. Déploiement

## 9. Conclusion


