from jinja2 import Environment, FileSystemLoader

titles = [
    {'title': "Домашнее задание"},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=titles)

print(msg)
