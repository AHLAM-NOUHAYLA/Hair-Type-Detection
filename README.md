# Hair-Type-Detection

Créé par Ahlam EL ASRI et Nouhayla EL-BIYAALI - Université Paris-Est Créteil (UPEC)


Le Deep Learning a transformé notre approche des problèmes complexes en permettant aux machines d'apprendre à partir des données. Ce projet Hair Type Detection exploite la puissance des réseaux de neurones convolutifs pour identifier automatiquement le type de cheveux à partir d'une image, parmi des catégories telles que Straight, Wavy, Curly, Dreadlocks et Kinky. Cette technologie trouve des applications dans les recommandations de soins capillaires personnalisés et les expériences interactives en beauté et mode.

## Table des matières

1. [Importation des bibliothèques](#importation-des-bibliothèques)
2. [Montage du drive et chargement des données](#montage-du-drive-et-chargement-des-données)
3. [Préparation des données](#préparation-des-données)

   a. [Prétraitement des images](#prétraitement-des-images)
   b. [Data augmentation](#data-augmentation)
   c. [Conversion des images en format JPG](#conversion-des-images-en-format-JPG)
   b. [Division des données](#division-des-données) 
   
5. [Modèlisation](#modèlisation)
6. [Entraînement du modèle](#entraînement-du-modèle)
7. [Evaluation](#evaluation)
8. [Test sur de nouvelles images](#test-sur-de-nouvelles-images)
9. [Déploiement](#déploiement)
10. [Conclusion](#conclusion)

## 1. Importation des bibliothèques

L'importation des bibliothèques nécessaires est une étape cruciale pour mettre en place un environnement complet de Deep Learning. Dans ce projet, plusieurs bibliothèques ont été utilisées pour accomplir différentes tâches :

- Matplotlib et Seaborn sont utilisées pour visualiser les résultats, notamment les courbes de performance et les matrices de confusion.
- PIL et shutil permettent de gérer et manipuler les images.
- TensorFlow/Keras fournit l'architecture principale pour la création, l'entraînement et le déploiement du modèle avec des modules comme MobileNetV2, Dense, et Dropout.
- Scikit-learn offre des fonctions pour la division des données (train_test_split) et l'évaluation des métriques comme la matrice de confusion, le F1-score et le ROC-AUC.
- Google Colab permet de monter le Google Drive et de charger des fichiers directement à partir du stockage en ligne, facilitant ainsi le travail collaboratif.
- Des callbacks comme EarlyStopping et ReduceLROnPlateau sont intégrés pour optimiser l’entraînement et éviter le sur-apprentissage.


## 2. Montage du drive et chargement des données

Dans ce projet, l'environnement de travail est Google Colab, une plateforme qui offre des ressources GPU/TPU pour l'exécution rapide de modèles d'apprentissage profond. Les données utilisées pour entraîner le modèle sont stockées sur Google Drive.

L'étape de montage du Drive est indispensable pour accéder aux fichiers directement à partir de l'espace de stockage personnel. Cette opération se fait via la commande drive.mount(), qui permet de connecter le Drive à l'environnement Colab.

Après le montage, le dossier contenant les données d'images est spécifié par le chemin data_dir, et les classes de données (par exemple, 'Wavy', 'Curly', 'Dreadlocks', 'Straight', 'Kinky') sont automatiquement listées en utilisant os.listdir(). Une fonction visualize_images est également mise en place pour afficher quelques images représentatives de chaque classe afin de vérifier l’intégrité des données et mieux visualiser la distribution des images.

Cette étape garantit que les données sont correctement chargées et prêtes pour la phase de préparation et d'entraînement du modèle.

## 3. Préparation des données

###   a. Prétraitement des images
La préparation des données est une étape clé dans tout projet de Deep Learning, car la qualité des données a un impact direct sur les performances du modèle. Dans ce projet, les images sont tout d’abord redimensionnées à une taille standard pour assurer une cohérence entre les entrées du réseau de neurones. Ensuite, les images sont normalisées, c'est-à-dire que les valeurs des pixels sont mises à l’échelle entre 0 et 1, ce qui facilite l’optimisation du modèle en réduisant l’effet des grandes variations d’intensité.

###   b. Data augmentation
Dans le but d’équilibrer les classes et d’améliorer la robustesse du modèle, une augmentation des données a été appliquée. Les images disponibles ne présentaient pas une distribution uniforme entre les différentes catégories de cheveux, ce qui aurait pu biaiser les prédictions du modèle. Pour remédier à cela, plusieurs techniques d’augmentation ont été utilisées, notamment :

- Rotation aléatoire pour introduire des variations d'angle.
- Zoom aléatoire afin de simuler différentes perspectives.
- Renversement horizontal pour augmenter la diversité des échantillons.
- Modification de la luminosité et du contraste afin d'adapter le modèle à différentes conditions d'éclairage.
- Décalage des couleurs pour rendre le modèle plus robuste aux variations de teinte.
  
Ces transformations ont été appliquées de manière aléatoire aux images afin d'améliorer la capacité du modèle à généraliser sur des données inconnues.

###   c. Conversion des images en format JPG
Enfin, une conversion des images a été effectuée pour assurer l'uniformité du format des fichiers. Toutes les images ont été converties en format JPG, garantissant ainsi une compatibilité optimale avec les outils de traitement et évitant tout problème lors du chargement des données.

###   d. Division des donnée
Pour s’assurer d’un bon entraînement et d’une évaluation fiable, les données ont ensuite été divisées en trois ensembles :

- Ensemble d'entraînement, utilisé pour apprendre les caractéristiques des images. (80%)
- Ensemble de validation, utilisé pour ajuster les hyperparamètres du modèle.(10%)
- Ensemble de test, utilisé pour évaluer la performance finale du modèle sur des données inédites.(10%)

## 4. Modèlisation

## 5. Entraînement du modèle

## 6. Evaluation

## 7. Test sur de nouvelles images

## 8. Déploiement

## 9. Conclusion


