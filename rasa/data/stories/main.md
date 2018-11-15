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

## path_register_notification
* asks_about_register_notifications
  - utter_register_notifications
  - action_buttons_notification
* register_notification{
    "registered_option": "Alerta da Comunidade",
    "registered_option": "Cardápio do Dia",
    "registered_option": "Cardápio da Semana",
    "registered_option": "Café da Manhã",
    "registered_option": "Almoço",
    "registered_option": "Jantar"
}
  - custom_start
  - action_register_notification
* affirm
  - action_another_notification

## path_register_notification
* asks_about_register_notifications
  - utter_register_notifications
  - action_buttons_notification
* register_notification{
    "registered_option": "Alerta da Comunidade",
    "registered_option": "Cardápio do Dia",
    "registered_option": "Cardápio da Semana",
    "registered_option": "Café da Manhã",
    "registered_option": "Almoço",
    "registered_option": "Jantar"
}
  - custom_start
  - action_register_notification
* deny
  - utter_finish_notification

## path_unregister_notification
* asks_about_unregister_notifications{
    {"option": "não", "notification": "notificação"},
    {"option": "nao", "notification": "notificaçao"},
    {"option": "não", "notification": "notificações"},
    {"option": "nao", "notification": "notificaçoes"},
    {"option": "sem", "notification": "notificação"},
    {"option": "sem", "notification": "notificaçao"},
    {"option": "sem", "notification": "notificações"},
    {"option": "sem", "notification": "notificaçoes"},
    {"option": "quero tirar", "notification": "notificação"},
    {"option": "quero tirar", "notification": "notificaçao"},
    {"option": "quero tirar", "notification": "notificações"},
    {"option": "quero tirar", "notification": "notificaçoes"},
    {"option": "tira", "notification": "notificação"},
    {"option": "tira", "notification": "notificaçao"},
    {"option": "para", "notification": "coisa"},
    {"option": "para", "notification": "notificações"},
    {"option": "para", "notification": "cardápio"},
    {"option": "para", "notification": "mandar"}
}
  - utter_unregister_notifications
  - action_buttons_notification
* unregister_notification{
    "unregistered_option": "Alerta da Comunidade",
    "unregistered_option": "Cardápio do Dia",
    "unregistered_option": "Cardápio da Semana",
    "unregistered_option": "Café da Manhã",
    "unregistered_option": "Almoço",
    "unregistered_option": "Jantar"
}
  - custom_start
  - action_unregister_notification
* affirm
  - action_trigger_unregister_notification

## path_unregister_notification
* asks_about_unregister_notifications{
    {"option": "não", "notification": "notificação"},
    {"option": "nao", "notification": "notificaçao"},
    {"option": "não", "notification": "notificações"},
    {"option": "nao", "notification": "notificaçoes"},
    {"option": "sem", "notification": "notificação"},
    {"option": "sem", "notification": "notificaçao"},
    {"option": "sem", "notification": "notificações"},
    {"option": "sem", "notification": "notificaçoes"},
    {"option": "quero tirar", "notification": "notificação"},
    {"option": "quero tirar", "notification": "notificaçao"},
    {"option": "quero tirar", "notification": "notificações"},
    {"option": "quero tirar", "notification": "notificaçoes"},
    {"option": "tira", "notification": "notificação"},
    {"option": "tira", "notification": "notificaçao"},
    {"option": "para", "notification": "coisa"},
    {"option": "para", "notification": "notificações"},
    {"option": "para", "notification": "cardápio"},
    {"option": "para", "notification": "mandar"}
}
  - utter_unregister_notifications
  - action_buttons_notification
* unregister_notification{
    "unregistered_option": "Alerta da Comunidade",
    "unregistered_option": "Cardápio do Dia",
    "unregistered_option": "Cardápio da Semana",
    "unregistered_option": "Café da Manhã",
    "unregistered_option": "Almoço",
    "unregistered_option": "Jantar"
}
  - custom_start
  - action_unregister_notification
* deny
  - utter_finish_unregister_notification

## path_calendar
* calendar
  - action_calendar
