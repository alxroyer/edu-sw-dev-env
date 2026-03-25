FROM maven:3.9.12-eclipse-temurin-21

# Memo:
#   `maven` `eclipse-temurin` based on Ubuntu, not Alpine.
#   Use `apt-get`, not `apk`.
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y openssh-server

# Prepare SSH files, directories and configurations.
RUN mkdir -p /run/sshd
RUN mkdir -p /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Set `root` pwd.
RUN echo 'root:pwdpwdpwd' | chpasswd

# Ensure `JAVA_HOME` set for `root`.
RUN echo "export JAVA_HOME=/opt/java/openjdk" >> /root/.bashrc

# Expose SSH port.
EXPOSE 22

# Start SSH server when the container starts.
CMD ["/usr/sbin/sshd", "-D"]
