# 🎬 n8n's Agent Builder Somehow Made Building Agents Even Easier (text to workflow)

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=TDHFkKSTJ30](https://www.youtube.com/watch?v=TDHFkKSTJ30)  
> **Date de publication** : 20250910  
> **Durée** : 00:18:58  
> **Identifiant vidéo** : `TDHFkKSTJ30`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **n8n's Agent Builder Somehow Made Building Agents Even Easier (text to workflow)**, Nate Herk décortique les capacités pratiques d'automatisation et de développement propulsées par les modèles de pointe.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Opus 5.5 & Claude Code** : Modèles d'ingénierie et agents de codage autonome.

### 🔑 Points Clés & Enseignements Stratégiques
- Optimiser le niveau d'effort et le raisonnement des modèles IA pour des résultats industriels.
- Automatiser les cycles de création logicielle de bout en bout.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:34]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All right, here we are in NNN and we're looking at this chat GPT-like interface and I'm just going to tell it to create this workflow. And I said that I need a workflow that will receive a form submission via webhook. We need to process information like the person's company, their budget, and their project description. We're going to use that information to qualify them as a hot, warm, or a cold lead. And that will be decided by doing some research on their company, seeing if they're in the right industry. We're also looking for budget. And finally, we want companies that are looking to implement custom AI solutions in their business. After it's done that analysis, I want these leads to be submitted into our CRM and ClickUp. I also want a Gmail notification and I want a Slack notification.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow avec assistant IA intégré)

**Contenu textuel & Code** : Prompt utilisateur : "I need a workflow that will receive a form submission via webhook... process the information like: the person's company, their budget, their project description... qualify them as a hot, warm or cold lead... submitted into our CRM in ClickUp, and I also want an Gmail notification as well as a Slack message..."

**Action / Démonstration** : L'assistant IA est en cours de traitement ("Working...") suite à la saisie du prompt pour générer automatiquement le workflow décrit.

![Interface n8n avec la fenêtre de chat "n8n AI" ouverte sur la droite, affichant un prompt détaillé de l'utilisateur demandant la création d'un workflow automatisé pour qualifier des leads.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000008_seg1.jpg)
*⏱️ 00:00:08 — Interface n8n avec la fenêtre de chat "n8n AI" ouverte sur la droite, affichant un prompt détaillé de l'utilisateur demandant la création d'un workflow automatisé pour qualifier des leads.*

---

### ⏱️ `[00:00:34 - 00:00:54]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So it thought about it. It searched through all the nodes that it has access to and then it gave us a little outline. So I'm just going to go ahead and approve this plan and now it's building that for us. Wow. So not only did it spit out this workflow that looks correct, on the right hand side it gives us a setup guide. So it tells us these six things still need to be configured and then it also tells us how to use this and activate it and actually push it into production.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (plateforme d'automatisation de workflows).

**Contenu textuel & Code** : Liste des nœuds du workflow : "Form Submission Webhook", "Workflow Configuration", "OpenAI Chat Model", "Company Research Tool", "Lead Qualification Agent", "Lead Routing", "Create ClickUp Lead", "Prepare Notification Data", "Send Gmail Notification", "Send Slack Alert", "Combine Notification Results".

**Action / Démonstration** : L'assistant IA est en cours d'exécution ("Working...") après que l'utilisateur a validé le plan ("Proceed with the plan").

![Interface n8n affichant un assistant IA en train de générer un workflow complexe pour la qualification de leads, avec une liste d'étapes d'automatisation planifiées dans le panneau latéral droit.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000039_seg2.jpg)
*⏱️ 00:00:39 — Interface n8n affichant un assistant IA en train de générer un workflow complexe pour la qualification de leads, avec une liste d'étapes d'automatisation planifiées dans le panneau latéral droit.*

---

### ⏱️ `[00:00:54 - 00:01:15]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And so if I click into a few of these nodes here, you can see that they're actually configured already. Besides needing to connect to our ClickUp account, we have variables being passed through this entire flow. So we've got the name right here, but then you can also see we're sending over content like the lead info as far as company, contact, email, phone, different information about the lead. It's giving us an AI analysis and a qualification level and also a score out of 100.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow)

**Contenu textuel & Code** : Expressions JavaScript n8n pour le mapping de données : `{{ $('Lead Qualification Agent').item.json.company_name + ' - ' + $('Lead Qualification Agent').item.json.qualification_level + ' Priority Lead' }}` et template de contenu Markdown intégrant des variables de webhook et d'agent.

**Action / Démonstration** : Configuration des paramètres de champ pour la création d'une tâche/d'un lead dans ClickUp au sein d'un workflow d'automatisation.

![Une fenêtre de configuration de nœud n8n intitulée "Create ClickUp Lead" est ouverte, affichant les paramètres de mapping de données entre les agents IA et ClickUp. Sur la droite, l'assistant IA de n8n fournit des instructions sur la configuration du workflow.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000059_seg3.jpg)
*⏱️ 00:00:59 — Une fenêtre de configuration de nœud n8n intitulée "Create ClickUp Lead" est ouverte, affichant les paramètres de mapping de données entre les agents IA et ClickUp. Sur la droite, l'assistant IA de n8n fournit des instructions sur la configuration du workflow.*

---

### ⏱️ `[00:01:16 - 00:01:39]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then down here, it's assigning a priority. And then after it updates that row in our CRM, it uses the set node to create an email subject, an email body. All of these have variables once again, and I didn't even tell it to do this. And then we have our message, and then it uses those variables to send off that Gmail or Slack alert. And then you can also see over here, our AI agent has a system prompt right here, and its HTTP request is already set up to Google the company URL.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflow d'automatisation) avec panneau latéral "n8n AI" ouvert.

**Contenu textuel & Code** : Expressions n8n de type : `{{ $('Lead Qualification Agent').item.json.company_name }}`. Le panneau latéral affiche des instructions textuelles sur l'authentification Gmail et Slack.

**Action / Démonstration** : Configuration manuelle des données de notification via l'interface d'expression de n8n pour formater les messages sortants.

![Une fenêtre de configuration de nœud n8n intitulée "Prepare Notification Data", affichant la définition dynamique de champs (emailSubject, emailBody, slackMessage) utilisant des expressions JSON injectant des variables provenant d'un agent de qualification de lead.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000121_seg4.jpg)
*⏱️ 00:01:21 — Une fenêtre de configuration de nœud n8n intitulée "Prepare Notification Data", affichant la définition dynamique de champs (emailSubject, emailBody, slackMessage) utilisant des expressions JSON injectant des variables provenant d'un agent de qualification de lead.*

---

### ⏱️ `[00:01:40 - 00:02:13]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that was a real quick demo. We're going to be diving deeper into this today with a few different examples. I'm going to talk about what works well, how to approach using this, and also talk about some of the limitations. So let's get into it. Okay, so this is what everyone's been waiting for, which is NN's native natural language to workflow or agent builder. And I'm super excited about this because it's going to really cut down the time that it takes to spin up a POC. And I think that's really exciting. But I also am a little bit worried about the false sense of security that it's going to bring to a lot of people. I think there's no problem in using this kind of technology. I'm definitely going to leverage it as well. But what's going to be really important is after you get your

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow low-code).

**Contenu textuel & Code** : Le canevas affiche un flux de travail composé de nœuds (Form Submission, Workflow Configuration, OpenAI Chat Model, Lead Routing, ClickUp Lead, Notification). La barre latérale droite détaille des instructions de configuration (Gmail, Slack, email) et un guide "How to Use" pour l'intégration.

**Action / Démonstration** : Visualisation du workflow automatisé prêt à être exécuté pour la qualification de leads et l'intégration CRM.

![Une vue de l'éditeur de workflow n8n montrant un pipeline automatisé de qualification de leads avec une barre latérale d'assistant IA.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000148_seg5.jpg)
*⏱️ 00:01:48 — Une vue de l'éditeur de workflow n8n montrant un pipeline automatisé de qualification de leads avec une barre latérale d'assistant IA.*

---

### ⏱️ `[00:02:13 - 00:02:36]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> initial workflow generated that you can dive into and understand why it's doing what it's doing and how to fix it, how to improve it, stuff like that. Kind of the same idea of you would never just download a template and push it into production or sell it to a client. You need to understand how it's working fundamentally. And so quick disclaimer, if you're opening up your NNN and you don't see this GPT-like interface, don't worry, it hasn't been officially rolled out to everyone yet.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflows visuels).

**Contenu textuel & Code** : Zone de texte centrale "Ask n8n to build...", suggestions de cas d'usage (ex: "Invoice processing pipeline", "RAG knowledge assistant", "Multi-agent research workflow"), et option "Start manually".

**Action / Démonstration** : L'utilisateur est invité à saisir une instruction pour générer automatiquement un workflow ou à commencer la construction manuelle par l'ajout d'un nœud.

![Interface de création de workflow dans n8n avec une zone de saisie pour générer des automatisations via IA, entourée de suggestions de modèles.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000219_seg6.jpg)
*⏱️ 00:02:19 — Interface de création de workflow dans n8n avec une zone de saisie pour générer des automatisations via IA, entourée de suggestions de modèles.*

---

### ⏱️ `[00:02:37 - 00:03:12]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So anyways, now that that's out of the way, what we're going to do today is talk about how this works and how to make your results better. So what I'm going to do today is three examples, one prompt that's pretty vague, one prompt that is detailed and specific with tech stack and stuff like that. And then we're going to do one that's kind of like a really agentic sub-agent type of system. And we'll just break down like what worked well and what didn't. All right. So this first one that we're going to do, like I said, super vague, which is create an AI agent that researches news every morning and emails me a newsletter. So super vague. So what's going on right now is NNN's AI builder is thinking about what we want, and it's going to search through NNN's documentation,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow).

**Contenu textuel & Code** : Zone de texte centrale "Ask n8n to build..." avec des suggestions d'automatisation (Invoice processing pipeline, RAG knowledge assistant, YouTube video chapters, etc.) et un bouton "Start manually".

**Action / Démonstration** : Le présentateur introduit l'interface de création de workflow assistée par IA avant d'entamer une démonstration de saisie de prompts.

![Capture d'écran de l'interface n8n montrant la zone de saisie pour la génération automatique de workflows par IA.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000246_seg7.jpg)
*⏱️ 00:02:46 — Capture d'écran de l'interface n8n montrant la zone de saisie pour la génération automatique de workflows par IA.*

---

### ⏱️ `[00:03:12 - 00:03:48]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> the nodes, and stuff like that in order to figure out how to build this workflow. So what happens is it comes back and says, okay, based on what you said, this is what I think you want. Here are the different nodes we're going to use. And then at this point, we can either approve it or we can request changes. So right now I'm just going to approve it and I want to see how well it does with a very vague prompt. And if you guys have ever played around with NNN's AI assistant on the right-hand side, which is what you typically would use, like if you want to troubleshoot a little bit. This is similar. It's just a builder rather than just an assistant. But anyways, you can see what's going on as it put the nodes in the workflow, and then it connected them. And now what I think it's doing is making sure that all of the variables actually flow from one node to the next. And we'll

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Plateforme d'automatisation n8n (n8n AI).

**Contenu textuel & Code** : Liste des nœuds suggérés par l'IA : "Daily Morning Trigger", "Workflow Configuration", "OpenAI Chat Model", "Web Research Tool", "News Research Agent", "Send Newsletter Email". Boutons d'action "Approve Plan" et "Request Changes".

**Action / Démonstration** : L'assistant IA a généré un plan de workflow en réponse à la requête de l'utilisateur et demande une validation pour procéder à la construction.

![Interface n8n avec l'assistant IA actif dans la barre latérale droite, proposant une structure de workflow pour la création d'une newsletter automatisée.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000321_seg8.jpg)
*⏱️ 00:03:21 — Interface n8n avec l'assistant IA actif dans la barre latérale droite, proposant une structure de workflow pour la création d'une newsletter automatisée.*

---

### ⏱️ `[00:03:48 - 00:04:21]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> take a look once this finishes up, which looks like it is done. So it gives us a setup guide, which is basically saying, hey, here's what's left to configure. And then it tells us how to actually use the workflow. So let's dive in real quick to see what it did. So the workflow starts with our scheduled trigger because I believe I said every morning we want this to go off. Yep, we said every morning. So it goes off at 7am. After that trigger goes off, we have some workflow configuration right here, which is apparently just setting the email recipient, which right now is unknown, the news topics, which defaulted to technology, AI and business, and then newsletter

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow low-code).

**Contenu textuel & Code** : Nœuds de workflow : Daily Morning Trigger, News Research Agent, OpenAI Chat Model, Web Research Tool, Send Newsletter Email. Paramètres configurables : destinataire email, sujets d'actualité (tech, IA, business) et style de newsletter.

**Action / Démonstration** : Présentation visuelle de la structure du workflow généré par l'IA et examen des paramètres de configuration personnalisables par l'utilisateur.

![Interface n8n affichant un workflow d'automatisation complet avec des nœuds de déclenchement, un agent de recherche IA et un panneau latéral de documentation "How to Setup".](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000356_seg9.jpg)
*⏱️ 00:03:56 — Interface n8n affichant un workflow d'automatisation complet avec des nœuds de déclenchement, un agent de recherche IA et un panneau latéral de documentation "How to Setup".*

![Gros plan sur la fenêtre de configuration du nœud "Workflow Configuration" dans n8n, permettant de définir les paramètres "emailRecipient", "newsTopics" et "newsletterStyle".](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000412_seg9.jpg)
*⏱️ 00:04:12 — Gros plan sur la fenêtre de configuration du nœud "Workflow Configuration" dans n8n, permettant de définir les paramètres "emailRecipient", "newsTopics" et "newsletterStyle".*

---

### ⏱️ `[00:04:21 - 00:04:43]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> style, which is professional summary with key highlights. So all that looks good. We would obviously have to configure our own email recipient right here. But let's move on to the next node, which was our news research agent. So by clicking to this guy, what we can do is we can look at the user message as well as the system message. And another cool thing in this update, once you guys have it, is that you can open these up on the side if you want to just look at it full screen.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (automatisation de workflows).

**Contenu textuel & Code** : - Image #1 : Champs "emailRecipient", "newsTopics" (technology, AI, business) et "newsletterStyle" (professional summary with key highlights).
- Image #3 : Prompt système détaillant le rôle d'assistant de recherche et l'utilisation d'outils web pour générer des newsletters basées sur des variables dynamiques.

**Action / Démonstration** : Navigation et inspection des paramètres de configuration à l'intérieur des nœuds d'un agent de recherche d'actualités automatisé.

![Interface de configuration du nœud "Workflow Configuration" montrant les paramètres d'email, les sujets d'actualité et le style de la newsletter.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000426_seg10.jpg)
*⏱️ 00:04:26 — Interface de configuration du nœud "Workflow Configuration" montrant les paramètres d'email, les sujets d'actualité et le style de la newsletter.*

![Vue d'ensemble du canevas de workflow n8n montrant l'enchaînement des agents, du déclencheur matinal jusqu'à l'envoi de l'email.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000432_seg10.jpg)
*⏱️ 00:04:32 — Vue d'ensemble du canevas de workflow n8n montrant l'enchaînement des agents, du déclencheur matinal jusqu'à l'envoi de l'email.*

![Panneau de configuration du "News Research Agent" affichant le prompt système et les instructions pour la recherche d'actualités.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000437_seg10.jpg)
*⏱️ 00:04:37 — Panneau de configuration du "News Research Agent" affichant le prompt système et les instructions pour la recherche d'actualités.*

---

### ⏱️ `[00:04:43 - 00:05:18]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So the user message for this agent is to research today's most important news and create a personalized newsletter for blank, which is the email recipient. Honestly, that's not super crucial because it doesn't really matter the email address it's going to. It should just be a good newsletter, but it's cool to see that it's able to use context and pass variables through. Anyways, it then said to include five to seven top stories with brief summaries and source links, make it engaging and informative. So one note here, typically with these sort of system instructions, that's really defining the behavior of the agent, I would throw in the system message rather than the user message, meaning I would put that down here rather

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflows).

**Contenu textuel & Code** : Prompt : "Research today's most important news and create a personalized newsletter for {{ $('Workflow Configuration').first().json.emailRecipient }}. Include 5-7 top stories with brief summaries and source links. Make it engaging and informative." Le workflow inclut des nœuds : Daily Morning Trigger, Workflow Configuration, News Research Agent, OpenAI Chat Model et Web Research Tool.

**Action / Démonstration** : Configuration du prompt système dans le nœud "News Research Agent" du workflow.

![Une vue de l'interface n8n montrant un workflow automatisé pour un agent de recherche d'actualités, avec un panneau latéral affichant le prompt système.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000452_seg11.jpg)
*⏱️ 00:04:52 — Une vue de l'interface n8n montrant un workflow automatisé pour un agent de recherche d'actualités, avec un panneau latéral affichant le prompt système.*

---

### ⏱️ `[00:05:18 - 00:05:50]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> than up here. That's not a huge deal, but just a little thing I noticed. But let's check out the actual system prompt, which is setting the role and the behavior of the agent itself. It says you are a news research assistant. Research the latest news on topics specified by the user and create a well-formatted newsletter. Use the web research tool to gather current information from multiple sources. Focus on these topics. Passes over a variable. Format the newsletter in blank, which is the newsletter style. And then it says with clear headlines, summaries, and source links. So we've noticed that it says use the web research tool to gather information. That's nice.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflow d'automatisation).

**Contenu textuel & Code** : Un prompt système pour un "News Research Agent" incluant des variables dynamiques : `{{ $('Workflow Configuration').first().json.newsTopics }}` et `{{ $('Workflow Configuration').first().json.newsletterStyle }}`.

**Action / Démonstration** : Modification et visualisation du prompt système configuré pour définir le rôle et le comportement de l'agent de recherche d'actualités.

![Une capture d'écran montrant l'interface d'édition de prompt au sein d'un nœud de workflow, avec un volet d'expression JavaScript à gauche et le résultat généré à droite.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000526_seg12.jpg)
*⏱️ 00:05:26 — Une capture d'écran montrant l'interface d'édition de prompt au sein d'un nœud de workflow, avec un volet d'expression JavaScript à gauche et le résultat généré à droite.*

---

### ⏱️ `[00:05:50 - 00:06:19]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Let's see what's actually going on down below in this tool. Okay, so you can see the tool is not configured at all It's still a default get request. There's no endpoint. There's no description So the tool isn't configured We would have to do that ourselves here Not too bad Especially for a first pass and then what I'm assuming is the output of this agent gets passed over as a variable in the Body of the email as you can see right here We have the HTML and the text and then we do get a daily news newsletter which is today's date and it's formatted nicely.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (plateforme d'automatisation de workflows).

**Contenu textuel & Code** : Nœuds de workflow : "Daily Morning Trigger", "Workflow Configuration", "News Research Agent", "OpenAI Chat Model", "Web Research Tool", "Send Newsletter Email". Configuration JSON et expressions JavaScript (`new Date().toLocaleDateString()`, `{{ $json.output }}`).

**Action / Démonstration** : Navigation et inspection des paramètres internes des nœuds du workflow pour vérification de la configuration.

![Fenêtre de configuration du nœud "Web Research Tool" montrant les paramètres HTTP GET par défaut non configurés.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000557_seg13.jpg)
*⏱️ 00:05:57 — Fenêtre de configuration du nœud "Web Research Tool" montrant les paramètres HTTP GET par défaut non configurés.*

![Vue d'ensemble du canevas n8n représentant un workflow d'agent de recherche de nouvelles avec différents nœuds connectés.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000605_seg13.jpg)
*⏱️ 00:06:05 — Vue d'ensemble du canevas n8n représentant un workflow d'agent de recherche de nouvelles avec différents nœuds connectés.*

![Fenêtre de configuration du nœud "Send Newsletter Email" montrant les champs pour l'envoi d'e-mails avec des expressions dynamiques (JSON).](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000612_seg13.jpg)
*⏱️ 00:06:12 — Fenêtre de configuration du nœud "Send Newsletter Email" montrant les champs pour l'envoi d'e-mails avec des expressions dynamiques (JSON).*

---

### ⏱️ `[00:06:20 - 00:06:38]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that's a nice touch as well. Cool. So that is just to show you guys a very, very vague prompt. It works, but then there's going to be a lot more to configure. So what we're going to do is we're going to go back. We're going to build this exact same system again, but I'm going to give it a much more detailed prompt and we'll compare how much better it is. All right. So I'm back with a more detailed prompt and I'm going to shoot it off.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : LangFlow (plateforme de construction de flux de travail IA).

**Contenu textuel & Code** : Diagramme de flux composé de nœuds : "Daily Morning Trigger", "Workflow Configuration", "News Research Agent" (relié à un "OpenAI Chat Model" et un "Web Research Tool") et "Send Newsletter Email".

**Action / Démonstration** : Le workflow est affiché en mode édition, prêt à être exécuté ou configuré par l'utilisateur.

![Une capture d'écran montrant l'interface visuelle de LangFlow avec un workflow automatisé pour la recherche de nouvelles et l'envoi de newsletters.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000624_seg14.jpg)
*⏱️ 00:06:24 — Une capture d'écran montrant l'interface visuelle de LangFlow avec un workflow automatisé pour la recherche de nouvelles et l'envoi de newsletters.*

---

### ⏱️ `[00:06:38 - 00:07:14]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I said to build an AI newsletter workflow that runs every morning at 7am and it should use Tavoli and Perplexity to research the top five trending AI and tech news stories. Then I said pass the results into Anthropic Cloud 3.5 Sonnet to write a well-structured email in HTML format. So what I wanted to do here was tell it exactly what chat model I wanted to use and the different tools that I wanted to use so it didn't just try to throw together a random HTTP request. I said the email should include a clear title, it should have subheaders for every story, it should use bold text, a short two to three sentence summary for each story, and at the bottom of the email we should have a sources section with the links to

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow).

**Contenu textuel & Code** : Prompt détaillé décrivant la création d'un workflow : utiliser Tavily et Perplexity pour la recherche, Claude 3.5 Sonnet pour la rédaction HTML, et Gmail pour l'envoi.

**Action / Démonstration** : L'assistant IA de n8n est en phase de réflexion ("Thinking...") après avoir reçu les instructions utilisateur pour générer les nœuds du workflow.

![Interface de n8n montrant le panneau latéral "n8n AI Assistant" où l'utilisateur saisit un prompt détaillé pour créer un workflow de newsletter IA automatisée.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000647_seg15.jpg)
*⏱️ 00:06:47 — Interface de n8n montrant le panneau latéral "n8n AI Assistant" où l'utilisateur saisit un prompt détaillé pour créer un workflow de newsletter IA automatisée.*

---

### ⏱️ `[00:07:14 - 00:07:40]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> all of the articles that it gathered. So once again, it searched through the nodes, it got all the details, and now it has a bit of a different workflow structure for us and we can go ahead and request changes if we want. But for now, we're gonna test out the one-shot prompting and I'm just gonna go ahead and approve this plan. And one thing that's interesting is Tavoli does have a community node, but maybe in this instance, I haven't installed it, or maybe because it's searching through NNN sort of node documentation, maybe it wasn't able to find that and pull it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflow avec volet latéral "n8n AI Assistant").

**Contenu textuel & Code** : Le panneau latéral affiche un résumé complet du workflow généré (newsletter IA quotidienne) incluant les étapes : "Daily 7 AM Trigger", "Tavily News Research", "Perplexity News Research", "Claude 3.5 Sonnet Model", et "Send Newsletter Email".

**Action / Démonstration** : L'assistant IA a terminé la planification et propose deux options à l'utilisateur : "Approve Plan" ou "Request Changes".

![Interface de la plateforme d'automatisation n8n affichant un assistant IA en pleine génération de workflow.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000721_seg16.jpg)
*⏱️ 00:07:21 — Interface de la plateforme d'automatisation n8n affichant un assistant IA en pleine génération de workflow.*

---

### ⏱️ `[00:07:40 - 00:08:05]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But either way, we'll see how it's able to set up these requests. Okay, there we go. So once again, it's done and it gave us a setup guide. So we'd have to configure our email address. We'd have to get Tably API key, Perplexity, Anthropic, Gmail, stuff like that. But let's go take a look at what it did with the workflow configuration. So once again, it did a set node upfront to set the email, the newsletter title, Tably API key, and the research query.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow low-code).

**Contenu textuel & Code** : Workflow composé de nœuds (Daily 7 AM Trigger, Tavily, Perplexity, Newsletter Writer Agent, Gmail) et une liste d'instructions textuelles "How to Setup" pour configurer les API et les identifiants.

**Action / Démonstration** : L'agent IA vient de finaliser la création du workflow et affiche le guide de configuration étape par étape pour l'utilisateur.

![Interface n8n affichant un workflow automatisé pour une newsletter quotidienne avec un assistant IA latéral fournissant des instructions de configuration.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000747_seg17.jpg)
*⏱️ 00:07:47 — Interface n8n affichant un workflow automatisé pour une newsletter quotidienne avec un assistant IA latéral fournissant des instructions de configuration.*

---

### ⏱️ `[00:08:05 - 00:08:26]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Okay, interesting. So what it would be doing is it would have us put our Tably API key here. And then because this is an HTTP request, it would basically just pass it over somewhere in here. Okay, right here. It would pass it over in the actual body request of the HTTP to Tably. So that is pretty cool though, because based on what I'm looking at, this does look correct.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflows).

**Contenu textuel & Code** : Workflow composé des nœuds : "Daily 7 AM Trigger", "Workflow Configuration", "Tavily News Research" (requête POST vers api.tavily.com), "Perplexity News Research" et "Combine Research Results". Le panneau latéral contient une liste de 5 étapes de configuration ("How to Setup").

**Action / Démonstration** : Le présentateur explique la configuration du nœud "Tavily News Research" et l'utilisation de la clé API au sein de la requête HTTP.

![Une capture d'écran de l'interface n8n montrant un workflow d'automatisation pour un générateur de newsletter, avec un panneau latéral affichant les instructions de configuration pour Tavily API, Perplexity et Anthropic.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000810_seg18.jpg)
*⏱️ 00:08:10 — Une capture d'écran de l'interface n8n montrant un workflow d'automatisation pour un générateur de newsletter, avec un panneau latéral affichant les instructions de configuration pour Tavily API, Perplexity et Anthropic.*

---

### ⏱️ `[00:08:26 - 00:08:48]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Meaning if we gave it a research query and our API key, this would work. So I'm actually just going to go ahead and do that real quick and throw my Tably API key in right there. And then we're going to take a look at perplexity real quick. I've connected my perplexity account, so we should be good there. And then our user message is actually going to be fixed. So every day it's just going to search for find the top five trending AI tech news stories from today.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (interface de création de workflows automatisés)

**Contenu textuel & Code** : Champs de saisie pour API keys (tavilyApiKey), requêtes de recherche (researchQuery : "trending AI technology news artificial intelligence machine learning") et instructions de configuration étape par étape dans le panneau de l'assistant AI.

**Action / Démonstration** : L'utilisateur est en train de configurer les variables d'environnement et les clés API nécessaires au bon fonctionnement du workflow automatisé d'IA.

![Une fenêtre de configuration de workflow au centre affiche divers champs de paramètres (emailRecipient, newsletterTitle, tavilyApiKey, researchQuery) tandis que le panneau latéral droit montre l'assistant n8n AI détaillant les étapes de configuration du projet.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000832_seg19.jpg)
*⏱️ 00:08:32 — Une fenêtre de configuration de workflow au centre affiche divers champs de paramètres (emailRecipient, newsletterTitle, tavilyApiKey, researchQuery) tandis que le panneau latéral droit montre l'assistant n8n AI détaillant les étapes de configuration du projet.*

---

### ⏱️ `[00:08:48 - 00:09:08]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that's all configured. It's obviously a lot easier for N8N to configure native nodes rather than an HTTP request. But you can see right here it was able to do a good job with Tably. We've got a merge node which is appending those results. And then we have our newsletter writer agent. We'll take a look at how this thing was prompted. Okay, so first let's look at the user message. Which is saying create an HTML newsletter from the following research data.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (Workflow automation platform).

**Contenu textuel & Code** : Workflow : "Daily 7 AM Trigger", "Tavily News Research", "Perplexity News Research", "Combine Research Results". Configuration du nœud : Prompt demandant la création d'une newsletter HTML à partir de données JSON, System Message définissant le rôle d'expert en newsletter IA.

**Action / Démonstration** : Visualisation et configuration des paramètres des nœuds au sein du canvas de workflow n8n pour l'automatisation de la génération de contenu.

![Interface n8n montrant un workflow d'automatisation de newsletter avec des nœuds de recherche (Tavily, Perplexity) et un nœud de fusion.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000853_seg20.jpg)
*⏱️ 00:08:53 — Interface n8n montrant un workflow d'automatisation de newsletter avec des nœuds de recherche (Tavily, Perplexity) et un nœud de fusion.*

![Configuration détaillée du nœud "Newsletter Writer Agent" dans n8n, affichant le prompt système et la structure du message utilisateur.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000903_seg20.jpg)
*⏱️ 00:09:03 — Configuration détaillée du nœud "Newsletter Writer Agent" dans n8n, affichant le prompt système et la structure du message utilisateur.*

---

### ⏱️ `[00:09:08 - 00:09:45]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then here is where we get all the research data. And then once again, it's giving us the format requirements up here I would personally put this in the system prompt instead, but still let's read through it real quick It's telling it to start with headers and then here would be the newsletter title. We would have header two tags We would have strong bold tags. We would have two to three sentence summaries So everything that I wanted in the initial prompt that I gave to this agent builder It has put into the prompt and then real quick Let's check out the actual system prompt, which is pretty short I would have expected this to be a little more detailed. It says you are an expert newsletter writer specializing in AI and tech news. Your task is to create a well formatted HTML newsletter from research data

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow).

**Contenu textuel & Code** : Un prompt définissant les exigences de formatage HTML pour une newsletter : utilisation de tags `<h1>`, `<h2>`, `<strong>`, structuration des résumés d'articles et inclusion d'une section sources, incluant des variables dynamiques `{ { $json.toJsonString() } }`.

**Action / Démonstration** : L'utilisateur visualise et explique les paramètres de configuration du noeud responsable de la mise en forme du contenu de la newsletter.

![Interface d'édition de noeud dans n8n montrant la configuration d'une "Expression" pour la rédaction d'une newsletter.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000917_seg21.jpg)
*⏱️ 00:09:17 — Interface d'édition de noeud dans n8n montrant la configuration d'une "Expression" pour la rédaction d'une newsletter.*

---

### ⏱️ `[00:09:45 - 00:10:20]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So then after it's able to write that newsletter It would go ahead and send it to the email recipient that we set earlier It would have a subject of the newsletter title plus today's date and then it would send it over as HTML formatting So now that we have no more read I've connected all my credentials I'm gonna go ahead and fill in the email that it's gonna send this to and then we'll just give it a run and see how it works All right, so I'm gonna go ahead and run this and it's gonna do research with Tavoli perplexity And then once that agent writes the final newsletter will go to my Gmail and we'll check it out Okay, interesting. So we already found one thing that's going wrong, which is it appended the data rather than merging it all back together

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (plateforme d'automatisation de workflow).

**Contenu textuel & Code** : Expressions JavaScript pour la récupération dynamique des données : `{{ $('Workflow Configuration').first().json.newsletterTitle }} - {{ $now.format('MMMM d, yyyy') }}`.

**Action / Démonstration** : Configuration détaillée des paramètres d'envoi d'e-mail et visualisation de l'exécution complète du pipeline d'automatisation de la newsletter.

![Interface de configuration du nœud "Send Newsletter Email" dans n8n, montrant les paramètres Gmail, l'objet dynamique avec la date du jour et le formatage HTML.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_000954_seg22.jpg)
*⏱️ 00:09:54 — Interface de configuration du nœud "Send Newsletter Email" dans n8n, montrant les paramètres Gmail, l'objet dynamique avec la date du jour et le formatage HTML.*

![Vue d'ensemble du workflow "Daily AI News Newsletter Generator" dans n8n, incluant les étapes de recherche (Tavily/Perplexity), l'agent Claude 3.5 Sonnet et l'envoi final.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001011_seg22.jpg)
*⏱️ 00:10:11 — Vue d'ensemble du workflow "Daily AI News Newsletter Generator" dans n8n, incluant les étapes de recherche (Tavily/Perplexity), l'agent Claude 3.5 Sonnet et l'envoi final.*

---

### ⏱️ `[00:10:20 - 00:10:58]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So this output two items which basically means we got two different newsletter copies So that's something we'll have to change but real quick Let's go check in to see how they actually turned out. Okay, so here's the first one and at first glance it looks great We've got a title. We've got different sources Maybe we want a little more meat in each of these sections But we do have our sources section down below and if we clicked into them We could see that they are real links that take us to articles and that is how the newsletter was actually created So that's the first one. This is probably the one that was tabloos research and now let's go look at the perplexity one Wow, so this one looks cool. This one was formatted differently So that's the importance of like being specific on how you want the HTML formatting because it looks a lot different

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Gmail (interface web).

**Contenu textuel & Code** : Le corps de l'e-mail contient des titres de sections sur l'IA (McKinsey, Santé, Modèles compacts, Innovations corporate) suivis de "Key insights" et d'une liste de sources en bas de page.

**Action / Démonstration** : Le présentateur affiche et examine le rendu visuel de la newsletter générée par l'automatisation.

![Aperçu du contenu d'un e-mail reçu dans Gmail, présentant la première version d'une newsletter générée automatiquement intitulée "Today's AI Newsletter".](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001030_seg23.jpg)
*⏱️ 00:10:30 — Aperçu du contenu d'un e-mail reçu dans Gmail, présentant la première version d'une newsletter générée automatiquement intitulée "Today's AI Newsletter".*

---

### ⏱️ `[00:10:58 - 00:11:30]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then we've got our sources down below, of course, again, which we can click on and it takes us to real articles This one actually pulled from a YouTube video, which is kind of cool. And we've also got a tech crunch AI Article. So that's kind of how the output was coming out So like I said, there's a few things that we want to change about this And what I'm curious to see is if we're able to use the AI builder to actually make changes So at the bottom it says let me know if you'd like to adjust anything Okay, so I gave it some constructive criticism and what's cool is it's thinking and it's working So we may see this in real time actually make these changes. Okay, so we got a little error

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Gmail (interface web) et n8n (plateforme d'automatisation de workflows).

**Contenu textuel & Code** : - Image 1 : Contenu textuel d'une newsletter IA avec des titres comme "Anthropic's Landmark Copyright Settlement" et une liste de sources (Crescando AI News, TechCrunch, etc.).
- Image 2 : Diagramme de workflow avec des nœuds de déclenchement (Daily 7 AM Trigger), des outils de recherche (Tavily, Perplexity), un agent d'écriture (Newsletter Writer Agent) lié à Claude 3.5 Sonnet, et une action finale d'envoi Gmail.

**Action / Démonstration** : - Image 1 : Illustration du résultat final de l'automatisation : un email envoyé avec succès contenant du contenu structuré.
- Image 2 : Présentation de l'architecture logique du workflow permettant la collecte, la rédaction et l'envoi automatisé de la newsletter.

![Une interface Gmail montrant un email généré automatiquement contenant des résumés d'actualités sur l'IA et une section "Sources" avec des liens cliquables.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001106_seg24.jpg)
*⏱️ 00:11:06 — Une interface Gmail montrant un email généré automatiquement contenant des résumés d'actualités sur l'IA et une section "Sources" avec des liens cliquables.*

![L'éditeur de workflow n8n montrant un pipeline automatisé intitulé "Daily AI News Newsletter Generator", utilisant Tavily, Perplexity, Claude 3.5 Sonnet et Gmail.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001114_seg24.jpg)
*⏱️ 00:11:14 — L'éditeur de workflow n8n montrant un pipeline automatisé intitulé "Daily AI News Newsletter Generator", utilisant Tavily, Perplexity, Claude 3.5 Sonnet et Gmail.*

---

### ⏱️ `[00:11:30 - 00:11:57]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Not sure what's going on there, but it looks like it is still working But anyways, what's going on here is I said the data wasn't merged correctly So I told it we should want one newsletter for both sources and then I wanted it to change the newsletter prompt to actually have Inline citations as well not just a sources section at the bottom So we want to know where each sentence is actually coming from explicitly. All right So it looks like it fixed it It found the issue, which was the merge node was set to append rather than sort of like combining stuff.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow low-code).

**Contenu textuel & Code** : Workflow composé de nœuds (Daily 7 AM Trigger, Tavily News Research, Perplexity News Research, Combine Research Results, Newsletter Writer Agent, Send Newsletter Email). Le chat latéral affiche une requête utilisateur demandant de fusionner les résultats de recherche et d'ajouter des citations en ligne dans la newsletter.

**Action / Démonstration** : L'utilisateur interagit avec l'assistant IA de n8n pour modifier la logique du workflow ("Newsletter Writer Agent") afin de corriger la fusion des données provenant de sources multiples.

![Une capture d'écran de l'interface n8n montrant un workflow de génération de newsletter automatisée et un panneau de chat latéral où l'utilisateur demande une correction sur la fusion des données et l'ajout de citations.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001137_seg25.jpg)
*⏱️ 00:11:37 — Une capture d'écran de l'interface n8n montrant un workflow de génération de newsletter automatisée et un panneau de chat latéral où l'utilisateur demande une correction sur la fusion des données et l'ajout de citations.*

---

### ⏱️ `[00:11:58 - 00:12:18]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And now it told us here are the changes that we made and how it works. So what I'm going to do is just go ahead and save. I'm going to execute the workflow and we'll just see if it did actually make those changes the way we wanted. And then we'll take a look at the final copy. And actually, just because I'm curious while it's doing this, I do want to see what it added into the system prompt of the AI agent or into the user prompt.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Plateforme d'automatisation de workflows n8n.

**Contenu textuel & Code** : Logique de workflow (nœuds, connexions, paramètres), prompt système de l'agent IA, instructions de fusion de données, et configuration du modèle Claude 3.5 Sonnet.

**Action / Démonstration** : Sauvegarde du workflow, lancement de l'exécution et inspection des paramètres de configuration du nœud agent.

![Vue d'ensemble de l'interface n8n affichant un workflow d'automatisation de newsletter avec des nœuds de recherche (Tavily/Perplexity) et un agent Claude 3.5 Sonnet, accompagnée du panneau latéral de l'IA détaillant les modifications apportées.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001203_seg26.jpg)
*⏱️ 00:12:03 — Vue d'ensemble de l'interface n8n affichant un workflow d'automatisation de newsletter avec des nœuds de recherche (Tavily/Perplexity) et un agent Claude 3.5 Sonnet, accompagnée du panneau latéral de l'IA détaillant les modifications apportées.*

![Gros plan sur la configuration interne du nœud "Newsletter Writer Agent" dans n8n, montrant le champ de prompt utilisateur, les options du modèle et l'état d'exécution en attente.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001213_seg26.jpg)
*⏱️ 00:12:13 — Gros plan sur la configuration interne du nœud "Newsletter Writer Agent" dans n8n, montrant le champ de prompt utilisateur, les options du modèle et l'état d'exécution en attente.*

---

### ⏱️ `[00:12:18 - 00:12:50]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Okay, so it added it into the user prompt and it said to include inline citations using one two etc after each sentence so that's basically the one change it made to the prompt and Now we'll take a look and once again It didn't actually change that merge node even though it knew it was wrong. It still has it appending So it's still going to create two different sources. So this is why it's really really important to still understand What workflows are doing because not only is having that knowledge going to make it easier for you to prompt this AI builder on what to build but it's going to actually help you troubleshoot and figure out, okay, maybe I'll just have to

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflow low-code).

**Contenu textuel & Code** : Diagramme de flux comprenant les nœuds : "Daily 7 AM Trigger", "Workflow Configuration", "Tavily News Research", "Perplexity News Research", "Combine Research Results", "Newsletter Writer Agent" (lié à un modèle "Claude 3.5 Sonnet") et "Send Newsletter Email".

**Action / Démonstration** : Le workflow est en cours d'exécution ("Executing workflow"), ce qui correspond au test de l'agent après la modification du prompt mentionnée par le présentateur.

![Une capture d'écran de l'interface de travail n8n montrant un workflow d'automatisation pour un "Daily AI News Newsletter Generator", avec des nœuds de recherche Tavily et Perplexity reliés à un agent de rédaction utilisant le modèle Claude 3.5 Sonnet.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001226_seg27.jpg)
*⏱️ 00:12:26 — Une capture d'écran de l'interface de travail n8n montrant un workflow d'automatisation pour un "Daily AI News Newsletter Generator", avec des nœuds de recherche Tavily et Perplexity reliés à un agent de rédaction utilisant le modèle Claude 3.5 Sonnet.*

---

### ⏱️ `[00:12:50 - 00:13:21]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> manually go change this real quick and then leverage AI to help me more with the prompting or with other variables to be passed over. But anyways, real quick, let's just go see if those inline sources came out. All right. Okay, cool. So we do have numbers like this is number one, this is number five, and you can see what they relate to down here. It would have been nice if it would have made these clickable as well. But because I didn't give it super, super detailed instructions, it didn't do that. Once again, the importance here is all the context that you feed into these AI assistants to help you do your job better and faster. But obviously this system works.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (workflow automation), Gmail (messagerie).

**Contenu textuel & Code** : - n8n : Nœuds de trigger, recherche Tavily/Perplexity, agent Newsletter Writer avec modèle Claude 3.5 Sonnet.
- Gmail : Texte de newsletter avec citations de type [1], [5] et une section finale "Sources" listant les références numérotées.

**Action / Démonstration** : - Image 1 : L'assistant IA n8n explique les modifications apportées au workflow (gestion des données, mode de fusion et formatage du prompt).
- Image 2 : Vérification du résultat final reçu dans Gmail pour confirmer l'intégration correcte des sources et de la numérotation.

![Interface n8n montrant un workflow d'automatisation de newsletter avec un assistant IA actif sur le panneau latéral droit.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001258_seg28.jpg)
*⏱️ 00:12:58 — Interface n8n montrant un workflow d'automatisation de newsletter avec un assistant IA actif sur le panneau latéral droit.*

![Interface Gmail affichant une newsletter générée automatiquement, incluant des citations numérotées dans le texte et une liste de sources en fin de message.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001305_seg28.jpg)
*⏱️ 00:13:05 — Interface Gmail affichant une newsletter générée automatiquement, incluant des citations numérotées dans le texte et une liste de sources en fin de message.*

---

### ⏱️ `[00:13:21 - 00:13:57]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All I had to do was put in my email address and my API keys. And then we are getting a newsletter that's formatted, which this was a lot quicker than if I would have built all this myself and prompted everything myself. All right. And so for the last test that we're going to do today, I'm just going to try to throw a pretty complex system at it. So I'm basically having it build a personal assistant. I said, I want to interact with it through Telegram. I want to have a Gmail subagent, a calendar subagent, a ClickUp subagent, and then it should use the think tool and use CloudSonna 3.7. So I'm interested to see how this is able to use an orchestrator agent with sub-agents and sub-tools and what it's going to do with those system prompts. Because in my mind,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (plateforme d'automatisation de workflow low-code).

**Contenu textuel & Code** : Le graphe de workflow comprend les étapes suivantes : "Daily 7 AM Trigger", "Workflow Configuration", "Tavily News Research", "Perplexity News Research", "Combine Research Results", "Newsletter Writer Agent" (utilisant le modèle "Claude 3.5 Sonnet") et "Send Newsletter Email".

**Action / Démonstration** : Le workflow est affiché à l'écran, prêt à être lancé via le bouton "Execute workflow" situé en bas au centre.

![Interface de la plateforme n8n affichant un workflow automatisé intitulé "Daily AI News Newsletter Generator", avec des nœuds connectés pour la recherche, la rédaction par IA et l'envoi d'e-mails.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001330_seg29.jpg)
*⏱️ 00:13:30 — Interface de la plateforme n8n affichant un workflow automatisé intitulé "Daily AI News Newsletter Generator", avec des nœuds connectés pour la recherche, la rédaction par IA et l'envoi d'e-mails.*

---

### ⏱️ `[00:13:57 - 00:14:25]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> this type of AI agent builder, natively in NNN, is going to be really, really good at workflows and passing over variables, but it may struggle a little bit more with autonomous systems. So let's let it search through the nodes and then we'll take a look. All right. So here it is. It's not great because we asked for our Gmail sub-agent and our Calendar sub-agent to have all of the tools, not just one, which here it's just send message and here is just create an event and ClickUp is just create a task.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflows).

**Contenu textuel & Code** : Prompt utilisateur détaillé demandant un assistant IA personnel avec des sous-agents pour Gmail, Calendar et ClickUp, utilisant la mémoire, un outil de réflexion ("think tool") et le modèle Claude Sonnet 3.7. Le panneau affiche les étapes en cours : "Searching nodes" et "Getting node details".

**Action / Démonstration** : L'assistant IA analyse les besoins de l'utilisateur et cherche les nœuds appropriés dans la bibliothèque n8n pour générer le workflow.

![Interface n8n affichant le panneau latéral "AI Assistant Builder" en train de traiter une requête complexe d'utilisateur pour construire un assistant IA multi-agents.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001404_seg30.jpg)
*⏱️ 00:14:04 — Interface n8n affichant le panneau latéral "AI Assistant Builder" en train de traiter une requête complexe d'utilisateur pour construire un assistant IA multi-agents.*

---

### ⏱️ `[00:14:25 - 00:14:59]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But let's take a look at how it's actually configured. So what's nice is that at least it labels everything and it tells you how to use it and what you need to set up. We're getting our Telegram input and then we're setting the system prompt and the user preferences and I'm assuming that those will feed right into the agent itself. But if we actually click into the agent I already see one big issue which is that it's looking for the connected chat trigger node for the input which is not actually here right now. Anyways from here the system message is basically saying you are a sophisticated personal assistant that helps users manage their digital life. You have access to specialized sub-agents for Gmail, Google,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (plateforme d'automatisation de workflow low-code).

**Contenu textuel & Code** : Configuration du "System Message" définissant le rôle de l'assistant IA, sélection des modèles (Claude Sonnet 3.7), et architecture des nœuds (Telegram Trigger, sous-agents, outils d'opérations).

**Action / Démonstration** : Navigation dans le canevas de workflow et ouverture du panneau de configuration des paramètres du nœud agent principal pour définir les instructions du système.

![Vue d'ensemble d'un workflow complexe dans n8n illustrant un assistant personnel multi-agents connecté à Telegram, incluant divers sous-agents pour Gmail, Google Calendar et ClickUp.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001433_seg31.jpg)
*⏱️ 00:14:33 — Vue d'ensemble d'un workflow complexe dans n8n illustrant un assistant personnel multi-agents connecté à Telegram, incluant divers sous-agents pour Gmail, Google Calendar et ClickUp.*

![Gros plan sur l'interface de configuration du nœud "Main Personal Assistant Agent", montrant les paramètres du prompt système, la sélection du modèle de chat et la gestion de la mémoire et des outils.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001442_seg31.jpg)
*⏱️ 00:14:42 — Gros plan sur l'interface de configuration du nœud "Main Personal Assistant Agent", montrant les paramètres du prompt système, la sélection du modèle de chat et la gestion de la mémoire et des outils.*

---

### ⏱️ `[00:14:59 - 00:15:21]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and ClickUp and you can use the Think tool to analyze requests, always provide helpful professional responses. So it may have just got confused with Telegram because I don't know if the chat ID and everything is configured correctly as well or the memory itself. But let's take a look at these sub agents and see how they're working. So we've got our user message, which is the Gmail request. Up here it says you are a specialized agent for Gmail operations.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Outil d'automatisation de workflows (n8n ou plateforme similaire de construction d'agents IA).

**Contenu textuel & Code** : Le "System Message" définit le rôle de l'IA : "You are a sophisticated personal assistant AI that helps users manage their digital life. You have access to specialized sub-agents for Gmail, Google Calendar, and ClickUp operations. Use the think tool to analyze requests and delegate."

**Action / Démonstration** : Le présentateur examine les paramètres de configuration du nœud de l'agent, notamment le message système et les options comme "Max Iterations" (fixé à 10) et "Enable Streaming".

![Interface de configuration d'un nœud "Main Personal Assistant Agent" dans un outil d'automatisation de workflow (type n8n).](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001504_seg32.jpg)
*⏱️ 00:15:04 — Interface de configuration d'un nœud "Main Personal Assistant Agent" dans un outil d'automatisation de workflow (type n8n).*

---

### ⏱️ `[00:15:21 - 00:15:52]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And down here it says you are a Gmail specialist to handle all email operations efficiently, even though it only has one tool. And then I'm assuming that the other sub agents are set up the same way. This one actually doesn't even have a user message. So this agent would error right away. And same thing with the ClickUp sub-agent, there's no user message here. The easiest way to fix that is we would literally just click on this button and the agent itself would be able to get a message from the main agent. But anyways, this kind of proved the point that I was trying to make, which is you probably don't want to use this to build complex multi-agent autonomous systems.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de conception d'agents IA (probablement une plateforme de type low-code/no-code comme n8n ou similaire).

**Contenu textuel & Code** : Configuration du "Calendar Sub-Agent" avec une description ("Specialized agent for Google Calendar operations"), un champ "Prompt (User Message)" vide marqué d'une alerte, et un "System Message" définissant l'agent comme un spécialiste de Google Calendar.

**Action / Démonstration** : Le présentateur passe en revue les paramètres du nœud agent et souligne l'absence de message utilisateur ("User Message"), ce qui provoquera une erreur d'exécution.

![Une fenêtre contextuelle de configuration d'un "Calendar Sub-Agent" affichant les paramètres système, le prompt utilisateur vide et les options de modèles de chat.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001529_seg33.jpg)
*⏱️ 00:15:29 — Une fenêtre contextuelle de configuration d'un "Calendar Sub-Agent" affichant les paramètres système, le prompt utilisateur vide et les options de modèles de chat.*

---

### ⏱️ `[00:15:52 - 00:16:26]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Because if I go back into this workflow builder and you can see there's some pre-built ones right here, right? Let's just say we're looking at an invoice processing pipeline. A system like this is going to be a workflow, meaning we're going to go from step one to step two, from step two to step three, and we're going to be able to keep this AI workflow on the path that we set for it very clearly. These types of workflows are a lot more predictable. They're a lot easier for human to build, which means it's going to be a lot easier for an AI system to build. And you can see that these prompts are specific. It's telling the workflow exactly what to extract, what type of information. It's telling it where to store the information in Airtable and when to actually

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflow avec volet d'assistance IA).

**Contenu textuel & Code** : Prompt utilisateur détaillant la création d'un workflow de parsing de factures, extraction de données vers Airtable et envoi d'un rapport hebdomadaire par email.

**Action / Démonstration** : L'assistant IA est en cours d'exécution ("Working...", "Searching nodes") pour générer automatiquement les étapes du pipeline.

![Interface de l'outil n8n affichant un assistant IA en train de traiter une requête de création de workflow pour le traitement automatisé de factures.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001601_seg34.jpg)
*⏱️ 00:16:01 — Interface de l'outil n8n affichant un assistant IA en train de traiter une requête de création de workflow pour le traitement automatisé de factures.*

---

### ⏱️ `[00:16:26 - 00:17:00]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> trigger this AI analysis and what to do with it. So I guess as we sort of start to wrap up here, what I'm trying to say is that this is super, super cool. I think it's going to be great to leverage this to help you with your prompting, setting up your HTTP requests, getting a really good idea of where to start. But what you need to do in order to actually make that efficient is you need to know very clearly what you want to build. And you need to understand how AI workflows actually work fundamentally. Because the more context you can feed in and the more information you have about like where does my data come from? What do I want to do with the data? What fields am I looking for? What type of AI analysis am I going to do? All of that information is going to make

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflows).

**Contenu textuel & Code** : Liste d'étapes de workflow (Invoice Upload Form, OpenAI Chat Model, Invoice Parser AI Agent, etc.) et une fenêtre de chat avec l'IA indiquant "Working..." et "Thinking...".

**Action / Démonstration** : L'assistant IA est en cours d'exécution ou de génération du workflow demandé par l'utilisateur ("Proceed with the plan").

![Interface de la plateforme n8n montrant un assistant IA en train de générer ou configurer un workflow automatisé pour le traitement de factures et l'envoi de rapports.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001635_seg35.jpg)
*⏱️ 00:16:35 — Interface de la plateforme n8n montrant un assistant IA en train de générer ou configurer un workflow automatisé pour le traitement de factures et l'envoi de rapports.*

---

### ⏱️ `[00:17:00 - 00:17:34]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> your job a lot easier and that's going to be super valuable because I'm aware of like sometimes you get in here and you don't know which nodes to use or where to start and this type of technology will give you a really really good place to start and from there you can customize it and learn what's going on. So you guys can see with a workflow like this I'm assuming that all these variables are going to be pretty much perfectly mapped over. We have an AI agent that's given a user prompts in order to parse the information. But look at this, guys, there's actually no live variables being fed into the agent. So this agent knows it needs to parse an invoice, but it's not actually receiving any invoice information. So you still want to be able to

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflows).

**Contenu textuel & Code** : Liste de tâches de l'assistant : "Validation Check", "Store Invoice Data", "Error Notification", "Weekly Report Schedule", "Report Configuration", "Fetch Weekly Invoice Data", "Report Analysis Model", "Spending Analysis AI Agent", "Send Weekly Report". Messages de l'assistant : "Adding nodes" (terminé), "Connecting nodes" (terminé).

**Action / Démonstration** : L'assistant IA est en train de construire et de câbler automatiquement un workflow complexe de traitement de factures et d'analyse de dépenses.

![Interface n8n affichant un workflow en cours de construction automatique par l'assistant IA, avec un panneau latéral de chat détaillant les étapes d'ajout et de connexion des nœuds.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001709_seg36.jpg)
*⏱️ 00:17:09 — Interface n8n affichant un workflow en cours de construction automatique par l'assistant IA, avec un panneau latéral de chat détaillant les étapes d'ajout et de connexion des nœuds.*

---

### ⏱️ `[00:17:34 - 00:18:10]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> look at this and identify that all of this is fixed, and there's no live variables being passed through. But then from there, we have a validation check, which is just making sure that this stuff exists, that it's not empty, everything like that. And if it's true, we're going to store the invoice data in Airtable, which will be the variables that we were looking for earlier. Anyways, I just wanted to show you guys how this AI builder works, my honest thoughts on what it's going to be good at and what it needs to improve on a little bit. And more importantly, I think the mindset of leveraging this stuff should be the same mindset that you have when it comes to AI automation in general, which is AI is not going to do everything, but if it can get me 70% of the way there or cut

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (outil d'automatisation de workflow low-code).

**Contenu textuel & Code** : - Image 1 : Expressions conditionnelles sur des variables JSON (`vendor_name`, `total_amount`, `invoice_date`) avec des opérateurs comme "exists", "is not empty" et "is greater than".
- Image 2 : Architecture du workflow : "Invoice Upload Form" -> "Workflow Configuration" -> "Invoice Parser AI Agent" -> "Validation Check" -> "Store Invoice Data" / "Error Notification".

**Action / Démonstration** : - Image 1 : Configuration des règles de validation des données extraites pour garantir l'intégrité avant le stockage.
- Image 2 : Présentation visuelle de la logique globale du workflow avant l'exécution.

![Fenêtre contextuelle "Validation Check" dans l'interface n8n, détaillant une série de conditions logiques (AND) pour vérifier l'existence et la validité des champs extraits d'une facture.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001743_seg37.jpg)
*⏱️ 00:17:43 — Fenêtre contextuelle "Validation Check" dans l'interface n8n, détaillant une série de conditions logiques (AND) pour vérifier l'existence et la validité des champs extraits d'une facture.*

![Vue d'ensemble du canevas de workflow n8n intitulé "AI Invoice Processing and Weekly Spending Analytics", montrant deux flux distincts connectant des nœuds d'IA, de validation et d'envoi.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001752_seg37.jpg)
*⏱️ 00:17:52 — Vue d'ensemble du canevas de workflow n8n intitulé "AI Invoice Processing and Weekly Spending Analytics", montrant deux flux distincts connectant des nœuds d'IA, de validation et d'envoi.*

---

### ⏱️ `[00:18:10 - 00:18:43]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> down 70% of my time from it, that is a huge win. And that's the way you should be thinking about approaching this as a tool that you can leverage to learn quicker and build quicker. And speaking of learning and building quicker, if that's something you're interested in, then definitely check out my plus community. The link for that is down in the description. We've got a great community of members who are learning and building with NNN every single day. And we also have a straight path to starting to monetize your AI automation and spinning up a one person AI agency. You can learn here as a beginner, move into the foundations of NNN, and then start to figure out how you can actually start to work with clients and build a business off of this. So if that sounds like

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : n8n (éditeur de workflow), Skool (plateforme communautaire).

**Contenu textuel & Code** : Diagrammes de flux avec nœuds "Invoice Parser AI Agent" et "Spending Analysis AI", fils de discussion communautaires, titres de cours (Agent Zero, One Person AI Agency, n8n Templates).

**Action / Démonstration** : Présentation technique d'un workflow d'automatisation puis navigation dans une plateforme éducative pour promouvoir des ressources d'apprentissage.

![Interface de conception de workflow n8n montrant l'automatisation du traitement des factures et des rapports de dépenses.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001818_seg38.jpg)
*⏱️ 00:18:18 — Interface de conception de workflow n8n montrant l'automatisation du traitement des factures et des rapports de dépenses.*

![Interface de la plateforme communautaire Skool "AI Automation Society Plus" affichant le fil d'actualité et les posts épinglés.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001826_seg38.jpg)
*⏱️ 00:18:26 — Interface de la plateforme communautaire Skool "AI Automation Society Plus" affichant le fil d'actualité et les posts épinglés.*

![Vue de l'onglet "Classroom" sur Skool, listant divers modules de formation sur les agents IA et les templates n8n.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001835_seg38.jpg)
*⏱️ 00:18:35 — Vue de l'onglet "Classroom" sur Skool, listant divers modules de formation sur les agents IA et les templates n8n.*

---

### ⏱️ `[00:18:43 - 00:18:57]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> something that you're interested in, then definitely check it out. The link for that is down in the description. But that's going to do it for today. If you guys enjoyed the video or learned something new, please give it a like. Definitely helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one. Thanks, everyone.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Flowise (plateforme low-code pour orchestrer des agents IA).

**Contenu textuel & Code** : Workflow composé de nœuds : "Invoice Upload Form", "Invoice Parser AI Agent", "OpenAI Chat Model", "Validation Check", "Store Invoice Data", et "Spending Analysis AI Agent".

**Action / Démonstration** : Visualisation et présentation du schéma de l'automatisation globale ("AI Invoice Processing and Weekly Spending Analytics") prête à être exécutée.

![Interface de construction de workflow visuel sur la plateforme Flowise, illustrant un processus automatisé de traitement de factures et d'analyse de dépenses.](../screenshots/TDHFkKSTJ30/TDHFkKSTJ30_001850_seg39.jpg)
*⏱️ 00:18:50 — Interface de construction de workflow visuel sur la plateforme Flowise, illustrant un processus automatisé de traitement de factures et d'analyse de dépenses.*

---

