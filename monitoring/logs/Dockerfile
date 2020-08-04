FROM docker.elastic.co/beats/filebeat:7.8.1
COPY filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown root:root /usr/share/filebeat/filebeat.yml
