import click
from .scanners import BaseScanner


@click.group()
def cli():
    """
    CLI tool to scan codebases for exposed secrets.
    """
    pass


@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, readable=True))
def scan_directory_command(directory):
    """
    Scan an entire directory for exposed secrets.
    """
    click.echo(f"Scanning {directory} for exposed secrets...")
    scanner = BaseScanner()
    results = scanner.scan_directory(directory)
    scanner.display_results(results)


@cli.command()
@click.argument('file_path', type=click.Path(exists=True, dir_okay=False, readable=True))
def scan_file_command(file_path):
    """
    Scan a single file for exposed secrets.
    """
    click.echo(f"Scanning {file_path} for exposed secrets...")
    scanner = BaseScanner()
    results = {file_path: scanner.scan_file(file_path)}
    scanner.display_results(results)


if __name__ == '__main__':
    cli()
