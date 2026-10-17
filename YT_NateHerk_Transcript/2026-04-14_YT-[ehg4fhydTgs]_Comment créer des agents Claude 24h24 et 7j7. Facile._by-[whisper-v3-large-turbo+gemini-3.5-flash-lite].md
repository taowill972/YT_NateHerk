# 🎬 How to Build 24/7 Claude Agents. Easy.

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=ehg4fhydTgs](https://www.youtube.com/watch?v=ehg4fhydTgs)  
> **Date de publication** : 20260414  
> **Durée** : 00:16:27  
> **Identifiant vidéo** : `ehg4fhydTgs`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
La vidéo de la chaîne Nate Herk | AI Automation explore l'arrivée tant attendue des routines au sein de Claude Code, permettant d'exécuter des agents IA autonomes 24h/24 et 7j/7 directement sur l'infrastructure Web d'Anthropic. Cette avancée majeure libère les développeurs des contraintes locales, rendant superflue l'obligation de laisser un ordinateur portable ouvert pour faire tourner des automatisations. Qu'elles soient déclenchées par un calendrier (via des tâches programmées), des webhooks ou des appels API, ces routines distantes s'exécutent de manière autonome dans un environnement cloud éphémère.

L'analyse technique menée par Nate Herk met toutefois en lumière plusieurs pièges pratiques indispensables à maîtriser pour réussir la migration de scripts locaux vers le web. Entre la gestion des secrets (absents des dépôts GitHub pour des raisons de sécurité), les configurations des environnements cloud, et les restrictions inhérentes à l'exécution sans état (stateless), la vidéo décortique trois cas d'usage concrets : l'envoi de messages via l'API ClickUp, l'analyse de commentaires via l'API YouTube, et les limites des automatisations basées sur des navigateurs (Playwright) nécessitant des sessions locales persistantes.

Loin d'un simple tutoriel théorique, ce retour d'expérience offre une feuille de route pragmatique pour concevoir des prompts robustes et uniques, capables de s'exécuter sans intervention humaine. Les démonstrations prouvent qu'avec les bons ajustements de variables d'environnement et de niveaux d'accès réseau, les agents Claude distants deviennent des rouages extrêmement fiables pour industrialiser des flux de travail complexes.

### 🛠️ Outils, Modèles & Logiciels Présentés
* **Claude Code** : L'interface de développement et d'automatisation d'Anthropic qui introduit les routines web pour exécuter des agents de manière asynchrone et distante.
* **Anthropic Web Infrastructure** : L'infrastructure cloud distante et sécurisée sur laquelle s'exécutent les routines sans nécessiter de ressource matérielle locale.
* **Opus 5.5** : Le modèle de pointe d'Anthropic (mentionné dans le contexte de la version) utilisé pour alimenter le raisonnement et l'exécution des tâches automatisées.
* **GitHub** : La plateforme de gestion de code source utilisée pour cloner et synchroniser les dépôts nécessaires à l'exécution distante des routines.
* **ClickUp** : L'outil de gestion de projet et de tâches utilisé dans les tests pour valider les intégrations d'API et l'envoi de messages automatisés.
* **YouTube Data API** : L'interface de programmation exploitée pour récupérer et analyser les commentaires récents des vidéos de manière automatisée.
* **Playwright CLI** : L'outil d'automatisation de navigateur mentionné pour souligner les limites des exécutions distantes sans état (absence de cookies et de sessions locales).

### 🔑 Points Clés & Enseignements Stratégiques
* **Affranchissement du matériel local** : L'introduction des routines web permet d'exécuter des agents Claude 24h/24 et 7j/7 sur l'infrastructure d'Anthropic, éliminant la nécessité de maintenir un ordinateur allumé.
* **Diversité des déclencheurs** : Les routines peuvent être lancées selon un calendrier précis (cadence horaire ou quotidienne), par des appels API ou en réaction à des événements (comme des webhooks GitHub).
* **Architecture sans état (Stateless)** : Chaque exécution distante clone temporairement un dépôt GitHub, effectue la tâche, puis détruit l'environnement, exigeant une conception robuste sans dépendance persistante locale.
* **Gestion sécurisée des secrets** : Les fichiers `.env` contenant les clés API étant ignorés par Git (`.gitignore`), les identifiants doivent impérativement être injectés via les variables d'environnement de l'environnement cloud.
* **Niveaux d'accès réseau et sécurité** : Par défaut en mode "de confiance" (restreint aux sources vérifiées d'Anthropic), l'environnement cloud doit parfois être basculé en mode "complet" pour autoriser les requêtes vers des API externes tierces.
* **Conception de prompts autonomes** : Puisque les routines sont conçues pour fonctionner en un seul prompt sans interaction humaine, les instructions doivent être extrêmement précises pour éviter que l'agent ne s'arrête en posant des questions.
* **Contournement des confusions de fichiers** : Il est recommandé de spécifier explicitement à l'agent d'utiliser les variables d'environnement cloud plutôt que de chercher un fichier `.env` inexistant dans le dépôt distant.
* **Limitations des automatisations par navigateur** : Les scripts dépendant de sessions locales, de cookies ou de navigateurs (comme Playwright) échouent en mode distant, car l'environnement cloud ne possède pas l'historique d'authentification de l'utilisateur.
* **Gestion des modifications de code** : Si une routine modifie activement la base de code ou effectue une revue, elle préserve le résultat en créant une nouvelle branche au lieu de tout supprimer.
* **Cadence minimale des tâches** : La fréquence de planification est limitée à un minimum d'une fois par heure pour les tâches programmées, ce qui reste largement suffisant pour la majorité des automatisations de productivité.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:34]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Cloud Code nous a enfin apporté des routines, ce qui signifie fondamentalement que vous pouvez injecter un prompt dans Cloud Code, mais il peut s'exécuter sur le Web, de sorte que votre ordinateur portable n'a pas besoin de rester ouvert. Et je suis tellement enthousiaste à ce sujet. J'ai déjà commencé à l'essayer. J'ai migré mes automatisations là-bas, mais il y a beaucoup de petits pièges, alors je suis ici pour vous expliquer exactement comment vous pouvez réellement configurer ces automatisations pour qu'elles fonctionnent. Donc aujourd'hui, le 14 avril, Cloud a tweeté, désormais en version préliminaire de recherche, les routines dans Cloud Code. Vous configurez une routine une seule fois, ce qui ressemble fondamentalement à un prompt, et elle peut s'exécuter selon un calendrier, à partir d'un appel API ou en réponse à un événement, et elle s'exécute sur l'infrastructure Web d'Anthropic. C'est donc génial. Vous pouvez donc appeler une routine à partir d'une API. Vous pouvez

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant X (Twitter)

**Contenu textuel & Code** : Publication de Claude : "Now in research preview: routines in Claude Code. Configure a routine once (a prompt, a repo, and your connectors), and it can run on a schedule, from an API call, or in response to an event."

**Action / Démonstration** : Présentation visuelle de l'annonce officielle des routines par le présentateur.

![Capture d'écran montrant un tweet officiel du compte @claudeai sur X (Twitter) annonçant les nouvelles routines dans Claude Code, avec le présentateur en médaillon dans le coin inférieur droit.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000009_seg1.jpg)
*⏱️ 00:00:09 — Capture d'écran montrant un tweet officiel du compte @claudeai sur X (Twitter) annonçant les nouvelles routines dans Claude Code, avec le présentateur en médaillon dans le coin inférieur droit.*

---

### ⏱️ `[00:00:34 - 00:01:07]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> déclencher par des événements GitHub, ou ils peuvent être programmés, ce qui ressemble aux automatisations programmées que nous avons déjà, mais maintenant ils s'exécutent sur le Web. Vous pouvez donc vraiment les créer à partir de n'importe où. Vous pouvez le faire ici même sous forme de déclencheur programmé pour exécuter des agents distants programmés, ce qui se trouve dans le terminal. Vous pourriez aussi aller sur clawed AI slash code. Vous pourriez donc le faire sur le Web. Et ici même, vous voyez, j'ai trois routines basées sur le Web ici même. Ou ce que je vais vous montrer aujourd'hui, c'est simplement de le faire dans l'application de bureau. Parce qu'ici même, si je vais dans mes tâches programmées, vous pouvez voir que j'en ai quelques-unes comme ces quatre qui sont locales. Et ensuite, j'ai ces quatre qui s'exécutent à l'intérieur d'un dépôt GitHub. Ce sont donc les distantes. Si je vais ici en haut et que je clique sur

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code, Claude Code v2.1.107 (CLI)

**Contenu textuel & Code** : Commande en cours de saisie '/sche' avec autocomplétion suggérant '/schedule' pour créer, mettre à jour ou exécuter des agents distants planifiés.

**Action / Démonstration** : Le présentateur tape une commande dans l'interface de ligne de commande Claude Code intégrée à l'éditeur pour planifier des agents.

![Interface de Visual Studio Code affichant un terminal intégré avec Claude Code et la saisie de la commande '/schedule'.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000042_seg2.jpg)
*⏱️ 00:00:42 — Interface de Visual Studio Code affichant un terminal intégré avec Claude Code et la saisie de la commande '/schedule'.*

---

### ⏱️ `[00:01:07 - 00:01:39]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> nouvelle tâche, c'est ici que nous pourrions configurer une nouvelle tâche locale ou une nouvelle tâche distante. C'est très similaire. Vous définissez le nom, vous définissez ce que Cloud doit faire, et voici le prompt réel. J'en parlerai donc plus en détail dans un instant, mais ensuite vous configureriez votre modèle, votre dépôt et votre environnement cloud. Vous définissez la cadence, horaire, quotidienne, les jours de semaine. Je crois que le minimum est d'une fois par heure. Genre, vous ne pourriez pas faire toutes les 10 minutes ou quelque chose comme ça, mais ce n'est quand même pas mal du tout. C'est ici que vous pourriez configurer tous vos connecteurs. Donc, si vous avez besoin de connecter Slack ou Gmail ou, vous savez, peu importe ce que c'est, vous pouvez les connecter juste ici, mais vous pouvez aussi tout simplement utiliser votre API classique

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application de gestion de tâches IA (interface web)

**Contenu textuel & Code** : Formulaire de création "New remote task" avec champs de saisie pour le nom (ex: Daily code review), la description des actions de Claude, sélection du modèle (Opus 4.6), du dépôt GitHub et options de planification (Hourly, Daily, Weekdays, Weekly, Custom).

**Action / Démonstration** : Configuration d'une nouvelle tâche planifiée distante pour l'assistant IA.

![Interface de configuration affichant une fenêtre modale pour créer une nouvelle tâche distante avec des champs pour le nom, la description du prompt, le choix du dépôt Git et la planification temporelle.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000115_seg3.jpg)
*⏱️ 00:01:15 — Interface de configuration affichant une fenêtre modale pour créer une nouvelle tâche distante avec des champs pour le nom, la description du prompt, le choix du dépôt Git et la planification temporelle.*

---

### ⏱️ `[00:01:39 - 00:02:12]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> des points de terminaison avec vos clés API. Et puis bien sûr, vous avez vos permissions. Vous pouvez donc choisir la manière dont Claude doit se comporter. Maintenant, une chose à propos de ceux-ci, c'est qu'ils sont conçus pour être un prompt unique. Vous n'êtes pas là. Vous voulez donc probablement vous assurer qu'il ne doit jamais s'arrêter et vous poser des questions. Sinon, à quoi bon l'automatisation ? Donc, comme je l'ai dit, il y a des tonnes de choses à explorer ici et je ne vais pas essayer de vous ennuyer, mais certaines de ces choses sont vraiment importantes car lorsque j'ai fait cette configuration pour la première fois, mes automatisations ne se sont pas simplement migrées pour fonctionner. Je vais donc vous dire les problèmes que j'ai rencontrés et, espérons-le, répondre à tout ce que vous avez besoin de savoir pour n'avoir pas à aller dans les commentaires et poser ces questions courantes

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application web de gestion de tâches distantes et Google Docs.

**Contenu textuel & Code** : Formulaire de création de tâche distante et plan de cours textuel sur les routines Claude Code.

**Action / Démonstration** : Configuration des paramètres de planification et des permissions d'accès pour les routines automatisées de l'assistant.

![Interface de configuration d'une tâche distante (New remote task) montrant les options de planification, le choix du dépôt et les permissions de Claude.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000147_seg4.jpg)
*⏱️ 00:01:47 — Interface de configuration d'une tâche distante (New remote task) montrant les options de planification, le choix du dépôt et les permissions de Claude.*

![Document de référence Google Docs intitulé « Claude Code Routines » présentant le plan du cours avec des sections comme What It Is, How It Works, CLAUDE.md et Connectors.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000204_seg4.jpg)
*⏱️ 00:02:04 — Document de référence Google Docs intitulé « Claude Code Routines » présentant le plan du cours avec des sections comme What It Is, How It Works, CLAUDE.md et Connectors.*

---

### ⏱️ `[00:02:12 - 00:02:32]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> des questions. Je peux simplement y répondre directement ici pour vous. Donc, laissez-moi juste, tout d'abord, très rapidement, vous montrer ce que j'ai testé. La première chose que je voulais tester, c'est si je venais ici et que je créais une nouvelle routine juste pour envoyer un message à mon ClickUp. Évidemment, ça n'a aucune valeur, mais je voulais juste voir comment ça fonctionnait. Parce que ce que je voulais faire, c'est voir si je pouvais faire cela sans ajouter mon connecteur ClickUp.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'application d'IA / automatisation de tâches planifiées (avec un panneau latéral comprenant New session, Search, Scheduled, Dispatch, Customize, et un mode Code sélectionné en haut).

**Contenu textuel & Code** : Liste de tâches planifiées : "Skool wins engagement", "AI news roundup", "Notification responses", "Youtube comment replies", "Testing Skool Wins", "Testing YT Comments", "Testing ClickUp API", ainsi que des tâches prévues pour aujourd'hui dans le panneau de gauche.

**Action / Démonstration** : Navigation et présentation des différentes routines et tâches automatisées configurées dans l'application.

![Interface d'une application d'automatisation montrant l'onglet des tâches planifiées (Scheduled) avec plusieurs routines et le présentateur en médaillon.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000217_seg5.jpg)
*⏱️ 00:02:17 — Interface d'une application d'automatisation montrant l'onglet des tâches planifiées (Scheduled) avec plusieurs routines et le présentateur en médaillon.*

---

### ⏱️ `[00:02:32 - 00:02:54]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et j'ai réellement réussi à lancer ça, mais ça n'a pas fonctionné tout de suite. Laissez-moi donc vous montrer ce à quoi j'ai été confronté. La façon dont cela fonctionne, c'est que vous avez besoin d'un dépôt GitHub pour y synchroniser le tout afin que cela puisse réellement s'exécuter. Ça va donc cloner mon projet Herc2 juste ici sur le web. Ça va être capable de lire mon fichier cloud.md. Ça va être capable de lire mes scripts et mes compétences. Et ensuite, une fois qu'il a terminé le travail, il détruit pour ainsi dire simplement ce petit clone GitHub dans le cloud.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'automatisation (avec panneau latéral listant des projets et tâches planifiées comme 'Skool wins engagement', 'Notification responses', etc.) et une webcam incrustée du présentateur en bas à droite.

**Contenu textuel & Code** : Nom de la tâche 'Testing ClickUp API', statut 'Active', dépôt GitHub associé 'nateherkai/Herk-2.0', instructions d'automatisation, répétition quotidienne à 9:00 AM CDT, et historique des exécutions ('Runs').

**Action / Démonstration** : Affichage des détails d'une tâche planifiée connectée à un dépôt GitHub pour illustrer la configuration et l'historique des exécutions (bouton 'Run now' visible).

![Interface d'une application montrant une tâche planifiée intitulée 'Testing ClickUp API' avec les détails du dépôt GitHub et l'historique des exécutions.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000238_seg6.jpg)
*⏱️ 00:02:38 — Interface d'une application montrant une tâche planifiée intitulée 'Testing ClickUp API' avec les détails du dépôt GitHub et l'historique des exécutions.*

---

### ⏱️ `[00:02:54 - 00:03:13]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais comme vous le savez, vous ne poussez pas vos secrets dans GitHub. Parce que si vous voyez ici, mon projet Herc2, c'est mon fichier .env avec toutes mes clés d'API. Et il est répertorié dans le gitignore, ce qui signifie essentiellement, hé, quand vous poussez vers GitHub, vous n'incluez pas ces fichiers. Donc ce que cela signifie, c'est qu'ici, si cela regarde seulement votre dépôt GitHub, il n'y a pas de .env.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code, Explorateur de fichiers, Terminal intégré, Claude Code CLI.

**Contenu textuel & Code** : Arborescence du projet Herk-2 avec les dossiers et fichiers (notamment .env et .gitignore), et l'interface de Claude Code affichant des commandes slash (/schedule, /claude-api, etc.).

**Action / Démonstration** : Navigation dans l'explorateur de fichiers de l'éditeur et utilisation du terminal Claude Code.

![Capture d'écran de l'interface de Visual Studio Code montrant l'explorateur de fichiers à gauche et un terminal intégré exécutant l'interface en ligne de commande de Claude Code. Le présentateur apparaît dans une petite fenêtre vidéo incrustée en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000259_seg7.jpg)
*⏱️ 00:02:59 — Capture d'écran de l'interface de Visual Studio Code montrant l'explorateur de fichiers à gauche et un terminal intégré exécutant l'interface en ligne de commande de Claude Code. Le présentateur apparaît dans une petite fenêtre vidéo incrustée en bas à droite.*

---

### ⏱️ `[00:03:14 - 00:03:33]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Alors, comment intégrez-vous vos clés API dans cette routine qui s'exécute sur le web ? Eh bien, ce que vous faites, c'est qu'à l'intérieur de cette tâche planifiée, vous avez un environnement cloud. Donc si je clique sur celui-ci, vous pouvez voir que celui-ci s'appelle NateHurt Cloud. Donc si j'ouvre les paramètres, qu'est-ce que vous voyez ? Vous avez le nom de cet environnement cloud, vous avez l'accès au réseau et vous avez des variables d'environnement.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de tâches planifiées (type outil d'automatisation IA avec Claude).

**Contenu textuel & Code** : Titre de la tâche : 'Testing ClickUp API', instructions : 'Send a message in the internal automations channel in my ClickUp...', et environnement 'Nate Herk Cloud'.

**Action / Démonstration** : Présentation de la configuration d'une tâche planifiée et sélection de l'environnement cloud contenant les clés API.

![Interface web montrant les détails d'une tâche planifiée nommée 'Testing ClickUp API' avec ses instructions et l'historique des exécutions.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000318_seg8.jpg)
*⏱️ 00:03:18 — Interface web montrant les détails d'une tâche planifiée nommée 'Testing ClickUp API' avec ses instructions et l'historique des exécutions.*

![Fenêtre modale d'édition de la tâche planifiée affichant le paramètre d'environnement cloud 'Nate Herk Cloud'.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000323_seg8.jpg)
*⏱️ 00:03:23 — Fenêtre modale d'édition de la tâche planifiée affichant le paramètre d'environnement cloud 'Nate Herk Cloud'.*

---

### ⏱️ `[00:03:33 - 00:03:54]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc juste ici, c'est là que je mets ma clé API YouTube, ma clé API ClickUp, toutes les autres clés API auxquelles je dois donner accès à cet environnement cloud. Et puis l'autre chose que vous devez faire, c'est que vous devez regarder les niveaux d'accès, car juste ici, vous pouvez voir que celui-ci est sur complet, mais par défaut, celui-ci sera sur de confiance, je crois. Et cela signifie que vous pouvez uniquement télécharger des paquets provenant de sources vérifiées d'Anthropic.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de configuration de l'environnement cloud (Claude Code / interface de gestion d'agent).

**Contenu textuel & Code** : Champs de configuration : nom "Nate Herk Cloud", accès réseau défini sur "Full", section des variables d'environnement masquées, et script de configuration (Setup script).

**Action / Démonstration** : Le présentateur explique comment configurer les clés API et les niveaux d'accès pour l'environnement cloud.

![Fenêtre modale de configuration des paramètres du cloud affichant les variables d'environnement et les niveaux d'accès réseau, avec le présentateur en médaillon dans le coin inférieur droit.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000338_seg9.jpg)
*⏱️ 00:03:38 — Fenêtre modale de configuration des paramètres du cloud affichant les variables d'environnement et les niveaux d'accès réseau, avec le présentateur en médaillon dans le coin inférieur droit.*

---

### ⏱️ `[00:03:55 - 00:04:15]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et quand nous en reparlerons plus tard, j'aurai un lien que vous pourrez consulter pour tous les voir. Vous pouvez même en faire un personnalisé si vous voulez autoriser des domaines spécifiques qui ne sont pas sur cette liste. Mais pour que ClickUp fonctionne dans ce cas-ci, j'ai dû passer en mode complet, car lorsque j'étais en mode approuvé, il m'a dit, hé, nous ne pouvons pas vraiment faire ça. Mais lorsque j'ai changé cela pour complet, cela m'a permis d'envoyer un message à mon ClickUp. Et c'est comme ça que j'ai obtenu ce message ici même qui dit simplement je teste que les tâches distantes fonctionnent et que les identifiants fonctionnent.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de configuration d'environnement cloud (type plateforme de développement ou assistant IA).

**Contenu textuel & Code** : Paramètre 'Network access' avec les options : None (Blocks Internet access for maximum security), Trusted (Downloads packages from verified sources), Full (Unrestricted Internet access for maximum flexibility), et Custom (Create a list of allowed domains).

**Action / Démonstration** : Le curseur sélectionne l'option 'Custom' dans le menu déroulant du réseau.

![Fenêtre modale de configuration 'Update cloud environment' affichant les options de contrôle d'accès réseau avec le menu déroulant ouvert listant None, Trusted, Full et Custom.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000400_seg10.jpg)
*⏱️ 00:04:00 — Fenêtre modale de configuration 'Update cloud environment' affichant les options de contrôle d'accès réseau avec le menu déroulant ouvert listant None, Trusted, Full et Custom.*

---

### ⏱️ `[00:04:15 - 00:04:40]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc en gros, quand ceux-ci s'exécutent, tout ce que vous avez ici comme instructions est ce qui sert de prompt. Et c'est exactement de la même manière que fonctionnent les tâches planifiées localement. Donc juste ici, vous pouvez voir que je dis, envoyer un message dans le canal ClickUp interne. Et juste ici, la chose exacte qu'il est dit était envoyer un message dans le canal ClickUp interne. Donc pensez à une tâche planifiée ou à une routine comme si vous tapiez essentiellement un prompt et que quelqu'un venait ensuite sur votre ordinateur portable et le tapait pour vous.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'automatisation ou tableau de bord d'agent IA

**Contenu textuel & Code** : Titre 'Testing ClickUp API', instruction 'Send a message in the Internal automations channel...', et l'historique des exécutions ('Runs').

**Action / Démonstration** : Navigation et présentation de la configuration d'une tâche planifiée connectée à l'API ClickUp.

![Capture d'écran montrant l'interface d'une application de gestion de tâches planifiées avec les détails d'une tâche intitulée 'Testing ClickUp API' incluant le dépôt associé, la récurrence quotidienne et les instructions textuelles.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000421_seg11.jpg)
*⏱️ 00:04:21 — Capture d'écran montrant l'interface d'une application de gestion de tâches planifiées avec les détails d'une tâche intitulée 'Testing ClickUp API' incluant le dépôt associé, la récurrence quotidienne et les instructions textuelles.*

---

### ⏱️ `[00:04:40 - 00:05:00]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> C'est donc exactement le même type d'interaction que lorsque vous parlez à Claude Code. Mais c'est pourquoi, encore une fois, vous voulez vous assurer que c'est assez précis pour qu'il puisse essentiellement le faire du premier coup. Bon, alors creusons un peu plus maintenant. Ce que j'ai essayé de faire, c'est d'en faire un autre, avec lequel je voulais qu'il soit capable d'utiliser l'API de données YouTube afin de récupérer des commentaires YouTube pour moi et de me donner une petite analyse dans, vous savez, ClickUp ou autre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'agent IA / application de développement

**Contenu textuel & Code** : Prompt utilisateur : "Send a message in the internal automations channel in my ClickUp that says..." et logs de l'agent cherchant les outils et envoyant le message avec succès.

**Action / Démonstration** : L'agent IA exécute la recherche de l'ID du canal ClickUp et envoie un message de test.

![Interface d'une application d'agent IA montrant une conversation de test avec ClickUp, avec le présentateur en médaillon vidéo en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000445_seg12.jpg)
*⏱️ 00:04:45 — Interface d'une application d'agent IA montrant une conversation de test avec ClickUp, avec le présentateur en médaillon vidéo en bas à droite.*

---

### ⏱️ `[00:05:01 - 00:05:22]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc voici le prompt que j'ai dit, n'est-ce pas ? Analyse 50 de mes commentaires les plus récents sur YouTube et donne-moi un bref récapitulatif sous forme de liste à puces. Ma clé API YouTube est disponible en tant que variable d'environnement. Utilise-la directement depuis l'environnement. Ne cherche pas de fichier .env. Parce que ce qui se passe, c'est que dans ton dépôt, n'est-ce pas ? Donc dans ce projet Herc2, quand je lance normalement ceci, il récupère toutes mes clés API à partir du .env.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application web (type interface de gestion de tâches/agent IA avec onglets Chat, Cowork, Code).

**Contenu textuel & Code** : Prompt affiché : "Analyze 50 of my most recent comments from YouTube and give me a quick three to five bullet point rundown. My YouTube API key is available as the environment variable YOUTUBE_API_KEY..."

**Action / Démonstration** : Visualisation du prompt planifié ("Testing YT Comments") avec une option de répétition quotidienne et un bouton "Run now".

![Interface d'une application de gestion de tâches ou d'agent IA montrant le prompt configuré pour analyser les commentaires YouTube.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000506_seg13.jpg)
*⏱️ 00:05:06 — Interface d'une application de gestion de tâches ou d'agent IA montrant le prompt configuré pour analyser les commentaires YouTube.*

---

### ⏱️ `[00:05:22 - 00:05:40]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et peut-être qu'il lit le cloud.md et réalise que c'est là que beaucoup d'entre eux résident. Donc par défaut, il va peut-être essayer de regarder dans le .env et il ne sera pas assez intelligent pour comprendre. Et donc pour ClickUp, ça allait, il l'a compris. Mais pour une raison quelconque avec celui de YouTube, il ne l'a pas fait. J'ai donc dû lui dire explicitement, hé, regarde dans la variable d'environnement plutôt que dans le .env.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code, Claude Code CLI (v2.1.107)

**Contenu textuel & Code** : Explorateur de fichiers montrant notamment `.env`, `CLAUDE.md`, et la liste des commandes de Claude Code avec `/schedule` sélectionné.

**Action / Démonstration** : Saisie d'une commande dans l'interface de Claude Code à l'intérieur de l'éditeur.

![Interface de Visual Studio Code avec le terminal intégré affichant l'outil Claude Code et le panneau latéral de l'explorateur de fichiers.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000527_seg14.jpg)
*⏱️ 00:05:27 — Interface de Visual Studio Code avec le terminal intégré affichant l'outil Claude Code et le panneau latéral de l'explorateur de fichiers.*

---

### ⏱️ `[00:05:40 - 00:06:00]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc vous pouvez voir que la première fois que je l'ai exécuté, à 12 h 41, je n'ai pas dit ça et il n'a pas pu le faire. Il a dit du genre, hé, je ne trouve pas ça, j'obtiens une erreur. Et j'ai même essayé de le lui dire ici et cela n'a toujours pas fonctionné. Mais ensuite, lors de cette toute dernière exécution, quand j'ai mis un peu à jour le prompt, il a pu le récupérer tout de suite en utilisant la clé API. Et maintenant j'ai une routine à distance qui fonctionnerait.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'agent IA avec panneau latéral de navigation et zone de chat.

**Contenu textuel & Code** : Historique d'exécution (« Testing YT Comments » run) avec des messages textuels : « API is returning 403 errors », « No YouTube API key in .env », « Good - I have cached comments from 4 recent videos », et un message de l'utilisateur : « I put my keys that you need to get YouTube data in the Claude environment variables. Look there. »

**Action / Démonstration** : Exécution d'un agent IA analysant des commentaires YouTube, passant d'une erreur d'authentification API à l'utilisation de données mises en cache et à la prise en compte des instructions de l'utilisateur.

![Interface d'une application d'agent IA montrant l'historique d'exécution d'un script d'analyse de commentaires YouTube avec des messages d'erreur API, l'utilisation de données en cache et un prompt utilisateur.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000545_seg15.jpg)
*⏱️ 00:05:45 — Interface d'une application d'agent IA montrant l'historique d'exécution d'un script d'analyse de commentaires YouTube avec des messages d'erreur API, l'utilisation de données en cache et un prompt utilisateur.*

---

### ⏱️ `[00:06:00 - 00:06:34]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Évidemment, je dois mettre ça à jour. Je vais migrer mes autres automatisations, mais c'était juste à des fins de test. Et puis une autre chose que je fais, c'est que j'ai quelques automatisations ici, qui ouvrent essentiellement un navigateur en utilisant Playwright CLI, et ça fait des trucs dans ma communauté School parce qu'il n'y a pas d'API accessible publiquement. On a en quelque sorte trouvé un moyen de l'automatiser sans utiliser de navigateur. Je ne vais pas vraiment entrer dans les détails pour l'instant. Mais ce que je voulais vous dire à ce sujet, c'est que j'ai essayé de transférer essentiellement cette automatisation, ou plutôt ce post d'engagement School wins, dans une session distante. J'ai donc copié exactement les mêmes prompts qui étaient dans ma tâche planifiée habituelle.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'automatisation / application de gestion de tâches.

**Contenu textuel & Code** : Cartes de tâches planifiées avec des horaires d'exécution (Skool wins engagement, AI news roundup, Notification responses, Youtube comment replies, etc.) et une barre latérale avec les options 'New session', 'Search', 'Scheduled', 'Dispatch'.

**Action / Démonstration** : Navigation dans le tableau de bord des tâches planifiées pour montrer les différentes automatisations configurées.

![Capture d'écran montrant l'interface d'une application d'automatisation avec un panneau de tâches planifiées (Scheduled), affichant différentes cartes d'automatisation (Skool wins engagement, AI news roundup, Youtube comment replies) et une incrustation vidéo du présentateur en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000608_seg16.jpg)
*⏱️ 00:06:08 — Capture d'écran montrant l'interface d'une application d'automatisation avec un panneau de tâches planifiées (Scheduled), affichant différentes cartes d'automatisation (Skool wins engagement, AI news roundup, Youtube comment replies) et une incrustation vidéo du présentateur en bas à droite.*

---

### ⏱️ `[00:06:34 - 00:07:06]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ensuite, j'ai juste ajouté ce petit extrait à la fin. Mais ce qui s'est passé, c'est que ça ne fonctionnait pas parce que ça disait en gros, hé, tu sais, comme quand tu fais ça, ça lance un navigateur, mais il n'y a pas de cookies parce que tout cela s'exécute à distance. Et tout ce que j'ai à regarder, c'est le dépôt GitHub. Je ne peux pas regarder les cookies locaux, tu sais, que nous avons utilisés lors des deux dernières sessions de cette automatisation. Et donc, il ne semble pas que cela fonctionnerait parce qu'encore une fois, ça n'a accès à rien de tout cela. Donc, si je voulais faire une automatisation comme celle-ci, je devrais utiliser un point de terminaison qui accepte une authentification sous forme de vrais cookies ou d'un en-tête ou, tu sais, comme une clé API.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application web d'assistant IA / plateforme d'automatisation (avec panneau latéral de projets et historique)

**Contenu textuel & Code** : "The scraper returned a session error -- no auth/skool_state.json found." et journaux d'exécution de l'agent.

**Action / Démonstration** : Exécution d'un agent IA testant un workflow d'automatisation et rencontrant une erreur d'authentification de session.

![Interface d'une application d'agent IA montrant l'exécution d'un workflow de scraping pour Skool, avec un message d'erreur concernant l'absence de fichier de session auth/skool_state.json.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000642_seg17.jpg)
*⏱️ 00:06:42 — Interface d'une application d'agent IA montrant l'exécution d'un workflow de scraping pour Skool, avec un message d'erreur concernant l'absence de fichier de session auth/skool_state.json.*

---

### ⏱️ `[00:07:06 - 00:07:42]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> parce que chacune de ces exécutions va être sans état. Et après l'exécution, le clone GitHub est tout simplement supprimé. Maintenant, l'exception à cela est si l'automatisation modifie quelque chose dans votre base de code ou effectue une révision. Si elle fait cela, elle va créer une nouvelle branche pour vous, ou elle va vous donner un certain type de résultat et pas seulement tout supprimer de ce qu'elle vient de faire. Mais pour une automatisation comme celle-ci, elle le supprimerait tout simplement. Mais j'espère qu'après que vous avez vu ces exemples, vous avez maintenant la capacité d'intervenir et, vous savez, d'apporter quelques modifications si nécessaire afin de vous assurer que vos automatisations s'exécutent. Et ce que je veux dire par là, c'est que vous comprenez que ce devrait être une instruction très spécifique. C'est ainsi que vous changez le modèle. Vous devez avoir un dépôt GitHub. Vous pouvez changer le

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'agent d'automatisation IA, mode « Code »

**Contenu textuel & Code** : Instructions d'exécution détaillées : changement de répertoire, exécution d'un script Python pour scraper des publications, analyse JSON et génération de commentaires personnalisés, avec un terminal intégré affichant une branche git (master -> claude/magical-carson-PQhwc).

**Action / Démonstration** : Initialisation d'une session et exécution de commandes pour automatiser le workflow d'engagement.

![Interface d'une application d'automatisation montrant une session de test en cours (« Testing Skool Wins ») avec des instructions textuelles et des commandes en cours d'exécution, ainsi qu'une petite fenêtre vidéo du présentateur en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000715_seg18.jpg)
*⏱️ 00:07:15 — Interface d'une application d'automatisation montrant une session de test en cours (« Testing Skool Wins ») avec des instructions textuelles et des commandes en cours d'exécution, ainsi qu'une petite fenêtre vidéo du présentateur en bas à droite.*

---

### ⏱️ `[00:07:42 - 00:08:11]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> paramètres pour vos environnements cloud juste ici. Vous définissez le calendrier, vous ajoutez tous les connecteurs dont vous pourriez avoir besoin, ce qui serait honnêtement un peu plus facile si vous ajoutiez juste un connecteur Slack, et ensuite vous pouvez définir vos permissions ici. Maintenant, l'autre chose à garder à l'esprit est que vous avez des limites. Donc, si je viens ici dans mes paramètres, vous pouvez voir que si je vais dans mon utilisation, nous avons nos limites de session régulières, nos limites de modèle, mais pour les fonctionnalités supplémentaires, nous avons des exécutions de routines quotidiennes incluses. Et je n'en ai encore exécuté aucune sur le calendrier réel. Je les ai juste testées, mais nous sommes à zéro sur 15.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application web Claude Code (Interface de gestion des routines et des tâches cloud).

**Contenu textuel & Code** : Paramètres de planification (Daily, 09:00 AM), gestion des connecteurs, et listes de routines automatisées (Testing Skool Wins, Testing YT Comments, Testing ClickUp API).

**Action / Démonstration** : Configuration des paramètres de planification et des connecteurs pour les environnements cloud automatisés de Claude Code.

![Interface de configuration d'une tâche planifiée dans l'application web Claude Code, avec les options de calendrier (Daily, Hourly, etc.) et la section pour ajouter des connecteurs.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000749_seg19.jpg)
*⏱️ 00:07:49 — Interface de configuration d'une tâche planifiée dans l'application web Claude Code, avec les options de calendrier (Daily, Hourly, etc.) et la section pour ajouter des connecteurs.*

![Tableau de bord principal de l'application web Claude Code affichant l'onglet 'Routhes' avec des cartes de routines programmées.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000756_seg19.jpg)
*⏱️ 00:07:56 — Tableau de bord principal de l'application web Claude Code affichant l'onglet 'Routhes' avec des cartes de routines programmées.*

---

### ⏱️ `[00:08:11 - 00:08:29]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je ne pourrais donc avoir que 15 automatisations exécutées avec des routines par jour parce que je suis sur le forfait maximum à 200 dollars par mois. Vos limites seraient moindres si vous êtes sur la version pro, je pense peut-être trois ou peut-être cinq. J'ai, j'ai cette information un peu plus tard, mais c'est juste quelque chose à garder à l'esprit. Très bien, alors plongeons un peu plus dans les détails ici qui pourraient répondre à certaines questions que vous vous posez.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web des paramètres de Claude (Usage).

**Contenu textuel & Code** : Barres de progression des limites d'utilisation (All models 24% used, Sonnet only 3% used, Daily included routine runs 0/15).

**Action / Démonstration** : Navigation dans les paramètres de la plateforme pour afficher les limites de routines quotidiennes.

![Capture d'écran montrant les paramètres d'utilisation de Claude avec les limites hebdomadaires, les fonctionnalités supplémentaires (Daily included routine runs 0/15) et l'utilisation supplémentaire.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000816_seg20.jpg)
*⏱️ 00:08:16 — Capture d'écran montrant les paramètres d'utilisation de Claude avec les limites hebdomadaires, les fonctionnalités supplémentaires (Daily included routine runs 0/15) et l'utilisation supplémentaire.*

---

### ⏱️ `[00:08:30 - 00:09:02]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je pense que c'est assez clair à ce stade de quoi il s'agit. Je vais vous donner ce document entier ainsi que tout le reste dont j'ai parlé dans ma communauté School gratuite. Le lien pour cela se trouve dans la description. Donc, certaines choses que je ne couvrirai peut-être pas, si vous voulez en lire davantage à ce sujet, alors allez simplement récupérer cette ressource gratuite. Donc, nous savons ce que c'est. Je pense que nous savons comment ça fonctionne, n'est-ce pas ? Comme vous définissez une routine qui est un prompt, vous connectez un dépôt GitHub, vous pouvez aussi le déclencher par des API ou par une action GitHub, et ensuite vous pouvez connecter vos connecteurs, et en gros, cela agit comme si vous parliez à votre propre code cloud en raison du fait que cela fonctionne à partir d'un dépôt cloné.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Document texte / Éditeur de documents

**Contenu textuel & Code** : Titre "Claude Code Routines", sections "What It Is", "Status", "How It Works", "CLAUDE.md Makes Routines Smart", "Three Trigger Types", "How This Compares to What Already Existed".

**Action / Démonstration** : Le présentateur explique et détaille le contenu du document partagé à l'écran.

![Un document texte structuré présenté à l'écran concernant "Claude Code Routines", avec le présentateur visible en incrustation vidéo en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000838_seg21.jpg)
*⏱️ 00:08:38 — Un document texte structuré présenté à l'écran concernant "Claude Code Routines", avec le présentateur visible en incrustation vidéo en bas à droite.*

---

### ⏱️ `[00:09:02 - 00:09:23]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Il va lire le fichier cloud.md automatiquement à chaque fois. Donc si vous avez un projet massif, comme un projet Herc2, par exemple, avec énormément de contexte et énormément de choses, peut-être que vous ne voulez pas mettre ce dépôt dans le cloud pour en faire une exécution de routine, parce qu'il y a beaucoup de contexte dans ce fichier Cloud.md et dans tout ce dépôt GitHub qui pourrait n'avoir aucune importance pour cette automatisation.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant une documentation ou un document Markdown.

**Contenu textuel & Code** : Titres : "What It Is", "How It Works", "CLAUDE.md Makes Routines Smart", "Three Trigger Types", "How This Compares to What Already Existed". Texte explicatif sur la façon dont les routines lisent automatiquement le fichier CLAUDE.md pour fournir du contexte (standards de codage, conventions, instructions).

**Action / Démonstration** : Présentation théorique et pédagogique du concept de fichier de contexte contextuel pour les agents IA.

![Une page de documentation technique expliquant le fonctionnement du fichier "CLAUDE.md" et son rôle dans l'automatisation de routines intelligentes, avec une vignette vidéo du présentateur en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000907_seg22.jpg)
*⏱️ 00:09:07 — Une page de documentation technique expliquant le fonctionnement du fichier "CLAUDE.md" et son rôle dans l'automatisation de routines intelligentes, avec une vignette vidéo du présentateur en bas à droite.*

---

### ⏱️ `[00:09:23 - 00:09:42]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc peut-être qu'il vaut mieux configurer un dépôt GitHub spécifique par routine planifiée. Mais bien sûr, les bonnes pratiques de Cloud.md, en y mettant les informations importantes, parce que tout cela va épuiser vos limites de session Cloud Code exactement de la même manière que si vous l'ouvriez dans Cloud Code, en discutant simplement avec lui.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant une page de documentation ou de notes.

**Contenu textuel & Code** : Titres de section ("What It Is", "How It Works", "CLAUDE.md Makes Routines Smart", "Three Trigger Types") et texte explicatif sur l'utilisation du fichier CLAUDE.md.

**Action / Démonstration** : Le présentateur explique les bonnes pratiques concernant le fichier CLAUDE.md et son impact sur les routines.

![Page de documentation avec du texte expliquant comment CLAUDE.md rend les routines intelligentes.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000928_seg23.jpg)
*⏱️ 00:09:28 — Page de documentation avec du texte expliquant comment CLAUDE.md rend les routines intelligentes.*

---

### ⏱️ `[00:09:42 - 00:10:01]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc encore une fois, trois types de déclencheurs : programmation, API, ce que je trouve vraiment génial. Vous pouvez avoir une autre automatisation qui fait une requête POST vers une sorte de routine. Et puis bien sûr, GitHub. Vous pouvez donc faire en sorte que cela se déclenche automatiquement, en quelque sorte via un webhook basé sur de nouvelles pull requests, de nouveaux pushs, de nouveaux problèmes, de nouvelles versions, des choses comme ça. Alors, comment cela se compare-t-il à ce qui existe déjà ?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Page web de documentation / Notes textuelles

**Contenu textuel & Code** : "Three Trigger Types", "Schedule - Cron-based", "API - POST to a dedicated endpoint", "GitHub - Reacts to repo events", avec le texte "API" mis en surbrillance.

**Action / Démonstration** : Le présentateur commente la section de documentation affichée à l'écran concernant les différents types de déclencheurs d'automatisation.

![Capture d'écran montrant une page de documentation textuelle listant les trois types de déclencheurs (Schedule, API, GitHub) avec en bas à droite une incrustation vidéo du présentateur.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_000947_seg24.jpg)
*⏱️ 00:09:47 — Capture d'écran montrant une page de documentation textuelle listant les trois types de déclencheurs (Schedule, API, GitHub) avec en bas à droite une incrustation vidéo du présentateur.*

---

### ⏱️ `[00:10:01 - 00:10:21]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Nous avons les routines, qui constituent la nouvelle fonctionnalité. Nous avons des tâches planifiées sur le bureau, et ensuite nous avons quelque chose comme simplement une commande slash loop. Donc, les routines s'exécutent sur le cloud d'Anthropic et ces deux autres s'exécutent sur votre machine. Avez-vous besoin que la machine soit allumée ? Non pour les routines, c'est énorme. Mais pour les tâches planifiées sur le bureau et pour loop, vous avez besoin que votre machine soit allumée. Avez-vous besoin d'une session ouverte ? Non, c'est la même chose pour les trois.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Document de présentation ou interface web type Notion/Doc.

**Contenu textuel & Code** : Tableau comparatif incluant les critères : "Runs on", "Needs machine on", "Needs open session", "Survives restarts", "Local file access", "Permission prompts" et "Min interval". On y lit notamment que les "Routines" s'exécutent sur le cloud Anthropic sans nécessiter de machine locale.

**Action / Démonstration** : Analyse comparative et explicative des différences techniques entre les systèmes d'automatisation locaux et cloud.

![Un tableau comparatif présentant les trois types de déclencheurs d'automatisation : "Routines (NEW)", "Desktop Scheduled Tasks" et "/loop", détaillant leurs exigences techniques et comportementales.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001006_seg25.jpg)
*⏱️ 00:10:06 — Un tableau comparatif présentant les trois types de déclencheurs d'automatisation : "Routines (NEW)", "Desktop Scheduled Tasks" et "/loop", détaillant leurs exigences techniques et comportementales.*

---

### ⏱️ `[00:10:22 - 00:10:41]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Est-ce qu'ils survivent aux redémarrages ? Les deux premiers oui, mais pas la boucle. Cela doit exister au sein d'une session spécifique. Accès aux fichiers locaux : non pour les routines, car cela fonctionne à partir du dépôt GitHub. Et pour les deux suivants, oui, vous avez accès aux fichiers locaux. Demandes d'autorisation : avec les routines, c'est entièrement autonome. Et pour ces deux-là, ils sont configurables. Et puis, l'intervalle minimum pour les routines est d'une heure.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Logiciel de présentation ou documentation web (type Notion).

**Contenu textuel & Code** : Tableau comparant sept critères techniques : Runs on, Needs machine on, Needs open session, Survives restarts, Local file access, Permission prompts, Min interval. La cellule "Survives restarts" pour "/loop" est mise en surbrillance bleue avec la valeur "No".

**Action / Démonstration** : Présentation comparative des capacités d'exécution et de persistance des différents types de déclencheurs pour les agents IA.

![Tableau comparatif structuré illustrant les différences techniques entre les "Routines (NEW)", les "Desktop Scheduled Tasks" et la commande "/loop".](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001026_seg26.jpg)
*⏱️ 00:10:26 — Tableau comparatif structuré illustrant les différences techniques entre les "Routines (NEW)", les "Desktop Scheduled Tasks" et la commande "/loop".*

---

### ⏱️ `[00:10:41 - 00:11:02]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ces deux-là peuvent tous les deux s'exécuter chaque minute si vous voulez. D'accord, alors parlons des environnements. Évidemment, votre .env est ignoré par git à moins que vous ne le poussiez dans le dépôt GitHub. Vous savez, en fin de compte, si vous le poussez dans un dépôt privé, vous êtes probablement tranquille, mais vous devez faire vraiment, vraiment attention parce qu'alors, vous savez, il y a un historique. Et si d'autres personnes, vous savez, finissent par collaborer dessus, vous ne voulez tout simplement pas faire ça.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web / Document de notes (type Notion ou Markdown) et flux vidéo de la webcam.

**Contenu textuel & Code** : Texte explicatif sur les environnements, la gestion du fichier .env, les variables d'environnement, l'accès réseau et la configuration sur claude.ai.

**Action / Démonstration** : Le présentateur explique les concepts liés aux environnements et au fichier .env tout en affichant la documentation textuelle à l'écran.

![Capture d'écran montrant une page de documentation textuelle avec la section "Environments" et le présentateur visible en incrustation vidéo en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001046_seg27.jpg)
*⏱️ 00:10:46 — Capture d'écran montrant une page de documentation textuelle avec la section "Environments" et le présentateur visible en incrustation vidéo en bas à droite.*

---

### ⏱️ `[00:11:02 - 00:11:21]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc vous voulez mettre vos clés API dans la variable d'environnement, comme je vous l'ai montré plus tôt. Vous voulez regarder l'accès réseau, qu'il soit complet, de confiance, aucun ou personnalisé, et potentiellement quelques scripts de configuration. Donc ce n'est pas quelque chose que je vous ai encore montré. Si vous créez une nouvelle tâche distante, vous pouvez faire un script de configuration, qui est en fait simplement un script qui s'exécutera lorsque cette nouvelle session démarrera avant le lancement de Cloud Code.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Documentation technique textuelle et interface web de paramétrage de routine.

**Contenu textuel & Code** : Texte explicatif sur les environnements, les clés API, l'accès réseau et script bash de configuration (`#!/bin/bash\nnpm install`).

**Action / Démonstration** : Présentation des options de configuration des environnements et de l'accès réseau pour les routines d'IA.

![Page de documentation textuelle listant les options des 'Environments' (variables d'environnement, accès réseau, script de configuration).](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001107_seg28.jpg)
*⏱️ 00:11:07 — Page de documentation textuelle listant les options des 'Environments' (variables d'environnement, accès réseau, script de configuration).*

![Interface de configuration modale montrant un champ 'Setup script' avec un script bash basique ('npm install').](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001117_seg28.jpg)
*⏱️ 00:11:17 — Interface de configuration modale montrant un champ 'Setup script' avec un script bash basique ('npm install').*

---

### ⏱️ `[00:11:21 - 00:11:40]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc si vous avez besoin d'installer des packages ou quoi que ce soit dans ce genre. D'accord, alors quelle est la différence entre « trusted » et « full » ? Donc « trusted » n'accède qu'aux services connus et vérifiés d'Anthropic, ce que je pensais avoir mis en lien juste ici, mais je viens de le mettre en lien là. Cela vous montre en gros tous les différents domaines qui sont autorisés. Donc juste ici, vous pouvez voir qu'on a les services d'Anthropic, on a le contrôle de version.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant une documentation technique.

**Contenu textuel & Code** : Texte explicatif sur la sécurité réseau, la différence entre 'Trusted' (accès restreint aux services vérifiés) et 'Full' (accès complet), et le proxy de sécurité HTTP/HTTPS.

**Action / Démonstration** : Le présentateur explique et commente la documentation affichée à l'écran concernant les paramètres réseau et de sécurité.

![Page de documentation détaillant les modes d'accès réseau 'Trusted' et 'Full' avec le présentateur en médaillon.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001126_seg29.jpg)
*⏱️ 00:11:26 — Page de documentation détaillant les modes d'accès réseau 'Trusted' et 'Full' avec le présentateur en médaillon.*

![Page de documentation en mode sombre abordant le proxy de sécurité, les domaines autorisés et les options de configuration.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001136_seg29.jpg)
*⏱️ 00:11:36 — Page de documentation en mode sombre abordant le proxy de sécurité, les domaines autorisés et les options de configuration.*

---

### ⏱️ `[00:11:41 - 00:11:59]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Nous avons aussi des plateformes cloud comme Google, des choses comme ça juste ici. Ce sont celles qui sont en quelque sorte déjà vérifiées. Alors, quel est le risque de passer en accès complet ? Eh bien, si Claude lit du contenu malveillant pendant une exécution, il pourrait théoriquement être piégé pour envoyer des données vers un serveur externe. Et avec Trusted, cette requête sortante serait bloquée.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant la documentation technique officielle.

**Contenu textuel & Code** : Documentation sur Network Access: Trusted vs Full, listant les risques de sécurité (Risk of Full).

**Action / Démonstration** : Le présentateur fait défiler la documentation et met en surbrillance les risques de sécurité liés à l'accès réseau complet.

![Capture montrant la navigation dans la documentation de configuration avec des catégories comme Cloud services and monitoring.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001145_seg30.jpg)
*⏱️ 00:11:45 — Capture montrant la navigation dans la documentation de configuration avec des catégories comme Cloud services and monitoring.*

![Capture montrant la section documentation sur Network Access comparant les modes Trusted et Full, avec du texte en surbrillance.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001150_seg30.jpg)
*⏱️ 00:11:50 — Capture montrant la section documentation sur Network Access comparant les modes Trusted et Full, avec du texte en surbrillance.*

---

### ⏱️ `[00:11:59 - 00:12:18]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Maintenant, le risque pratique pour les dépôts privés où vous contrôlez les entrées est très faible, mais je voulais vraiment au moins le reconnaître. Donc, les connecteurs, c'est différent du simple ajout de votre clé API. C'est plutôt du genre des connecteurs que vous ajouteriez à votre chat Claude actuel ou à Claude Cowork, où vous vous connecteriez via OAuth à des services comme Slack, ClickUp ou des choses de ce genre. Voici quelques détails de sécurité.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation de diapositives / Navigateur web

**Contenu textuel & Code** : Texte à l'écran : "Network Access: Trusted vs Full", "Trusted - Can only reach known/vetted services", "Full - Can make outbound requests to anything on the internet", "Risk of Full", "Practical risk for private repos...: Very low", et la section "Connectors" en bas.

**Action / Démonstration** : Le présentateur explique les différences de sécurité entre les accès réseau de type "Trusted" et "Full" pour les agents IA.

![Une diapositive de présentation avec du texte détaillant la sécurité réseau des environnements d'IA, avec le présentateur visible dans un encadré en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001204_seg31.jpg)
*⏱️ 00:12:04 — Une diapositive de présentation avec du texte détaillant la sécurité réseau des environnements d'IA, avec le présentateur visible dans un encadré en bas à droite.*

---

### ⏱️ `[00:12:18 - 00:12:40]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Je ne vais pas entrer trop en profondeur là-dedans. Vous pourriez aussi faire un peu plus de recherches et télécharger ce document. Mais bien sûr, il y a certaines choses à garder à l'esprit, comme vos déclencheurs d'API ou ce qui se passe avec vos dépôts GitHub et les branches. Parce qu'encore une fois, tout va s'exécuter en tant que vous. Donc si vous ne testez pas ces routines avant de simplement les lancer toutes les heures ou quelque chose comme ça, vous devez simplement réfléchir à ce qui pourrait se passer avec les autorisations et ce genre de choses.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web / Document de documentation technique.

**Contenu textuel & Code** : Texte sur la sécurité, la protection des déclencheurs d'API, les jetons, les limites d'exécution et l'identité des commits (GitHub, Slack, Linear).

**Action / Démonstration** : Le présentateur commente les points de sécurité et les précautions à prendre lors de l'utilisation des routines.

![Une page de documentation affichant les détails de sécurité, avec le présentateur en médaillon en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001223_seg32.jpg)
*⏱️ 00:12:23 — Une page de documentation affichant les détails de sécurité, avec le présentateur en médaillon en bas à droite.*

---

### ⏱️ `[00:12:40 - 00:13:15]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Limites et quotas. Donc il semble que sur la version Pro, vous pouvez avoir cinq exécutions par jour, sur la version Max vous pouvez avoir 15 exécutions par jour et sur les versions Équipe et Entreprise vous pouvez avoir 25 routines par jour. Si vous atteignez la limite, les organisations avec l'utilisation supplémentaire activée peuvent la dépasser moyennant un dépassement facturé à l'utilisation, et ensuite nous avons l'intervalle programmé minimum qui est d'une heure et il y a aussi des limites de ressources, donc chacune de ces routines dans le cloud fonctionne sur 4 vCPU, 16 gigaoctets de RAM et 30 gigaoctets d'espace disque, donc encore une fois, réfléchissez bien à ceci : est-ce que vous envoyez un dépôt GitHub absolument massif dans le cloud en ce moment pour l'exécuter ? Cela pourrait simplement gaspiller des ressources sans aucune raison. Donc, qu'est-ce qui persiste par rapport à

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Document de présentation ou page web textuelle.

**Contenu textuel & Code** : Texte listant les limites d'exécution quotidienne (Pro : 5 runs/day, Max : 15 runs/day, Team : 25 runs/day, Enterprise : 25 runs/day) ainsi que les limites de ressources (4 vGPUs, 16 GB RAM, 30 GB disk).

**Action / Démonstration** : Le présentateur commente les limites et quotas d'utilisation des différentes versions de l'outil d'IA.

![Une diapositive de présentation montrant les détails de sécurité, les limites et les quotas des exécutions quotidiennes selon les différents abonnements (Pro, Max, Team, Enterprise).](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001249_seg33.jpg)
*⏱️ 00:12:49 — Une diapositive de présentation montrant les détails de sécurité, les limites et les quotas des exécutions quotidiennes selon les différents abonnements (Pro, Max, Team, Enterprise).*

---

### ⏱️ `[00:13:15 - 00:13:41]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Qu'est-ce qui est détruit ? Les branches cloud sont poussées vers votre dépôt GitHub et la session reste également. Donc comme vous l'avez vu, si je venais ici et que je regardais toutes ces tâches, je pourrais voir toutes les exécutions passées et je pourrais aller les consulter pour voir si quelque chose ne va pas. Mais l'environnement cloud réel qui est cloné sera détruit. Fondamentalement, la règle générale ici est que si quelque chose est local ou si le code du cloud ne peut pas l'atteindre dans votre dépôt GitHub ou via une API, alors cela ne fonctionnera pas.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de routines / application de développement

**Contenu textuel & Code** : Configuration d'une routine planifiée, instructions textuelles et historique des exécutions (Runs) avec horodatages.

**Action / Démonstration** : Consultation de l'interface d'automatisation et visualisation de l'historique des exécutions passées de la tâche.

![Interface de gestion de tâches et de code montrant une routine planifiée ("Testing Skool Wins") avec la liste des exécutions passées ("Runs").](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001328_seg34.jpg)
*⏱️ 00:13:28 — Interface de gestion de tâches et de code montrant une routine planifiée ("Testing Skool Wins") avec la liste des exécutions passées ("Runs").*

---

### ⏱️ `[00:13:41 - 00:14:00]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Nous avons déjà parlé un peu de la rédaction de bons prompts, mais vous voulez vraiment qu'ils soient plus spécifiques. Par exemple, avec mon automatisation programmée ici, c'est beaucoup plus spécifique, n'est-ce pas ? J'ai une compétence que je veux qu'il exécute. Je lui donne l'ordre des opérations, mais quelque chose qui ressemble plus à celui sur les commentaires YouTube, ce n'est pas ce que vous voudriez y mettre à moins que vous ne définissiez une compétence pour simplement le laisser s'exécuter.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web d'automatisation et de gestion de tâches.

**Contenu textuel & Code** : Instructions détaillées avec des commandes du type `cd "C:/Users/nateh/OneDrive/Desktop/Skool Automations" && python scripts/...`.

**Action / Démonstration** : Présentation d'un prompt ou d'instructions spécifiques contenant des ordres d'opérations séquentiels pour une automatisation.

![Interface d'une automatisation programmée montrant les instructions avec des lignes de commande Python et un aperçu vidéo du présentateur en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001346_seg35.jpg)
*⏱️ 00:13:46 — Interface d'une automatisation programmée montrant les instructions avec des lignes de commande Python et un aperçu vidéo du présentateur en bas à droite.*

---

### ⏱️ `[00:14:00 - 00:14:24]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Parce qu'encore une fois, c'est censé être un prompt unique. Vous voulez donc vous assurer qu'il réussit du premier coup. D'accord, alors pourquoi est-ce si excitant ? Et pourquoi est-ce que cela surpasse l'automatisation normale ? Parce que nous conservons en fait le cadre agentique. Vous savez, quand je parle du cadre WAT où nous avons des flux de travail, des agents et des outils, lorsque nous poussons réellement ces automatisations vers le cloud et que ce n'est qu'en quelque sorte un script Python, nous perdons la partie agentique.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Document texte / Éditeur de notes ou page web de présentation.

**Contenu textuel & Code** : Texte expliquant les avantages des routines par rapport à l'automatisation classique (n8n, Zapier) avec la boucle de raisonnement agentique de Claude Code, listant l'auto-correction et la résolution de problèmes.

**Action / Démonstration** : Le présentateur commente les points affichés à l'écran concernant les différences entre l'automatisation traditionnelle et le cadre agentique.

![Capture d'écran montrant une page de texte explicatif intitulée 'Why This Beats Normal Automation', avec une incrustation vidéo du présentateur en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001406_seg36.jpg)
*⏱️ 00:14:06 — Capture d'écran montrant une page de texte explicatif intitulée 'Why This Beats Normal Automation', avec une incrustation vidéo du présentateur en bas à droite.*

---

### ⏱️ `[00:14:24 - 00:14:45]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Nous n'envoyons vraiment que les outils et le flux de travail. Mais dans ce cas, nous gardons le WA et le T tous les deux en cours d'exécution parce que l'agent regarde le CloudMD, il regarde ses scripts et il détermine quoi faire. Et s'il rencontre des erreurs au milieu de l'exécution, il s'auto-corrigera. Et si vous le configurez de la bonne manière, il pourra en quelque sorte laisser une trace mémorielle et il pourra laisser, vous savez, des mises à jour.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Logiciel de prise de notes ou éditeur de documents (type Notion/Obsidian).

**Contenu textuel & Code** : Texte explicatif structuré : "Why This Beats Normal Automation", comparant les automatisations rigides (n8n, Zapier) avec la capacité d'auto-correction et de résolution de problèmes contextuelle de Claude Code. Inclut une liste de conseils pratiques ("The catch: test everything first").

**Action / Démonstration** : Affichage pédagogique des concepts théoriques expliquant le fonctionnement de l'agent IA mentionné dans le segment audio.

![Une capture d'écran montrant une présentation textuelle (probablement dans Notion ou un éditeur Markdown) expliquant les avantages des "Routines" basées sur Claude Code par rapport aux automatisations classiques.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001429_seg37.jpg)
*⏱️ 00:14:29 — Une capture d'écran montrant une présentation textuelle (probablement dans Notion ou un éditeur Markdown) expliquant les avantages des "Routines" basées sur Claude Code par rapport aux automatisations classiques.*

---

### ⏱️ `[00:14:46 - 00:15:05]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Même si chaque exécution est sans état, vous pouvez quand même faire en sorte qu'elles s'améliorent continuellement. Et très rapidement, faisons un survol éclair de ces questions courantes. Ai-je besoin de connaître la syntaxe cron ? Non. Vous pouvez simplement planifier en langage naturel, super facilement. Peut-il accéder à mes fichiers locaux ? Non. Il obtient seulement ce qui se trouve dans votre dépôt GitHub ou vos API. Quel modèle utilise-t-il ? Vous pouvez choisir n'importe quel modèle, comme vous l'avez vu.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Editeur de texte/Note (Type Notion)

**Contenu textuel & Code** : Texte explicatif comparant les automatisations classiques (n8n, Zapier) aux "Routines" basées sur Claude Code, mettant en avant l'auto-correction et la résolution de problèmes contextuelle. Liste de points de contrôle pour les tests : "Run now", vérification des clés API, accès réseau et instructions de gestion d'erreurs.

**Action / Démonstration** : Présentation théorique illustrant la supériorité de l'agentique sur les workflows rigides et conseils de bonnes pratiques pour tester les routines.

![Une page de présentation (type document Notion ou guide Markdown) expliquant les avantages des routines basées sur l'IA par rapport aux automatisations classiques.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001450_seg38.jpg)
*⏱️ 00:14:50 — Une page de présentation (type document Notion ou guide Markdown) expliquant les avantages des routines basées sur l'IA par rapport aux automatisations classiques.*

---

### ⏱️ `[00:15:06 - 00:15:24]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pouvez-vous le voir fonctionner en temps réel ? Oui, vous pouvez cliquer sur exécuter maintenant et vous pouvez évidemment le voir s'exécuter juste là. De la même manière que vous leisseriez dans Claude. Vous pouvez même lui parler une fois que c'est terminé ou l'interrompre et ensuite continuer. Peut-il utiliser mon service MCP ? Oui, c'est ce que sont les connecteurs. Des coéquipiers peuvent-ils utiliser mes routines ? Non, celles-ci appartiennent à votre compte individuel.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant une page de FAQ.

**Contenu textuel & Code** : Texte de la FAQ abordant des questions telles que : 'Can I watch it work in real time?', 'Can it use my MCP servers?', 'What's the cost?'.

**Action / Démonstration** : Le présentateur commente les points de la FAQ affichés à l'écran concernant le fonctionnement en temps réel et les sessions sur claude.ai.

![Une page web affichant une foire aux questions (FAQ) sur l'utilisation des routines, avec en bas à droite une incrustation vidéo du présentateur.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001510_seg39.jpg)
*⏱️ 00:15:10 — Une page web affichant une foire aux questions (FAQ) sur l'utilisation des routines, avec en bas à droite une incrustation vidéo du présentateur.*

---

### ⏱️ `[00:15:24 - 00:15:57]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Vous pourriez être en mesure de les partager si vous êtes sur un forfait d'équipe, mais je n'ai pas encore testé cela moi-même. Quel est le coût ? C'est juste votre utilisation d'abonnement normale. Donc gardez cela à l'esprit. Que se passe-t-il lorsqu'une exécution échoue ? Chacune d'entre elles sera enregistrée dans votre historique. Vous pouvez donc aller voir pourquoi elles ont échoué. Vous pourriez peut-être même faire en sorte qu'à la fin de chaque routine, il soit dit : Hé, si cela échoue, envoie-moi simplement un message Slack pour me le faire savoir, des choses comme ça. Et puis-je tester une exécution avant de la lancer en direct ? Oui. En fait, vous devriez la tester plusieurs fois avant qu'elle ne soit en direct. Vous allez simplement dans la routine, vous cliquez sur Exécuter maintenant, et ensuite elle apparaîtra comme étant en cours d'exécution. Et puis vous la regardez, vous savez, vous la regardez suivre son ordre d'opérations et vous pouvez intervenir et vous pouvez

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Document textuel / Page web de FAQ

**Contenu textuel & Code** : Texte de la FAQ listant des questions/réponses sur les fonctionnalités (MCP, coûts, échecs d'exécution, tests) avec la question « What happens when a run fails? » mise en surbrillance en bleu.

**Action / Démonstration** : Le présentateur explique la gestion des erreurs et des échecs d'exécution en parcourant les questions de la FAQ.

![Une page de FAQ textuelle affichée à l'écran, avec une question mise en surbrillance concernant l'échec des exécutions, tandis que le présentateur apparaît dans un encadré en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001532_seg40.jpg)
*⏱️ 00:15:32 — Une page de FAQ textuelle affichée à l'écran, avec une question mise en surbrillance concernant l'échec des exécutions, tandis que le présentateur apparaît dans un encadré en bas à droite.*

---

### ⏱️ `[00:15:57 - 00:16:18]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> l'aider à se corriger afin que vous ayez l'assurance que, lorsqu'il lancera le prompt la prochaine fois, vous n'aurez plus du tout à intervenir. Mais de toute façon, c'est tout pour celui-ci. J'espère que ces conseils et certains des exemples que je vous ai montrés ont été utiles. Et maintenant, vous pouvez aller essayer de migrer vos tâches planifiées ou toute autre automatisation que vous aviez l'intention de construire vers ces routines basées sur le web et ne plus avoir besoin de garder votre matériel allumé.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion d'agents IA et réseau social X (Twitter).

**Contenu textuel & Code** : Prompt de test de commentaires YouTube et post de @claudeai concernant les routines.

**Action / Démonstration** : Navigation et présentation des résultats d'analyse de commentaires YouTube puis d'une annonce sur X.

![Interface web montrant une session de test de commentaires YouTube avec l'historique des interactions de l'agent IA et le présentateur en médaillon.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001602_seg41.jpg)
*⏱️ 00:16:02 — Interface web montrant une session de test de commentaires YouTube avec l'historique des interactions de l'agent IA et le présentateur en médaillon.*

![Flux du réseau social X (Twitter) affichant un post de Claude annonçant une preview de recherche pour les routines dans Claude Code.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001608_seg41.jpg)
*⏱️ 00:16:08 — Flux du réseau social X (Twitter) affichant un post de Claude annonçant une preview de recherche pour les routines dans Claude Code.*

---

### ⏱️ `[00:16:19 - 00:16:27]` | Segment #42

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Donc, si vous avez apprécié la vidéo ou si vous avez appris quelque chose de nouveau, n'hésitez pas à mettre un pouce bleu. Ça m'aide énormément. Et comme toujours, je vous remercie d'être arrivés jusqu'à la fin de la vidéo. Je vous vois sur la prochaine. Merci tout le monde.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant la plateforme X (Twitter) avec le profil de Claude et une miniature d'interface utilisateur en aperçu.

**Contenu textuel & Code** : Publication Twitter annonçant : "Now in research preview: routines in Claude Code. Configure a routine once (a prompt, a repo, and your connectors), and it can run on a schedule, from an API call, or in response to an event."

**Action / Démonstration** : Navigation et présentation visuelle d'un tweet d'annonce sur les nouvelles fonctionnalités de Claude Code.

![Capture d'écran montrant le fil d'actualité de la plateforme X (Twitter) avec un post du compte officiel de Claude (@claudeai) présentant une nouveauté en research preview (routines in Claude Code), accompagné d'une vidéo incrustée du présentateur en bas à droite.](../screenshots/ehg4fhydTgs/ehg4fhydTgs_001621_seg42.jpg)
*⏱️ 00:16:21 — Capture d'écran montrant le fil d'actualité de la plateforme X (Twitter) avec un post du compte officiel de Claude (@claudeai) présentant une nouveauté en research preview (routines in Claude Code), accompagné d'une vidéo incrustée du présentateur en bas à droite.*

---

