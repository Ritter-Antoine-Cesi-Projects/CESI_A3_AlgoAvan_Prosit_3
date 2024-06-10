# Prendre connaissance de la situation et la clarifier

## Contexte

Suite à la preuve de la complexité de notre problème, nous devons chercher à produire un algorithme pour une solution à grande échelle.

## Mots Clefs

- Recherche opérationnelle
- Méta-heuristique
- Simplexe
- Systèmes d'équations/inéquations
- Programmation dynamique
- Programmation linéaire
- Approche adaptative
- Ensemble de sous-problèmes
- Planification
- Modélisation
- Résolution générique

# **Analyse du Besoin**

## **Problème(s)**

- Quel type de méthode de programmation utiliser pour résoudre notre problème d’optimisation ?
- Quelle méthode de planification utiliser ?

## **Contraintes**

- Complexité de l’algorithme
- Nombre de villes
- Algorithme facile à implémenter

## **Livrables**

- Implémentation de l’algorithme

# **Généralisation du problème**

- Problème de planification
- Méthode de programmation

# Pistes de solutions

- Nous allons peut-être devoir faire une planification ? (Léo R)
- La planification permet de délimiter le problème ? (Antonin)
- Peut-être que le simplexe est une solution globale que l’on peut appliquer à notre problème (Julien)
- Les méta-heuristiques sont des méthodes que l’on conçoit pour s’adapter à un problème (Gabriel)
- On ne peut pas être sûr que la méthode choisie est la plus optimale (Lukas)
- La programmation dynamique permet de mieux modéliser notre situation que le simplexe (Matthis)
- Les méta-heuristiques permettent d’avoir la solution la plus optimale (Antonin)
- La programmation dynamique s’adapte à notre problème alors que la programmation linéaire est générique (Julien)
- La méta-heuristique n’est pas de la programmation (code) (Antonin)

# **Plan d’action**

1. Se renseigner sur la programmation linéaire et dynamique
2. Se renseigner sur les différentes méthodes de modélisation
3. Se renseigner sur la différence entre programmation et planification
4. Se renseigner sur l’implémentation des méta-heuristiques
5. Se renseigner sur le Simplexe
6. Choisir un modèle adapté à notre algorithme
7. Tester avec la programmation linéaire avant d’essayer d’autres méthodes
8. Trouver le meilleur compromis entre complexité de conception, temps d’exécution et qualité de résultats
9. Réaliser les livrables

# **Notion de cours**

## Mots Clefs

- **Recherche opérationnelle** : Discipline qui utilise des méthodes analytiques avancées pour aider à prendre des décisions. Elle applique des techniques mathématiques et informatiques pour optimiser les processus et systèmes complexes dans divers domaines comme la logistique, la production, les finances et les services.
- **Méta-heuristique** : Algorithmes généraux conçus pour trouver des solutions approximatives à des problèmes d'optimisation complexes. Contrairement aux heuristiques spécifiques à un problème particulier, les méta-heuristiques sont plus flexibles et peuvent être adaptées à divers types de problèmes. Exemples courants : algorithmes génétiques, recuit simulé, et colonies de fourmis.
- **Simplexe** : Algorithme de résolution de problèmes de programmation linéaire. Développé par George Dantzig, il permet de trouver la solution optimale en parcourant les sommets d'un polytope dans un espace de dimension n, en passant d'une solution de base à une autre, jusqu'à atteindre la solution optimale.
- **Systèmes d'équations/inéquations** : Ensemble de plusieurs équations ou inéquations (relations d'inégalité) impliquant les mêmes variables. La résolution de ces systèmes consiste à trouver les valeurs des variables qui satisfont toutes les équations ou inéquations simultanément.
- **Programmation dynamique** : Méthode de résolution de problèmes complexes en les décomposant en sous-problèmes plus simples. Elle est particulièrement utile pour les problèmes d'optimisation où les sous-problèmes se chevauchent. La technique consiste à mémoriser les solutions des sous-problèmes pour éviter de les recalculer.
- **Programmation linéaire** : Technique d'optimisation mathématique où l'objectif est de maximiser ou minimiser une fonction linéaire, sous des contraintes linéaires. Elle est utilisée dans divers domaines pour la planification, l'allocation de ressources et la gestion de la production.
- **Approche adaptative** : Méthodologie qui ajuste dynamiquement les stratégies ou les paramètres en fonction des changements dans l'environnement ou des résultats intermédiaires obtenus. Cette approche est couramment utilisée dans les algorithmes d'optimisation et d'apprentissage automatique pour améliorer la performance et la robustesse.
- **Ensemble de sous-problèmes** : Dans la résolution de problèmes complexes, un problème peut être divisé en plusieurs sous-problèmes plus petits et plus gérables. Ces sous-problèmes peuvent être résolus individuellement et leurs solutions combinées pour résoudre le problème initial.
- **Planification** : Processus de création de plans détaillés pour atteindre un ou plusieurs objectifs spécifiques. Cela peut inclure la gestion des ressources, la définition des étapes nécessaires, et la mise en place de stratégies pour surmonter les obstacles potentiels.
- **Modélisation** : Processus de création d'un modèle abstrait qui représente un système réel ou hypothétique. En recherche opérationnelle, la modélisation consiste à traduire un problème pratique en termes mathématiques afin de pouvoir le résoudre analytiquement ou à l'aide d'algorithmes.
- **Résolution générique** : Méthode ou algorithme qui peut être appliqué à une large variété de problèmes sans être spécifiquement conçu pour un seul type de problème. Les techniques génériques sont souvent flexibles et robustes, capables de s'adapter à différents types de données et de structures problématiques.

## Recherche opérationelle

### Les origines de la recherche opérationnelle

Si la recherche opérationnelle, en abrégé RO, est aujourd’hui présente dans la plupart des domaines civils, ses racines sont habituellement attribués aux services militaires. La seconde guerre mondiale, de part son envergure, créa une besoin urgent d’allouer de manière efficace des ressources limitées aux différentes opérations militaires et aux activités au sein de chaque opération. En particulier, l’organisation militaire britannique, puis américaine, mis à contribution un grand nombre de scientifiques pour gérer ces allocations, et s’occuper d’autres problèmes stratégiques et tactiques. Ce faisant, ils furent appelés à poursuivre des recherches sur des opérations (militaires), et constituèrent les premières équipes de RO. Leurs efforts furent signifactifs dans la marche vers la victoire, par exemple en ce qui touche l’utilisation du radar, nouvellement développé. Ces succès encouragèrent la poursuite de l’utilisation de la RO dans d’autres domaines. La croissance importante de l’industrie d’après-guerre entraîna des problèmes, causés par la complexité croissante et la spécialisation dans les organisations, problèmes en fait proches de ceux présent lors du conflit. Au début des années 1950’s, la RO avait pénétré une multitude d’organisations commerciales, industrielles, et gouvernementales. Et ce n’était que le début.

Au moins deux autres facteurs ont joué un rôle clé dans la croissance rapide de la RO. Tout d’abord, des progrès substantiels ont été obtenus très tôt afin d’améliorer les techniques de RO. Ces techniques, dans leur mise en pratique, furent soutenues par l’essor des outils informatiques.

### La nature de la recherche opérationnelle

“Rechercher sur des opérations” touche tous les problèmes reliés à la conduite et à la coordination des opérations (activítés) au sein d’une organisation. Cette organisation peut représenter des domaines très divers: l’industrie manufacturière, le transport, la construction, les télécommuncations, la finance, les soins de santé,. . . . La RO, associée à la révolution informatique, pénètre pratiquement tous les secteurs d’activités de la vie courante, même si sa présence est souvent invisible.

La première étape de la “recherche” est l’observation attentive du problème et sa formulation, ainsi que la collecte de données associées. Il convient par la suite de construire un modéle scientifique qui tente l’abstraire l’essence du problème réel. Tout modèle est une simplification de la réalité, mais cette représentation doit être sudffisamment précise pour capturer les caractéristiques essentielles de la situation, et de pouvoir tirer des conclusions valides pour le problème réelle. Il conviendra dès lors de tester ce modèle, et de le modifier au besoin.

Une caractéristique additionnelle est que la RO essaye souvent de trouver une meilleure solution (dite solution optimale) pour le problème examiné. Cette solution peut ne pas être unique. Cette recherche d’optimalité est un thème important en RO, mais si son interprétation en terme managériels peut être délicate.

Il est difficile pour un individu de pouvoir maîtrise tous les aspects du problèmes à l’étude, de sorte que la RO est généralement plus un travail d’équipe, avec des experts en mathématiques, statistiques et probabilités, ingénierie, économie, administration, informatique, physiques, sciences comportementales, et les techniques spécifiques de la RO.

### Modélisation

Un modèle, telle que considéré dans ce cours, est une construction mathématique utilisée pour représenter certains aspects significatifs de problèmes du monde réel. Il y a beaucoup de types différents de modèles mathématiques, mais nous nous focaliserons dans un premier temps sur les modèles d’optimisation. Il y a trois composantes principales dans un modèle d’optimisation:

**Variables:** elles représentent les composantes du modèle qui peuvent être modifiées pour créer des configurations différentes.

**Contraintes:** elles représentent les limitations sur les variables.

**Fonction objection:** cette fonction assigne une valeur à chaque configuration différente. Le terme “objectif” vient du fait que l’objectif est d’optimiser cette fonction.

**Exemple 1** (Un exemples de décisions binaires (oui/non)). Un étudiant en quête d’une université projette de visiter les campus de trois universités du Maine au cours d’un voyage unique, débutant et finissant à l’aéroport de Portland. Les trois établissements sont dans les villes de Brunswick, Lewiston, et Waterville, et l’étudiant ne veut visiter chaque ville qu’une seule fois, tout en maintenant le trajet total le plus court possible. Les distances entre ces villes sont données dans la Table 1.1.

| Ville | Portland | Brunswick | Lewiston | Waterville |
| --- | --- | --- | --- | --- |
| Portland | 0 | 26 | 34 | 78 |
| Brunswick | 26 | 0 | 18 | 52 |
| Lewiston | 34 | 18 | 0 | 51 |
| Waterville | 78 | 52 | 51 | 0 |

Table 1.1 – Distances entre les villes (miles)

## Programmation linéaire

### Introduction

La programmation mathématique recouvre un ensemble de techniques d’optimisation sous contraintes qui permettent de d´eterminer dans quelles conditions on peut rendre maximum ou minimum une fonction objectif $Z(X_j)$ de $n$ variables $X_j$ **liées par $m$ relations ou contraintes $H_i(X_j) ≤ 0$.

De nombreux problèmes de l’entreprise peuvent s’exprimer en termes d’optimisation contrainte, aussi rencontre t-on de multiples applications de la programmation mathématique et ceci dans pratiquement tous les domaines de la gestion.

La gestion de production est le domaine ou` ces applications sont les plus nombreuses. On citera entre-autres :

- l’élaboration de plans de production et de stockage,
- le choix de techniques de production,
- l’affectation de moyens de production,
- la détermination de la composition de produits.

Les applications sont également nombreuses dans le domaine du marketing avec, en particulier :

- le choix de plans-média,
- la détermination de politiques de prix,
- la répartition des efforts de la force de vente,
- la sélection des caractéristiques du produit.

On citera encore des applications en matière financière (choix de programmes d’investissements), en matière logistique (gestion des transports) et en matière de gestion des ressources humaines (affectation de personnel).

Si les applications de la programmation mathématique sont aussi nombreuses, on doit l’attribuer en grande partie à la souplesse de ses techniques en ce qui concerne leur formulation mais aussi à la relative simplicité des méthodes de résolution utilisables dans les cas les plus courants et pour lesquelles existent des programmes informatiques largement répandus.

Parmi les techniques de programmation mathématique la programmation linéaire est la plus classique.

### Modélisation d’un programme linéaire

La formalisation d’un programme est une tâche délicate mais essentielle car elle conditionne la découverte ultérieure de la bonne solution. Elle comporte les mêmes phases quelles que soient les techniques requises ultérieurement pour le traitement (programmation linéaire ou programmation non linéaire) :

1. La détection du problème et l’identification des variables. Ces variables doivent correspondre exactement aux préoccupations du responsable de la décision. En programmation mathématique, les variables sont des variables décisionnelles.
2. La formulation de la fonction économique (ou fonction objectif) traduisant les préférences du décideur exprimées sous la forme d’une fonction des variables identifiées.
3. La formulation des contraintes. Il est bien rare qu’un responsable dispose de toute liberté d’action. Le plus souvent il existe des limites à ne pas dépasser qui revêtent la forme d’équations ou d’inéquations mathématiques.

Le responsable d’une décision ne dispose que de sa compétence pour réaliser une formalisation correcte du problème posé car il n’existe pas de méthode en la matière.

# Solutions

# Ressources

[www.iro.umontreal.ca](https://www.iro.umontreal.ca/~bastin/Cours/IFT1575/IFT1575.pdf)

[1. La Modélisation - Recherche Operationnelle](https://www.youtube.com/watch?v=Zy-iTwA9tfU)

[Programmation linéaire avec Excel - ScholarVox Université](https://univ.scholarvox.com/reader/docid/88802765/page/1)

[educnet.enpc.fr](https://educnet.enpc.fr/file.php/297/CoursROPonts.pdf)

[abenkhalifa.wordpress.com](https://abenkhalifa.wordpress.com/wp-content/uploads/2015/02/cours-ro-final333.pdf)

[www-lmpa.univ-littoral.fr](https://www-lmpa.univ-littoral.fr/~smoch/documents/M2-RO/recherche-operationnelle-chap2.pdf)