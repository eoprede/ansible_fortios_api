# Running Ansible in Docker

Documentation on how to run Ansible in Docker.

## Why?

It's mainly a convenience thing - instead of installing Ansible and then doing additional manipulations to install fortios_api module, I can simply run a container.

Another use case - running multiple different Ansible versions on the same host - I need to do it now, where systems guys are running 2.4 and I need additional F5 modules that are available in 2.6

Not to mention that there are still people who use Windows machines and containers provide nice and easy way to run Ansible from it (you just need to use absolute paths to forward the directory).

## How?

Easiest option - just pull image from docker hub and run it.

    docker pull eoprede/ansible_fortios_api
    docker run --rm -it -v $(pwd):/ansible/playbooks eoprede/ansible_fortios_api test.yaml

First command downloads the image. Second command shares your current directory with the container and runs an ansible-playbook test.yaml command. Then the container is cleaned up after it finishes the execution. So basically you can think of it as just an ansible executable, except instead of `ansible-playbook` command you will have to type `docker run --rm -it -v $(pwd):/ansible/playbooks eoprede/ansible_fortios_api`

If you want to customize the image (i.e. you want some additional modules, or you want to run 2.6.0rc) you can just edit the Dockerfile and build image yourself. To build the image, enter the directory with Dockerfile and run

    docker build -t ansible_fortios_api .

After that you can run your local container with

    docker run --rm -it -v $(pwd):/ansible/playbooks ansible_fortios_api

## Credits and additional documentation

I used the following work for this container: https://github.com/walokra/docker-ansible-playbook
You can find additional documentation, including how to run it with vault, at the link above.