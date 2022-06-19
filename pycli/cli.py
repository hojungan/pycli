import click
import os


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):  # sourcery skip: for-append-to-extend, list-comprehension
        rv = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                rv.append(filename.replace(".py", ""))
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"pycli.commands.{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """
    Some information on using wt CLI
    """
    pass


if __name__ == "__main__":
    cli()