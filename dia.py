import click

from diaplexus.game import release_date


@click.group()
def cli():
    return True


@cli.command('build-release-dates')
def cmd_build_release_dates():
    rendered = release_date.render_releases()
    with open(r'.\docs\game\release-date\2018\index.html', 'w') as out:
        out.write(rendered)


if __name__ == '__main__':
    cli()
