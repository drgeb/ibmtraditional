FROM ibmcom/websphere-traditional:profile
COPY sample.servlet-2.1.0.war /tmp/
COPY scripts /tmp/scripts

RUN wsadmin.sh -lang jython -conntype NONE -c "AdminApp.install('/tmp/sample.servlet-2.1.0.war', '[ -appname sample.servlet-2.1.0 -contextroot /sample.servlet-2.1.0 -MapWebModToVH [[ sample.servlet-2.1.0.war sample.servlet-2.1.0.war,WEB-INF/web.xml default_host]]]')"

  #RUN wsadmin.sh -lang jython -conntype NONE -f '/tmp/scripts/sample.servlet-setup.py'

RUN wsadmin.sh -lang jython -conntype NONE -f /tmp/scripts/modJDBCSettings.py
 
