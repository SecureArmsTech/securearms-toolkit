import typer

app = typer.Typer(help="P2P relay service commands")

@app.command()
def start():
    """Start local relay service (echo stub)"""
    typer.echo("[relay] Starting local P2P relay... [stub]")

@app.command()
def status():
    """Print relay status"""
    typer.echo("[relay] Relay status: RUNNING (stub)")

@app.command()
def config(path: str = typer.Option(..., help="Path to JSON config file")):
    """Load relay config from file"""
    typer.echo(f"⚙️ [relay] Loading config from {path}... [stub]")
