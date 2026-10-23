# 🎬 Why 99% of AI Automations Fail in Production

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=Irk4-DO5qgM](https://www.youtube.com/watch?v=Irk4-DO5qgM)  
> **Date de publication** : 20250807  
> **Durée** : 00:17:40  
> **Identifiant vidéo** : `Irk4-DO5qgM`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Why 99% of AI Automations Fail in Production**, Nate Herk décortique les capacités pratiques d'automatisation et de développement propulsées par les modèles de pointe.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Opus 5.5 & Claude Code** : Modèles d'ingénierie et agents de codage autonome.

### 🔑 Points Clés & Enseignements Stratégiques
- Optimiser le niveau d'effort et le raisonnement des modèles IA pour des résultats industriels.
- Automatiser les cycles de création logicielle de bout en bout.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:34]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Today I'm going to be talking about five error handling techniques that you need to master if you want to push your workflows into production. It depends on the use case but sometimes a workflow needs elements of all five of these techniques in order for you to actually be able to set it and forget it and have peace of mind that it's going to run and take care of errors the right way. So I'm going to walk through all five of these. I'm going to show you guys examples and number four is super super powerful and I feel like it's hardly ever talked about so you guys will see what I mean by that. So I don't want to waste any time here. Let's hop straight into this workflow so I can show you guys these error handling techniques. Okay. So real quick, before we jump into the

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:00:34 - 00:01:06]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> actual examples I've had for you guys here, I wanted to talk about what does production ready mean? So in NNN, when you're building a workflow and you're kind of in your test environment where you're testing out things and you're changing things and you see the data flow through live, you're in an inactive workflow. And as soon as you, you know, flick this switch and you turn this to an active workflow, it basically means, okay, this is live. If people, you know, whatever your trigger is, your trigger is actively listening now. So if people are emailing you or, you know, sending you a chat and WhatsApp or whatever, the workflow will actually do things and take action in

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:06 - 00:01:42]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> your tools. And that's exactly what an active workflow means. And in order for you to trust that you're ready to go into production and make this an active workflow, there's multiple elements, right? There's like security. There is just the consistency of the outputs and the quality of the outputs in general. But we're focusing today on the error handling aspect, which really is for the peace of mind. Because imagine if you didn't have proper error handling set up and you weren't getting notifications and things weren't, you know, continuing down the path, you could wake up to like 2000 fails and the whole logic is wrong and you're missing all these different orders and stuff like that. So production ready error handling in my mind means you have a workflow that when it errors,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:43 - 00:02:19]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> it's sending you notifications, it's logging all of those errors, it has retry and fallback logic, and when it fails, it fails safely. Meaning it's not emailing thousands of people or deleting records from your database or inserting a ton of records in your database. And the reason why you have to plan for those failures is because the failures are inevitable. In a production environment, things will fail. But near the end, we're going to talk about building guardrails. And in order to build guardrails, you need to know what type of failures are coming. As much as you can predict edge cases, you don't know what you don't know, and things are going to happen. So by tracking and logging all of your errors, you can start to identify patterns. And when you start to identify

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:19 - 00:02:51]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> patterns, you can build guardrails against those patterns. So anyways, that's enough blabbering from me. Let's just move on right here to the first type of error handling that we're going to talk about, which is kind of like the lowest hanging fruit and the easiest one to set up. Every single workflow you have should be pointing to some sort of error workflow, which, you know, that's number one, error workflows. So what an error workflow is, is it's a separate workflow that starts with an error trigger. And the error trigger can link up to any of your active workflows. And the idea is that whenever an active workflow errors, it will just notify this workflow,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:51 - 00:03:24]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and then you can set up the logic of what do I want to happen with an error. So I'm not gonna go, I'm not gonna dive into how you actually set this up. I linked a full video on my YouTube channel right here, if you guys wanna check that out. But let's say Mr. Bad Agent here has an Airtable tool, and the Airtable credential all of a sudden expires, or the scope changes or something. If we weren't having this agent pointing to this error workflow, we would basically have no idea that thousands of records are erring, And we would have no idea what happened later because we would come back and check our workflow and we'd see we have all these errors, but we wouldn't know the error message.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:24 - 00:03:44]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So it'd be really hard to debug. So because we can set up the logic to do whatever we want, we can go ahead and check the error logger. We can get our notification and fix it as soon as possible. So that's number one, error workflows. Number two is the ability to have our workflows retry on failure. What this means is that whenever our node faces an error, it's just gonna try again.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:44 - 00:04:02]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And you can control like wait this much time and then try again, try again five times, and then just move on, whatever you want. And the use case here is, you know, sometimes a server might just have some temporary downtime or sometimes there's a little bug. Sometimes it is a good thing to just make sure your workflow nodes will just retry.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:02 - 00:04:26]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And the way you do that is within any node, so like an AI agent node, you're gonna go up to your settings and you can see right here, you can turn on the switch that says retry on fail. So I'll turn that on and you can see it now opens up these two other things that say max tries, how many times you want it to retry, and then how long do you want it to wait between tries? So you have a couple of levers here to pull in order to change the way that the logic of this retry works.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:26 - 00:04:46]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And like I said, it's not just an AI agent node, it's basically any node in NNN. So something like a Gmail API, you can also do a retry and fail. And then even NNN's core nodes that don't even really use like a different server or AI at all, like a code node, you can have it retry on fail, HTTP requests, like basically any node in here can retry and fail.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:46 - 00:05:05]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that's a really easy sort of like, you know, low barrier to entry type of retry on failure you could do. There is another kind of like more advanced technique called polling, which isn't exactly retry on failure, but kinda, and I'll kind of touch on that in the guardrail section at the end of the video. But let's move on to number three, which is having a fallback LLM. So let's set the scene here.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:05 - 00:05:23]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We have a fallback agent with open router as the brain. Let's say we come in here and we basically want it to retry and fail three times. Okay. But what happens is I set up this open router credential with a fake key. So it's not going to work. So when I go ahead here and I try to chat to the agent, what's going to happen is it's going to fail. It's going to try again.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:23 - 00:05:48]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> It's going to try again. And it tried three times before it gave us the error message of, you know, invalid credential. So what we can do is have even another error handling technique in here where we have our retry, but we can also do a fallback model. So if I check this on, it basically allows us to connect a different model in case the main one fails. So let's say open router is our favorite and we're using GPT 4.1 mini, open routers down or open AI is down.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:48 - 00:06:20]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> What we can do is we can connect another model over here and we can just go with Google Gemini and now we have this model in place. So now if I save this workflow and I say hi, it's going to try that first model. It fails and then what happens is it just goes to the fallback model and now we make sure that we're still at least getting some sort of answer. And if you don't see that fallback model option. I think it was a new release of NNN 1.101, somewhere around there. So go ahead and update it and then you should see that. All right. So number four, like I said, this was my favorite one and I feel like it's not talked about very often, but this is the ability to have your nodes

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:20 - 00:06:58]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> continue on an error. So there are times when you may have like some fallback logic or whatever it is, but for some reason, something just isn't working. But what you don't want to happen is for your entire flow to stop. So think about this example. Every morning you have like a thousand new entries to process and you want to do some research and you want to, I don't know, write some sort of content. What happens is if you're going to like loop through all a thousand of those runs and the first item fails, then the rest of the 999 will not get processed. But if you can have it just continue, even if it errors, then maybe 998 of them are good, two are bad, but at least you're

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:58 - 00:07:32]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> not just left sitting there with absolutely nothing. So let me show you guys a quick example of that. We've got this code node. Don't worry about the code node. Basically, I just told this to output three different values for us. Google, Meta, and Vidya. It's going to output those items and loop through them and do research on them using Tavoli. And what's going to happen is I have the third one set up to error the body request. So if I run this real quick, we're going to see it pulling those three items. It's going to loop through. The first one's going to go fine. The second one's going to go fine. And now the third one is going to error. And what happens is it stopped the flow. So if we had 20 more to process, it wouldn't process them. And

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:32 - 00:07:52]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> just in case you guys are curious, the reason why it stopped the flow is because I had the actual value being passed over with quotation marks. So if you guys know like a JSON body, if you have double quotes, it's going to break that request. So you guys can see if I'm at run one, it was fine because the search query was Google with no double quotations. Run two was fine, but run three failed.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:52 - 00:08:21]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And that had the double quotations around NVIDIA. So what we can do is change the setting in this HTTP request to Tavli to continue even if that one of the runs fails. So I can click in here, I can go to settings, and all I have to do is change the on error, which is by default to stop the whole workflow, and we just switch that to continue. So it's the exact same flow. I'm going to execute this. It's going to pull in those three items. It's going to loop through them. The first one's good. Second one's good. The third one fails, but it doesn't fail and stop the whole workflow.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:21 - 00:08:55]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So if I go into the Tavli node now, we can see that the first two ran, right? They have their search results. And the third one just basically sent an error message, which was JSON parameter needs to be valid JSON, but it still followed the rest of the loop. And if there were 20 more, the remaining 20 would have got processed as well. And then if we want to get even more robust to maybe track things that didn't work in a separate one, we can actually do one more thing, where if I move this trigger down here, we can have the errored items go down a separate branch, which is a continue on error. And so you guys may have seen this in some of my other videos where

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:55 - 00:09:29]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I have some agents doing this to log different outputs based on if I was successful or if the agent fails, it's going to do this. But let me show you guys an example real quick. In the settings of Tavoli, we just changed the on error operation to continue using an error output, which creates an extra output. And now if I trigger this guy, it's going to run those exact same three queries. The first one's going to be fine. Second one's going to be fine. Third one's going to error, but not stop the workflow. And now you can see basically what happened is we had two items go down the success branch. Where's the two? Right here. I can't hover over it,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:29 - 00:09:47]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> but it's right in the middle. And then we have one item go down the error branch. So I can click into this node. We can have the error item was NVIDIA, but two success ones were Google and meta, as you can see. So now we're able to maybe feed in this path. We can create some new logics.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:47 - 00:10:21]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We can send ourselves an email and say, okay, here are the variables that erred or something like that just so we still have that tracking going on. Okay so number five is polling that I kind of alluded to earlier. I said it was going to be in the guardrail portion but I made it its own thing right. So polling is basically a technique where we're going to check in on the status of something until it's done. So here the example that I have for you guys is we're going to make one request to PyAPI to generate us an image using AI. What happens is we hit PyAPI server and we say hey I want an image and I want it to look like this and then they basically start working on that item.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:21 - 00:10:53]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And what happens is we have a different request that we need to make in order to get the item back But if we make a request and the item isn't done It would basically just we wouldn't have our image, but we would still continue down the rest of the workflow So what we do is use a technique called polling. So let me show you guys what that looks like I'm gonna hit execute workflow and basically it's going to make a post request to PI API to create that image And then we check in right here if the image is done and the image is not done So now you can see we're gonna wait until the image is done So it's waiting it checked back again still not done and check back a third time still not done

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:53 - 00:11:27]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And we're literally just gonna sit here and keep polling until the image actually comes back And that's how you can make sure you don't have to play around with like do I wait 30 seconds or what's the average time? Do I wait a minute? This lets us make sure that we only continue down the true branch with the rest of the automation once it's done So if you watch any of my like faceless shorts videos or anything like that We pretty much always use a polling technique to make sure that our assets are ready to go So you can see here it had to check a total of eight times and on the eighth time the image was done So if I click into this little expression right here, we can see that we actually do have our image URL

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:11:27 - 00:12:04]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Let me just open this up to prove to you guys it's here and we have our beautiful picture of a waffle person and so real quick I'll just show you guys how this works. So like I said, here's the first request We're making our request to PI API and we said hey We want a picture of a waffle personified as a human the waffles wearing a suit and tie from there we do an initial wait. So I put one second for the sake of the example, but usually you still want to make this like, you know, 40 or something like that, according to the average wait time. After that, we check in on the status of our request, we send over the task ID, stuff like that. And what you can see is on the first one, we got back a code 200. So no errors happened, we still got a

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:12:04 - 00:12:29]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> successful response. But if we scroll down, we can basically see that we don't have a URL. And what we're actually looking for is the status field right here. And it says status equals processing. So that basically tells us that we're not done yet. The second run status is processing, the fifth run status is processing, but on the eighth one, the status is completed. So all I'm thinking to myself is, okay, how do we make sure we don't move on until the status is complete?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:12:30 - 00:12:55]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Well, what we would do is we have a if node right here, which all we're doing is we're checking if the status equals completed. And when it does, it goes down the true branch, but the previous seven runs, it went down the false branch and the false branch is just a, you know, a 20 second wait, five second wait, whatever. And then it goes back. So this is an infinite loop until status equals completed. And then we can configure the rest of the logic this way down the true branch.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:12:55 - 00:13:28]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that's basically how polling works. Just keep in mind that depending on the service you're hitting, you may not need to poll, but if you do need to poll, they're always going to be a little bit different as far as how do you actually do it. So status equals processing and then status equals finished or status equals running and then status equals done. So you kind of have to understand both what does a in progress run look like and what does a completed run look like, and then you can adjust your conditional logic. Okay. And finally, I just wanted to show you guys an example of guardrail, but I wanted to talk about real quick, the mindset of error handling

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:13:28 - 00:13:48]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and building guardrails. So what I always love to say is that you don't know what you don't know. And when you build a really, really robust wire map and you think about your data sources and your transformation, you also probably think about what are things that could go wrong. And you always should assume that more than just that can go wrong because the world is unpredictable and LLMs are unpredictable.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:13:48 - 00:14:07]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And you don't know what people may say to your system, or you don't know what type of, you know, inputs your system may get. So because we have a system where we're able to log all of our errors and full visibility, hopefully into the executions, that's where we can sort of identify, okay, when we get results that are bad, why was that?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:14:07 - 00:14:26]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Or when we actually get an error message, why was that? And in automation, your best friend is predictability. So if you're able to spot patterns in certain errors, that basically creates a little bit of predictability as far as when this type of input comes through, what happens, where does it break? And what can I build to protect against it breaking right there?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:14:27 - 00:14:49]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then you kind of do so. So a real quick example that's happened to me in some production workflows frequently, and it's really easy to forget about, is just a body request of an API being broken. So we're gonna go back to that tably example that we used up here when we were doing this continue on error thing. So as you guys know, if we send over something to a body request, it's going to fail if it has double quotes or new lines or anything like that.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:14:49 - 00:15:08]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So what I did here is I'm setting pineapples on pizza with double quotes, and that's being fed into our tably request down here in the body, which is breaking it, of course, because there's double quotes. And what happens is maybe you have an AI node that's feeding in a body request stuff like that. And in test environment, It's working because you're not dealing with those double quotes.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:15:08 - 00:15:26]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But if you know that that breaks automations or that breaks requests, then you can just build in a guardrail ahead of time to make sure that that never happens. So we can use this really simple script expression, whatever you want to call it, where it's literally just saying, I'm gonna replace any double quotes and now we have none of them.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:15:26 - 00:15:47]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So as you can see, if I remove that, we have double quotes, I paste that in and now we have no double quotes. So this basically makes sure that no matter what happens, we're able to have Tavoli still process the information every time. And actually what's pretty cool is if we get rid of this HTTP request because Tavoli actually has just a verified community node now, if you didn't know.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:15:47 - 00:16:14]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So we're connected to Tavoli and all I have to do is drag in my search query right here. And what happens is, oh, actually this is connected to the wrong thing. So I'm dragging in this output into our search query. We have pineapples on pizza with double quotes, but you guys can see I can execute it and it's still gonna work. Because what I'm assuming is going on on the backend is Tavali knew about this and they built in that guardrail when they were creating this community node.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:16:14 - 00:16:39]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Because whether I'm feeding over pineapples on pizza with double quotes, or I feed it over without double quotes, they both still work. So sometimes if a verified community node or a native node is available, just go for that one because they might have some of this error handling and guardrails already built into place. And by the way, if you guys wanna access this entire template for free, just to play around with some of this error handling stuff, then you can get it, like I said, for free in my FreeSchool community.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:16:39 - 00:17:07]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All you have to do is join it in the link in the description. And once you get in here, just search for the title of the video up here. Or if you click on YouTube resources and go to the title of the video, you will then be able to see a JSON file. And that's what you'll download and import into your NN. And you'll have the exact template right here that we were looking at today. If you like this type of content and you're looking to have some more discussions around stuff like production ready workflows and error handling and surround yourself with a community of like-minded individuals, then definitely check out my paid community.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:17:07 - 00:17:27]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> The link for that is also down in the description. We've got an amazing community of over 2000 members who are building with NNN, shipping off production workflows every single day, and sharing their learnings and their challenges. We've also got a classroom section with two full courses, Agent Zero, which is the foundations of AI for beginners, and then 10 hours to 10 seconds where you learn how to identify, design and build time-sign animations.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:17:27 - 00:17:39]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'd love to see you guys in those communities, but that is gonna be it for the video. If you enjoyed or if you learned something new, please give it a like, Definitely helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one. Thanks guys.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

