FROM ibmcom/websphere-traditional:8.5.5.12-profile

ENV PROFILE_HOME /opt/IBM/WebSphere/AppServer/profiles/AppSrv01
ENV WAS_HOME /opt/IBM/WebSphere/AppServer
ENV THIN_CLIENT_HOME /opt/IBM/WebSphere/ThinClient

ENV APPNAME sample.servlet-2.1.0
ENV ARTIFACT  ${APPNAME}.war
ENV CONTEXTROOT /${APPNAME}

#RUN wsadmin.sh -lang jython -conntype NONE -c "AdminApp.install('${THIN_CLIENT_HOME}/target/${ARTIFACT}', '[ -appname ${APPNAME} -contextroot ${CONTEXTROOT} -MapWebModToVH [[ ${ARTIFACT} ${ARTIFACT},WEB-INF/web.xml default_host]]]')"

COPY --chown=was:was was-config.props /work/config
COPY --chown=was:was target/${ARTIFACT} /work/app
COPY --chown=was:was scripts/configureWebSphere.py /work/
COPY --chown=was:was wsadminlib/bin/wsadminlib.py /work/
COPY --chown=was:was configure.sh /work
COPY --chown=was:was run_py_script.sh /work
COPY --chown=was:was modify_password.sh /work

RUN cd /work && /work/configure.sh /work/configureWebSphere.py