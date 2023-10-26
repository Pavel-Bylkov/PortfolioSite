#!/bin/zsh
export $(xargs <.env)
python ./PortfolioSite/manage.py runserver
