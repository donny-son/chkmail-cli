from validate_email import validate_email
import typer


def main(email: str):
    is_valid = validate_email(email_address=email)
    typer.echo(f"{email} is {'valid ✅' if is_valid else 'invalid 🚫'}")


typer.run(main)
