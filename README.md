Bienvenue au tutoriel du fonctionnement de la râpe IA Markov 2000 !  

Pour commencer, nous allons parler de la fabrication de la râpe. Ensuite, nous verrons comment préparer et contrôler l'ordinateur et, pour finir, je vous montrerai comment la faire fonctionner.  

Matériel nécessaire  

Avant de commencer, voici la liste du matériel dont vous aurez besoin pour créer une râpe Markov 2000 fonctionnelle :  

- 1 fer à souder à l’étain pour les brasures  
- 1 bobine d’étain  
- 1 kit de jumpers Arduino (mâle-femelle et mâle-mâle)  
- 1 bouton de borne d’arcade  
- 2 potentiomètres compatibles Arduino  
- 1 écran bleu à cristaux liquides sans I2C  
- 1 râpe à fromage  
- 1 imprimante 3D  
- 1 découpeuse laser  
- 12 boulons et écrous M3x30  
- 1 plaque de plexiglas blanc de 4 mm (50x80 cm)  
- 1 bombe de peinture acrylique mate noire  
- 1 tube en acier de 5 mm de diamètre intérieur  

---

ÉTAPE 1 : Préparer et souder tous les éléments  

![IA QUOI LA DEDANS _ (1)](https://github.com/user-attachments/assets/7b4edf87-f9f3-4400-bebb-7ace0b77505d)

⚠ ATTENTION ! Ne soudez pas encore le bouton et les potentiomètres, car les câbles doivent d'abord passer dans les trous de la râpe.  

---

ÉTAPE 2 : Découpe laser du carénage  

Pour cette étape, nous allons utiliser une découpeuse laser. Prenez votre plaque de PMMA de 4 mm (ou trolase noir/blanc) et lancez la découpe du fichier "Plaque de trolase habillage rape v3.SVG".  

---

ÉTAPE 3 : Assemblage

1. Découpez votre tube en acier de 5 mm en tronçons de 20 mm.  
2. Fixez les plaques sur la râpe (pensez à percer tous les trous nécessaires au préalable).  
3. Utilisez les boulons et écrous M3x30 pour fixer le carénage.  

---
------------  ETAPE A CORRIGER -----------------
Ensuite, nous allons voir comment configurer l'ordinateur.  

Logiciels requis  

Pour commencer, vous devez installer trois logiciels sur votre ordinateur :  

- **Arduino IDE**  
- **VS Code** de Microsoft  
- **Python 3** (version minimale requise) – Téléchargeable sur : [https://www.python.org/](https://www.python.org)  

⚠ **ATTENTION !** Lors de l’installation de Python, assurez vous de bien l’ajouter au **PATH**.

---

Après cela, ajoutez le dossier **TM-SCREEN** sur le bureau de votre ordinateur.  

### **Ouverture du projet dans VS Code**  

1. Ouvrez **VS Code**.  
2. Cliquez sur **Fichier > Ouvrir un dossier** (**File > Open Folder**).  
3. Sélectionnez le dossier **TM-SCREEN**.  

Cela chargera l’ensemble du dossier dans l’onglet de gauche.  

4. Ouvrez le fichier **Python** contenu dans le dossier.  
5. VS Code devrait normalement vous demander d’installer l’extension **Python** sur votre ordinateur. Installez-la si ce n’est pas déjà fait.  

![302d3364e0134f43e909c34b77ef948b](https://github.com/user-attachments/assets/9e61ce41-9673-4819-84cf-5b299cdddb17)

---

## **ÉTAPE 4 : Création de la variable d'environnement Python**  

Ensuite, vous devez associer la variable d’environnement disponible dans le fichier **.env** avec le fichier **requirements.txt**.  

---

## **ÉTAPE 5 : Vous pouvez râper des mots** 🧀💻 



