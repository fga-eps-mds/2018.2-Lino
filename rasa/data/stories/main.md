## path_start
* start{"command": "start"}
  - utter_start

## path_help
* help{"command": "help"}
  - utter_help

## path_greetings
* greet
  - utter_greet

## path_thanks
* thanks
  - utter_thanks

## path_goodbye
* goodbye
  - utter_goodbye
  - utter_restart

## path_compliments
* compliments
  - utter_compliments_reply

## path_fallback
* out_of_scope
  - utter_default

## path_asks_documents
* asks_about_documents
  - utter_documents

## path_asks_regular_proof
* asks_regular_proof
  - action_regular_proof

## path_asks_register_proof
* asks_register_proof{"documents": "Comprovante de matrícula", "documents": "comprovante de matrícula", "documents": "Comprovante de matricula", "documents": "Comprovante de Matrícula", "documents": "comprovante de Matrícula", "documents": "Comprovante de Matricula", "documents": "comprovante de Matricula"}
  - action_register_proof

## path_asks_gmail
* asks_about_gmail
  - utter_gmail

## path_asks_schedule
* asks_about_schedule{"documents": "grade horaria", "documents": "grade horária"}
  - action_schedule

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

## path_handle_register_notifications
* notification_types{"notification_types": "Cadastrar"}
  - custom_start
  - action_buttons_notification
* notifications
  - action_register_notification
* affirm{"notification_types": "Cadastrar"}
  - action_show_notifications_types

## path_handle_register_notifications
* notification_types{"notification_types": "Cadastrar"}
  - custom_start
  - action_buttons_notification
* notifications
  - action_register_notification
* deny{"notification_types": "Cadastrar"}
  - utter_finish_notification

## path_handle_unregister_notifications
* notification_types{"notification_types": "Remover"}
  - custom_start
  - action_buttons_notification
* notifications
  - action_unregister_notification
* affirm{"notification_types": "Remover"}
  - action_show_notifications_types

## path_handle_unregister_notifications
* notification_types{"notification_types": "Remover"}
  - custom_start
  - action_buttons_notification
* notifications
  - action_unregister_notification
* deny{"notification_types": "Remover"}
  - utter_finish_unregister_notification

## path_handle_visualize_notification
* notification_types{"notification_types": "Visualizar"}
  - action_list_notifications
* affirm{"notification_types": "Visualizar"}
  - action_show_notifications_types

## path_handle_visualize_notification
* notification_types{"notification_types": "Visualizar"}
  - action_list_notifications
* deny{"notification_types": "Visualizar"}
  - utter_finish_notification

## path_calendar
* calendar
  - action_calendar

## path_offenses
* offenses
  - utter_offenses
