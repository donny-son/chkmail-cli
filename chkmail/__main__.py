from validate_email import validate_email
import typer
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="E-Mail Checker", style="magenta")


def main(email: str):
    is_valid = validate_email(email_address=email)
    table.add_column("E-Mail", justify="center", style="cyan", no_wrap=True)
    table.add_column("Validity", justify="center")
    table.add_row(email, "✅" if is_valid else "🚫")
    console.print(table)


typer.run(main)
