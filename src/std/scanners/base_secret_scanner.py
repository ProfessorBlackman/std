import os
import re

from rich.console import Console
from rich.table import Table
from tqdm import tqdm

from ..patterns import SECRET_PATTERNS


class BaseSecretScanner:
    console = Console()

    def scan_directory(self, path: str) -> dict:
        """
        Scan a directory recursively for secrets.
        :param path:str: The path to the directory to scan.
        :return:results: dict: A dictionary containing the results of the scan.
        """
        results = {}
        file_paths_discovered = []
        for root, _, files in os.walk(path):
            for file in files:
                file_paths_discovered.append(os.path.join(root, file))

        for file_path in tqdm(file_paths_discovered, desc="Scanning files", unit="file"):
            secrets_found = self.scan_file(file_path)
            if secrets_found:
                results[file_path] = secrets_found

        return results

    def scan_file(self, file_path: str) -> list:
        """
        Scan a file for secrets.
        :param file_path:str : The path to the file to scan.
        :return:secrets:list: A list of secrets found in the file.
        """
        secrets = []
        try:
            with open(file_path, 'r', errors='ignore') as file:
                content = file.read()
                for secret_type, pattern in SECRET_PATTERNS.items():
                    matches = re.findall(pattern, content)
                    if matches:
                        secrets.append((secret_type, matches))
        except Exception as e:
            self.console.print(f"[red]Error reading {file_path}: {e}[/red]")
        return secrets

    def display_results(self, results: dict):
        if results:
            table = Table(title="Secrets Found")
            table.add_column("File Path", style="cyan", no_wrap=True)
            table.add_column("Secret Type", style="magenta")
            table.add_column("Secret Value", style="yellow")

            for file_path, secrets in results.items():
                for secret_type, matches in secrets:
                    for match in matches:
                        table.add_row(file_path, secret_type, match)

            self.console.print(table)
        else:
            self.console.print("[green]No secrets found.[/green]")
