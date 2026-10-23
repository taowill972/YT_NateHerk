# 🎬 How to Build a WhatsApp Agent with n8n (credential tutorial)

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=A0OwvNOLNlw](https://www.youtube.com/watch?v=A0OwvNOLNlw)  
> **Date de publication** : 20250805  
> **Durée** : 00:07:03  
> **Identifiant vidéo** : `A0OwvNOLNlw`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **How to Build a WhatsApp Agent with n8n (credential tutorial)**, Nate Herk décortique les capacités pratiques d'automatisation et de développement propulsées par les modèles de pointe.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Opus 5.5 & Claude Code** : Modèles d'ingénierie et agents de codage autonome.

### 🔑 Points Clés & Enseignements Stratégiques
- Optimiser le niveau d'effort et le raisonnement des modèles IA pour des résultats industriels.
- Automatiser les cycles de création logicielle de bout en bout.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:36]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Today I'm going to show you guys the quickest and easiest way to set up end-to-end with WhatsApp so that when someone messages our business account we can have an AI agent on the back end responding to them, booking in a meeting, whatever we want them to do. So right now you can see I have a WhatsApp trigger and if I click into this you can see that we need to create a credential. So if I click on that it prompts us for a client ID and a secret so we have to head over to business.facebook.com in order to set this up. So this is what the page should look like. I'm going to go ahead and log in with my Facebook account and once you log in it's going to look like this if you've already set up like a business portfolio. If you haven't, on this left hand side, you're going to expand this open and then down here, create business portfolio. And yes, this is

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:00:36 - 00:01:12]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Hercules detailing, which used to be my car detailing company. Anyways, you're going to go down here to the bottom left and click on settings. And then right here under accounts, you can see apps. So you're going to click on that. And then you're going to add an app right here. And you're going to click on create a new app ID. Now right here, it says your account must be confirmed before you can create a new app. So please confirm your account by adding a mobile number or credit card. So if you haven't done that, you're going to go ahead and confirm your account real quick. All right. So now that I went ahead and confirmed my account, I can actually create an app ID. So I'm going to click on that. And what we're going to do is go ahead and create this app. All right. So I just threw in NNN test as my name. I'm going to hit next. Now we have use cases. I'm just going to scroll to the bottom and hit other and continue on. Now we have to select

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:12 - 00:01:47]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> an app type and it cannot be changed after you create the app. So for this case, I'm going to go ahead and use business so we can use WhatsApp. And then we're pretty much just confirming the details and selecting the right business portfolio for this to go under. And now I'm going to click on create app. All right, now that we've got to this screen, what we want to do is set up the WhatsApp. So I'm going to click on the setup button right here. And we're going to go over to the left-hand side under app settings and click on basic. And now here's the screen that we were looking for where we can right here, get our app ID and our secret. So I'm first of all, just going to copy this app ID. We're going to paste that right into here as the client ID. And then I'm going to go back into this screen, copy the app secret and paste it into NN. There we go.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:47 - 00:02:08]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Everything's been set up. I'm going to hit save and we should get a green message right here that that says connection tested successfully. Okay, so now we have the trigger set up, but we need to make sure we set up like a number that it's going to text from and that we can respond back to it. And unfortunately it's not super simple because there's like two different types of credentials, one for the trigger and one for the node that's gonna send a message back to that same number.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:08 - 00:02:29]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So let's set that up real quick. So I'm gonna click on the plus right after the WhatsApp trigger, and I am just going to add an AI agent just so I can show you guys how it'll look when you have an agent getting your messages and responding to you in WhatsApp. And now we just need to connect an AI chat model to give the agent a brain. So I'm just gonna hook up open router real quick. And then what we wanna do is add another node after this agent to send a message back to WhatsApp.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:29 - 00:02:50]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So we'll click on WhatsApp Business Cloud and we will choose send message. And now here's the issue. You can see we don't have a credential set up because this is a different type of WhatsApp node. So we're gonna have to create a new credential, but this is different than a ID and a secret. This is an access token and a business account ID. So let's head back over to our meta suite and set this up.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:50 - 00:03:08]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All right, so we're gonna switch back over here. And what we need to do now is on this left-hand side under WhatsApp, we're gonna click on API setup. So this is what your screen should look like. Right here, you can see we have a test number, which is one that Facebook is just gonna provide. You can go ahead and connect like a business phone number if you want. But right now we're just gonna stick with that test number. And then we also need to input a recipient phone number.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:08 - 00:03:29]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm gonna throw that in there real quick. Now that we've set that up, we can go ahead up here and click generate access token. So I'm gonna click on this button. It's gonna ask us if we're good to continue on this Facebook account. So N8N test will receive your name and profile picture. I'm gonna continue. You can opt in for just this WhatsApp account or you can just opt into all current and future. So I'm gonna do that. And then we're basically just reviewing what this app can do.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:29 - 00:03:48]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So manage your WhatsApp accounts and manage and access conversations in WhatsApp. So if you're good with that, you'll hit save. And now that we're connected, what we have is our access token right up here and our business account right here. So I'm gonna copy the access token and I just pasted that in right here. Switch back over. We're gonna grab our WhatsApp business account ID and then we're gonna paste that in right here.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:48 - 00:04:17]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All right, there we go. to hit save and hopefully we get green once again connection tested successfully and now we can go ahead and test out the whole flow. So I'm going to connect the sender phone number which is the test one that Facebook gave us. I'm going to add in my WhatsApp number with the country code and everything so we can test out if it works and then for the text body I'm just going to put test to make sure that this actually goes through. All right so let's close out here and hit save and so right now just because our workflow is inactive we're going to have to execute workflow every time to make sure that our WhatsApp triggers listening.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:17 - 00:04:36]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Once your app is in production, you won't have to do this. All right, so what I did over here is my WhatsApp, and this is the test number. So I'm gonna hit execute workflow. This triggers now listening for us. So I'm just gonna right here say hi, and we'll see if our antigen workflow grabs it, which it did. But now we just have to actually configure this agent real quick to accept the message.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:36 - 00:04:55]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm gonna click into the agent. For the user message, I'm gonna choose to find below. And all I have to do is drag in the actual field that has the variable, which is our text message. So that would be right here at the bottom. You can see the message I sent was high. So we're going to grab that body field. And now the agent's going to see whatever we send to it in WhatsApp. Okay, so that's set up.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:55 - 00:05:14]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I'm just going to hit save. We're going to hit execute workflow once again. And now it should be listening to us. I don't know why visually it's doing that. Just a little bug. But I'm going to say hello. The WhatsApp trigger is going to get that message. The agent's going to think about it and respond to us. And we get the message that we set up, which was test. So from here, you're basically done.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:14 - 00:05:34]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All you want to do is configure the agent's response. to be the thing that's sent back to us in WhatsApp. So the way we do that is we click into this node right here, instead of sending over test, we're gonna send over the variable, which is whatever the agent responds to us with. So I'm just gonna grab the output, put that right here. And now when we do our final test, this should work and we can have a conversation with this AI agent.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:34 - 00:05:55]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So once again, I'm gonna hit execute workflow. I'm going to come into WhatsApp and just say, tell me a joke. And it's going to get that message. The agent's gonna actually write us a joke and we get it back to us in WhatsApp. It says, sure, here's one for you. Why don't scientists trust atoms? Because they make up everything. And from here, you can obviously like connect memory, you can connect some tools, you can connect your different CRMs or whatever you need to do.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:56 - 00:06:20]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And now people can access this phone number. Once again, you can switch out for your business phone number and you should be able to have this WhatsApp N8N automation built and running for you. And another thing just to keep in mind as well is that if people are able to just constantly text this number right here, if you're using an open router or like an open AI or Anthropic or any closed source AI model where you pay for credits, it will be eating up your credits every time someone messages it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:20 - 00:06:42]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So if someone spams it with like a million messages, that cost will fall on you. So I just wanted to throw that out there real quick, but hopefully now you are set up with WhatsApp and you are good to go and start building some automations. And if you're looking for some support when you're setting up this type of automation on the backend with NNN, definitely check out my paid community. The link for that will be down in the description. And it's a really cool space of almost 2000 members who are always building every day with NNN.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:42 - 00:07:05]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Besides the community aspect, we have a classroom with two full courses, Agent Zero, which is the foundations of AI automation, and then 10 hours to 10 seconds where you learn how to identify, design, and build time-saving automations. I'd love to see you guys in this community, but that's going to do it for the video. If you learned something new or this was helpful, please give it a like. It helps me out a ton, and I'll see you guys in the next one. Thanks so much, everyone.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

