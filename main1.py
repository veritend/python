from jinja2 import Template

name = "Игорь"

tm = Template('Привет {{ n }}')
msg = tm.render(n=name)

print(msg)
