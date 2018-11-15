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
  - action_send_week_menu

## path_dinner_meal
* asks_menu
  - utter_menu
* asks_dinner_menu{"meal": "jantar"}
  - action_daily_dinner

## path_lunch_meal
* asks_menu
  - utter_menu
* asks_lunch_menu{"meal": "almoço"}
  - action_daily_lunch

## path_breakfast_meal
* asks_breakfast_menu{"meal": "cafe da manhã"}
  - action_daily_breakfast

## path_handle_notifications
* asks_about_register_notifications
  - utter_operation_type
  - action_show_notifications_types

## path_handle_notifications2
* notification_types{"notification_types": "Cadastrar"}
  - custom_start
  - action_register_notification

## path_handle_notifications3
* notification_types{"notification_types": "Remover"}
  - utter_goodbye

## path_handle_notification4
* notification_types{"notification_types": "Visualizar"}
  - action_daily_breakfast

## path_calendar
* calendar
  - action_calendar
