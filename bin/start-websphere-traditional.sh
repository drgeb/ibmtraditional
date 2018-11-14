#!/usr/bin/env bash


def startme () {
    echo STARTING
    docker run --name ${NAME}-h ${NAME} \
           -p ${WSADMIN_SSL_CONSOLE_PORT}:${WSADMIN_SSL_CONSOLE_PORT} \
           -p 9442:${WSADMIN_HTTPS_PORT} \
           -p ${HTTP_TRANSPORT_PORT}:${HTTP_TRANSPORT_PORT} \
           -p ${DB2_SERVER_PORT}:${DB2_SERVER_PORT} \
           -d ${IMAGE}
}

def retrievel_password () {
    echo RETRIEVE PASSWORD
    docker exec ${NAME} cat /tmp/PASSWORD
}

def open_admin_browser_page () {
    echo OPEN ADMIN BROWSER PAGE
    start chrome http://localhost:${WSADMIN_SSL_CONSOLE_PORT}/ibm/console/logon.jsp
}

def open_application_browser_page () {
    echo OPEN APPLICATION BROWSER PAGE
    start chrome http://localhost:${HTTP_TRANSPORT_PORT}/${CONTEXT_ROOT}
}

def watch_logs () {
    start docker logs -f --tail=all ${NAME}
}

def build () {
    cd ${SANDBOX_HOME}\${NAME}
    docker build -t ${IMAGE}.
}

def stop () {
    docker stop ${NAME}
}

def remove () {
    docker rm ${NAME}
}

def ssh () {
    start docker exec -ti ${NAME}/bin/bash
}

def docker_commit () {
    docker commit fa526e74dd72 ${IMAGE}
}

def wsadmin () {
    #/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/wsadmin
    #Enter username
}


# https://hub.docker.com/r/ibmcom/websphere-traditional/
# https://hub.docker.com/r/ibmcom/websphere-traditional/
# http://david.currie.name/archives/2016/09/25/building-application-images-with-websphere-traditional
# https://www.ibm.com/support/knowledgecenter/en/SSZLC2_8.0.0/com.ibm.commerce.install.doc/refs/rigsrvportno.htm
# WebSphere Application Server administrative console secure port. This port requires SSL.
# WebSphere Application Server HTTPS transport port.


IF "%~1"=="" GOTO END
IF "%~1"=="start" GOTO START
IF "%~1"=="-p" GOTO RETRIEVE_PASSWORD
IF "%~1"=="admin" GOTO OPEN_ADMIN_BROWSER_PAGE
IF "%~1"=="app" GOTO OPEN_APPLICATION_BROWSER_PAGE
IF "%~1"=="logs" GOTO WATCH_LOGS
IF "%~1"=="build" GOTO BUILD
IF "%~1"=="stop" GOTO STOP
IF "%~1"=="rm" GOTO REMOVE
IF "%~1"=="ssh" GOTO SSH

