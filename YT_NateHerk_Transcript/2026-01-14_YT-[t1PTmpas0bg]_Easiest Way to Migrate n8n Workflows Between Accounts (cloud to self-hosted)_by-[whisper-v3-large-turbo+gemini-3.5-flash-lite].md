# 🎬 Easiest Way to Migrate n8n Workflows Between Accounts (cloud to self-hosted)

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=t1PTmpas0bg](https://www.youtube.com/watch?v=t1PTmpas0bg)  
> **Date de publication** : 20260114  
> **Durée** : 00:10:58  
> **Identifiant vidéo** : `t1PTmpas0bg`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Easiest Way to Migrate n8n Workflows Between Accounts (cloud to self-hosted)**, Nate Herk décortique les capacités pratiques d'automatisation et de développement propulsées par les modèles de pointe.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Opus 5.5 & Claude Code** : Modèles d'ingénierie et agents de codage autonome.

### 🔑 Points Clés & Enseignements Stratégiques
- Optimiser le niveau d'effort et le raisonnement des modèles IA pour des résultats industriels.
- Automatiser les cycles de création logicielle de bout en bout.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:21]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Today I'm going to be showing you guys a really easy and safe way to migrate hundreds of workflows between two NNN instances. And in this example I'll be going from NNN cloud to my NNN self-hosted. I'm going to give you guys everything that you need for free to do this migration. So first I'm just going to walk through exactly how this workflow works and what it's doing and then at the end I'll show you how you can set it up and how to download all this stuff for free. So let's get into it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:00:21 - 00:00:54]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All right so this is the workflow. It's super simple. It's made up of a total of three different types of nodes. So let me just real quick walk through the actual system and how this works. So you can see we actually have two workflows. We have this one up here and this one and they're both just going to be manually executed So what we're doing up here on the top one is we're going to pull in all of our current workflows from our old instance Using the NNN node We're going to pull in all those workflows and then we're going to push them into a google sheet And the reason we're doing this is just so we have storage of workflows so that we can later check them off So we know which ones we've migrated and which ones we haven't because if you're not doing any sort of logging and tracking

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:00:54 - 00:01:12]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Somewhere externally you may end up accidentally moving over some of your workflows like 10 times and then it becomes a whole mess in your new NNN. So after we've moved over all of our old workflows into a Google Sheet, all we have to do is hit that Google Sheet again, pull them back in, and then we just feed them into the new NNN. And we were able to use NNN's API to do this.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:13 - 00:01:33]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So if that didn't make any sense yet, let me just plug in my NNN credentials and then we'll give it a run and I'll show you exactly what I mean. So there are two different NNN API keys that you're gonna need to get. The first one is in your old instance. So this is my old cloud instance right here. What I'm gonna do is I'm gonna go over here to the settings and I'm gonna come up here to NN API. And then all I have to do right here is click on create API key.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:33 - 00:01:53]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I'll give it a name. So this is just gonna be test. You can make it expire or you can make it not expire at all. So I'll just leave it as this and I'll go ahead and hit save. And now it gives me this API key, which all I have to do is go ahead and copy that right there. And now that I've copied that API key, all I have to do is come into this NN node, go ahead and create a new credential. And I just have to paste in the API key right here.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:54 - 00:02:27]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Now, the other thing you are gonna have to do is you're gonna have to grab your base URL from up here, and you probably can't see it on my screen right now. And then after the dot cloud, or like the end of your base URL, you have to do slash API slash v1. So to make this easier, I'm just going to right now do slash API slash v1. And then I'm going to grab my base URL from up top right here. And then I'm going to paste it in the beginning. So now you can see I have nateherk.app.endedon.cloud slash and make sure there's not two slashes like there is here, API slash v1. And so I'm just going to go ahead and make sure that I label this credential as

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:27 - 00:02:50]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> my NNN cloud account. And we'll go ahead and save that credential. So now that this is set up, you can see what we're doing here is we're basically hitting NNN and we're saying we want to pull in all of our workflows. So when I execute this step, you can see that I got 512 items, meaning in my cloud instance right now, I've got 512 workflows. And I'm not actually going to do all 512 just because it would be very slow and it might mess up the recording.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:50 - 00:03:10]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So what I'm going to do instead is let's just pretend that I have 25 workflows in here. So I'm going to limit it to 25, hit execute step. And now you can see that we're going to get only 25 workflows instead of those 512. And even just 25 workflows is still a ton of data. Because what's going on in each of those workflows is we have an updated at time, a created at time, the name, if it's active or not.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:10 - 00:03:28]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We have all of these other things. We have every single node, all the parameters, all the different versions. And so it's a huge, nasty chunk of JSON whenever you are looking at a workflow. So same thing if you ever downloaded a JSON template from a community like mine, and then you go ahead and import it. This is what's actually going on behind the scenes that makes up the workflow.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:28 - 00:03:47]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So hopefully you guys understand now why we're logging everything, because there is a good chance if you're doing tons and tons of workflows, maybe something crashes. So if you're logging everything on something external like a Google Sheet, you'll be just fine. So what I'm going to do is I'm just going to click execute workflow, which is going to pull in the 25 items. It's going to loop through and it's going to one by one add it to a Google Sheet.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:47 - 00:04:10]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm gonna switch over to that sheet. And you can see right now, it's adding in workflows slowly one at a time. And it's giving us the ID. It's giving us the name of the workflow. And then it's marking the status as to process. And this makes it really easy for us later because as we're pulling in workflows, we're only gonna pull in workflows if the status equals to process. And then after we actually move them to the new self-hosted instance, we mark them off as processed.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:11 - 00:04:44]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And that's like I said, how we make sure we actually know which ones have been migrated and which ones haven't. So I'm just gonna let this finish up. we'll get all 25 in here and then I'll show the next phase of the workflow. All right, there we go. We got all 25 items pushed into the sheet. You can see here now we have 25 and now let's talk about what's going on down here. So down here we have our Google sheet and what we're doing is we're pulling in rows, but you can see that we have a filter, which means we're only going to pull in rows if the status column equals to process. So right here, I'll click execute step and we should see all 25 of those items come back as you can see right there. And of course, if I was to go into the

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:44 - 00:05:18]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Google sheet and I mark off this first one as process, for example, and I come back in here and then hit execute step, we should now only see 24 items actually ready to process. So out of these 24 workflows, we have the ID and that's all we actually need to do the next node, which is looking up that ID so that we can get the actual JSON makeup of that workflow. So that's what we're doing in this next node. This is once again, still our NNN cloud account. So the old one that we want to migrate workflows from, and we're just doing a get workflow operation where we're looking it up by ID. So there's 24 IDs on this left-hand side. We're putting all those in the

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:18 - 00:05:52]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> middle. So when I hit execute step here, we should see 25 workflows popping out on the other side. And that's exactly what we see here. Now this could be more than 24. It could be hundreds and hundreds. So what we want to do is once again, set up a loop so that we can just process one at a time to limit our chances of anything going wrong. But before I show you how this loop works, let's talk about this node here. So these other ended in nodes, as you can see, are either getting many workflows or getting one workflow. And so what we're doing in this one is we're actually going to create a workflow. And in order to do that, we have to send over a workflow object, which is made up of JSON. So we'll be sending over the name of the workflow, the nodes,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:52 - 00:06:12]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> the connections, and the settings. You can see I've got some variables in here with a couple expressions in the front, but don't worry about it. This JSON and this entire workflow that you're looking at right here will be available to download for free. So you won't have to worry about it. But if you want to also build this for yourself, just take a screenshot of this real quick and then have ChatGPT write it out for you. But this is where we have to make a credential for our new instance.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:13 - 00:06:34]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm gonna switch over real quick to my self-hosted instance, which you can see there are only two total workflows in here. And what we need to do is get an API key. And real quick, since you guys ask me this all the time, I'm using Hostinger VPS to self-host my NNN instance. And you can actually get a 10% off annual plans with code NateHerc. And also if you're in my plus community, AIS Plus, you can get a bigger discount.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:34 - 00:06:53]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So check that out in the link in the description. But this is what the landing page looks like. You can see it says deploy NNN in one click, and you can even get started for just five bucks a month. So it's a lot cheaper than NN Cloud. I also made a full YouTube video walking through this exact process of setting up NN on Hostinger. So if you wanna check that out, I'll tag that right up there. All right, anyways, back in my self-hosted, we're gonna do the same exact thing.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:53 - 00:07:12]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I'm gonna go to my settings. I'm gonna go to NN API. We're gonna go ahead and create a new API key. I'll call this one demo. We'll let that expire in 30 days, that's fine. And now I'm gonna go ahead and click this API key to copy it. We're gonna do the exact same thing in this NN node real quick. I'm going to go ahead and create a new credential. I'm going to paste in the API key.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:12 - 00:07:32]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And we have to do the base URL thing once again. So I'm going to once again type API slash V1. I'm going to go back into self-hosted. And I'm going to grab my base URL, which is pretty much, I guess you'll just see it right here. nand.blahblahblah.hostinger.cloud. And then we have slash API slash V1.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:32 - 00:07:51]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm just going to name this nand self-hosted. We'll hit save. and now we have this end-to-end node pretty much completely configured. And now this end-to-end node is ready for us and we can run the rest of the flow. So I'm just gonna go ahead and execute workflow. We've already seen how these first two steps, it's gonna pull in 24 workflows that are ready to process.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:52 - 00:08:15]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We grab the JSON for all of those and now we're gonna loop through, push them into the new account and then update the status in the sheet. So if I go into my cloud instance of end-to-end and I go back home, you should see now that we're getting workflows added in, we now have eight, we started with two. if I give this a refresh, we should have a few more now. There we go, we have 12. And if I go into that Google Sheet, you can see that they're slowly one by one getting marked off as processed, as you can see.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:16 - 00:08:34]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So this basically just helps us keep track, like I've mentioned many times before. So I'm gonna mark this last one as to process just so I can run one more all the way through and show you guys what the actual JSON body looks like in here. So we're passing over a workflow object. And if I open this up, you can see, once again, we have name and we have nodes, which is actually a lot longer than you may think.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:34 - 00:09:08]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> we have the connections and then we have the settings. So all of this basically just tells the self-hosted instance how to make the workflow and what the parameters are and how to actually connect the strings and things like that. So if I open up one of the workflows, you can see that it actually has even the stickers. It has all the naming conventions. It has all the parameters filled out already. As you can see, there's a user prompt in here. So it moves over everything just as you had it in your cloud version. The only thing that won't move over is, you know, credentials and users and executions and things like that. And there's really no great way to do that besides just manually resetting. So I know some of you guys are going to ask about what if

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:08 - 00:09:29]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> you wanted to move workflows from a cloud to a local. It's similar, but it's not quite as simple because obviously this Ended End API works a little bit differently because you have to somehow be able to speak to that local instance. But if you just get a little creative, there's lots of simple ways to do this because let's say you pull in your workflows up here from your cloud instance, you're getting everything you need in order to actually build the workflow.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:29 - 00:09:49]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So you could basically just write all of the JSON of the workflow into something like a Google Sheet or wherever you want to store it. And then you could just pull that into your local instance of NNN. And then, of course, from there, you can just create the workflows. Or if you're on NNN Cloud, you could go to your panel, you could go to manage, and you can click on export. And this lets you actually just download all of your workflows in a zip file.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:49 - 00:10:22]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And it's just all of the JSONs that you would need to actually import into your local instance. Okay, so just wanted to wrap up real quick with how do you actually access this template if you want to migrate your workflows? Well, you can get this for free by joining my free school community The link for that will be down in the description All you have to do to find that is you can search for the title of video You can go in the classroom and look through the templates You'll be able to find it in here and when you find the post associated with that video Like pretend it's this one you'd be able to download that workflow json right here and then import it I will even include a copy of this google sheet template if you want to just be able to plug everything right in

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:22 - 00:10:41]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> just like the template suggests. So then the only thing you'll have to do is you'll have to go get your two different NN API keys. And remember, you can use code NATEHERC to get 10% off annual plans at Hostinger. Or if you're interested in getting a larger discount and checking out a community of over 3,000 members who are building with NN every day and building businesses with NN every day, then definitely check out my plus community.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:41 - 00:10:58]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> The link for that is also down in the description. But anyways, that's gonna do it for today. I know it was a quick one, but hopefully it is a very specific use case that if you run into it, this video helps you out. And if you enjoyed it, you learned something new then please give it a like it definitely helps me out a ton and as always i appreciate you guys making it to the end of the video i'll see you on the next one thanks everyone

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

