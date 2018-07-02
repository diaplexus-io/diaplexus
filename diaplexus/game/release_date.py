import csv

import jinja2


TEMPLATES_DIR = r'.\templates'


def render_template(
    template_folder, template_file, template_data
):
    autoescape = jinja2.select_autoescape(['html'])
    env = jinja2.Environment(
        autoescape=autoescape,
        loader=jinja2.FileSystemLoader(template_folder)
    )
    template = env.get_template(template_file)
    return template.render(**template_data)


def load_releases():
    with open('./resources/game_release-date_2018.csv') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        records = []
        for line in csv_reader:
            record = dict(zip(header, line))
            records.append(record)

    return records


def render_releases():
    records = load_releases()
    rendered = render_template(
        template_folder=TEMPLATES_DIR,
        template_file='game_release-date.html',
        template_data={
            'release_dates': records
        }
    )
    return rendered
