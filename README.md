<h1 align="center">Chinese conversational assistant robot</h1>
<p align="center">
  <a href="#overview">Overview</a> 
  <a href="#features">Features</a>
  <a href="#howto">How to</a>
  <a href="#underthehood">Under the hood</a>
  <a href="#todo">ToDo</a>
</p>

<p align="center"><img src="materials/conversation.gif?raw=true"/></p>
<h2 align="center">Overview</h2>
**RASA** may be the best open source to help people build their own auotomatic assitant robot. Here,  I will show you how to build a very basic chat robot that handle multiple tasks with rasa.


<h2 align="center">Features</h2>
- Conversational, not just dumb **asked-and-reply** pattern, but can follow the conversation in a very natural way.
- Can extract the certain information pieces by using slotting filling and name entity recognition.
- Handle multiple missions and tasks.

<h2 align="center">How to</h2>
Frist, clone the reposity and download dependeices:
```shell
  pip install -r requirements.txt
```
Then, train our model
```shell
  rasa train
```
Ok, here you go
```shell
  rasa shell
```

<h2 align="center">Under The Hood</h2>
Before we start, make sure you have already knew the basics of [rasa](https://rasa.com/docs/)

### Be conversational with story
Traidiotional robot follow a **asked-and-reply** pattern, which robot can only responde after a user input, and most of time , the response given by robot allways has nothing to do with the previous talks, which make the experience of talking with a robot like ** talking with robot**. 
Whereas, Rasa can maintain a  converational state by using its memery policy and  reponse like acting a certain play.
For eamples, when the robot find you are sad(what we call `intent recognition`, nothing more than a text classification), the robot will throw out a joke and cheer you up, then, it will ask your feedbacks, if that helps, the robot can response a poistive messasagem otherwise it will do something else.
To make that happen, Rasa use a so-called  `story` mechanism to make the conversation more conversational.
`story` can be written as following(check the `stories.md` in ):
```text
## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
```
So the `sad scenario` has three certain stages to interacte with our users, fell free to and more stages.

### Retrieve certain informations
Often , the robot need to extract some imformation pieces to complete a certain mission, let's say you wanna call a taxi, then the robot need to know where  you wanna go.  There're to ways to achieve that:
- Slotting filling by asking user some questions until all slots being filled.
- Also ask the user some questions, but use a NER service to extract informations.
Here we use the scond method. Rasa allow us to write custom [NLU Components](https://rasa.com/docs/rasa/api/custom-nlu-components/), here I call a bert-ner api service to extract neccessary informations for me, which is locations here. You can check this [repositry](https://github.com/superjcd/fst2) to easily train and build your own ner models here

### Make actions
After knowing the intent of our user, and got neccessay information, the robot then can actually do some staff for us. But here, for simplicty, I just let the robot reponde without doint anything, but you can write your own [actions](https://rasa.com/docs/rasa/core/actions/#).

<h2 align="center">TODO</h2>
- Bring NLG to robot by using language model like GPT2.
