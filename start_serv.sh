#!/bin/zsh
export $(xargs <.env)
python ./PortfolioSite/manage.py makemigrations
python ./PortfolioSite/manage.py migrate
python ./PortfolioSite/manage.py runserver
