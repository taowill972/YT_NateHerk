# 🎬 Build Your First RAG Pipeline for Better RAG (step-by-step)

> **Chaîne** : [Nate Herk | AI Automation](https://www.youtube.com/@nateherk/featured)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=5uw1wE6niGc](https://www.youtube.com/watch?v=5uw1wE6niGc)  
> **Date de publication** : 20251018  
> **Durée** : 00:16:24  
> **Identifiant vidéo** : `5uw1wE6niGc`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **Build Your First RAG Pipeline for Better RAG (step-by-step)**, Nate Herk décortique les capacités pratiques d'automatisation et de développement propulsées par les modèles de pointe.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Opus 5.5 & Claude Code** : Modèles d'ingénierie et agents de codage autonome.

### 🔑 Points Clés & Enseignements Stratégiques
- Optimiser le niveau d'effort et le raisonnement des modèles IA pour des résultats industriels.
- Automatiser les cycles de création logicielle de bout en bout.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:30]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Today we're going to be talking about RAG pipelines and the importance of keeping your database up to date. At this point I'm assuming you've already built some sort of vector database RAG agent before. If you haven't, I built a full course on that. You can go watch that video up here. And then when you're done with that video, come back over here and we're going to build out a data pipeline. In today's example, we're going to make sure whenever we drop a PDF into a Google Drive, it gets put into our vector database. Whenever we update that file in Google Drive, it will also get put into our database and the old one will be deleted. And then of course, if we delete the file out of Google Drive, it will also be deleted out of our vector database.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:00:30 - 00:01:02]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I don't want to waste any time. Let's get into the video. All right, real quick, before we hop into NNN, I wanted to do a few slides about why data pipelines matter for the success of your AI agents. The idea of setting up a knowledge base that all of your agents can pull from is that the knowledge in there is accurate and up to date. So if your data is messy, outdated, or scattered everywhere, your AI agent is going to struggle to deliver actual real answers. So what we need to do is we need to design automated rag pipelines to make sure that they're constantly checking to make sure that the vector database is accurate or wherever the data is being stored.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:02 - 00:01:36]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So when I think of a data pipeline, I think of three steps. I think of the raw material that we take in. I think of the processing line of what actually happens to that raw material. And then I think of where it ends up sitting. So quick practical and an example of this is in this workflow, I've got my transcripts pipeline. So the raw material that I'm giving it is I'm uploading a URL of a YouTube video right here. And then we move into the processing flow where I get the transcript from it. I'm extracting the actual transcript and I'm extracting the timestamps, merging that back together. And this was basically me cleaning up and getting the data ready to be

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:01:36 - 00:02:09]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> ingested into the final product, which is our super base vector database right over here. So we've got four essential components to be thinking about. The first one is the trigger. What actually starts the process of getting data into a vector database or deleting data from a vector database? This could be new emails come in and you want those to get vectorized. This could be a new row in a Google Sheet It could be a file upload or it could even be some sort of criteria is met And let me show you again what I mean by that with a real example of this YouTube transcript pipeline After we get a YouTube video into our vector database We then put it in a Google Sheet

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:09 - 00:02:32]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And so the Google Sheet would look like this where we get the title the URL and the transcript and then also we would have a status So it would be processed or if I changed it to remove then that would trigger off this second flow down here. This would go off whenever a row status equals remove and then it would filter out all the other rows and then it would get rid of the vectors where it came from that video.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:32 - 00:02:51]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So hopefully that makes sense. If it didn't, you can go ahead and watch this YouTube transcript video, which I'll tag right up here. But that's just a way for me to make sure that my vector database is only having YouTube videos that I want to chat with. And then we have inputs. And these are the data sources that we need to process. You really want to know exactly what your data sources look like and how they're going to be coming in.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:02:51 - 00:03:09]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Because predictability is your best friend. Are they going to be PDFs? Are they going to be CSVs? Are they going to be both? Are they going to be images or is it just going to be text? You need to understand this stuff in order to make that middle portion of your RAG pipeline actually good. And then of course we take those inputs and we process them, we clean them up, we remove duplicates.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:09 - 00:03:31]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We make sure that they're ready to go. We give them metadata, stuff like that. And then we actually shove them into our vector database or relational database, wherever we actually want to keep them. So I really just wanted to preface this stuff because it's really, really important to think about what data am I currently processing? And then later, how can I scale this up? So a great example today is we're just going to be building a flow to handle PDFs.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:31 - 00:03:55]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But later on, if we knew, okay, we might also need Word docs and Excel files and stuff like that, then you could come in here and build a system like this, where you're watching a Google Drive folder. but then you also have a switch to handle PDFs, text files, Excels, and all of them get processed differently because they're different types of files, but then ultimately they all go into the same vector database. So that's just an example I wanted to show you guys real quick of what I meant by understanding these core components and why predictability is your best friend.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:03:55 - 00:04:29]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So now that we got all of that boring stuff out of the way, let's get started with this build. So the first thing we're going to build is the pipeline that takes a new doc that we drop into Google Drive folder and it puts it into a vector database. So super simple. We're going to start off here by grabbing a Google Drive node and we're going to grab a trigger that is on changes involving a specific folder. First thing here after you connect your Google Drive account is to choose the folder. So after you connect your Google Drive account, you want to choose the folder that you're going to be looking in. We're going to grab one that I just made called RAG. There we go. And

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:04:29 - 00:05:01]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> then what are we watching for? We're watching for a new file being created in this folder. So what I'm gonna do real quick is go over to my Google Drive and we're gonna take this policy and FAQ document And I am just going to move this into our folder called RAG as you can see right here Moving into RAG and then we go back to NNN and I hit fetch test event We should now see that that folder has arrived. We're sorry not the folder the file. You can see if I scroll over Somewhere there it is. It is called policy and FAQ document. So we've got that data here What I'm gonna do now is just pin this to keep it here for now

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:01 - 00:05:21]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> The next thing we're going to do is actually download this file because all that came back here was like metadata about the file, its ID, its title, all that kind of stuff. So I'm going to grab another Google Drive node. We're going to do download file and I'm going to change the file we're looking for to be by ID. And then all I have to do here is find the ID of the file that triggered this workflow.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:22 - 00:05:43]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> OK, so I just scroll down a little bit, but I found it. It is right here. I'm going to drag that into the box. And now we have this variable which represents the ID of the incoming file. and I'm just going to click execute step. And now we should see the binary over here. Actually, I forgot that this is a Google Doc. So what I'm going to do is I'm going to add an option down here where I can actually download any Google Doc as a PDF.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:05:43 - 00:06:16]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I can click on add conversion. And rather than turning a doc into HTML, I can turn a doc into PDF. And if I run this again, we should now see right here that this is coming through as a PDF. So perfect. We've got what we want. And now it's as simple as that. I'm just going to add a Supabase step. We're gonna add a Supabase vector store and we're gonna add documents to it So I'm choosing the table to put it in in Supabase which is called documents as you can see here's my environment And this is the table we're gonna put it in We don't need to add any other options We just need to add our default data loader and this is important because right now it's looking for JSON

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:16 - 00:06:37]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But what we actually want to give it is binary as you can see we have our PDF right here is binary So I'm gonna change that to binary. We're gonna leave everything else up here as default for the sake of the example But we are going to add some metadata This is going to be very important for us later when we need to update and delete files. So I'm going to add metadata. The first thing that I'm going to add is file name.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:38 - 00:06:56]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm going to do some camel case there, put in file name, and then we just need to go back to the schema of this file and find its name. So if I scroll down here, we can see the name is policy and FAQ document. I'm going to throw that right in there. And then we're going to add one more metadata property, which is going to be date.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:06:56 - 00:07:24]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and then I'm just going to type in two open curly braces and do dollar sign now. So whenever we get a new piece of information put into our vector database, we can see the exact date and time that it was uploaded. That way we can just later on validate that if we update a file in our Google Drive, that it updates in Superbase as well. Okay, cool. So we have file name and date as our metadata. That's all we're going to do for now. And then I'm going to add an embedding. So I'm going to choose OpenAI.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:25 - 00:07:43]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> We've already got this all set up. We've got text embedding three small, which has to be the same as your embedding model for your database. So we're good to go here. And now I'm just going to run this. And this is going to put that policy and FAQ document into our super base. Cool. So it says five items should be there. So we should refresh this and see five items. Oh, they popped up right there.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:07:44 - 00:08:03]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And if we go to the metadata and open this up, we can see that we have title and producer because I guess it got that from the binary data itself. But we also have the metadata down here that we added, which was date and file name right there. And instead of file name, you could have also done file ID. As long as you have some sort of unique variable that you can reference later.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:03 - 00:08:22]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And you guys will see exactly what I mean by that when we do this next pipeline. Real quick, before we build that next pipeline, I'm just gonna build a really, really quick AI agent so we can validate that it is able to read this document. Okay, so set that up real quick. I'm just gonna ask it, what is our shipping policy?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:22 - 00:08:42]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> shoot that off and we should get an answer from the vector database. I didn't even give the agent a prompt or anything. We just hooked it up to a tool and look how smart this guy is. So we've got our shipping policy, orders are processed within one to two business days. Standard shipping takes three to seven business days. And you can see right here that it is correct.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:08:42 - 00:09:10]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> All right, cool. So the next step is we now need to create a flow that when we update this file, it will also update in our Subabase vector database. So what we're gonna do is we're going to add another trigger which is going to be another Google Drive trigger. So you might think to just do on changes to a specific file, which is fine if your vector database only has one file, but what we're gonna do is on changes involving a specific folder instead, just in case you drop in many files in this folder.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:10 - 00:09:35]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So we're gonna choose that same one again, which was called rag, and we're gonna be watching for a file updated rather than a file created. All right, so I just changed the name. It used to be Tech Haven, as you can see in the vector database, the policy and FAQ doc store name is Tech Haven. But I just came in here and changed it to Greengrass. So now when we test this trigger, it should pull in that file because the file had a change made to it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:35 - 00:09:55]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So we got this information back. But now before we download the file, what we want to do is want to get rid of all of the vectors in Supabase where the file name equals policy and FAQ document. because these are now outdated vectors. So to do this, we're going to add another node. And this is going to be a Supabase node, not a VectorStore node, just a regular Supabase node.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:09:56 - 00:10:14]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And we're going to choose delete a row. So once again, we need to choose the table, which is documents. And keep in mind, this is a table that has embedding. So it is a VectorStore, but we're able to use the regular Supabase node here. So what we want to do is delete. We're going to delete a row in this documents table, but instead of build manually, we're going to choose string.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:14 - 00:10:37]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then I'm going to change this to an expression and paste in this expression right here, which is metadata dash arrow arrow file name, which is the metadata field equals like period asterisk. So kind of a mouthful and not a super intuitive string, but this is how it's going to work. And what we need to do now is just go down to grab the file name of this file.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:37 - 00:10:56]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And like I said, you could use the ID. You could use anything that's unique to this file. I just decided to go with name because it looks a little less intimidating for the sake of the demo. So now we have any vectors where the metadata of file name equals this, it's going to delete. So if I hit execute step, we should see five items were output.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:10:57 - 00:11:18]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Because we had five vectors right here, and these should disappear any second. Now there you go, they're gone. So now we know our vector database is clean of old vectors. And now all we have to do is same thing up here, download the file, and then put it into Supabase. So I'm actually going to copy this Supabase right here and just put it right here. And then I'm going to grab another Google Drive node in order to download the file.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:11:18 - 00:11:39]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And we just need to download by ID once again. And we're going to choose the ID from the Google Drive file that triggered this workflow, which is at the bottom right here. Same thing, actually, though. I'm going to do the file conversion and make sure the doc is getting turned into a PDF and then download it. Okay. One thing did happen, though, which let me explain what happened.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:11:39 - 00:11:59]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So we pulled back five files, but they're all the same one. And the reason why that happened is because when we deleted five rows from Supabase, this has five items, which makes Google Drive think that it needs to output five items as well. So we're going to click onto this node. We're going to go to settings, and we're just going to say execute only once. And now when we run this again, it's only going to have one, as you can see.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:11:59 - 00:12:32]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And now we're able to just hook that puppy into Supabase. And when we run this, I believe everything should be set up. we should still in our data loader have the metadata but we need to fix this because the name is not mapped correctly so we're going to go back to the google drive trigger we're going to scroll down to get to the name which is all the way near the bottom they make it so hard to find there it is policy and faq dock so now this flow has the right metadata and you can see now it's good we're passing over a new date and time and then we're going to go ahead and run this one as well and

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:12:32 - 00:13:08]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> because it's basically the same file it should still be five items we should go to supabase and wait for these to pop in. And you can see now that the vector is updated because it says store name is Greengrass rather than Tech Haven. And once again, we could come up here and chat with the agent and say, what is our store name? Send that off and it should hit Supabase right here and come back with Greengrass. There you go. Our store name is Greengrass. Okay. So we now have our flow that puts a file into Supabase when it is put into a Google Drive folder. We've got one that when we update that file, it's going to delete the old records and then put the new ones into Subabase.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:13:09 - 00:13:33]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And now the last thing we need to do is what happens if we actually just delete that file, or we want to delete it? How do we make sure Subabase deletes them? So we have a bit of a band-aid fix, but it does work. And also keep in mind, what I'm trying to show you guys here is the idea of building these pipelines, not saying that this is the optimized way to chunk and split and embed data into a Subabase Vector Store. We're just keeping it simple here with the main foundational high-level concepts.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:13:34 - 00:13:55]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So anyways, the fix we have here, because as you can see, when we go to Google Drive and we go to triggers and we do on changes involving a specific folder, there's not one, sorry, let me just grab the folder. There's not a watch for file deleted. Not exactly sure why. Obviously they have something on their end, which is like sending over the data off of their web hooks and triggers, whatever.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:13:56 - 00:14:15]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But there's not that option there. So what we do is we're going to go file created, but we're going to choose a different folder. We're going to choose a new one that we made called the recycling bin. So now it's watching a separate folder for anything that gets put in the recycling bin. So what I'm gonna do is go over to this policy and FAQ doc. We're gonna go ahead and move it once again.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:14:15 - 00:14:34]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'm gonna move this to the recycling bin folder, as you can see. Now it's gone from there and it should have gone into our recycling bin right here. Same file though. And now if we go into NNN and we fetch test event, we should see that we got this file, which was once again, hopefully, the policy and FAQ document right here.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:14:34 - 00:14:53]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And then it's actually really simple because we don't have to ingest anything, we just have to delete. All we have to do is throw this right in here and make sure that everything's mapped up correctly, which is metadata file name like name, execute that. We should get five items over here and then we should see them be deleted from Superbase just like that.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:14:53 - 00:15:13]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So it was really that simple. And now we have two different Google Drive folders That's as soon as we either drop something in, update those contents, or move it from there to a recycling bin folder, our SubaBase Vector database will be taken care of. Once again, this wasn't for showing you how to optimally process data and put it in.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:15:13 - 00:15:32]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> This was more about the idea of it and how you can think about creating these different triggers and using metadata to actually filter and delete things. So I hope you guys were able to watch this one, understand what's going on and follow along. As always though, you'll be able to download this exact workflow. I'll also have like sticky notes and a setup guide and stuff. All you have to do to get that for free is join my free school community.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:15:32 - 00:15:51]` | Segment #40

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> The link for that will be down in the description. Once you get in there, it will look like this. You'll just need to navigate to the YouTube resources. And every single one of my videos here has some sort of resource. So right here is my developer agent and you have the developer agent JSON to download. And if you're looking to dive a little deeper with a more hands-on learning experience, then definitely check out my plus community. The link for that is also down in the description.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:15:51 - 00:16:12]` | Segment #41

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Got a great community of over 2,500 members who are building with NNN every day and building businesses with N8N. It's a super active group. We've been having some really fun calls and discussions lately. And we also have a full classroom section where we dive into the foundations with Agent Zero, N8N with 10 hours to 10 seconds, and then a new course for our annual members called One Person AI Automation Agency.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

### ⏱️ `[00:16:12 - 00:16:24]` | Segment #42

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So I'd love to see you guys in these calls in the community, but that's gonna do it for the video. If you enjoyed this one or you learned something new, please give it a like. Definitely helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one. Thanks everyone.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales et mise en contexte méthodologique.

**Action / Démonstration** : Explications face caméra et démonstration conceptuelle.

---

