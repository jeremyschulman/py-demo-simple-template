from jinja2 import Template
import yaml

datavars = yaml.load(open('datavars.yml').read())
template = Template(open('srx-policer.j2').read())
print template.render(datavars)

