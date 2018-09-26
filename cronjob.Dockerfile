FROM debian:latest
FROM python:3.6

RUN apt-get update && apt-get install --reinstall -y locales tzdata

RUN sed -i 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen

RUN locale-gen pt_BR.UTF-8

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR
ENV LC_ALL pt_BR.UTF-8

RUN dpkg-reconfigure --frontend noninteractive locales

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && apt-get -y install cron

ADD /rasa/crontab /etc/cron.d/menu-cron

RUN chmod 0644 /etc/cron.d/menu-cron
RUN crontab /etc/cron.d/menu-cron

CMD ["cron", "-f"]