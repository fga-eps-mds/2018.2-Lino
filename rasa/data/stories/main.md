## path_greetings
* greet
  - utter_greet

## path_help
* help{"command": "help"}
  - utter_help

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

## path_asks_regular_proof
* asks_regular_proof
  - action_regular_proof

## path_asks_register_proof
* ask_register_proof{"documents": "Comprovante de matrícula", 
    "documents": "comprovante de matrícula",
    "documents": "Comprovante de matricula",
    "documents": "Comprovante de Matrícula", 
    "documents": "comprovante de Matrícula", 
    "documents": "Comprovante de Matricula",
    "documents": "comprovante de Matricula"}
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

## path_register_notification
* asks_about_notifications
  - utter_notifications
  - action_buttons_notification
* register_notification
  - custom_start
  - action_register_notification

## path_calendar
* calendar
  - action_calendar
