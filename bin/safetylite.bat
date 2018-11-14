@SET a=@
%a% REM "%~dp0" takes the argument %0 (the path to this script) and returns the drive and path to the
%a% REM homedirectory of this script, i.e returns the absolute path minus the file name. Note
%a% REM that this includes the final directory separator char.

%a% SET SHELL_SCRIPT_PATH=%~dp0

%a% REM https://hub.docker.com/r/ibmcom/websphere-traditional/
%a% REM https://hub.docker.com/r/ibmcom/websphere-traditional/
%a% REM http://david.currie.name/archives/2016/09/25/building-application-images-with-websphere-traditional
%a% REM https://www.ibm.com/support/knowledgecenter/en/SSZLC2_8.0.0/com.ibm.commerce.install.doc/refs/rigsrvportno.htm
%a% REM WebSphere Application Server administrative console secure port. This port requires SSL.
%a% REM WebSphere Application Server HTTPS transport port.

%a% SET WSADMIN_SSL_CONSOLE_PORT=9043
%a% SET WSADMIN_HTTPS_PORT=9443
%a% SET HTTP_TRANSPORT_PORT=9080
%a% SET DB2_SERVER_PORT=50000
%a% REM SET IMAGE=ibmcom/websphere-traditional:profile
%a% SET IMAGE=safetylite/live:latest
%a% SET NAME=safetylite
%a% SET CONTEXT_ROOT=SafetyLiteWeb

@REM CONFIGURE GENERAL TOOLS USED
%a% CALL "%SHELL_SCRIPT_PATH%\start-websphere-traditional.bat" %*