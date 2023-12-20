# Speech to Text | Meeting summarizer model
---
## Description
* The goal is to make a model which **translates audio from meetings and encodes it to a text file**, which on completion is *summarized* in to a smaller, concise *list of bullet points* covering the entire meeting. The initial idea is to implement it through pre-trained models, but the accuracy and efficiency has to take care of.
* There are a few considersation. First, that it should desirably also support *mulit-lingual conversation*, with **english** being the primary support, and additional support for **hindi** and at least the default regional language.
* The end goal however, is to wrap this model into a presentable *web-app*, with gui interface to start the recording, and add the administrators to the meetings, which will *recieve the summary as a text file in the mail box* automatically, without manual intervention.

## Problem Statement
`To create a machine learning model which can listen to the audio from meetings and translate the speech to text, and finally output a summary of the entire meeting in a text format. This model can further be wrapped inside a graphical interface for easier access, where the summarized text has to be sent to the administrators of the meeting provided on onset.`

## Course of Action
* using google's standard api to convert speech to text
  * setting a baseline 
  * finding accuracy
  * improving on the same
* dumping the output to a text file
  * that is then picked up for summarizing
  * using sumy standard module 
  * improving on the same
