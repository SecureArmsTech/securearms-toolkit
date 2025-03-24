import typer
from securearms.core import wallet, relay, setup, debug

app = typer.Typer(help="SecureArms Toolkit CLI")

# Register subcommands
app.add_typer(wallet.app, name="wallet", help="Manage keys, balance, send/receive")
app.add_typer(relay.app, name="relay", help="Start or inspect P2P relays")
app.add_typer(setup.app, name="setup", help="Initialize configs and CLI environment")
app.add_typer(debug.app, name="debug", help="Debugging and logging options")

if __name__ == "__main__":
    app()
