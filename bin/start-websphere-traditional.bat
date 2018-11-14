@SET a=@

%a% REM https://hub.docker.com/r/ibmcom/websphere-traditional/
%a% REM https://hub.docker.com/r/ibmcom/websphere-traditional/
%a% REM http://david.currie.name/archives/2016/09/25/building-application-images-with-websphere-traditional
%a% REM https://www.ibm.com/support/knowledgecenter/en/SSZLC2_8.0.0/com.ibm.commerce.install.doc/refs/rigsrvportno.htm
%a% REM WebSphere Application Server administrative console secure port. This port requires SSL.
%a% REM WebSphere Application Server HTTPS transport port.

:PARSE
%a% IF "%~1"=="" GOTO END
%a% IF "%~1"=="start" GOTO START
%a% IF "%~1"=="-p" GOTO RETRIEVE_PASSWORD
%a% IF "%~1"=="admin" GOTO OPEN_ADMIN_BROWSER_PAGE
%a% IF "%~1"=="app" GOTO OPEN_APPLICATION_BROWSER_PAGE
%a% IF "%~1"=="logs" GOTO WATCH_LOGS
%a% IF "%~1"=="build" GOTO BUILD
%a% IF "%~1"=="stop" GOTO STOP
%a% IF "%~1"=="rm" GOTO REMOVE
%a% IF "%~1"=="ssh" GOTO SSH
%a% SHIFT
%a% GOTO PARSE

:START
%a% echo STARTING
%a% docker run --name %NAME% -h %NAME%^
    -p %WSADMIN_SSL_CONSOLE_PORT%:%WSADMIN_SSL_CONSOLE_PORT%^
    -p 9442:%WSADMIN_HTTPS_PORT%^
    -p %HTTP_TRANSPORT_PORT%:%HTTP_TRANSPORT_PORT%^
    -p %DB2_SERVER_PORT%:%DB2_SERVER_PORT%^
    -d %IMAGE%
%a% SHIFT
%a% goto PARSE

:RETRIEVE_PASSWORD
%a% echo RETRIEVE PASSWORD
%a% docker exec %NAME% cat /tmp/PASSWORD
%a% SHIFT
%a% goto PARSE

:OPEN_ADMIN_BROWSER_PAGE
%a% echo OPEN ADMIN BROWSER PAGE
%a% start chrome https://localhost:%WSADMIN_SSL_CONSOLE_PORT%/ibm/console/logon.jsp
%a% SHIFT
%a% goto PARSE

:OPEN_APPLICATION_BROWSER_PAGE
%a% echo OPEN APPLICATION BROWSER PAGE
%a% start chrome http://localhost:%HTTP_TRANSPORT_PORT%/%CONTEXT_ROOT%
%a% SHIFT
%a% goto PARSE

:WATCH_LOGS
%a% start docker logs -f --tail=all %NAME%
%a% SHIFT
%a% goto PARSE

:BUILD
%a% cd %SANDBOX_HOME%\%NAME%
%a% docker build -t %IMAGE% .
%a% SHIFT
%a% goto PARSE

:STOP
%a% docker stop %NAME%
%a% SHIFT
%a% goto PARSE

:REMOVE
%a% docker rm %NAME%
%a% SHIFT
%a% goto PARSE

:SSH
%a% start docker exec -ti %NAME% /bin/bash
%a% SHIFT
%a% goto PARSE

:DOCKER_COMMIT
%a% docker commit fa526e74dd72 %IMAGE%
%a% SHIFT
%a% goto PARSE

:WSADMIN
%a% REM /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/wsadmin
%a% REM Enter username
%a% REM
%a% SHIFT
%a% goto END

:END 