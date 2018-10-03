## path_asks_documents
* greet
  - utter_greet
* asks_about_documents
  - utter_documents
* goodbye
  - utter_goodbye
  - utter_restart

## path_asks_gmail
* greet
  - utter_greet
* asks_about_gmail
  - utter_gmail
* goodbye
  - utter_goodbye
  - utter_restart

## path_daily_meal
* greet
  - utter_greet
* asks_about_menu
  - utter_menu
* asks_daily_menu{"period": "hoje", "meal": ""}
  - action_daily_menu
* goodbye
  - utter_goodbye
  - utter_restart

## path_weekly_meal
* greet
  - utter_greet
* asks_about_menu
  - utter_menu
* asks_weekly_menu
  - utter_weekmenu
* goodbye
  - utter_goodbye
  - utter_restart

## path_asks_notification
* greet
  - utter_greet
* asks_about_notifications
  - utter_notifications
* notification
  - action_ask_notification
* goodbye
  - utter_goodbye
  - utter_restart
 
## path_fallback
* out_of_scope
  - utter_default
* goodbye
  - utter_goodbye
  - utter_restart
