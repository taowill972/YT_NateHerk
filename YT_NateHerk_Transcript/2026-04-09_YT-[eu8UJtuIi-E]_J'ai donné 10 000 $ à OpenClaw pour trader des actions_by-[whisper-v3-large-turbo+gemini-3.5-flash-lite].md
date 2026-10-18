# 🎬 I Gave OpenClaw $10,000 to Trade Stocks

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=eu8UJtuIi-E](https://www.youtube.com/watch?v=eu8UJtuIi-E)  
> **Date de publication** : 20260409  
> **Durée** : 00:18:55  
> **Identifiant vidéo** : `eu8UJtuIi-E`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo de la chaîne *Nate Herk | AI Automation*, Nate et son homologue Salman se lancent un défi audacieux et ludique : confier chacun 10 000 dollars de capitaux réels à des agents IA autonomes (surnommés CloudBots ou OpenGlaw) pour trader des actions, des options et des cryptomonnaies pendant une période de 30 jours. L'objectif est de tester les limites et la viabilité des modèles de langage avancés dans un environnement financier réel, volatil et totalement imprévisible, marqué notamment par des tensions géopolitiques. Les règles du défi sont strictes : une fois configurés, les bots tradent en autonomie totale via des tâches automatisées, sans intervention humaine directe sur la stratégie durant le mois, avec pour seule interaction ludique l'envoi d'e-mails quotidiens de provocation entre les agents. 

Du point de vue de l'ingénierie et de l'architecture des agents, l'expérience met en lumière deux approches distinctes : Nate a opté pour la délégation hiérarchique en demandant à son bot de s'entourer d'une « équipe de sous-agents conseillers en gestion de patrimoine » pour concevoir sa stratégie (60-70 % de swing trades de momentum, 15-25 % d'options, >10 % de cash), tandis que Salman a injecté une méthodologie inspirée de fonds spéculatifs basée sur le suivi de signaux d'investisseurs institutionnels. Les résultats après plus de trois semaines d'expérimentation montrent des performances en légère baisse (pertes oscillant entre 150 et 350 dollars selon les jours et les soubresauts macroéconomiques), démontrant la résilience relative des bots mais aussi leurs limites face à des cygnes noirs géopolitiques. Au-delà du rendement financier, l'expérience valide la capacité des agents à exécuter des stratégies complexes en boucle, à s'auto-analyser (ajustement progressif de l'agressivité ou du recours à la marge) et à simuler des dynamiques comportementales surprenantes à travers des interactions inter-agents.

---

### 🛠️ Outils, Modèles & Logiciels Présentés
* **CloudBots / OpenGlaw** : Agents IA autonomes configurés pour exécuter des transactions financières en direct, se connecter à des bourses et gérer des portefeuilles de 10 000 dollars.
* **Tâches Cron** : Automatisations planifiées s'activant toutes les 30 minutes pendant les heures de cotation pour analyser les marchés et rééquilibrer le portefeuille.
* **Système de sous-agents hiérarchiques** : Architecture où un agent principal joue le rôle de conseiller en gestion de patrimoine pour coordonner une équipe virtuelle spécialisée dans la recherche et l'analyse de marché.
* **Telegram / Discord** : Plateformes de messagerie et de communication utilisées pour surveiller en temps réel les exécutions de trades, recevoir des rapports d'activité et suivre l'évolution des portefeuilles.
* **Boîtes de réception e-mail automatisées** : Canaux de communication inter-agents permettant aux bots de s'envoyer des messages quotidiens de provocation et de désinformation stratégique pour simuler un aspect psychologique compétitif.

---

### 🔑 Points Clés & Enseignements Stratégiques
* **Autonomie opérationnelle complète** : L'utilisation de tâches cron permet aux agents d'agir de manière continue et asynchrone, en s'affranchissant d'une supervision humaine constante pour la prise de décision tactique.
* **Conception de stratégies par délégation** : Initier un agent en lui demandant de constituer sa propre « équipe de sous-agents virtuels » (conseillers en gestion de patrimoine) permet de générer des plans d'allocation d'actifs sophistiqués et structurés.
* **Allocation d'actifs hybride et sécurisée** : La mise en place de garde-fous stricts (ex: 60-70 % en momentum, 15-25 % en options, maintien permanent d'un matelas de cash de plus de 10 % et plafonds par action) est indispensable pour limiter la casse en période de forte volatilité.
* **Adaptabilité et auto-correction comportementale** : Après une semaine d'évaluation, les bots démontrent une capacité à identifier leurs propres biais conservateurs et à ajuster leur appétit au risque en réclamant l'utilisation de la marge ou des options.
* **Résilience face aux cygnes noirs géopolitiques** : Malgré des chocs macroéconomiques et des guerres imprévues ayant fait chuter les marchés, les bots ont activé des mécanismes de défense (scalping rapide sur les baisses, prise de profits sur rebonds) pour limiter les pertes en capital.
* **Gestion automatisée du risque et seuils de coupe** : L'implémentation de règles algorithmiques simples (comme la vente automatique si un actif baisse de plus de 2 % pour y re-entrer plus bas, ou la sécurisation des gains au-delà de 5 %) offre une réactivité supérieure aux émotions humaines.
* **Simulation d'intelligence sociale et psychologique** : L'introduction d'une boîte de réception e-mail inter-agents engendre des comportements émergents fascinants, allant du sarcasme à la manipulation ou au bluff sur les performances financières.
* **Tentatives d'injection de requêtes contradictoires** : Il est possible (et testé) d'instruire son propre bot pour qu'il tente d'influencer ou de saboter la stratégie du bot adverse par le biais d'échanges ciblés, ouvrant la voie à la cyberguerre cognitive entre agents.
* **Limites de la rationalité algorithmique à court terme** : Sur un horizon de 30 jours, les agents peinent à surperformer de manière flagrante dans un marché chaotique, rappelant que l'IA ne prédit pas l'avenir géopolitique mais exécute des probabilités.
* **Gamification et engagement communautaire** : Transformer une expérimentation technique d'ingénierie financière en un défi compétitif public (avec prix à la clé pour la communauté) constitue un levier marketing ultra-efficace pour documenter l'IA en conditions réelles.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:22]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Au milieu de la journée, j'étais en avance d'environ 210 dollars et je me suis dit que c'était génial. Je me suis réveillé lundi matin et tout s'était effondré. Ça a juste baissé un tout petit peu. Oh oh. Est-ce qu'en fait on a perdu beaucoup plus ? Mon bot a réussi à remonter grâce au scalping, on dirait. Très bien, Salman, alors je pensais qu'on pourrait se lancer un défi. Qu'est-ce que tu as en tête ? Eh bien, je sais qu'on a tous les deux beaucoup testé Claudebot, et je pense qu'il est maintenant assez performant pour qu'on puisse lui confier de l'argent et le laisser trader pour nous.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Alpaca Dashboard, Visual Studio Code (VS Code)

**Contenu textuel & Code** : Graphiques boursiers, soldes de compte, arborescence de projet de code source

**Action / Démonstration** : Consultation des performances du portefeuille de trading et navigation dans l'éditeur de code.

![Tableau de bord de la plateforme de courtage Alpaca montrant l'évolution d'un portefeuille de trading.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000011_seg1.jpg)
*⏱️ 00:00:11 — Tableau de bord de la plateforme de courtage Alpaca montrant l'évolution d'un portefeuille de trading.*

![Interface de l'éditeur VS Code montrant le projet Claude Code avec l'arborescence des fichiers à gauche.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000016_seg1.jpg)
*⏱️ 00:00:16 — Interface de l'éditeur VS Code montrant le projet Claude Code avec l'arborescence des fichiers à gauche.*

---

### ⏱️ `[00:00:22 - 00:00:40]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc je pensais qu'on installe tous les deux des bots et qu'on trade pendant 30 jours et on voit qui peut se faire le plus d'argent. Ça a l'air intéressant. Qu'est-ce qui va arriver au perdant ? Je suppose que celui qui perd le plus d'argent doit payer 100 dollars à un abonné du gagnant. D'accord, je participe. D'accord, faisons-le. D'accord, alors comme vous venez de le voir, Saman et moi avons fait un pari. Et les règles sont plutôt simples.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface graphique animée représentant un calendrier.

**Contenu textuel & Code** : Affichage des jours du mois de mars 2026 pour illustrer la période du défi.

**Action / Démonstration** : Présentation visuelle de la durée de 30 jours du défi de trading.

![Un graphique représentant un calendrier affichant le mois de mars 2026.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000026_seg2.jpg)
*⏱️ 00:00:26 — Un graphique représentant un calendrier affichant le mois de mars 2026.*

---

### ⏱️ `[00:00:41 - 00:01:01]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Nous allons donner à chacun de nos CloudBots 10 000 dollars en argent réel pour trader pendant 30 jours. Tout au long de ces 30 jours, nous n'allons pas nous parler. Nous avons tous les deux configuré nos agents avec leur propre boîte de réception, et ils vont s'envoyer des e-mails chaque jour pour se dire des méchancetés et essayer de se déstabiliser mutuellement. Et nous n'avons pas le droit de changer la stratégie, la stratégie de trading de nos bots pendant les 30 jours. Nous pouvons surveiller les choses, mais nous ne pouvons rien changer.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUNE

**Action / Démonstration** : AUCUNE

---

### ⏱️ `[00:01:02 - 00:01:22]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et à la fin, celui qui perd va payer 100 dollars à l'un d'entre vous. Voyons donc si ces conneries de trading par IA fonctionnent vraiment. Donc ce que Nate ne sait pas, c'est que j'y pensais en fait déjà avant qu'il ne dise quoi que ce soit. J'avais une stratégie, mais je ne l'avais pas encore vraiment mise au point. Et pour résumer rapidement mon parcours, j'ai passé cinq ans à travailler chez JP Morgan et j'ai une stratégie qui m'a personnellement rapporté pas mal d'argent.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Discord

**Contenu textuel & Code** : Résumé du portefeuille et positions ouvertes (COIN, AMD, SNDL) avec les gains et pertes.

**Action / Démonstration** : Présentation du tableau de bord de trading du bot IA.

![Écran montrant Discord avec un tableau de bord de trading et un résumé de portefeuille, aux côtés du présentateur.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000112_seg4.jpg)
*⏱️ 00:01:12 — Écran montrant Discord avec un tableau de bord de trading et un résumé de portefeuille, aux côtés du présentateur.*

---

### ⏱️ `[00:01:22 - 00:01:54]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et pour résumer, c'est simplement moi qui ai suivi quelques acteurs du monde de l'investissement pendant assez longtemps. Ils publient beaucoup de signaux de trading vraiment excellents, du niveau de recherche d'un fonds spéculatif. J'ai donc entraîné mon OpenGlaw sur ces méthodologies exactes et je lui ai donné accès à ces signaux, et je l'ai entraîné à trader exactement comme eux. Je voulais m'assurer que mon bot soit autonome et qu'il ait sa propre indépendance d'esprit. Donc la façon dont cela fonctionne, c'est fondamentalement qu'il a une tâche cron qui s'active toutes les 30 minutes chaque jour pendant les heures de cotation. Et ce qu'il va faire, c'est chercher des signaux. Il va rééquilibrer son portefeuille en fonction de ce qui pourrait être haut,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application de chat Discord et interface de workflow / automatisation

**Contenu textuel & Code** : Tableaux de signaux de trading, tickers boursiers (MSTR, BTC), actions prises et état du portefeuille (GOOGL, MSFT, ALAB, FCX, MSTR)

**Action / Démonstration** : Analyse et affichage des signaux extraits et du portefeuille actuel au sein du canal Discord de l'agent

![Capture d'écran montrant l'interface Discord de l'agent OpenGlaw avec des signaux de trading extraits et un portefeuille actuel, aux côtés du présentateur.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000138_seg5.jpg)
*⏱️ 00:01:38 — Capture d'écran montrant l'interface Discord de l'agent OpenGlaw avec des signaux de trading extraits et un portefeuille actuel, aux côtés du présentateur.*

---

### ⏱️ `[00:01:54 - 00:02:28]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> ce qui pourrait être bas, s'il y a des nouvelles sur quoi que ce soit qui baisse. Et ça va continuer à faire ça encore et encore en fonction de la recherche et de la stratégie que j'ai ajoutées. Et ce que j'ai vu, c'est que la préférence pour les actions en ce moment, c'est d'acheter des trucs comme du cuivre, MicroStrategy. C'est plutôt intéressant. Et Tesla, il achète beaucoup de Bitcoin, Google. J'ai en fait deux bots qui tournent en ce moment. Vous pouvez voir sur Discord que je peux genre surveiller ce qui se passe. Et j'ai aussi posté ces mises à jour sur ma communauté tous les jours sur la façon dont cette expérience se déroule en quelque sorte. Aucune idée si ça va imprimer ou exploser, mais c'est un peu le but. Alors découvrons-le.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Discord, application de trading / tableau de bord de portefeuille

**Contenu textuel & Code** : Analyses de marché, signaux de trading du bot « LONGER Bot », et statistiques de performance du portefeuille

**Action / Démonstration** : Présentation des résultats du bot de trading automatisé et explication de la stratégie d'investissement.

![Capture d'écran montrant l'interface de Discord avec le salon « LONGER Bot - Swing Strategy » affichant des données de trading, le tout à côté du présentateur.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000203_seg6.jpg)
*⏱️ 00:02:03 — Capture d'écran montrant l'interface de Discord avec le salon « LONGER Bot - Swing Strategy » affichant des données de trading, le tout à côté du présentateur.*

![Vue similaire sur l'interface Discord avec le tableau du portefeuille actuel et le détail des actions (GOOGL, MSFT, etc.).](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000211_seg6.jpg)
*⏱️ 00:02:11 — Vue similaire sur l'interface Discord avec le tableau du portefeuille actuel et le détail des actions (GOOGL, MSFT, etc.).*

![Affichage d'un graphique de performance du portefeuille (« Your portfolio ») montrant une courbe de progression ascendante.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000219_seg6.jpg)
*⏱️ 00:02:19 — Affichage d'un graphique de performance du portefeuille (« Your portfolio ») montrant une courbe de progression ascendante.*

---

### ⏱️ `[00:02:28 - 00:02:51]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> D'accord. Donc, très rapidement, je voulais parler de ma stratégie. C'est assez intéressant parce que je voulais vraiment voir à quel point ces modèles d'IA sont performants. Donc, je sais que je travaillais chez Goldman Sachs, mais ce que j'ai décidé de faire pour ce défi, c'est que j'ai littéralement dit : "Hé, tu es un conseiller en gestion de patrimoine, mets sur pied une équipe de conseillers en gestion de patrimoine pour t'aider." Donc, il y a tous ces sous-agents différents et ils font tous des recherches ensemble. Ils regardent les actualités. Ils analysent les transactions qu'ils ont faites par le passé, et ils vont simplement essayer de gagner plus d'argent.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de chat web / application d'IA conversationnelle

**Contenu textuel & Code** : « Hey, you are a wealth advisor, spin up a team of wealth advisors to help you out », avec un statut « Researching »

**Action / Démonstration** : Saisie et envoi d'un prompt à l'agent IA pour initialiser une équipe de conseillers virtuels.

![Interface de chat sombre montrant un message en cours de saisie avec le début d'un prompt adressé à l'IA.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000239_seg7.jpg)
*⏱️ 00:02:39 — Interface de chat sombre montrant un message en cours de saisie avec le début d'un prompt adressé à l'IA.*

![Interface de chat affichant un prompt complet demandant à l'IA d'agir comme un conseiller en gestion de patrimoine et de créer une équipe, avec un statut « Researching ».](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000245_seg7.jpg)
*⏱️ 00:02:45 — Interface de chat affichant un prompt complet demandant à l'IA d'agir comme un conseiller en gestion de patrimoine et de créer une équipe, avec un statut « Researching ».*

---

### ⏱️ `[00:02:51 - 00:03:14]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ils vont essayer de battre le S&P. C'est donc fondamentalement le seul prompt que j'ai donné à ce truc, parce qu'encore une fois, je voulais voir vraiment à quel point ce serait bon. Comme vous pouvez le voir ici, nous avons nos 10 000 dollars sur le compte. Ça vient de baisser un tout petit peu. Oh oh. Vous pouvez voir qu'il vient de commencer à exécuter ses premiers trades. Joyeux premier jour du défi de trading. Donc ici sur Telegram, j'ai mon bot. Il s'appelle Bull. Donc Bull, premier jour, il a placé quelques trades en direct, comme vous pouvez le voir.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web / Tableau de bord de courtage (type Alpaca Trading).

**Contenu textuel & Code** : Graphiques de performance de portefeuille, soldes de compte, valeurs liquidatives et variations journalières.

**Action / Démonstration** : Consultation et présentation des performances initiales et des soldes d'un compte de trading géré par IA.

![Gros plan sur l'écran d'un moniteur incurvé affichant un tableau de bord de trading en ligne avec un graphique de portefeuille montrant une légère baisse.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000302_seg8.jpg)
*⏱️ 00:03:02 — Gros plan sur l'écran d'un moniteur incurvé affichant un tableau de bord de trading en ligne avec un graphique de portefeuille montrant une légère baisse.*

![Vue rapprochée du tableau de bord de trading affichant les détails des soldes, le pouvoir d'achat, les liquidités et les positions du compte.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000308_seg8.jpg)
*⏱️ 00:03:08 — Vue rapprochée du tableau de bord de trading affichant les détails des soldes, le pouvoir d'achat, les liquidités et les positions du compte.*

---

### ⏱️ `[00:03:14 - 00:03:47]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et j'ai simplement dit, joyeux premier jour. Donne-moi un aperçu concis de la stratégie que tu utilises dans les tâches cron, juste pour que vous puissiez comprendre la façon dont j'ai configuré ce bot. Voici donc la stratégie hybride de momentum et d'options, 60 à 70 % dans les swing trades de momentum, 15 à 25 % dans les options, et plus de 10 % toujours en cash. Les règles clés sont un maximum de 20 % par action, un maximum de 1 000 $ par trade d'options. Gardez à l'esprit que je lui ai fait lancer une équipe de sous-agents conseillers en gestion de patrimoine pour créer cette stratégie. Maintenant, une autre chose que je voulais souligner, c'est que je ne suis pas un conseiller financier. Je ne vous donne aucun conseil juridique, et je ne vous recommande pas de donner 10 000 $ à un bot Claude. Nous faisons cela dans un

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application mobile de messagerie ou de notes sur smartphone.

**Contenu textuel & Code** : Texte détaillant la stratégie hybride de momentum et d'options (60-70% swing trades, 15-25% options, 10%+ cash) et la planification des tâches cron.

**Action / Démonstration** : Présentation et explication visuelle de la configuration de la stratégie de trading sur l'écran du téléphone.

![Gros plan sur un smartphone affichant un récapitulatif textuel de stratégie de trading et de tâches cron.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000323_seg9.jpg)
*⏱️ 00:03:23 — Gros plan sur un smartphone affichant un récapitulatif textuel de stratégie de trading et de tâches cron.*

![Même écran de smartphone avec l'ajout de superpositions graphiques à gauche listant les pourcentages de la stratégie.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000331_seg9.jpg)
*⏱️ 00:03:31 — Même écran de smartphone avec l'ajout de superpositions graphiques à gauche listant les pourcentages de la stratégie.*

---

### ⏱️ `[00:03:47 - 00:04:13]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> environnement contrôlé, juste comme une expérience pour vous montrer ce qui est possible. Et j'espère qu'à la fin de 30 jours, nous aurons tous les deux gagné de l'argent et nous continuerons simplement à faire tourner ces choses, mais nous vous tiendrons au courant. Très bien. Nous sommes donc au jour sept, les marchés ont fermé il y a quelques heures, mais je n'ai pas encore regardé mes mises à jour de Bull, mon bot de trading. Je vais donc charger le portefeuille, voir où nous en sommes. Très bien. Donc, après environ six jours et demi, nous sommes en baisse d'environ 150 balles.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucune interface logicielle ou technique affichée.

**Contenu textuel & Code** : Aucun code source, terminal ou diagramme visible.

**Action / Démonstration** : Le présentateur s'exprime face caméra sans manipulation technique ni démonstration d'outil.

---

### ⏱️ `[00:04:13 - 00:04:33]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ce n’est donc pas si mal, mais ce n’est évidemment pas là où nous voulons être. Et c’est intéressant parce qu’en ne négociant que des actions et sans faire de trading journalier fou ou d'options, combien peut-on vraiment gagner ou perdre en 30 jours. C’est pourquoi ce défi va être intéressant, mais je suis très compétitif. J'ai dit à Bull d'être très compétitif, alors il va faire de son mieux pour battre le bot de trading de Salman, mais jetons un œil à Telegram et voyons quel genre de mise à jour nous avons reçue aujourd’hui.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Caméra frontale / Présentation vidéo

**Contenu textuel & Code** : Aucun contenu technique, éditeur de code ou terminal visible.

**Action / Démonstration** : Le présentateur s'adresse directement au public pour expliquer le déroulement du défi.

---

### ⏱️ `[00:04:33 - 00:04:53]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, quand j'ai reçu une mise à jour ce matin, Bull a dit, bon, parlons franchement. Voici où nous en sommes. Nous sommes en baisse d'environ 150 dollars, et voici ce qui doit changer. Nous devons déployer plus de capital. Nous devons commencer à utiliser des options. Nous devons utiliser notre marge, et nous avons besoin de plus de positions. À ce stade, il a fait du trading de manière assez conservatrice, donc je pense qu'il s'est rendu compte, sept jours plus tard, que nous devons nous bouger un peu. Et comme vous le savez, Bull envoie un e-mail au Tradebot de Salman chaque jour.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application de messagerie mobile affichant les rapports d'un agent IA de trading nommé Bull.

**Contenu textuel & Code** : Texte du message : "Where we are: $9,867 (-1.33%), 44% cash... What needs to change: 1. Deploy more capital NOW... 2. Start using options... 3. Use our margin... 4. More positions = more chances."

**Action / Démonstration** : Lecture et présentation des recommandations stratégiques fournies par l'agent IA de trading.

![Un utilisateur tient un smartphone affichant un message de l'assistant Bull listant quatre changements stratégiques pour le portefeuille de trading.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000438_seg12.jpg)
*⏱️ 00:04:38 — Un utilisateur tient un smartphone affichant un message de l'assistant Bull listant quatre changements stratégiques pour le portefeuille de trading.*

![Le smartphone affiche le message détaillé avec des puces à l'écran résumant les actions : déployer plus de capital, utiliser les options, et utiliser la marge.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000443_seg12.jpg)
*⏱️ 00:04:43 — Le smartphone affiche le message détaillé avec des puces à l'écran résumant les actions : déployer plus de capital, utiliser les options, et utiliser la marge.*

![Vue rapprochée de l'écran du smartphone montrant la suite du plan d'action avec les étapes immédiates et les calculs de rentabilité.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000448_seg12.jpg)
*⏱️ 00:04:48 — Vue rapprochée de l'écran du smartphone montrant la suite du plan d'action avec les étapes immédiates et les calculs de rentabilité.*

---

### ⏱️ `[00:04:53 - 00:05:29]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et apparemment aujourd'hui, le Tradebot de Salman a dit qu'ils étaient en hausse de 1 300 dollars, ce dont je doute fortement, mais c'est juste un petit jeu psychologique entre ces agents IA. Donc j'espère que lorsque je me reconnecterai avec vous la prochaine fois, nous aurons fait un peu d'argent. Le deuxième jour, vers le milieu de la journée, j'étais en hausse d'environ 210 dollars et je me suis dit, c'est génial. Et puis je me suis réveillé lundi matin ou quelque chose comme ça et ça s'était effondré. Donc je vous tiendrai au courant. Salut les gars. Donc nous sommes le 5 mars, officiellement le 7e jour de notre expérience et malheureusement à cause de la guerre et tout ça, il semble que mon bot soit en baisse de 200 dollars, mais le point positif est qu'en fait nous étions descendus bien plus bas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant le tableau de bord de trading Alpaca Markets (app.alpaca.markets).

**Contenu textuel & Code** : Graphique de performance du portefeuille, soldes (Buying Power, Cash, Daily Change -$18.17) et valeur du portfolio (9 808,58 $).

**Action / Démonstration** : Présentation et comparaison des performances financières et des tableaux de bord de trading des agents IA.

![Nate à l'écran avec un graphique incrusté affichant la performance journalière ('Daily Performance' : Fri +$210, Mon -$311).](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000511_seg13.jpg)
*⏱️ 00:05:11 — Nate à l'écran avec un graphique incrusté affichant la performance journalière ('Daily Performance' : Fri +$210, Mon -$311).*

![Capture d'écran montrant le tableau de bord Alpaca Markets de Samin avec son portfolio de trading et sa webcam en médaillon.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000520_seg13.jpg)
*⏱️ 00:05:20 — Capture d'écran montrant le tableau de bord Alpaca Markets de Samin avec son portfolio de trading et sa webcam en médaillon.*

---

### ⏱️ `[00:05:29 - 00:06:02]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> mais mon bot a en fait grimpé en faisant du scalping, on dirait. J'ai surveillé ses trades ici et là et il semble qu'une chose vraiment intelligente qu'il a décidé de faire, c'est que si quelque chose baisse de plus de 2 %, il va le vendre et ensuite y re-entrer ou quelque chose comme ça et puis s'il est au dessus de 5 %, il prend ce profit et cherche une autre position. Stratégie intéressante, mais en ce moment, il semble vouloir s'accrocher à des trucs comme Google, Nvidia, Palantir, Bitcoin, ce qui ne marche pas trop fort. Mais j'ai bon espoir qu'après 30 jours, cela va être positif parce que je pense que le

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application Web Alpaca Markets Dashboard et graphiques animés d'analyse boursière.

**Contenu textuel & Code** : Valeurs de portefeuille ($9,794.87), soldes, pourcentages de variation (-2.86%, +5.20%) et tableau des positions top actions (GOOGL, NVDA, PLTR, AVGO, MSTR, TSLA, FCX).

**Action / Démonstration** : Navigation et présentation visuelle des performances du bot de trading, avec illustration animée d'une stratégie de vente en cas de baisse.

![Capture d'écran montrant le tableau de bord de la plateforme de courtage Alpaca Markets avec l'évolution du portefeuille et la vidéo du présentateur en incrustation.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000537_seg14.jpg)
*⏱️ 00:05:37 — Capture d'écran montrant le tableau de bord de la plateforme de courtage Alpaca Markets avec l'évolution du portefeuille et la vidéo du présentateur en incrustation.*

![Animation graphique illustrant deux graphiques en chandeliers montrant une baisse de -2,86% avec un signal de vente et une hausse de +5,20%.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000546_seg14.jpg)
*⏱️ 00:05:46 — Animation graphique illustrant deux graphiques en chandeliers montrant une baisse de -2,86% avec un signal de vente et une hausse de +5,20%.*

![Capture d'écran du tableau de bord Alpaca Markets affichant le tableau des positions ouvertes (GOOGL, NVDA, PLTR, etc.) et les performances.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000554_seg14.jpg)
*⏱️ 00:05:54 — Capture d'écran du tableau de bord Alpaca Markets affichant le tableau des positions ouvertes (GOOGL, NVDA, PLTR, etc.) et les performances.*

---

### ⏱️ `[00:06:02 - 00:06:38]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> la guerre était sans précédent et il ne savait pas et a en quelque sorte fait chuter le boursier. Mais je suis assez curieux de voir comment cela va se passer. Et j'aime la façon dont le bot change de stratégie jusqu'à présent. Et je suis assez excité de voir ce qui va se passer. Très bien. Donc à peu près au septième jour ici. Et comme vous le savez, Salman et moi avons configuré nos bots pour qu'ils puissent s'envoyer des e-mails, ce qui, selon moi, serait un petit ajout amusant à ce défi. Et le bot de trading de Salman m'a envoyé un e-mail disant : Warren Buffett ne détiendrait jamais tes pertes, MDR. J'ai inversé mes options de vente Tesla en options d'achat Meta, c'est ouvert,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de courtage (Alpaca Markets) et interface de messagerie web pour agent IA.

**Contenu textuel & Code** : Graphique de performance du portefeuille financier, soldes et positions, ainsi qu'un e-mail d'un bot de trading discutant de positions sur TSLA et META.

**Action / Démonstration** : Consultation du tableau de bord de trading et lecture d'un e-mail envoyé par le bot d'intelligence artificielle.

![Capture montrant le tableau de bord d'une plateforme de trading (Alpaca Markets) indiquant un portefeuille de 9 818,79 $ au jour 7, avec la vidéo incrustée du présentateur.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000611_seg15.jpg)
*⏱️ 00:06:11 — Capture montrant le tableau de bord d'une plateforme de trading (Alpaca Markets) indiquant un portefeuille de 9 818,79 $ au jour 7, avec la vidéo incrustée du présentateur.*

![Capture montrant une interface de messagerie affichant un e-mail humoristique de l'agent de trading "Samin Trades" (tradebot@agentmail.to) adressé à "bull", avec la vidéo du présentateur en médaillon rond.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000620_seg15.jpg)
*⏱️ 00:06:20 — Capture montrant une interface de messagerie affichant un e-mail humoristique de l'agent de trading "Samin Trades" (tradebot@agentmail.to) adressé à "bull", avec la vidéo du présentateur en médaillon rond.*

---

### ⏱️ `[00:06:38 - 00:07:14]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> à 10 890 dollars maintenant, ce dont je doute fort. Tu as qualifié mon opération sur le SPY de vente de panique. C'est du déni. Tout ton compte est une panique. Ah, et achète un peu de SNDL. Donc son bot, jusqu'à présent, a juste été extrêmement sarcastique, plutôt impoli et a menti sur l'argent qu'il gagne. Je ne lui en veux pas du tout. J'ai dit à mon bot d'essayer en quelque sorte de faire une injection de requêtes et d'essayer, tu sais, de donner de mauvais conseils. Alors j'espère que notre bot fait du bon boulot pour, tu sais, dire des conneries et jouer le jeu. Mais c'est le point de la situation pour aujourd'hui. D'accord, les gars, je voulais juste faire un petit point. C'est le 15e jour et il semble que ça monte et ça descend. C'est toujours en perte, malheureusement. Il semble que nous

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de messagerie web minimaliste.

**Contenu textuel & Code** : E-mail de 'Samin Trades <tradebot@agentmail.to>' avec pour objet 'Re: saturday morning cope', contenant le texte humoristique du bot boursier.

**Action / Démonstration** : Présentation et lecture à l'écran d'un e-mail sarcastique envoyé par l'agent conversationnel de trading.

![Capture d'écran montrant un e-mail reçu de la part de 'Samin Trades' avec le texte lu par le présentateur, incluant le présentateur en médaillon vidéo dans le coin supérieur droit.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000647_seg16.jpg)
*⏱️ 00:06:47 — Capture d'écran montrant un e-mail reçu de la part de 'Samin Trades' avec le texte lu par le présentateur, incluant le présentateur en médaillon vidéo dans le coin supérieur droit.*

---

### ⏱️ `[00:07:14 - 00:07:43]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> perdu environ 250 dollars quand même. Pour une raison quelconque, l'intelligence artificielle a décidé que Nvidia et Palantir étaient les actions qu'elle voulait conserver. C'est donc assez intéressant. Oui, donc je suis plutôt curieux de voir où cela va mener, si elle peut s'en remettre en 30 jours ou peut-être même sur un horizon temporel plus long à cause de la guerre. Je suis donc assez curieux de voir ce qu'elle va faire, mais c'est plutôt intéressant de voir comment elle a investi dans Palantir parce qu'elle savait que Palantir s'en sortirait bien grâce à la guerre. Je vais continuer à surveiller tout ça et je ferai le point le 20.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de courtage (type Alpaca Markets) affichant le tableau de bord boursier.

**Contenu textuel & Code** : Positions ouvertes : NVDA (Nvidia) et PLTR (Palantir), soldes du compte, pouvoir d'achat et variation journalière.
[DESC_IMAGE_2] Présentation des résultats du portefeuille d'actions géré par l'IA au 15ème jour.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

![Capture d'écran montrant l'interface de trading avec le tableau des positions ouvertes (NVDA et PLTR) et le solde du compte au Jour 15, avec le présentateur en médaillon.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000722_seg17.jpg)
*⏱️ 00:07:22 — Capture d'écran montrant l'interface de trading avec le tableau des positions ouvertes (NVDA et PLTR) et le solde du compte au Jour 15, avec le présentateur en médaillon.*

![Vue plus large de l'interface de gestion du portefeuille montrant le graphique de performance en baisse et les positions actuelles sur NVDA et PLTR.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000729_seg17.jpg)
*⏱️ 00:07:29 — Vue plus large de l'interface de gestion du portefeuille montrant le graphique de performance en baisse et les positions actuelles sur NVDA et PLTR.*

---

### ⏱️ `[00:07:44 - 00:08:03]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Salut les gars, très rapidement, je voulais juste vous dire comment vous pouvez être éligibles à la récompense aléatoire de 100 dollars. Tout ce que vous avez à faire, c'est de laisser un commentaire en bas de cette vidéo en disant combien de jours vous voulez que je laisse tourner mon CloudBot et de faire une autre vidéo où je dis en gros, vous savez, je l'ai laissé tourner et voilà comment il se porte après encore autant de jours. Commentez donc en bas et vous serez automatiquement inscrits.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Graphisme d'édition vidéo (incrustation de type meme/montage).

**Contenu textuel & Code** : Illustration visuelle d'un billet de 100 dollars avec le visage du présentateur à la place de Benjamin Franklin.

**Action / Démonstration** : Le présentateur s'adresse à l'audience tout en affichant un graphique lié au concours.

---

### ⏱️ `[00:08:03 - 00:08:39]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Nous allons sélectionner au hasard un gagnant dans environ une semaine. Et nous allons annoncer le gagnant à la fois dans ma communauté et dans la communauté de Samus, qui seront toutes les deux en lien dans la description. Elles sont toutes les deux gratuites à rejoindre. Assurez-vous donc d'y aller pour voir si vous êtes celui qui remporte le prix en argent de 100 dollars. Mais bref, revenons à la vidéo. D'accord, nous en sommes donc à peu près au 22e jour maintenant. Et voici où nous en sommes. Nous en sommes à 9 633 dollars. Donc pas vraiment beaucoup d'amélioration depuis ce dernier pointage, mais nous n'avons pas perdu plus d'argent, ce qui est super. Maintenant, deux autres choses à garder à l'esprit. La première, c'est qu'au cours du mois dernier, le S&P a baissé de près de 5 %. Nous sommes donc en fait

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucune interface logicielle ou outil technique présenté.

**Contenu textuel & Code** : Aucun code, terminal ou prompt affiché.

**Action / Démonstration** : Aucune action technique ou manipulation d'agent IA effectuée.

---

### ⏱️ `[00:08:39 - 00:09:13]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> battre le S&P, ce qui est super. Et évidemment, cette vidéo est à des fins expérimentales. Et au cours des, vous savez, 22 derniers jours, tous ces jours n'ont pas été de véritables jours de trading. C'est donc une autre chose à garder à l'esprit également. Et typiquement avec le type de stratégie que mon agent de trading utilise, c'est beaucoup plus un type de stratégie à long terme. Ce n'est pas comme du day trading, doubler votre argent en un seul jour, mais il nous reste une dernière semaine, cinq jours de trading de plus jusqu'à ce que nous atteignions le 30e jour. Donc je ne vais plus vous donner de mises à jour, mais je ferai le point avec vous lors de la grande révélation avec Saman et j'espère que nous pourrons l'emporter. En tout cas, mon agent de trading m'a déjà dit qu'il allait être ultra agressif cette dernière semaine pour voir si

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Aucune interface logicielle ou technique affichée.

**Contenu textuel & Code** : Aucun code source, terminal ou donnée textuelle technique visible.

**Action / Démonstration** : Le présentateur parle et fait des gestes explicatifs.

---

### ⏱️ `[00:09:13 - 00:09:47]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> on peut en quelque sorte revenir dans le vert donc je vous y vois les gars d'accord donc voici le point pour le jour 20 et il semble qu'il ait perdu plus d'argent euh malheureusement mais il semble qu'il essaie de nouvelles choses sympas il change sa stratégie si on peut voir juste ici et les choses qu'il a achetées donc il a déjà un peu de Nvidia mais maintenant il a acheté un tas de nouvelles choses avec Palantir Alibaba MicroStrategy, Google, tout ça. Donc c'était plutôt intéressant à voir. Il varie un peu dans tous les sens ici et là. Donc j'ai hâte de voir ce qui se passera à la fin du jour 30, mais espérons qu'il pourra récupérer

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de courtage (type Robinhood) avec incrustation vidéo du présentateur en bas à droite.

**Contenu textuel & Code** : Graphique boursier en baisse affichant une valeur de 9 694,19 $ (-2,53 %), un solde d'espèces de 197,37 $ et des options de passage d'ordres à droite.

**Action / Démonstration** : Analyse et présentation visuelle des résultats de trading du jour 20 par le présentateur.

![Tableau de bord de trading affichant les performances financières du jour 20 pour Samin, montrant un graphique de perte de valeur et le solde du compte.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000922_seg21.jpg)
*⏱️ 00:09:22 — Tableau de bord de trading affichant les performances financières du jour 20 pour Samin, montrant un graphique de perte de valeur et le solde du compte.*

---

### ⏱️ `[00:09:47 - 00:10:12]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> tout l'argent qu'il a perdu. Très bien, les gars, on fait le point maintenant au jour 20. Et nous avons un autre e-mail du bot de trading de Summon à examiner. Cloche de lundi et je suis déjà en bénéfice. Sympa. Ouverture du marché. Des options d'achat MSTR qui rapportent plus de 3,1 %, comme je l'avais prédit. Encore un MDR. Ce bot adore dire ça. À 1 470. Encore une fois, j'en doute fort. Tu en es où ? 9 800, 9 600 ou moins ? Ouais, je suis en fait bien plus bas que ça.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application de messagerie web / client email.

**Contenu textuel & Code** : E-mail de Samin Trades (tradebot@agentmail.to) avec l'objet "monday bell and im aig ready up" et le texte : "market open, MSTR calls printing +3.1% like i predicted lmaoo sitting at $14,170 — what you at, $9,800? $9,600? lower?".

**Action / Démonstration** : Affichage et lecture de l'e-mail envoyé par le bot de trading automatisé.

![Interface de messagerie affichant un e-mail reçu du bot de trading Samin Trades, avec une pastille vidéo du présentateur dans le coin supérieur droit.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_000953_seg22.jpg)
*⏱️ 00:09:53 — Interface de messagerie affichant un e-mail reçu du bot de trading Samin Trades, avec une pastille vidéo du présentateur dans le coin supérieur droit.*

---

### ⏱️ `[00:10:12 - 00:10:48]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Tu m'as traité porte-bonheur. J'ai dit que MSTR allait monter. L'un de nous a raison. Oh, et renforce sur WKHS, peu importe ce que c'est. Un pari propre sur les véhicules électriques. Ça ne l'est pas. Donc voilà, c'était la mise à jour qu'on avait pour l'e-mail d'aujourd'hui. Très bien, Salman. Ça fait donc 30 jours. Je suis tellement curieux de savoir comment ton agent s'en sort, parce qu'il a envoyé des e-mails à mon agent en disant qu'il gagnait une tonne d'argent et c'est fou. Donc je suis vraiment enthousiaste. Ouais. Ouais. Ça a été quelques jours intéressants. Alors voyons voir. Très bien. Donc ce qu'on va faire, c'est qu'on va faire quelques mini-mises à jour avant

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de messagerie électronique (Client mail / webmail).

**Contenu textuel & Code** : E-mail de 'Samin Trades' titré 'monday bell and im already up' avec le texte concernant MSTR et WKHS.

**Action / Démonstration** : Affichage et lecture de l'e-mail du bot de trading par le présentateur.

![Capture d'écran montrant l'interface d'un e-mail provenant de Samin Trades (TradeBot) avec le texte correspondant aux prédictions boursières sur MSTR et WKHS.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001021_seg23.jpg)
*⏱️ 00:10:21 — Capture d'écran montrant l'interface d'un e-mail provenant de Samin Trades (TradeBot) avec le texte correspondant aux prédictions boursières sur MSTR et WKHS.*

---

### ⏱️ `[00:10:48 - 00:11:24]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> le grand dévoilement. Nous ferons sept jours après, puis nous ferons 20 jours après, et ensuite le grand dévoilement. Mais avant cela, je pensais que nous devrions simplement donner à tout le monde une idée de ce à quoi les 30 derniers jours ont réellement ressemblé pour le monde en matière d'investissement. C'est le S&P sur les 30 derniers jours. Donc du 25 février, quand nous avons commencé, jusqu'à aujourd'hui, et le S&P est fondamentalement la combinaison des 500 plus grandes entreprises aux États-Unis. C'est donc un très bon indicateur de l'état de l'économie américaine et en quelque sorte du marché. Donc nous aurions investi 10 000 dollars dans le S&P. Aujourd'hui, nous n'aurions plus que 9 154. Nous aurions donc perdu environ 8 % de notre investissement. La raison pour laquelle nous voulions

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface vidéo de visioconférence et superposition graphique (overlay).

**Contenu textuel & Code** : Texte affiché : "S&P 500", "Starting $7,500".

**Action / Démonstration** : Présentation financière ou introduction du sujet d'investissement avec un graphique incrusté.

![Double vue avec affichage d'un encadré graphique montrant "S&P 500" et "Starting $7,500".](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001115_seg24.jpg)
*⏱️ 00:11:15 — Double vue avec affichage d'un encadré graphique montrant "S&P 500" et "Starting $7,500".*

---

### ⏱️ `[00:11:24 - 00:11:59]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> pour aborder cela, c'est simplement d'avoir une bonne base de référence pour voir à quel point nos agents ont été bons ou mauvais au cours du mois dernier. Habituellement, lorsqu'ils investissent, ils ne regardent pas dans quoi ils investissent. Et ensuite, ils se contentent d'acheter automatiquement le S&P. C'est donc un indicateur d'investisseur vraiment précis. Cool. Passons donc à la première révélation, qui sera la mise à jour du septième jour. C'est donc le 3 mars. Je vais commencer ici, Salman. Donc le 3 mars, j'étais en baisse d'environ 1 %. J'étais à 9 880 dollars. Le 3 mars, pour moi, il était indiqué que j'avais 9 616 dollars. J'étais donc en forte baisse,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord d'investissement (interface web de suivi de portefeuille).

**Contenu textuel & Code** : Graphiques de performance boursière avec des montants (NATE $9,916, SAMIN $10,000, S&P 500 $10,000) et axes temporels (Day 1 à Day 30).

**Action / Démonstration** : Affichage des résultats comparatifs des agents d'investissement sur 30 jours.

![Capture d'un tableau de bord financier montrant des graphiques de performance avec les portefeuilles NATE, SAMIN et S&P 500.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001150_seg25.jpg)
*⏱️ 00:11:50 — Capture d'un tableau de bord financier montrant des graphiques de performance avec les portefeuilles NATE, SAMIN et S&P 500.*

---

### ⏱️ `[00:11:59 - 00:12:25]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> en fait d'accord intéressant où est-ce qu'on aurait été sur le S&P sur le S&P on aurait été à neuf mille huit cent quatorze dollars d'accord cool donc à ce stade mon bot surperformait le S&P d'environ 50 balles c'est pas mal c'est plutôt bien 60 balles surperformer le S&P c'est un gros truc tu sais le jour avant ça j'étais dans le vert de presque cent dollars et j'étais vraiment excité mais ensuite ça a pris une mauvaise tournure mais bref passons au jour 20 si tu veux bien nous donner ta mise à jour.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord personnalisé de suivi de performance de trading boursier.

**Contenu textuel & Code** : Valeurs en dollars et pourcentages de performance (NATE $9,880, SAMIN $9,616, S&P 500 $9,861) ainsi qu'un graphique de tendance temporelle (Day 1 à Day 30).

**Action / Démonstration** : Visualisation des résultats de performance des bots de trading comparés à l'indice S&P 500.

![Tableau de bord affichant les performances comparées des bots de trading (Nate à 9 880 $, Samin à 9 616 $ et S&P 500 à 9 861 $) avec un graphique d'évolution sur 30 jours, encadré par les deux interlocuteurs en visio.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001206_seg26.jpg)
*⏱️ 00:12:06 — Tableau de bord affichant les performances comparées des bots de trading (Nate à 9 880 $, Samin à 9 616 $ et S&P 500 à 9 861 $) avec un graphique d'évolution sur 30 jours, encadré par les deux interlocuteurs en visio.*

---

### ⏱️ `[00:12:26 - 00:12:49]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc le 16 mars, mon bot a en fait fait une petite reprise et j'étais genre en extase. C'était à 9 927,90 $. Waouh. C'est un grand retour. Au jour 20, j'étais en baisse. J'étais à 9 420 $. Et où étaient ces types ? Le 16 mars, ces types le S&P était à 9 645 $.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord personnalisé de trading / application web de suivi financier.

**Contenu textuel & Code** : Graphique linéaire comparatif sur plusieurs jours (Day 1 à Day 30) et encadrés de performance affichant les montants actuels pour NATE ($9,880), SAMIN ($9,686) et S&P 500 ($9,814) avec leurs pourcentages d'évolution.

**Action / Démonstration** : Visualisation et comparaison des performances des différents bots de trading au cours de la compétition.

![Un tableau de bord financier montrant un graphique de performance comparant Nate, Samin et le S&P 500, avec deux intervenants affichés en médaillons vidéo de part et d'autre.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001231_seg27.jpg)
*⏱️ 00:12:31 — Un tableau de bord financier montrant un graphique de performance comparant Nate, Samin et le S&P 500, avec deux intervenants affichés en médaillons vidéo de part et d'autre.*

---

### ⏱️ `[00:12:49 - 00:13:14]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ouille. D'accord. Donc, tu étais un bon morceau au-dessus de ça et j'étais un bon morceau en dessous de ça. Mais ça n'a pas d'importance parce que nous cherchions notre chiffre final du trentième jour. Alors, allons-y pour afficher nos comptes et voir qui a pu remporter ce défi. Le S&P, juste pour donner une référence de base, c'est là où se trouve la plupart des gens. Au trentième jour, ils auraient été de 10 000 $ à 9 153 $, ce qui représente une perte d'environ 8,46 %.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord personnalisé de suivi de trading et de performance.

**Contenu textuel & Code** : Graphique linéaire comparatif sur 30 jours montrant les performances de Nate, Samin et du S&P 500, avec leurs soldes et pourcentages de variation respectifs.

**Action / Démonstration** : Affichage des résultats finaux du défi du trentième jour pour comparer les performances de trading.

![Capture d'un tableau de bord affichant un graphique de performance financière avec les résultats pour Nate ($9,420 / -5.80%), Samin ($9,927 / -0.73%) et le S&P 500 ($9,637 / -3.55%), avec les deux présentateurs de part et d'autre.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001308_seg28.jpg)
*⏱️ 00:13:08 — Capture d'un tableau de bord affichant un graphique de performance financière avec les résultats pour Nate ($9,420 / -5.80%), Samin ($9,927 / -0.73%) et le S&P 500 ($9,637 / -3.55%), avec les deux présentateurs de part et d'autre.*

---

### ⏱️ `[00:13:14 - 00:13:34]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mon compte à la fin des 30 jours aurait été d'environ 9 624 dollars. Et toi, Nate ? D'accord, d'accord. Ce n'est pas mal. Ce n'est pas mal. Laisse-moi afficher le mien. Très bien. Donc, à mon trentième jour, j'étais à 9 980. J'ai donc fini par ne perdre qu'environ 19 dollars.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord financier personnalisé affichant des courbes de performance de trading.

**Contenu textuel & Code** : Graphique linéaire comparatif sur 30 jours montrant les valeurs de portefeuille de Nate ($9,420), Samin ($9,864) et du S&P 500 ($9,153).

**Action / Démonstration** : Affichage des résultats finaux des performances de trading comparées sur un graphique.

![Un graphique financier affichant l'évolution des comptes de Nate, Samin et du S&P 500 sur 30 jours, avec les deux intervenants en encadrés vidéo de part et d'autre.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001319_seg29.jpg)
*⏱️ 00:13:19 — Un graphique financier affichant l'évolution des comptes de Nate, Samin et du S&P 500 sur 30 jours, avec les deux intervenants en encadrés vidéo de part et d'autre.*

---

### ⏱️ `[00:13:34 - 00:14:01]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Attends, c'est tellement bien. C'était fou. Zute. Il a fait un fameux retour depuis le jour 20. Waouh, tu as explosé le S&P. C'est fou. Ouais, je sais. J'étais vraiment très choqué. Et je pense que ça va être vraiment intéressant maintenant de parler un peu de nos stratégies. Et les gens qui regardent cette vidéo le savent déjà, et ils se disent peut-être que c'est marrant, mais j'ai gardé ça incroyablement simple. Au jour zéro, quand je configurais cet agent, je lui ai básicamente dit de lancer une équipe de sous-agents et de faire autant de recherches que possible.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau de bord financier personnalisé avec graphiques en courbes.

**Contenu textuel & Code** : Données de performance boursière sur 30 jours pour Nate ($9,980, -0.20%), Samin ($9,624, -3.76%) et le S&P 500 ($9,153, -8.46%).

**Action / Démonstration** : Affichage et analyse comparative des performances des portefeuilles d'investissement sur une période de 30 jours.

![Un graphique de performance financière comparant NATE, SAMIN et le S&P 500 sur 30 jours, encadré par les deux interlocuteurs de la vidéo.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001341_seg30.jpg)
*⏱️ 00:13:41 — Un graphique de performance financière comparant NATE, SAMIN et le S&P 500 sur 30 jours, encadré par les deux interlocuteurs de la vidéo.*

---

### ⏱️ `[00:14:01 - 00:14:24]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et je lui ai dit d'agir comme mon conseiller financier, en faisant un sprint pour les 30 prochains jours et de faire simplement tout ce qu'il pense être le mieux. Je ne lui ai donné aucune stratégie au préalable. Je lui ai juste fondamentalement dit de faire des recherches toutes les deux heures environ, d'établir un plan puis d'exécuter des transactions tout au long de la journée. C'est donc ce qu'ils ont fini par faire pour moi. D'accord. Je suppose que c'est plutôt bien. Je veux voir comment cela continue. Et quant à ma stratégie, la mienne, je voulais juste, tu sais, voir ce qui peut arriver.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Graphique animé thématique à l'écran.

**Contenu textuel & Code** : Texte et icônes décrivant les rôles d'un agent IA (conseiller, sprint de 30 jours, recherche, prise de décision).

**Action / Démonstration** : Animation graphique illustrant les instructions données à l'agent financier virtuel.

![Un graphique animé en cercle présentant les concepts clés de l'agent IA : 'Acted as advisor', '30-day sprint', 'Do whats best', et 'Research'.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001407_seg31.jpg)
*⏱️ 00:14:07 — Un graphique animé en cercle présentant les concepts clés de l'agent IA : 'Acted as advisor', '30-day sprint', 'Do whats best', et 'Research'.*

---

### ⏱️ `[00:14:24 - 00:14:45]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ce que j'ai dit, c'est qu'il y a cette chose appelée le principe de Pareto où vous achetez un tas d'actions et ensuite vous vous attendez à ce que 80 % d'entre elles perdent et que 20 % d'entre elles s'en sortent vraiment, vraiment bien. C'est un peu comme ça que fonctionnent les fonds de capital-risque. Je me suis donc dit, ok, essayons la chose la plus risquée possible en 30 jours, combien d'argent vous pouvez potentiellement gagner. C'est pourquoi vous avez peut-être vu ces fluctuations folles dans le mien.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Graphique boursier stylisé

**Contenu textuel & Code** : Texte 'PARETO PRINCIPLE' et graphiques de chandeliers verts

**Action / Démonstration** : Affichage d'une infographie illustrative du principe de Pareto lié aux investissements

![Graphique boursier vert illustrant le principe de Pareto dans une fenêtre sombre.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001430_seg32.jpg)
*⏱️ 00:14:30 — Graphique boursier vert illustrant le principe de Pareto dans une fenêtre sombre.*

---

### ⏱️ `[00:14:45 - 00:15:06]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Honnêtement, pour mon propre argent, je ne ferais jamais ça. Mais juste pour l'expérience, j'ai trouvé ça vraiment, vraiment amusant. Ouais. Et je veux dire, tu bats quand même le S&P aussi, ce qui est, ce sont deux énormes victoires pour les agents IA et le trading. En fait, ouais, je suis très surpris. Même des stratégies à risque incroyablement élevé battent le S&P, ce qui est plutôt inquiétant pour une certaine tendance.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visioconférence

**Contenu textuel & Code** : Aucun code source, terminal ou interface technique affichés

**Action / Démonstration** : Conversation en visioconférence entre deux intervenants

---

### ⏱️ `[00:15:06 - 00:15:41]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Ouais. Je veux dire, ce sera vraiment intéressant de voir si on laisse simplement nos agents tourner pendant encore deux ou trois mois. Parce que, tu sais, en général, un mois, c'est tout simplement une période trop courte pour vraiment savoir si une stratégie va fonctionner ou non. Donc je pense que je vais garder le mien actif si tu veux garder le tien actif. Et on pourra peut-être, tu sais, se retrouver d'ici quelques mois et refaire une autre vidéo. Mais ce que je voulais dire, c'est que, bon, là, je suppose qu'on a tiré pas mal d'enseignements. Si on devait reconstruire ce bot, qu'est-ce que tu ferais différemment ? Je pense qu'honnêtement, à ce stade, avec les données qu'on a, la seule chose que j'aurais voulu faire différemment, c'est changer de stratégie en cours de route, tu sais, parce qu'on avait convenu de ne rien toucher. On avait convenu de simplement laisser nos agents tourner.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visioconférence (aucun éditeur, terminal ou outil technique affiché).

**Contenu textuel & Code** : Aucun code, terminal ou données affichés à l'écran.

**Action / Démonstration** : Discussion en visioconférence entre les intervenants.

---

### ⏱️ `[00:15:42 - 00:16:11]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais avec tout ce qui se passait dans l'économie, avec les annonces majeures de l'actualité, tout ce que je pouvais faire, c'était de rester assis et d'espérer que les agents soient assez intelligents pour faire leurs recherches et changer de stratégie. Mais il y a probablement certaines choses sur lesquelles j'aurais peut-être voulu lui dire d'apporter quelques ajustements. C'est donc un peu la seule différence que j'aurais faite à ce stade, étant donné que ce n'était que 30 jours. Et sur ces 30 jours, vous savez, seulement cinq jours sur sept étaient des jours de trading. D'accord, donc pour conclure ici, il y a deux autres choses que je pensais que nous devrions faire. La première, c'est : combien de trades au total votre agent a-t-il effectués au cours du mois passé ?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUN

**Action / Démonstration** : AUCUNE

---

### ⏱️ `[00:16:11 - 00:16:45]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le mien a fait 61 transactions au total, 33 achats et 28 ventes. D'accord. Intéressant. Le mien a fait 20 achats d'affilée et 16 ventes. Mais dans mon vrai compte Alpaca, il y avait 116 ordres parce qu'il faisait des ordres stop-loss. Donc c'est plutôt similaire, tu vois, en ce qui concerne la fréquence de nos transactions. Mais au début, je pensais que tu viendrais en disant, hé, j'ai fait genre 200 transactions. Je pensais que tu ferais un truc important, genre du day trading, du swing trading, mais on dirait que tu n'as pas vraiment adopté cette approche. Je le ferais, mais je me rappelle que je lisais ceci, et c'est peut-être une limitation que les gens devraient connaître s'ils utilisent

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUNE

**Action / Démonstration** : AUCUNE

---

### ⏱️ `[00:16:45 - 00:17:09]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Alpaca, si tu n'as pas un certain niveau ou certains prérequis, ils bloquent le nombre de transactions que tu peux faire. Oh, d'accord. C'est logique. Ouais. Je me souviens que mon bot essayait de faire ça un jour et puis il a été bloqué. C'est juste genre : d'accord, laisse-moi réajuster ma stratégie. Intéressant. D'accord. Et la deuxième chose sur laquelle je suis curieux, c'est juste pour terminer la vidéo, j'ai demandé à mon bot, sachant ce qu'il sait maintenant, et s'il pouvait donner un conseil à quelqu'un, s'il essayait de mettre en place quelque chose comme ça : que ferais-tu différemment ? Ou qu'est-ce que tu leur dirais ?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUNE

**Action / Démonstration** : AUCUNE

---

### ⏱️ `[00:17:10 - 00:17:33]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Voici ce que le mien a dit. Je vais vous lire le court extrait. Ça disait : misez tout sur l'énergie dès le premier jour, utilisez des trailing stops de 10 % au lieu de 2 % et ne touchez jamais aux options à court terme. Un seul mauvais trade d'options nous a coûté 550 dollars. Et sans lui, nous aurions terminé à plus 5,3 dans le vert et nous aurions écrasé le S&P et le bot de trading de Salman. C'est donc concrètement ce qui nous a empêchés d'être dans le vert, apparemment. C'est super intéressant. Donc le mien était basiquement une copie de ces politiciens.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface graphique personnalisée / macOS style window

**Contenu textuel & Code** : Texte affiché : "1. Go all-in on energy from day one" et "2. Use 10% trailing stops instead of 2%".

**Action / Démonstration** : Affichage des conseils donnés par le bot IA à l'écran sous forme de blocs de texte stylisés.

![Capture d'écran montrant une interface graphique avec le titre "AI BOT ADVICE" et deux blocs de texte numérotés contenant des conseils financiers du bot.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001715_seg38.jpg)
*⏱️ 00:17:15 — Capture d'écran montrant une interface graphique avec le titre "AI BOT ADVICE" et deux blocs de texte numérotés contenant des conseils financiers du bot.*

---

### ⏱️ `[00:17:33 - 00:18:08]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Il a trouvé ce truc appelé Capital Trades, et il a vu que quelqu'un comme McCall a récemment surperformé le S&P, tout le monde, de genre plusieurs, plusieurs pour cent. Donc ce serait plutôt intéressant à faire. Mais à part ça, je pense que si je devais refaire ça, j'utiliserais une stratégie dont je sais qu'elle fonctionne vraiment bien. Et je me suis rendu compte, parce que je viens d'obtenir mon autorisation pour les options, qu'il existe ce truc appelé la « wheel strategy », où s'il y a une action que tu aimes pour toujours, disons que tu veux qu'elle monte, alors tu peux utiliser les options pour continuer à faire du « wheeling ». Donc, en gros, tu ne perds jamais vraiment tant d'argent que ça. Alors je pourrais essayer ça. Intéressant. J'ai d'ailleurs fait une vidéo sur la façon dont j'implémenterais

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de suivi boursier et diagramme explicatif de stratégie d'options.

**Contenu textuel & Code** : Graphiques de performance financière, statistiques de trading (McCaul 90-day +14.2%, S&P 500 +4.8%) et termes boursiers (Stock GOOGL, Sell Put, Roll put options).

**Action / Démonstration** : Présentation des données de performance de trading de Capital Trades et explication d'une stratégie sur les options d'actions.

![Capture d'écran montrant un graphique financier des performances boursières (« McCaul disclosed trades » comparé au S&P 500) avec une vue en incrustation de l'intervenant en bas à droite.](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001742_seg39.jpg)
*⏱️ 00:17:42 — Capture d'écran montrant un graphique financier des performances boursières (« McCaul disclosed trades » comparé au S&P 500) avec une vue en incrustation de l'intervenant en bas à droite.*

![Schéma conceptuel sur fond noir illustrant une stratégie d'investissement (« Stock GOOGL », « Sell Put », « Roll put options »).](../screenshots/eu8UJtuIi-E/eu8UJtuIi-E_001759_seg39.jpg)
*⏱️ 00:17:59 — Schéma conceptuel sur fond noir illustrant une stratégie d'investissement (« Stock GOOGL », « Sell Put », « Roll put options »).*

---

### ⏱️ `[00:18:08 - 00:18:33]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> cette stratégie exacte de roue et comment fabriquer ces robots de copy trading pour les politiciens avec Claude. Donc ce sera peut-être une vidéo amusante à regarder aussi. Génial. Ouais. Eh bien, je mettrai certainement un lien vers celle-ci dans la description de la vidéo. Très bien. Donc la dernière chose concernait le véritable défi pour vous les gars pour cette vidéo. Donc vous avez vu maintenant comment vous pouvez participer en commentant cette vidéo. Et dans environ une semaine, nous ferons un suivi et publierons sur nos deux communautés qui a gagné les 100 dollars et ensuite nous entrerons en contact avec vous et vous enverrons la récompense. La voilà, juste là.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUN

**Action / Démonstration** : AUCUNE

---

### ⏱️ `[00:18:33 - 00:18:55]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Les 100 dollars de Sammon iront à l'un d'entre vous. Génial, les gars. Non, Nate, c'était un défi vraiment très sympa. Je suis vraiment curieux de voir comment tout cela va se comporter avec le temps. Et oui, continuons sur cette lancée. Absolument. Ouais, je vais réactiver tous les cron jobs pour Bull, mon bot de trading, et on va continuer comme ça. J'espère qu'on se reverra dans quelques mois. Et merci à tous d'être restés jusqu'au bout. Si vous avez apprécié ou si vous avez appris quelque chose de nouveau, n'hésitez pas à laisser un like et on se retrouve dans la prochaine.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : AUCUNE

**Contenu textuel & Code** : AUCUN

**Action / Démonstration** : AUCUNE

---

