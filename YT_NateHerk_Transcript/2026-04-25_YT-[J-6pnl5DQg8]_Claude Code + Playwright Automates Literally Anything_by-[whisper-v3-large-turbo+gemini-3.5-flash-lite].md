# 🎬 Claude Code + Playwright Automates Literally Anything

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=J-6pnl5DQg8](https://www.youtube.com/watch?v=J-6pnl5DQg8)  
> **Date de publication** : 20260425  
> **Durée** : 00:18:50  
> **Identifiant vidéo** : `J-6pnl5DQg8`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Claude Code + Playwright Automates Literally Anything**, Nate Herk décortique les capacités pratiques d'automatisation et de développement propulsées par les modèles de pointe.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Opus 5.5 & Claude Code** : Modèles d'ingénierie et agents de codage autonome.

### 🔑 Points Clés & Enseignements Stratégiques
- Optimiser le niveau d'effort et le raisonnement des modèles IA pour des résultats industriels.
- Automatiser les cycles de création logicielle de bout en bout.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:35]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So when you give a tool as powerful as Claude Code, access to literally control a browser, if you think about it, you can actually automate anything, whether that's stress testing an app, downloading reports, or even playing a game like you guys saw in my other video. So today I walk through three use cases that you can use when you connect Playwright CLI to Claude Code to control your browser. The first one is having it actually QA a web app and finding bugs and then fixing them. The second one is searching for dentists and finding their contact information. And then the third one, a question that everyone's asking is, can browser use actually control sessions where you need to be logged in? So I show off what I'm able to do in my

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web, VS Code / Cursor (avec terminal intégré Opus/Claude Code), plateforme communautaire Skool.

**Contenu textuel & Code** : Textes de commentaires ("As long as you don't pull a 'claude mythos'..."), formulaires de contact web, logs de terminaux IA ("Opus 4.6 1M").

**Action / Démonstration** : Automatisation de la navigation web, saisie automatisée de commentaires et interaction avec des formulaires de contact via des agents IA.

![Capture d'écran montrant le site Best Buy avec une fenêtre contextuelle de demande de géolocalisation.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000009_seg1.jpg)
*⏱️ 00:00:09 — Capture d'écran montrant le site Best Buy avec une fenêtre contextuelle de demande de géolocalisation.*

![Capture d'écran montrant une interface de communauté Skool avec un agent IA répondant automatiquement aux commentaires.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000017_seg1.jpg)
*⏱️ 00:00:17 — Capture d'écran montrant une interface de communauté Skool avec un agent IA répondant automatiquement aux commentaires.*

![Capture d'écran montrant le site web "Vision Dental" intégré dans une interface de développement (type VS Code/Cursor).](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000026_seg1.jpg)
*⏱️ 00:00:26 — Capture d'écran montrant le site web "Vision Dental" intégré dans une interface de développement (type VS Code/Cursor).*

---

### ⏱️ `[00:00:35 - 00:01:07]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> school account. So I don't want to waste any time. Let's get straight into the video. All right. So I am in a fresh Cloud Code project, as you can see. I'm in a folder called Browser Automation Demo, but there's nothing in here just so you guys can follow along with exactly what I'm doing. So the first thing to do is install Playwright CLI so that we can actually do some browser automation. So I'm just going to go into plan mode and I'm going to say, hey, Cloud Code, I want to use Playwright CLI in order to do some browser automation stuff, whether that means testing out web apps or taking screenshots of things, whatever the case, I just need you to figure out how you can install this for me and then go ahead and build a plan and let's do it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension Claude Code.

**Contenu textuel & Code** : Zone de saisie de prompt "Ctrl esc to focus or unfocus Claude" et logo de Claude Code au centre.

**Action / Démonstration** : Préparation de l'environnement de travail dans VS Code pour lancer une session d'automatisation avec l'agent Claude.

![Interface de Visual Studio Code affichant l'extension Claude Code dans un projet vide nommé "Browser Automation Demo".](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000043_seg2.jpg)
*⏱️ 00:00:43 — Interface de Visual Studio Code affichant l'extension Claude Code dans un projet vide nommé "Browser Automation Demo".*

---

### ⏱️ `[00:01:07 - 00:01:33]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I know I'm telling you guys to use Playwright CLI, but this is literally what I did when I decided I wanted to try out some browser automations, except for I said, Hey, I need you to research the different tools and the different pros and cons and help me figure out what I should do. I played on with Chrome dev tools for a little bit, but now I'm using Playwright CLI. And one reason for that while we're letting this load is that if I do slash context in here, you can see that the Chrome Dev Tools MCP takes up so many tokens because there's so many different tools and each tool has a description.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension/terminal Claude Code intégré.

**Contenu textuel & Code** : Commandes Bash visibles : "ls -la" pour lister le répertoire et vérification des versions de "node", "npm" et "npx". Le prompt affiche : "hey Claude Code! I want to use Playwright...".

**Action / Démonstration** : L'agent est en phase de réflexion ("Thinking") et d'exploration de l'état actuel du projet avant d'exécuter des commandes.

![Une capture d'écran de l'interface VS Code montrant l'agent Claude Code en train d'analyser un projet d'automatisation de navigateur.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000114_seg3.jpg)
*⏱️ 00:01:14 — Une capture d'écran de l'interface VS Code montrant l'agent Claude Code en train d'analyser un projet d'automatisation de navigateur.*

---

### ⏱️ `[00:01:34 - 00:02:01]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that sounds like, hmm, maybe I don't wanna use the MCP server. Let me just go ahead and try this Playwright CLI. And it works really well. All right, so the plan is done. We have an empty project. We're going to initialize the project, install Playwright, create a demo script, test things out. I'm gonna go ahead and accept this plan. And now I'll check with you guys when that's done. All right, so you can see that it is done. it's been installed and then it also tried it out already. So it ran a script to open up this page and then screenshot it. And that got saved right here. So as you can see, it was able to do that.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (éditeur de code).

**Contenu textuel & Code** : Document Markdown : "Plan: Set Up Playwright for Browser Automation". On y voit le contexte ("Empty project directory...") et l'étape 1 : "Initialize the project - Run npm init -y to create a package.json".

**Action / Démonstration** : Présentation du plan d'action généré par l'IA pour automatiser la configuration d'un projet Playwright.

![Capture d'écran de l'éditeur VS Code affichant un fichier Markdown nommé "Claude's Plan" détaillant les étapes pour configurer Playwright dans un projet vide.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000140_seg4.jpg)
*⏱️ 00:01:40 — Capture d'écran de l'éditeur VS Code affichant un fichier Markdown nommé "Claude's Plan" détaillant les étapes pour configurer Playwright dans un projet vide.*

---

### ⏱️ `[00:02:01 - 00:02:37]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> It was able to take a screenshot, which means that everything is working. So now that we have this initial stuff set up, I'm just going to go ahead and do a slash init to basically just initialize the environment and give us a claw.md file. All right. So there are tons of great use cases when it comes to using a browser automation, whether that is looking through Amazon or applying to a ton of positions or, you know, downloading reports from websites that don't have an API. And what's awesome about this is it will build out these scripts that run the browser automation, right? And when you pair those custom scripts with a skill, it gets really powerful because then that process of opening up the browser and doing certain things becomes consistent and

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension/terminal Claude Code intégré.

**Contenu textuel & Code** : Historique de discussion confirmant l'installation de Playwright et la création d'un script de démo (demo.js), suivi de la commande saisie par l'utilisateur "/init".

**Action / Démonstration** : L'utilisateur a saisi la commande "/init" dans l'interface de l'agent IA pour configurer l'environnement du projet.

![Une capture d'écran de l'interface VS Code montrant l'interaction avec Claude Code confirmant la réussite de l'automatisation Playwright et l'initialisation du projet.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000210_seg5.jpg)
*⏱️ 00:02:10 — Une capture d'écran de l'interface VS Code montrant l'interaction avec Claude Code confirmant la réussite de l'automatisation Playwright et l'initialisation du projet.*

---

### ⏱️ `[00:02:37 - 00:02:56]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> repeatable. But one thing that I think is really cool about browser automations is the ability to basically test things and automate QA. So an example I wanted to walk through with you guys is I'm going to use Cloud Code in here to build us a quick web app that's gonna be like a multi-page form. And I don't wanna test it myself. I wanna have it test it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension Claude Code active.

**Contenu textuel & Code** : Arborescence de fichiers du projet "BROWSER AUTOMATION DEMO" incluant des dossiers comme .claude et node_modules, ainsi que le champ de saisie de l'assistant "ctrl esc to focus or unfocus Claude".

**Action / Démonstration** : Initialisation de l'environnement de développement pour entamer la création d'une application web multi-pages via l'agent IA.

![Interface de Visual Studio Code affichant l'extension Claude Code dans un volet latéral, avec le présentateur en médaillon dans le coin inférieur gauche.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000242_seg6.jpg)
*⏱️ 00:02:42 — Interface de Visual Studio Code affichant l'extension Claude Code dans un volet latéral, avec le présentateur en médaillon dans le coin inférieur gauche.*

---

### ⏱️ `[00:02:56 - 00:03:14]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then it has to find the bugs, find suggestions and then fix itself. So it's gonna be us building a web app or a form and it's gonna be like completely hands-off. That's the goal at least. So let's hop into plan mode and let's get started. I need you to build me a form submission website. Now I want this to basically be one page per question.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension Claude Code active.

**Contenu textuel & Code** : Zone de saisie de texte "Ctrl esc to focus or unfocus Claude" et structure de fichiers du projet "BROWSER AUTOMATION DEMO" visible dans la barre latérale.

**Action / Démonstration** : Le présentateur s'apprête à interagir avec l'agent Claude Code pour lancer la création du site web demandé.

![Interface de Visual Studio Code affichant l'extension Claude Code en mode conversationnel, avec le présentateur en médaillon dans le coin inférieur gauche.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000301_seg7.jpg)
*⏱️ 00:03:01 — Interface de Visual Studio Code affichant l'extension Claude Code en mode conversationnel, avec le présentateur en médaillon dans le coin inférieur gauche.*

---

### ⏱️ `[00:03:14 - 00:03:47]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So as soon as I open up the page, it should ask me for my first name. And then there should be a button that prompts me to hit enter. When I hit enter, I go to the next page and then I have my last name and then I have my phone number and then I have my business and I have maybe, let's just say eight questions about me and kind of getting me onboarded into this, you know, fake business or whatever. I just want to do this to see and test the functionality of what you're able to build me here. Okay. So that is phase one, phase one, we're going to get an initial version of the website. And then before I even open it up and test it, we're going to go into plan mode again

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension Claude Code.

**Contenu textuel & Code** : Interface utilisateur de Claude Code avec un champ de saisie textuel indiquant "ctrl esc to focus or unfocus Claude" et des options de configuration ("Plan mode", "settings.local.json").

**Action / Démonstration** : Le présentateur s'apprête à interagir avec l'agent Claude Code pour automatiser la création du formulaire décrit vocalement.

![Une capture d'écran de l'interface de VS Code montrant l'extension Claude Code en cours d'exécution dans un panneau latéral, avec une zone de saisie pour interagir avec l'IA.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000323_seg8.jpg)
*⏱️ 00:03:23 — Une capture d'écran de l'interface de VS Code montrant l'extension Claude Code en cours d'exécution dans un panneau latéral, avec une zone de saisie pour interagir avec l'IA.*

---

### ⏱️ `[00:03:47 - 00:04:08]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and see if just Cloud Code with the browser automation can test it, iterate, test it, iterate. Okay, here is our plan. Multi-page onboarding form. The user wants a polished multi-page onboarding form. We have the architecture. There's 12 total questions, which look good to me. We've got some files that's gonna make, some implementation details here, and all of this looks good to me.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code avec l'extension Claude (Claude Dev/Cline).

**Contenu textuel & Code** : Arborescence du projet "Browser Automation Demo" et logs de l'agent IA : "Explore the project at...", "Read package.json", état "Simmering...".

**Action / Démonstration** : L'agent IA est en train d'explorer la structure du répertoire pour comprendre les fichiers existants avant de commencer le développement du formulaire.

![Interface de VS Code montrant l'extension Claude en pleine action, avec une arborescence de fichiers à gauche et une fenêtre de chat d'agent IA à droite analysant le projet.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000352_seg9.jpg)
*⏱️ 00:03:52 — Interface de VS Code montrant l'extension Claude en pleine action, avec une arborescence de fichiers à gauche et une fenêtre de chat d'agent IA à droite analysant le projet.*

---

### ⏱️ `[00:04:08 - 00:04:29]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So we're gonna go back into the main session and accept those changes. Okay, so that just finished up. We have the files have been created. we've got a server that this is running on. It's gonna be on a local host. We also have 12 one per page questions. And what I noticed it doing is it was taking screenshots and I didn't even tell it to. So if I open up screenshots, you can see we now have these pictures.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code (avec l'extension Claude intégrée).

**Contenu textuel & Code** : Liste des fichiers générés (index.html, serve.js, test-onboarding.js), instructions d'exécution (npm run serve, npm run test:onboarding) et description du flux de travail de l'automatisation (12 questions).

**Action / Démonstration** : L'utilisateur visualise le rapport final de l'agent IA après la génération du code et des scripts d'automatisation.

![Une capture d'écran de l'interface VS Code montrant une interaction avec l'agent Claude, détaillant les fichiers créés pour une automatisation de navigateur et les commandes terminal pour lancer le serveur et les tests.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000413_seg10.jpg)
*⏱️ 00:04:13 — Une capture d'écran de l'interface VS Code montrant une interaction avec l'agent Claude, détaillant les fichiers créés pour une automatisation de navigateur et les commandes terminal pour lancer le serveur et les tests.*

---

### ⏱️ `[00:04:29 - 00:04:50]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So let me just look at these. We've got number one, which is what is your first name? Number two, last name, best phone number to reach you at. There's even, if you can see, there's like one of those scroll bars at the top where it's like showing how many questions in they are. So for a one-shot prompt and the fact that it's already flipping through and taking screenshots, I'm pretty impressed. But we have to see how it's able to actually test it out.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec extension Claude/Cursor).

**Contenu textuel & Code** : Arborescence de fichiers ("onboarding/screenshots/"), instructions textuelles sur l'exécution d'un script Node.js et de Playwright ("npm run test:onboarding"), et aperçu visuel d'une question de formulaire ("Best phone number to reach you?").

**Action / Démonstration** : Le présentateur passe en revue les étapes du processus d'automatisation de formulaire via l'interface de développement.

![L'éditeur Visual Studio Code affiche une structure de projet contenant des captures d'écran de formulaire d'onboarding, avec une fenêtre de chat Claude active présentant des instructions pour tester une automatisation Playwright.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000434_seg11.jpg)
*⏱️ 00:04:34 — L'éditeur Visual Studio Code affiche une structure de projet contenant des captures d'écran de formulaire d'onboarding, avec une fenêtre de chat Claude active présentant des instructions pour tester une automatisation Playwright.*

---

### ⏱️ `[00:04:50 - 00:05:11]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So now I'm gonna go back into plan mode and I'm gonna say, yep, absolutely. Spin up a server so that you can actually run this. And then what I want you to do is use your browser use and test it out. So fill in the fields, click through, and if there's any bugs or if there's anything wrong with the functionality of the site, make note so that you can go ahead and fix the actual site itself.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec l'extension Claude intégrée).

**Contenu textuel & Code** : Documentation du projet "Browser Automation Demo" incluant les commandes `npm run serve`, `npm run test:onboarding`, et l'URL `http://localhost:3000`. Liste des étapes de l'automatisation (12 questions) visible dans le panneau de chat.

**Action / Démonstration** : L'utilisateur est en "Plan mode" dans l'interface de l'agent, préparant le lancement du serveur pour permettre le test de l'automatisation du formulaire via le navigateur.

![Une capture d'écran de l'éditeur VS Code montrant une interaction avec l'interface de chat de l'agent Claude, détaillant les instructions pour lancer un serveur local et exécuter des tests d'automatisation Playwright.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000456_seg12.jpg)
*⏱️ 00:04:56 — Une capture d'écran de l'éditeur VS Code montrant une interaction avec l'interface de chat de l'agent Claude, détaillant les instructions pour lancer un serveur local et exécuter des tests d'automatisation Playwright.*

---

### ⏱️ `[00:05:11 - 00:05:44]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And I also want you to do this in a headed browser so that I can watch what's going on So I'm gonna shoot that off. It's gonna make a plan, but that is one important distinction By default you could say hey I always want you to run playwright in a headed browser But there is headed or headless meaning it could be running this headless where it wouldn't show us on screen But it is still running on its own tab and clicking through things. Okay Here is the QA pass the headed browser testing. I'm not gonna read this I think that this is pretty clear of what we want. I'm gonna go ahead and accept it So what happens is for every kind of like bot that we want to run, it has to write its own script.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec une extension d'assistant IA intégrée.

**Contenu textuel & Code** : Le prompt de l'utilisateur demande à l'IA de lancer un serveur (`npm run serve`), de tester le flux du formulaire via un navigateur "headed" (avec interface graphique) pour observer le processus, et de noter les éventuels bugs.

**Action / Démonstration** : L'assistant IA est en cours de traitement de la requête, comme l'indique l'indicateur "Shimmying..." dans la console de discussion.

![Une capture d'écran de l'interface VS Code avec une fenêtre de chat de l'assistant IA active au centre, détaillant les instructions pour tester un formulaire web.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000520_seg13.jpg)
*⏱️ 00:05:20 — Une capture d'écran de l'interface VS Code avec une fenêtre de chat de l'assistant IA active au centre, détaillant les instructions pour tester un formulaire web.*

---

### ⏱️ `[00:05:44 - 00:06:16]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I believe that this is this one that it's writing, which is the test onboarding.js. And this is basically what instructs the bot on what to do. And then when we wanted to turn this into a skill, which is basically like QAing our website, we would say, okay, when you want to QA, then you run the bot and then you take the feedback from the bot and then you make changes and then you run the bot again. And so that's how we can turn kind of like all of these different pieces into an actual process. Okay. Also that wasn't even the script, the script that it's writing for this is QA dash test. So now you see what I mean. Okay. So the window just popped up.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec intégration d'agent IA, probablement Claude Code/Cursor).

**Contenu textuel & Code** : Arborescence de fichiers (dont `test-onboarding.js`) et historique de chat montrant la commande : `cd "c:/Users/nateh/OneDrive/Desktop/Browser Automation Demo" && node serve.js &`.

**Action / Démonstration** : L'agent exécute un serveur HTTP en arrière-plan et s'apprête à générer/exécuter un script de test QA ("headed browser test").

![Interface de l'éditeur Visual Studio Code avec un panneau de discussion Claude actif, montrant l'exécution d'une commande Bash pour démarrer un serveur local et la préparation d'un test QA.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000552_seg14.jpg)
*⏱️ 00:05:52 — Interface de l'éditeur Visual Studio Code avec un panneau de discussion Claude actif, montrant l'exécution d'une commande Bash pour démarrer un serveur local et la préparation d'un test QA.*

---

### ⏱️ `[00:06:16 - 00:06:48]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I'm going to move it into view and we should be able to watch it fill in. It's did, it did Nathan. Okay. It went backwards. Now it's on the second one, Nathan Harrison, filling in a phone number. It's continuing to click through Harrison tech. We've got a email. We've got founder and CEO. it shows a company size look from a drop down okay technology referral primary goal website continue and anything else okay it looks like it's having a little bit of trouble here now it keeps kind of glitching out but once again I'm not going to stop it I'm going to let it figure out

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec fenêtre de navigateur intégrée localhost:3000).

**Contenu textuel & Code** : Formulaire web "Best phone number to reach you?", champ de saisie rempli avec "(555) 234-5678", bouton "Continue".

**Action / Démonstration** : Automatisation de la saisie de formulaire par un agent IA dans l'interface de l'application.

![Une interface de formulaire web interactive intégrée dans VS Code, affichant une demande de numéro de téléphone avec des données saisies automatiquement par un agent.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000624_seg15.jpg)
*⏱️ 00:06:24 — Une interface de formulaire web interactive intégrée dans VS Code, affichant une demande de numéro de téléphone avec des données saisies automatiquement par un agent.*

---

### ⏱️ `[00:06:48 - 00:07:08]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> what it needs to do okay so it just shut down and now it said okay found some issues let me review the screenshots to understand what happened so what you guys didn't notice is that in there it took more screenshots. So we can see now we have QA and we have all of these screenshots that it took during that test. So it says, okay, the UI looks polished. That's great. It did look really good.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Éditeur de code Cursor (fork de VS Code).

**Contenu textuel & Code** : Liste de tâches "Update Todos", messages système de l'agent : "Found some issues! Let me review the screenshots...", et chemins d'accès aux fichiers image (qa-16-after-textarea-enter.png, qa-17-review-page.png).

**Action / Démonstration** : L'agent IA analyse automatiquement des captures d'écran après avoir rencontré des problèmes lors de l'exécution d'un test QA automatisé.

![L'interface de Cursor (éditeur de code) affichant le flux d'exécution d'un agent IA en pleine analyse de bugs via des captures d'écran.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000653_seg16.jpg)
*⏱️ 00:06:53 — L'interface de Cursor (éditeur de code) affichant le flux d'exécution d'un agent IA en pleine analyse de bugs via des captures d'écran.*

---

### ⏱️ `[00:07:08 - 00:07:40]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But the first bug is that enter on text area didn't advance to review. It stayed on the notes page. The second bug is that the review page never loaded. The test found zero review items and the edit button was intercepted by a stale page overlay. And now it was able to use that feedback to fix the actual bugs in the site itself. And this is just really cool because if you've ever built software or websites or apps or whatever, there are so many bugs and you don't always find them until it's maybe too late or maybe a customer found it. So the fact that you can automate QA by having multiple different headed browsers or even headless browsers spin up and you can say, hey,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec extension d'agent IA).

**Contenu textuel & Code** : Historique de discussion détaillant les bugs : "Bug 1: Enter on textarea didn't advance to review" et "Bug 2: The review page never loaded". Chemins de fichiers (screenshots, index.html) et accès à settings.local.json.

**Action / Démonstration** : L'agent IA analyse les retours des tests automatisés et s'apprête à lire le code source pour corriger les problèmes de navigation identifiés dans le formulaire.

![Interface de l'éditeur VS Code montrant une interaction avec un agent IA (Claude Code) qui analyse deux bugs identifiés lors d'un test d'automatisation de navigateur.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000716_seg17.jpg)
*⏱️ 00:07:16 — Interface de l'éditeur VS Code montrant une interaction avec un agent IA (Claude Code) qui analyse deux bugs identifiés lors d'un test d'automatisation de navigateur.*

---

### ⏱️ `[00:07:40 - 00:08:17]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> you test for X, you test for Y, you test for Z and just have them running and fixing and running and fixing is a complete game changer. And now without me even asking, it says, okay, I'm going to start the server and I'm going to rerun the test. So we're basically getting it stuck in this loop of testing, validating, testing, validating. And, you know, it's really, really cool. So I think it's doing another quick test just to see if it truly is good, but okay, nice. So second test went all the way through and now it should be shutting down and telling us what it learned. As you can

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code, environnement de développement avec agent IA intégré (probablement Claude Code).

**Contenu textuel & Code** : Commandes terminal `node serve.js &` et `node qa-test.js`, interface web de formulaire de saisie de données.

**Action / Démonstration** : Exécution automatisée de tests QA par l'agent : lancement du serveur, puis déclenchement du script de test pour vérifier le fonctionnement du formulaire.

![Interface de l'éditeur VS Code montrant l'agent IA en train d'exécuter des commandes Bash pour démarrer un serveur en arrière-plan et relancer les tests QA.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000749_seg18.jpg)
*⏱️ 00:07:49 — Interface de l'éditeur VS Code montrant l'agent IA en train d'exécuter des commandes Bash pour démarrer un serveur en arrière-plan et relancer les tests QA.*

![Interface de VS Code affichant un navigateur intégré (localhost:3000) montrant un formulaire interactif (question sur le nom de famille) en cours de test automatisé.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000759_seg18.jpg)
*⏱️ 00:07:59 — Interface de VS Code affichant un navigateur intégré (localhost:3000) montrant un formulaire interactif (question sur le nom de famille) en cours de test automatisé.*

---

### ⏱️ `[00:08:17 - 00:08:49]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> see, it just shut down. So now you can see it has finally passed the tests and it goes ahead and ends the process because now the server is good. So like I said, the next step from there would be to turn that into a skill. But what else can we do with browser automations? Because they're definitely not perfect, right? So let's say we wanted to do something on the web. Let's say we wanted it to just be able to go to Google search for, I don't know, let's just say dentists and maybe capture like some phone numbers. All right, here is our plan. Build a playwright script that automates Google search to find dentist offices in California. We will basically launch the browser,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code (avec l'extension Claude ou Cursor).

**Contenu textuel & Code** : Le chat affiche des corrections de bugs spécifiques : "Bug 1 - textarea Enter key logic was inverted" et "Bug 2 - Page stacking caused click interception". Il mentionne également que le serveur en arrière-plan a été arrêté après la validation des tests.

**Action / Démonstration** : L'agent IA confirme la résolution des bugs et propose de lancer le serveur avec la commande `npm run serve`.

![Une capture d'écran de l'interface VS Code montrant une conversation avec l'assistant IA Claude, détaillant la résolution de bugs dans un projet d'automatisation de navigateur.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000825_seg19.jpg)
*⏱️ 00:08:25 — Une capture d'écran de l'interface VS Code montrant une conversation avec l'assistant IA Claude, détaillant la résolution de bugs dans un projet d'automatisation de navigateur.*

---

### ⏱️ `[00:08:49 - 00:09:26]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> do the Google search, collect the links, visit each site and print a summary. So that looks good to me. We're going to go ahead and shoot this off. And hopefully it's going to be decent on the first try. I'm going to tell you guys right now, it's probably not, but what's going to happen is we're going to have it learn. So it's going to open up the browser. It's going to fail. And we're going to say, okay, keep learning, keep updating the script and don't stop until you're done. I literally stepped away to go get water and it actually, I came back and I saw a browser open with some dentist offices up. Wow. So it visited all five sites and it was able to find some phone numbers.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Cursor (éditeur de code basé sur VS Code) avec l'agent IA actif dans le panneau latéral.

**Contenu textuel & Code** : Plan d'exécution : 1. Créer 'find-dentists.js', 2. Référencer 'ga-test.js' et 'demo.js', 3. Exécuter 'node find-dentists.js', 4. Vérifier la sortie console et les captures d'écran dans le dossier 'screenshots/'.

**Action / Démonstration** : L'agent IA est en phase de "Vibing..." (préparation/réflexion) après approbation du plan par l'utilisateur, prêt à exécuter le script d'automatisation.

![Interface de l'éditeur Cursor affichant un plan d'action d'un agent IA pour automatiser une recherche Google et la collecte de données sur des sites de dentistes.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000858_seg20.jpg)
*⏱️ 00:08:58 — Interface de l'éditeur Cursor affichant un plan d'action d'un agent IA pour automatiser une recherche Google et la collecte de données sur des sites de dentistes.*

---

### ⏱️ `[00:09:26 - 00:09:47]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Now that's really cool because it actually learned while it was going and it said that Google blocked the automation. So it switched to DuckDuckGo. So I told it this time, don't stop until it actually finds five phone numbers. So it's going to be a little bit more aggressive. And this time I'm actually here to watch it. Okay. So here we are. It just searched for dentist office LA.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code avec l'extension Claude (interface de chat intégrée).

**Contenu textuel & Code** : - Image #1 : Rapport d'exécution de l'agent mentionnant "Google blocked the automation (CAPTCHA), so I switched to DuckDuckGo".
- Image #2 : Invite de commande ("prompt") demandant à l'agent d'être plus agressif et de ne pas s'arrêter avant d'avoir trouvé 5 numéros de téléphone, suivi de l'exécution du fichier `find-dentists.js`.

**Action / Démonstration** : Analyse d'un échec d'automatisation (CAPTCHA), adaptation de la stratégie (changement de moteur de recherche) et relance de l'agent avec des instructions plus strictes.

![Interface de VS Code montrant l'historique de discussion avec Claude AI où l'agent explique avoir basculé sur DuckDuckGo suite à un blocage Google.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000931_seg21.jpg)
*⏱️ 00:09:31 — Interface de VS Code montrant l'historique de discussion avec Claude AI où l'agent explique avoir basculé sur DuckDuckGo suite à un blocage Google.*

![Interface de VS Code montrant Claude AI en train de recevoir une nouvelle instruction pour relancer le script de recherche de numéros de téléphone.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000942_seg21.jpg)
*⏱️ 00:09:42 — Interface de VS Code montrant Claude AI en train de recevoir une nouvelle instruction pour relancer le script de recherche de numéros de téléphone.*

---

### ⏱️ `[00:09:47 - 00:10:06]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> You can see there's a phone number. I just saw one on screen, so it probably grabbed that screenshot. I see another one on this page, so it's getting pretty lucky here. It's finding the phone numbers pretty quick. But what I just noticed is it's still going to the site and it's still clicking on the contact button. Even though the phone number was up in the top right, visible, it still clicked on the contact button, which I thought is pretty cool.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code, Navigateur web (via automatisation).

**Contenu textuel & Code** : Code Node.js (require Playwright/fs/path), commande Bash : "node find-dentists.js", logs d'exécution ("Dentist Contact Info Finder").

**Action / Démonstration** : L'agent automatise la navigation sur des sites de dentistes pour extraire des numéros de téléphone et des informations de contact.

![Une page web de cabinet dentaire "Beverly Hills Prestige Dental Group" affichée dans un navigateur automatisé par l'agent.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000952_seg22.jpg)
*⏱️ 00:09:52 — Une page web de cabinet dentaire "Beverly Hills Prestige Dental Group" affichée dans un navigateur automatisé par l'agent.*

![Une page web de contact d'un autre cabinet dentaire "Vision Dental" montrant des coordonnées et un formulaire.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_000957_seg22.jpg)
*⏱️ 00:09:57 — Une page web de contact d'un autre cabinet dentaire "Vision Dental" montrant des coordonnées et un formulaire.*

![L'interface de l'éditeur VS Code montrant l'exécution d'un script Bash pour automatiser le scraping de coordonnées de dentistes.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001002_seg22.jpg)
*⏱️ 00:10:02 — L'interface de l'éditeur VS Code montrant l'exécution d'un script Bash pour automatiser le scraping de coordonnées de dentistes.*

---

### ⏱️ `[00:10:06 - 00:10:30]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So this time it got all these phone numbers for these dental offices. So naturally the next question that I'm sure you guys have is how could it work on things that I'm already logged into? So let's just find out. So I'm gonna go to plan mode and just ask it what would happen. So there are a couple of approaches. We could do persistent browser profile, meaning it can launch a browser using my existing Chrome user data, which already has me logged into school.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec extension d'automatisation IA / Claude Code).

**Contenu textuel & Code** : Tableau de données : "Personal Dental Office (LA)" et "West Coast Dental (LA)" avec numéros de téléphone et emails. Champ de saisie prompt en bas avec la commande "/c".

**Action / Démonstration** : Le présentateur interagit avec l'interface de l'IA pour planifier l'automatisation de sites nécessitant une authentification utilisateur.

![Interface de l'éditeur Visual Studio Code affichant un assistant IA (Claude Code) dans un volet latéral, avec une liste de cabinets dentaires et leurs coordonnées.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001012_seg23.jpg)
*⏱️ 00:10:12 — Interface de l'éditeur Visual Studio Code affichant un assistant IA (Claude Code) dans un volet latéral, avec une liste de cabinets dentaires et leurs coordonnées.*

---

### ⏱️ `[00:10:30 - 00:11:03]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We can do manual login and handoff in headed mode, or we could connect to a running browser. Okay, so that's pretty cool. It could open up the browser, I could sign in, and then I could just basically keep that signed in and have it do whatever it needs to do. But I do wanna try option one, which it recommended in the first place. Okay, so we have the plan, which is going to go into my school community. It's going to go to the win channel and it's going to like those posts. So we've got the context, the approach. Obviously, you guys know what these plans look like. Let's just see what it did on this first try. And I'm going to go ahead and accept. Okay, so apparently when it runs this, I'm going to have to log in

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension Claude.

**Contenu textuel & Code** : Texte expliquant l'option 3 ("Connect to Running Browser") et proposant un plan pour automatiser des tâches sur la plateforme Skool (ouverture de navigateur, connexion manuelle, automatisation des réponses).

**Action / Démonstration** : Consultation du plan d'exécution suggéré par l'IA pour l'automatisation du navigateur.

![Interface de VS Code montrant une discussion avec Claude AI détaillant les options d'automatisation de navigateur via Playwright.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001038_seg24.jpg)
*⏱️ 00:10:38 — Interface de VS Code montrant une discussion avec Claude AI détaillant les options d'automatisation de navigateur via Playwright.*

---

### ⏱️ `[00:11:03 - 00:11:35]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> manually the first time, but then in the future, it will basically save that session. So let's see how that works. All right, it opened up school.com. Okay, it opened up school.com. Okay, so what just happened is it opened it up and then it closed it and then it opened it up and it went to my community and closed it And now I think it's actually gonna let me log in. So let me try that real quick Okay, so I logged in and then the browser shut down. So now I said, okay, cool I logged in hopefully now when it launches up this browser, it already has me logged in. Okay, so there it is nice You can see that I am already logged in which is great. Okay, so it's trying to find the wins channel

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code, Navigateur web (Skool), Assistant IA intégré (type Claude Code).

**Contenu textuel & Code** : URL "skool.com", logs de terminal : "Skool Auto-Liker", "Community: ai-automation-society-plus", prompt : "The browser should be open on your screen now...".

**Action / Démonstration** : Démonstration d'automatisation de navigation web : l'agent ouvre Skool, navigue vers une communauté spécifique, et attend une interaction utilisateur pour continuer le processus.

![Une fenêtre de navigateur web affichant la page de la communauté "AI Automation Society Plus" sur la plateforme Skool.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001111_seg25.jpg)
*⏱️ 00:11:11 — Une fenêtre de navigateur web affichant la page de la communauté "AI Automation Society Plus" sur la plateforme Skool.*

![Une fenêtre de navigateur web affichant la page d'accueil "Discover communities" de Skool, montrant plusieurs communautés disponibles.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001119_seg25.jpg)
*⏱️ 00:11:19 — Une fenêtre de navigateur web affichant la page d'accueil "Discover communities" de Skool, montrant plusieurs communautés disponibles.*

![L'interface de l'éditeur VS Code avec une conversation active dans l'assistant IA, indiquant que le script "skool-like-wins.js" est en cours d'exécution.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001127_seg25.jpg)
*⏱️ 00:11:27 — L'interface de l'éditeur VS Code avec une conversation active dans l'assistant IA, indiquant que le script "skool-like-wins.js" est en cours d'exécution.*

---

### ⏱️ `[00:11:35 - 00:12:11]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> It looks like it found it all of these look like they are wins now. Let's see what it's able to do here If it's oh, I just saw it try to like the post. Okay it just liked that one interesting so it's like liking them and unliking them so that's one thing we're gonna have to fix but it is scrolling down it got to the wins channel and it is now trying to like post but as you guys can see it's not perfect so i hope that it's able to realize that it's not really liking them yeah it's basically going like unlike like unlike and it also just said liking too fast so let's see if it's able to learn okay there we go all right so what i'm

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code (avec une fenêtre de navigation active).

**Contenu textuel & Code** : Interface de la plateforme Skool avec un flux de publications, des commentaires, et un classement (Leaderboard) sur la droite.

**Action / Démonstration** : L'agent IA est en train de naviguer et de scroller automatiquement sur la page web pour interagir avec les publications de la communauté.

![Une capture d'écran montrant l'éditeur VS Code avec une fenêtre de navigateur intégrée (Skool) affichant le flux de la communauté "AI Automation Society Plus".](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001144_seg26.jpg)
*⏱️ 00:11:44 — Une capture d'écran montrant l'éditeur VS Code avec une fenêtre de navigateur intégrée (Skool) affichant le flux de la communauté "AI Automation Society Plus".*

---

### ⏱️ `[00:12:11 - 00:12:48]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> to do at this point is, you know, I've seen enough. I'm going to shut this down and hopefully it's able to use that feedback to get better. So the login persisted. It found the wins channel. It even found the heart shaped SVG buttons, but it crashed during the page evaluate for liking. So it's seen all that and now it's going to make the script even better. So I will say with browser automations, I think that this is completely normal, which is why I had a little bit of doubt earlier in the dentist example, but literally every time that you use the script, it's going to get better. So it's about to run it again. Let's see how it does this time. It was able to just find the wins channel. Now, one thing I might want to tell it is I might want to sort it from newest posts rather

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec extension d'agent IA intégrée).

**Contenu textuel & Code** : Commande Bash de lancement de script (node skool-like-wins.js), logs d'erreur "Exit code 1", et analyse textuelle de l'agent sur l'échec de la fonction 'page.evaluate'.

**Action / Démonstration** : L'agent rapporte un crash lors de l'exécution de l'automatisation "Skool Auto-Liker" et analyse une capture d'écran de débogage (skool-02-channel-selected.png).

![Interface de VS Code montrant une interaction avec un agent IA dans un panneau latéral, incluant l'historique d'exécution d'un script d'automatisation.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001221_seg27.jpg)
*⏱️ 00:12:21 — Interface de VS Code montrant une interaction avec un agent IA dans un panneau latéral, incluant l'historique d'exécution d'un script d'automatisation.*

---

### ⏱️ `[00:12:48 - 00:13:16]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> than just going straight to the wins channel. And it went ahead and shut down again. So it's continuously trying to learn and get better at this script. I'm actually going to stop this and I'm going to try to course correct it a little bit. So I'm going to go into plan mode. I'm going to say, so a couple of issues from the first couple of runs. The first thing is that it was hitting the like button like four times. So it ended up not even liking the post. The second thing is once you switch to the wins channel, try to filter the posts by newest.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code (avec l'extension Claude Code active).

**Contenu textuel & Code** : Journal d'exécution de l'agent : "It worked! But it only found 1 like button...", lecture du fichier "skool-03-final.png", et réflexion sur l'ajustement du sélecteur SVG.

**Action / Démonstration** : L'agent IA réalise un diagnostic autonome pour identifier les bons sélecteurs suite à l'échec de détection des boutons "Like" sur la plateforme Skool.

![Interface VS Code affichant l'exécution de Claude Code en train d'analyser une capture d'écran pour corriger une erreur de sélection de bouton "Like".](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001255_seg28.jpg)
*⏱️ 00:12:55 — Interface VS Code affichant l'exécution de Claude Code en train d'analyser une capture d'écran pour corriger une erreur de sélection de bouton "Like".*

---

### ⏱️ `[00:13:16 - 00:13:36]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So there's a little kind of sandwich bar menu option near the channel filter, and that will allow you to change the view to newest. And then you can go through and make sure that all of the posts are liked. You can tell that they are liked because the thumbs up icon on the post will be yellow rather than gray.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code (avec extension IA intégrée)

**Contenu textuel & Code** : Code JavaScript utilisant la bibliothèque Playwright pour automatiser un navigateur, avec un message d'erreur d'exécution ("Exit code 1") et un diagnostic sur la recherche de boutons "like" dans une page.

**Action / Démonstration** : Analyse et débogage par l'IA d'un script d'automatisation de navigateur (Playwright) pour corriger un sélecteur CSS/SVG défaillant.

![Capture d'écran de l'éditeur VS Code montrant l'interface de l'agent IA "Claude" en cours d'exécution dans le projet "Browser Automation Demo", avec un diagnostic d'erreur sur un sélecteur SVG.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001321_seg29.jpg)
*⏱️ 00:13:21 — Capture d'écran de l'éditeur VS Code montrant l'interface de l'agent IA "Claude" en cours d'exécution dans le projet "Browser Automation Demo", avec un diagnostic d'erreur sur un sélecteur SVG.*

---

### ⏱️ `[00:13:36 - 00:13:57]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All right, so we got the browser open. Nice, it was just able to switch to newest. And now it's going through and liking. It skipped over that one because it already liked it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web (Google Chrome) ouvert dans VS Code.

**Contenu textuel & Code** : URL de la page Skool (triée par "newest"), flux de publications communautaires, barre latérale d'exploration des fichiers de VS Code.

**Action / Démonstration** : L'agent automatise la navigation sur la plateforme pour interagir avec les publications (liker) et filtrer les nouveaux contenus.

![Une capture d'écran montrant le navigateur Chrome intégré au sein de l'éditeur VS Code, affichant la plateforme communautaire Skool "AI Automation Society Plus".](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001341_seg30.jpg)
*⏱️ 00:13:41 — Une capture d'écran montrant le navigateur Chrome intégré au sein de l'éditeur VS Code, affichant la plateforme communautaire Skool "AI Automation Society Plus".*

---

### ⏱️ `[00:13:57 - 00:14:17]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Yeah, this is awesome. This seems to be doing the trick. It's liking my own posts, which is a little bit eh, but besides that, it's actually working. And it's skipping over the ones that are already yellow, which is great. It even just went to the next page and it's still liking. So this would go through and like every single post in the wins channel.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : VS Code (avec navigateur intégré), plateforme Skool.

**Contenu textuel & Code** : Liste de posts communautaires avec des métadonnées (noms des auteurs, titres, horodatages) et des icônes d'interaction visibles dans une interface web sombre.

**Action / Démonstration** : Exécution d'un script d'automatisation (agent) qui navigue dans le flux de la communauté et interagit automatiquement avec les publications.

![Une capture d'écran montrant une fenêtre de navigateur ouverte au sein de l'éditeur VS Code, affichant la plateforme communautaire Skool "AI Automation Society Plus" où un agent IA semble parcourir et interagir avec les publications.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001402_seg31.jpg)
*⏱️ 00:14:02 — Une capture d'écran montrant une fenêtre de navigateur ouverte au sein de l'éditeur VS Code, affichant la plateforme communautaire Skool "AI Automation Society Plus" où un agent IA semble parcourir et interagir avec les publications.*

---

### ⏱️ `[00:14:17 - 00:14:37]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm gonna shut that down now, just because I don't want it to go ahead and do all that right now. But that worked and it took what? Maybe four or five iterations. And now what I would do is I would build a skill out of that. So I could just say, hey, run the school-like skill. So anyways, I know that that was kind of a simple use case, but the point I was trying to prove is that, yes, you can automate stuff in areas where you need to be logged in.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Visual Studio Code avec l'extension Claude (interface de chat intégrée).

**Contenu textuel & Code** : Commande Bash affichée : `cd "c:\Users\nateh\OneDrive\Desktop\Browser Automation Demo" && node skool-like-wins.js 2>&1`. Le journal de l'agent indique : "Exit code 1", "Skool Auto-Liker", et un retour sur l'exécution précédente (liker 30 posts sur 2 pages).

**Action / Démonstration** : L'agent affiche le résultat d'une exécution de script Node.js et propose une zone de saisie pour soumettre un nouveau message ou instruction.

![Interface de l'éditeur VS Code affichant un agent conversationnel en cours d'exécution d'un script d'automatisation.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001422_seg32.jpg)
*⏱️ 00:14:22 — Interface de l'éditeur VS Code affichant un agent conversationnel en cours d'exécution d'un script d'automatisation.*

---

### ⏱️ `[00:14:37 - 00:15:11]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And also, like, school is one of the least automation-friendly platforms ever. So, okay, so I was going to just post the video there, but I decided that I wanted to keep this going a little bit to show you guys what's actually possible with this. So what's really cool is now that you have these Playwright CLI automations that can do things in your browser, and it can save your cookies. So basically you stay logged in. You can actually start to automate things when you use the desktop app. Now you could also use something like, um, you know, modal or trigger and just deploy those automations there. But I like to use the desktop app for my scheduled

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Play.ai (application web d'automatisation basée sur l'IA).

**Contenu textuel & Code** : Liste de projets : "Skool wins engagement", "AI news roundup", "Notification responses", "Youtube comment replies". La zone de texte indique "Reply..." avec une option "Ask permissions" et un chemin de répertoire local.

**Action / Démonstration** : Le présentateur illustre l'interface de travail de l'outil d'automatisation où il prépare une nouvelle session de codage ou d'interaction avec l'IA.

![L'interface de l'application Play (Play.ai) affichant le mode "Code" avec une barre latérale listant des projets d'automatisation planifiés (Skool, YouTube, etc.) et une fenêtre de saisie pour l'assistant IA.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001445_seg33.jpg)
*⏱️ 00:14:45 — L'interface de l'application Play (Play.ai) affichant le mode "Code" avec une barre latérale listant des projets d'automatisation planifiés (Skool, YouTube, etc.) et une fenêtre de saisie pour l'assistant IA.*

---

### ⏱️ `[00:15:11 - 00:15:45]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> tasks because I get the more agentic ability because when these scheduled runs actually run, it's an agent literally like you see in cloud code walking through what's going on. So for example, I have basically created this bot in my school community. So his name is AIS Agent and as you can see it's posting things like daily news roundups And it's responding to all of its notifications And it even today made a happy birthday post for me, which I didn't tell to do It just knew information about me and it did this completely autonomously So I've got it doing things like everyday engaging with school wins So if I click on today's run you can see that it shows me what it engaged with and it ran all these commands

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Cloud Code (éditeur/plateforme d'automatisation) et Skool (plateforme communautaire).

**Contenu textuel & Code** : Liste de tâches automatisées planifiées (Daily/Custom) dans Cloud Code ; texte de publication automatique humoristique sur Skool par "Ais Agent".

**Action / Démonstration** : Navigation dans les projets automatisés de Cloud Code et démonstration visuelle d'une interaction générée par un agent IA au sein d'une communauté.

![Interface de l'application de développement Cloud Code affichant une barre latérale avec une liste de projets automatisés (Scheduled) comme "Skool wins engagement" et "AI news roundup".](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001519_seg34.jpg)
*⏱️ 00:15:19 — Interface de l'application de développement Cloud Code affichant une barre latérale avec une liste de projets automatisés (Scheduled) comme "Skool wins engagement" et "AI news roundup".*

![Interface de la plateforme communautaire Skool montrant une publication automatique faite par le bot "Ais Agent" souhaitant un joyeux anniversaire à Nate Herk, avec les interactions des membres en dessous.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001536_seg34.jpg)
*⏱️ 00:15:36 — Interface de la plateforme communautaire Skool montrant une publication automatique faite par le bot "Ais Agent" souhaitant un joyeux anniversaire à Nate Herk, avec les interactions des membres en dessous.*

---

### ⏱️ `[00:15:45 - 00:16:18]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And it basically just shoots over this prompt and it invokes the skill to do this every time I've also got it doing the AI news roundup and I've also got it responding to all of the notifications in school It looks like there's actually one running right now We've hit some sort of error But because this is a Gentic It's going to keep trying different things in order to make sure that we're actually able to get this to go through And remember how I talked about with playwrights CLI You have to use the skill more and more or run the script more and more in order for it to understand What to click on and where to submit things and it has to learn how the actual ui of in this case school works

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Outil d'automatisation (type interface propriétaire d'agent IA).

**Contenu textuel & Code** : Workflow détaillé : "1. Change to the project directory: cd...", "2. Run the scraper...", "3. Parse the JSON output...". Liste de résultats identifiant des posts d'utilisateurs sur Skool et mentionnant une exécution de commandes en cours.

**Action / Démonstration** : L'agent IA exécute une séquence de commandes pour scraper des posts "wins" sur Skool, filtrer les commentaires manquants, et préparer une réponse personnalisée.

![Interface d'un outil d'automatisation IA affichant le workflow "Skool wins engagement" en cours d'exécution, avec la liste des posts identifiés et les commandes associées.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001553_seg35.jpg)
*⏱️ 00:15:53 — Interface d'un outil d'automatisation IA affichant le workflow "Skool wins engagement" en cours d'exécution, avec la liste des posts identifiés et les commandes associées.*

---

### ⏱️ `[00:16:18 - 00:16:40]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and all of these automations I have running in a headless browser, meaning when I have my computer open, I don't see the tab pop up and I don't see it happen. But right now I told it to go into that happy birthday post and respond to all the comments on that post. And so now it is pulling up this browser. It needs to figure out how do I actually navigate to that post that I made. So it's going to its notifications and it's just going to look through the notifications and click on those and respond to them.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Application de gestion d'agents IA (probablement une plateforme d'automatisation type Windsurf ou similaire), navigateur web intégré.

**Contenu textuel & Code** : Prompt : "I want you to go into the Skool community and look at the post you made today... and I want you to respond to all of the comments on that post."

**Action / Démonstration** : L'agent IA est en train de "réfléchir" (Thinking...) pour exécuter l'automatisation, puis ouvre le navigateur pour accéder à la plateforme Skool et interagir avec les commentaires.

![Interface d'une application d'automatisation IA affichant une session de codage en cours avec un prompt utilisateur demandant de répondre aux commentaires d'un post spécifique sur Skool.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001623_seg36.jpg)
*⏱️ 00:16:23 — Interface d'une application d'automatisation IA affichant une session de codage en cours avec un prompt utilisateur demandant de répondre aux commentaires d'un post spécifique sur Skool.*

![La même interface avec une fenêtre de navigateur ouverte par-dessus, montrant la communauté Skool "AI Automation Society Plus" en train de charger les notifications.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001635_seg36.jpg)
*⏱️ 00:16:35 — La même interface avec une fenêtre de navigateur ouverte par-dessus, montrant la communauté Skool "AI Automation Society Plus" en train de charger les notifications.*

---

### ⏱️ `[00:16:41 - 00:17:15]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And as it goes through this agentic loop, it starts creating new tools. Because one time someone said, hey, AIS agent, can you please vote on my poll? But the agent couldn't figure it out. So what it had to do is it had to figure out What does it actually mean to vote and where do I click and once it did that it turned that into another script? And then it was able to make sure that its skill was updated so that in the future It was a bit more autonomous and could actually vote on polls Cool, so what it did here is it made a to-do list of all of the different comments that it needs to respond to So here's the comment and then here's the actual reply that it's going to make And now it's launching up this browser and it's going to individually go through and respond to these

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de type "Agentic IDE" (probablement Windsurf ou un outil similaire d'automatisation d'agents).

**Contenu textuel & Code** : Prompt utilisateur demandant de répondre à des commentaires sur un post Skool, suivi d'une commande Bash exécutant un script Python nommé "scrape_notification" et d'un état de réflexion ("Thinking...").

**Action / Démonstration** : L'agent est en phase d'exécution d'un script d'automatisation pour naviguer dans les notifications Skool et identifier les commentaires cibles.

![Interface d'un agent IA traitant une requête utilisateur pour automatiser une réponse sur la plateforme Skool via un script Python.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001649_seg37.jpg)
*⏱️ 00:16:49 — Interface d'un agent IA traitant une requête utilisateur pour automatiser une réponse sur la plateforme Skool via un script Python.*

---

### ⏱️ `[00:17:15 - 00:17:47]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And because it's been doing this so many times it knows that it needs to hit reply under each comment Type it out maybe even tag people and then hit the submit button So obviously this isn't perfect, right? Like there's still things that I'm working through I'm sometimes it responds to people twice because it forgot to mark the notification as read But I basically just told my community. Hey, I'm experimenting with some browser automations And if you see AIS agent just kind of like doing some random weird things just ignore it So the other thing that I want you guys to keep in mind is that we are using playwright CLI There are other CLIs out there that do browser automations and I've been having great success with Playwright.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Plateforme communautaire Skool (navigateur web) intégrée dans un environnement de développement ou de gestion d'agents.

**Contenu textuel & Code** : Commentaires de la communauté, mentions @Nate Herk, zone de saisie de texte "REPLY", interface de l'agent "Ais Agent".

**Action / Démonstration** : Démonstration du comportement automatisé d'un agent IA qui lit, rédige et publie des réponses aux commentaires des membres de la communauté Skool.

![Interface de la plateforme communautaire Skool affichant un fil de discussion où un agent IA nommé "Ais Agent" interagit avec les utilisateurs.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001723_seg38.jpg)
*⏱️ 00:17:23 — Interface de la plateforme communautaire Skool affichant un fil de discussion où un agent IA nommé "Ais Agent" interagit avec les utilisateurs.*

![Gros plan sur l'interface de Skool montrant une zone de texte active où l'agent IA est en train de rédiger une réponse à un commentaire, avec les options de soumission visibles.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001731_seg38.jpg)
*⏱️ 00:17:31 — Gros plan sur l'interface de Skool montrant une zone de texte active où l'agent IA est en train de rédiger une réponse à un commentaire, avec les options de soumission visibles.*

![Vue du fil de discussion Skool montrant l'agent IA ayant posté plusieurs réponses consécutives, illustrant le processus automatisé de réponse aux commentaires.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001739_seg38.jpg)
*⏱️ 00:17:39 — Vue du fil de discussion Skool montrant l'agent IA ayant posté plusieurs réponses consécutives, illustrant le processus automatisé de réponse aux commentaires.*

---

### ⏱️ `[00:17:47 - 00:18:09]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But I also have been seeing people talk about other CLIs to do this. And the reason why we're using a CLI compared to the MCP, like I said, is we're just going to save a lot of tokens. But here's a little comparison you can see. There's also something like for cell agent browser or open CLI, or, you know, there's multiple other CLIs that do computer automations. And I think what you'd be looking for is finding the one that has the best balance of token efficiency as well as performance.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation de type tableau comparatif (UI web/document).

**Contenu textuel & Code** : Tableau détaillant les aspects suivants pour trois outils CLI : Token Efficiency, Speed/Performance, Best For, Claude Integration et Community Buzz. Inclut une recommandation textuelle sous le tableau.

**Action / Démonstration** : Analyse comparative et recommandation d'outils CLI pour l'automatisation avec Claude Code.

![Un tableau comparatif intitulé "Quick Comparison for Claude Code Users" présentant les caractéristiques de Playwright CLI, Vercel agent-browser et OpenCLI.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001752_seg39.jpg)
*⏱️ 00:17:52 — Un tableau comparatif intitulé "Quick Comparison for Claude Code Users" présentant les caractéristiques de Playwright CLI, Vercel agent-browser et OpenCLI.*

---

### ⏱️ `[00:18:09 - 00:18:42]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I don't care so much about speed, but I meant more like the performance of how actually good is it at clicking around and learning how to improve the script so that next time it doesn't make the same mistakes. I'm going to be testing out other options and seeing which ones I think are the best, but at the moment I've mainly been using Playwright CLI. But that is going to do it for the video. Now the next step would be once you understand how to create all these browser automations, how do you actually make them fire automatically all the time, kind of like what I've got set up here. So if you want to learn how to do that, then check out my video about scheduled tasks, which you can watch right up here. Hopefully

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Tableau comparatif (web) ; Interface de travail Claude Code (session de codage).

**Contenu textuel & Code** : Comparaison technique des outils CLI ; Journal de logs de tâches (réponses aux commentaires) et commande Bash `python scripts/post_comment.py` sur un répertoire local.

**Action / Démonstration** : Analyse comparative des performances des outils d'automatisation ; Exécution en temps réel d'un script d'automatisation des réponses aux commentaires par l'agent.

![Un tableau comparatif détaillé présentant trois outils d'automatisation (Playwright CLI, Vercel agent-browser, OpenCLI) selon plusieurs critères techniques (efficacité des tokens, vitesse, intégration, etc.).](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001817_seg40.jpg)
*⏱️ 00:18:17 — Un tableau comparatif détaillé présentant trois outils d'automatisation (Playwright CLI, Vercel agent-browser, OpenCLI) selon plusieurs critères techniques (efficacité des tokens, vitesse, intégration, etc.).*

![Interface de l'agent IA (Claude Code) affichant une session de codage en cours, avec une liste de tâches, une exécution de commande Bash et l'état "Finagling..." indiquant un processus d'ajustement.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001834_seg40.jpg)
*⏱️ 00:18:34 — Interface de l'agent IA (Claude Code) affichant une session de codage en cours, avec une liste de tâches, une exécution de commande Bash et l'état "Finagling..." indiquant un processus d'ajustement.*

---

### ⏱️ `[00:18:42 - 00:18:50]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I see you guys over there, but if you enjoyed the video, you learned something new, please give a like. It definitely helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one. Thanks everyone.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web (Skool) au sein d'un environnement de travail (possiblement Cursor ou VS Code).

**Contenu textuel & Code** : Fil de discussion contenant des messages d'utilisateurs et une réponse automatisée d'un "Ais Agent" souhaitant un bon anniversaire à Nate.

**Action / Démonstration** : Démonstration de l'interaction automatisée d'un agent IA répondant en temps réel sur une plateforme communautaire.

![Interface web de la plateforme Skool affichant un fil de discussion communautaire "AI Automation Society Plus" où un agent IA répond aux commentaires des membres.](../screenshots/J-6pnl5DQg8/J-6pnl5DQg8_001844_seg41.jpg)
*⏱️ 00:18:44 — Interface web de la plateforme Skool affichant un fil de discussion communautaire "AI Automation Society Plus" où un agent IA répond aux commentaires des membres.*

---

