## path_greetings
* greet
  - utter_greet

## path_goodbye
* goodbye
  - utter_goodbye
  - utter_restart
    
## path_fallback
* out_of_scope
  - utter_default

## path_asks_documents
* asks_about_documents
  - utter_documents

## path_asks_gmail
* asks_about_gmail
  - utter_gmail

## path_daily_meal
* asks_menu
  - utter_menu
* asks_daily_menu{"period": "hoje"}
  - action_daily_menu

## path_weekly_meal
* asks_menu
  - utter_menu
* asks_weekly_menu{"period": "semana"}
  - utter_weekmenu

## path_register_notification
* asks_about_notifications
  - utter_notifications
* register_notification
  - custom_start
  - action_register_notification

## path_calendar
* calendar
  - action_calendar