import click
import requests
import json
import pycli.services.env as env


@click.command()
@click.argument("city")
def cli(city):
    API_KEY = env.getenv(env.WEATHER)
    if API_KEY is None:
        click.secho("You need to add API key. Try `pycli config --help`", fg="red")
        raise click.Abort()

    __WEATHER_API = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    result = requests.get(__WEATHER_API)
    data = json.loads(result.text)
    click.echo(f"Condition: {data['weather'][0]['description'].upper()}")
    click.echo(f"Temperature: {data['main']['temp']} Celcius")
    click.echo(f"Feels Like: {data['main']['feels_like']} Celcius")
    click.echo(f"Humidity: {data['main']['humidity']}%")
    click.echo(f"Wind: {data['wind']['speed']}Km/h")