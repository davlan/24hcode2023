
Le Mans School Of AI

Partie 1 : classez rapidement les photos

Le service communication des 24h reçoit une quantité très importante de photos en
provenance de sources multiples. Certaines sont professionnelles et d’autres non... Mais les
photos amateurs, les photos des spectateurs peuvent contenir des pépites donc on ne peut
pas les négliger !

Votre mission est donc d’entraîner un modèle de classification pour classer les photos
reçues en 3 catégories

● Les photos “parfaites” : la voiture est l'objet principal de la photo, pas trop de publicité
ou alors elle est floue, image nette au moins pour la voiture, pas de crash, etc.
(libellé : “ok”)

● Les photos “à retoucher” : présence de personnes identifiables ou de nombreuses
personnes, photos où la voiture est floue, présence de panneaux de signalisation ou
des poteaux verts, présence d'un panneau publicitaire très lisible (libellé :
“retoucher”)

● Les photos “inutiles” : les photos qui ne concernent pas la course, les photos des
concerts, des animations, des stands de restauration, ou les photos trop larges dans
lesquelles les voitures ne sont pas l'objet principal, photos de crash, etc. (libellé :
“exclure”)

Pour évaluer votre réussite nous passerons votre classificateur sur un jeu de données
d’évaluation auquel vous n’avez pas accès afin d’attribuer un taux de performance sur ce jeu
de données de référence.

Modalité d’évaluation :

● Vous devez prévoir le lancement de votre modèle de classification sur un dataset
d’évaluation : un répertoire contenant les 3 sous-répertoires “ok”, “retoucher” et
“exclure” qui contiendront des photos

● Votre code doit évaluer le classement de chaque photo et vérifier si son classement
est correct ou non vis-à-vis du label, ceci afin de donner en résultat un taux de
résultat conforme au classement attendu

● Les frameworks proposent des fonctions de ce type en standard (ex.
“model.evaluate” avec tensorflow/keras)
Remarque pour le projet final : maintenant que vous savez facilement classer des photos
vous êtes libres d’enrichir ce classificateur ou d’en proposer d’autre dans votre solution (cf.
partie 4)

Partie 2 : corrigez les photos

Parmi les photos reçues vous avez maintenant quelques photos très intéressantes mais qui
nécessitent d’être un peu améliorées. Mais vous n’avez plus de graphistes !

Heureusement un modèle d’IA révolutionnaire est capable d’appliquer une correction sur
une photo à partir d’une simple description. Il faut que vous mettiez cet outil à disposition de
votre équipe.

Avec un premier modèle d’IA, vous allez proposer à un utilisateur de décrire en texte ce qu’il
veut sélectionner dans une image et ainsi produire un masque en noir et blanc de la partie
de la photo à corriger (en blanc la partie à modifier, en noir la partie non concernée).
⇒ “the car” ⇒

Avec un second modèle d’IA, vous allez permettre à l’utilisateur de décrire la modification
qu’il veut réaliser sur la photo et en utilisant le masque précédent. Cela produira donc une
image corrigée.

+ “Mario kart, cartoon, Nintendo, videogame”
⇒
(regardez l’annexe “Conseils” avant de débuter)
Pour évaluer votre programme, nous vous demanderons de repartir de l’image
“porsche-911.jpg” qui est dans le dataset d’évaluation de la partie 1, dans la classification
“retoucher”. En effet une publicité est bien trop visible, vous devez la supprimer grâce à ce
nouvel outil et nous en faire la démonstration.

Partie 3 : stylisez vos photos

Le service de communication a pour objectif de produire un book qui raconte cette course.
Pour se distinguer, il est important de donner un style à ce support !

Là encore une IA peut vous aider, vous avez quartier libre pour trouver une solution et
l’implémenter dans votre application.

Exemple :
⇒
Pour évaluer votre programme, nous vous demanderons de repartir de l’image que vous
avez modifié dans la partie 2 et de la décliner selon 3 images de style que nous vous
fournirons au moment de l’évaluation.

Partie 4 : assemblez votre solution

Vous avez maintenant toutes les briques mais vos collègues de la communication ne sont
pas des informaticiens, proposez-leur une application intégrant ces différentes fonctions qui
soit utilisable facilement.

Pour évaluer votre programme, en utilisant le jeu de photos de la partie 1, montrez nous
l'enchaînement des fonctions :

- classement

- transformation

- application d’un style

Des fonctionnalités supplémentaires peuvent vous rapporter des points bonus !

Partie 5 : racontez-nous cette belle course

En utilisant ce nouvel outil à votre disposition, le jeu de photos que nous vous fournissons
pour cette 5ème partie et avec votre imagination produisez “votre book” de cette édition 100
ans des 24h.

Votre style est complètement libre : peinture, manga, BD, photo-réalisme, comique ou
dramatique, etc.

Etonnez-nous !

Attention : le service juridique est inquiet des problématiques posées par l’usage de ces
nouveaux outils. Conservez-bien, en parallèle de votre production finale, l’ensemble des
images sources ainsi que les étapes intermédiaires des transformations pour que nous
ayons la chaîne d’audit en cas de contrôle.

Conseils

Le sujet

Vous avez choisi notre sujet : Merci !

C’est notre premier sujet au 24h du code alors si 
vous rencontrez la moindre difficulté
n’hésitez pas à nous solliciter, l’équipe est située au rez de chaussé, sur la gauche face à
l’escalier principal.

Un serveur Discord vous est proposé pour échanger entre vous et avec nous, en parallèle
de l’événement

Le machine learning, l’intelligence artificielle sont en plein essor ces dernières années. En
24h il est impossible d’entraîner le prochain ChatGPT mais avec ce sujet vous allez :

● Créer un modèle de classification d’image à partir d’un modèle pré-entraîné

● Découvrir et intégrer dans votre application les modèles open source de
manipulation d’image les plus aboutis à ce jour
Le sujet est organisé en plusieurs parties qui se suivent mais vous pouvez (devriez ?)
paralléliser les travaux dans le groupe pour optimiser ces 24h.
CPU ? GPU ?

Les modèles d’IA requièrent de la puissance de calcul importante et s’appuient donc
généralement sur la carte graphique de l’ordinateur (le GPU).

Pour ce sujet, nous avons sélectionné des tâches qui ne nécessitent pas de GPU donc pas
d’inquiétude. Le support de votre GPU accélère les calculs donc il peut être utile mais ne
perdez pas de temps à le mettre en place si cela n’est pas natif.

Framework ?

Plusieurs framework existent pour développer et exécuter des modèles d’IA. Les deux plus
célèbres sont Pytorch et Tensorflow.

Pour ces 24h nous vous recommandons le framework Pytorch qui est généralement plus
accessible. Si vous préférez utiliser Tensorflow alors exploitez Keras qui est la sur-couche
intégrée qui simplifie grandement la construction et l’exécution d’un modèle.

Hugging Face ?

Dans le cadre de ces 24h vous utiliserez des modèles pré-entrainés et le site de référence
dans ce domaine est HuggingFace (https://huggingface.co/).

Nous vous fournirons les modèles pré-téléchargés car ils pèsent plusieurs Go mais la
création d’un compte peut vous être utile pour découvrir les modèles, la documentation, etc.

Où trouver les jeux de données du sujet ?

Deux solutions disponibles :

● Clef USB disponible auprès des porteurs du sujet

● Téléchargement sur un partage FTP sur le réseau local : demandez l’adresse IP et
les logins/mot de passe aux porteurs du sujet

Google Colab

Si vous rencontrez des difficultés à faire fonctionner des modèles d’IA en local sur votre
PC/Mac, vous pouvez utiliser le service Google Colab pour les parties 1 à 3 du sujet. Il
faudra certainement prévoir de revenir en local pour la partie 4 cependant...

Zoom sur la partie 1 du sujet

Le jeu de photos vous est fourni par nos soins. Pensez à constituer votre dataset pour votre
propre évaluation de votre modèle.
Juste deux mots clefs pour vous aider : labellisation, VGG16

Zoom sur la partie 2 du sujet
Pour cette partie vous devez obligatoirement utiliser les modèles suivants :

● “ClipSeg” : pour décrire textuellement ce que vous voulez sélectionner dans une
image et ainsi produire un masque de sélection
(https://huggingface.co/CIDAS/clipseg-rd64-refined)

● “Stable Diffusion InPainting” : pour modifier une photo à partir d’un masque et d’une
description textuelle de la modification à apporter
(https://huggingface.co/stabilityai/stable-diffusion-2-inpainting)
