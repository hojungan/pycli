import click
import pycli.services.env as env

@click.group()
@click.pass_context
def cli(ctx):
    """
    Add environment variable values
    """
    pass

@cli.command()
@click.option('--api-key', type=str, default=None, help="OpenWeather API Key")
@click.pass_obj
def add(ctx, api_key):
    if api_key:
        if env.getenv(env.WEATHER) is None:
            env.setenv(env.WEATHER, api_key)
            click.secho("Weather API key added", fg='green')
        else:
            click.secho("You already have API key", fg='cyan')
    else:
        click.secho("Please provide API Key", fg="bright_red")
        raise click.Abort()