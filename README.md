# Hair-Type-Detection

Le Deep Learning a transformé notre approche des problèmes complexes en permettant aux machines d'apprendre à partir des données. Ce projet Hair Type Detection exploite la puissance des réseaux de neurones convolutifs pour identifier automatiquement le type de cheveux à partir d'une image, parmi des catégories telles que Straight, Wavy, Curly, Dreadlocks et Kinky. Cette technologie trouve des applications dans les recommandations de soins capillaires personnalisés et les expériences interactives en beauté et mode.

## Table des matières

1. [Importation des bibliothèques](#importation-des-bibliothèques)
2. [Montage du drive et chargement des données](#montage-du-drive-et-chargement-des-données)
3. [Préparation des données](#préparation-des-données)
4. [Modèlisation](#modèlisation)
5. [Entraînement du modèle](#entraînement-du-modèle)
6. [Evaluation](#evaluation)
7. [Test sur de nouvelles images](#test-sur-de-nouvelles-images)
8. [Déploiement](#déploiement)
9. [Conclusion](#conclusion)

## Importation des bibliothèques

L'importation des bibliothèques nécessaires est une étape cruciale pour mettre en place un environnement complet de Deep Learning. Dans ce projet, plusieurs bibliothèques ont été utilisées pour accomplir différentes tâches :

- Matplotlib et Seaborn sont utilisées pour visualiser les résultats, notamment les courbes de performance et les matrices de confusion.
- PIL et shutil permettent de gérer et manipuler les images.
- TensorFlow/Keras fournit l'architecture principale pour la création, l'entraînement et le déploiement du modèle avec des modules comme MobileNetV2, Dense, et Dropout.
- Scikit-learn offre des fonctions pour la division des données (train_test_split) et l'évaluation des métriques comme la matrice de confusion, le F1-score et le ROC-AUC.
- Google Colab permet de monter le Google Drive et de charger des fichiers directement à partir du stockage en ligne, facilitant ainsi le travail collaboratif.
- Des callbacks comme EarlyStopping et ReduceLROnPlateau sont intégrés pour optimiser l’entraînement et éviter le sur-apprentissage.


## Montage du drive et chargement des données

Dans ce projet, l'environnement de travail est Google Colab, une plateforme qui offre des ressources GPU/TPU pour l'exécution rapide de modèles d'apprentissage profond. Les données utilisées pour entraîner le modèle sont stockées sur Google Drive.

L'étape de montage du Drive est indispensable pour accéder aux fichiers directement à partir de l'espace de stockage personnel. Cette opération se fait via la commande drive.mount(), qui permet de connecter le Drive à l'environnement Colab.

Après le montage, le dossier contenant les données d'images est spécifié par le chemin data_dir, et les classes de données (par exemple, 'Wavy', 'Curly', 'Dreadlocks', 'Straight', 'Kinky') sont automatiquement listées en utilisant os.listdir(). Une fonction visualize_images est également mise en place pour afficher quelques images représentatives de chaque classe afin de vérifier l’intégrité des données et mieux visualiser la distribution des images.

Cette étape garantit que les données sont correctement chargées et prêtes pour la phase de préparation et d'entraînement du modèle.

## Préparation des données

## Modèlisation

## Entraînement du modèle

## Evaluation

## Test sur de nouvelles images

## Déploiement

## Conclusion


