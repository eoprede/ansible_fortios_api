FROM alpine:3.7

ENV ANSIBLE_VERSION 2.5.5

ENV BUILD_PACKAGES \
bash \
curl \
tar \
openssh-client \
sshpass \
git \
python \
py-boto \
py-dateutil \
py-httplib2 \
py-jinja2 \
py-paramiko \
py-pip \
py-yaml \
ca-certificates \
rsync

RUN set -x && \
\
echo "==> Adding build-dependencies..." && \
apk --update add --virtual build-dependencies \
gcc \
musl-dev \
libffi-dev \
openssl-dev \
python-dev && \
\
echo "==> Upgrading apk and system..." && \
apk update && apk upgrade && \
\
echo "==> Adding Python runtime..." && \
apk add --no-cache ${BUILD_PACKAGES} && \
pip install --upgrade pip && \
pip install python-keyczar docker-py && \
pip install f5-sdk && \
pip install netaddr && \
\
echo "==> Installing Ansible..." && \
pip install ansible==${ANSIBLE_VERSION} && \
\
echo "==> Cleaning up..." && \
apk del build-dependencies && \
rm -rf /var/cache/apk/* && \
\
echo "==> Adding hosts for convenience..." && \
mkdir -p /etc/ansible /ansible && \
echo "[local]" >> /etc/ansible/hosts && \
echo "localhost" >> /etc/ansible/hosts

RUN mkdir /source
RUN cd /source && git clone https://github.com/eoprede/ansible_fortios_api.git
RUN rsync -a /source/ansible_fortios_api/module_utils/ /usr/lib/python2.7/site-packages/ansible/module_utils/ && \
rsync -a /source/ansible_fortios_api/fortios/ /usr/lib/python2.7/site-packages/ansible/modules/network/fortios/

ENV ANSIBLE_GATHERING smart
ENV ANSIBLE_HOST_KEY_CHECKING false
ENV ANSIBLE_RETRY_FILES_ENABLED false
ENV ANSIBLE_ROLES_PATH /ansible/playbooks/roles
ENV ANSIBLE_SSH_PIPELINING True
ENV PYTHONPATH /ansible/lib
ENV PATH /ansible/bin:$PATH
ENV ANSIBLE_LIBRARY /ansible/library

WORKDIR /ansible/playbooks

ENTRYPOINT ["ansible-playbook"]
