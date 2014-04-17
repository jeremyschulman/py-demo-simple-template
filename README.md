# Template Rendering 101

This repo contains very simple demos that illustrates the bare-basics needed to load a YAML data file and render it with a Jinja2 template.  The "subject matter" was taken from a blog post by Ethan Banks, [here](http://ethancbanks.com/2014/04/11/how-to-simple-juniper-srx-rate-limiting-via-policer/).

Be sure to read more from Ethan on his blog site, [The Peering Introvert](http://ethancbanks.com/) and on [Packet Pushers](http://packetpushers.net/).

## Python Script Usage

````
user@linux> python demo_render.py
````

output looks like [this](demo_render.conf).

## Ansible Playbook Usage
````
[jeremy@linux]$ ansible-playbook ansible.pb.yml 

PLAY [simple template render] ************************************************* 

TASK: [build demo_render.conf] ************************************************ 
changed: [localhost]

PLAY RECAP ******************************************************************** 
localhost                  : ok=1    changed=1    unreachable=0    failed=0   
````
creates file [demo_render.conf](demo_render.conf).

## Further Reading

* [YAML](http://www.yaml.org/)
* [Jinja2](http://jinja.pocoo.org/docs/)
* [Ansible](docs.ansible.com)
