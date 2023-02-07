# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    Makefile                                             ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 12:22:33 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/07 12:23:48 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

include .env

SECRETS_DB_SCRIPT	=	./.scripts/setsecrets_db.sh

WEB_CONTROLLER_NAME	=	db_controller

usage:
	@echo "Usage:"
	@echo "make install        -> Creates DB container"
	@echo "make run            -> Starts the already created DB"
	@echo "make runController  -> Starts the controller"
	@echo "make runAll         -> Starts the DB and the controller"
	@echo "make stop           -> Stops DB container"
	@echo "make stopController -> Stops DB controller container"
	@echo "make stopAll        -> Stops both containers"
	@echo "make uninstall      -> Removes the DB container"
	@echo "make dockerls       -> Check current state of dockers"

# Config files

.env: ${SECRETS_DB_SCRIPT}
	@bash ${SECRETS_DB_SCRIPT}

# Commands

install:
	docker run -d --name ${DB_NAME} -p ${DB_PORT}:5432 -e POSTGRES_PASSWORD=${DB_USR_PASSWD} -e POSTGRES_USER=${DB_USR} -e POSTGRES_DB=postgres postgres:latest

run:
	docker start ${DB_NAME}

runController:
	docker start ${WEB_CONTROLLER_NAME}

runAll: run runController

stop:
	docker stop ${DB_NAME}

stopController:
	docker stop ${WEB_CONTROLLER_NAME}

stopAll: stop stopController

uninstall: stop
	docker rm ${DB_NAME}

dockerls:
	docker ps -a
	@echo
	@echo
	@echo "docker images"
	docker images
	@echo
	@echo
	docker volume ls
