FROM ibmcom/websphere-traditional:8.5.5.12-profile

ENV PROFILE_HOME /opt/IBM/WebSphere/AppServer/profiles/AppSrv01
ENV WAS_HOME /opt/IBM/WebSphere/AppServer
ENV THIN_CLIENT_HOME /opt/IBM/WebSphere/ThinClient
ENV JYTHON_VERSION 2.5.2
ENV JYTHON_INSTALLER jython-installer-${JYTHON_VERSION}.jar
ENV JAVA_HOME ${THIN_CLIENT_HOME}/java
ENV PATH "${THIN_CLIENT_HOME}/java/bin:${PATH}"
ENV PYAML_TARGZ_PACKAGE PyYAML-3.13M.tar.gz
ENV APPNAME sample.servlet-2.1.0
ENV ARTIFACT  ${APPNAME}.war
ENV CONTEXTROOT /${APPNAME}

COPY ${ARTIFACT} /tmp/
COPY scripts /tmp/scripts

USER root
RUN mkdir -pv $THIN_CLIENT_HOME
RUN mkdir -pv $THIN_CLIENT_HOME/lib
RUN mkdir -pv $THIN_CLIENT_HOME/lib/jython
RUN mkdir -pv $THIN_CLIENT_HOME/properties
RUN mkdir -pv $THIN_CLIENT_HOME/etc
RUN mkdir -pv $THIN_CLIENT_HOME/logs
RUN mkdir -pv $THIN_CLIENT_HOME/profiles
RUN cp -r ${WAS_HOME}/java ${THIN_CLIENT_HOME}

COPY wsadminlib ${THIN_CLIENT_HOME}/wsadminlib

USER was
  
RUN wsadmin.sh -lang jython -conntype NONE -c "AdminApp.install('/tmp/${ARTIFACT}', '[ -appname ${APPNAME} -contextroot ${CONTEXTROOT} -MapWebModToVH [[ ${ARTIFACT} ${ARTIFACT},WEB-INF/web.xml default_host]]]')"

COPY scripts/createStringNameSpaceBinding.py ${THIN_CLIENT_HOME}/wsadminlib/bin/createStringNameSpaceBinding.py
RUN cd ${THIN_CLIENT_HOME}/wsadminlib/bin/ \
  && wsadmin.sh -lang jython -conntype NONE -f createStringNameSpaceBinding.py

RUN unset JYTHON_VERSION=2.5.2
RUN unset JYTHON_INSTALLER=jython-installer-${JYTHON_VERSION}.jar
RUN unset JAVA_HOME=${THIN_CLIENT_HOME}/java
RUN unset PYAML_TARGZ_PACKAGE=PyYAML-3.13M.tar.gz
#-Dwsadmin.script.libraries.packages=path1;path2;
#RUN cdwsadmin.sh -lang jython -conntype NONE -f '/tmp/scripts/sample.servlet-setup.py'
#RUN thinClient.sh -lang jython -conntype NONE -f /tmp/scripts/modJDBCSettings.py /tmp/scripts/modJDBCSettings.yaml
 
