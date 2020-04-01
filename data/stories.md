## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help

* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## 订阅
* ask_for_subscribe
  - utter_can_do
  - subscribe_form
  - form{"name": "subscribe_form"}   <!--Activate the form-->
  - form{"name": null}     <!--deactivatee the form-->


## 打车服务, 满意
* call_taxi
  - utter_ask_location
  - action_listen
* go_somewhere
  - call_taxi_action
* feedback{"feedback_value": "positive"}
  - slot{"feedback_value": "positive"}
  - utter_happy

## 打车服务， 不满意
* call_taxi
  - utter_ask_location
  - action_listen
* go_somewhere
  - call_taxi_action
* feedback{"feedback_value": "negative"}
  - slot{"feedback_value": "negative"}
  - utter_improve


## 失败
* out_of_scope
  - utter_out_of_scope





