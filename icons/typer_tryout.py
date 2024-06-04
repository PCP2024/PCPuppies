import typer
# from processing.processing_fun import *
# from dataio.loading_fun import *
# from dataio.saving_fun import *
# from analyze.analysis_fun import *

app = typer.Typer(help='Our PCP CLI')

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye():
    print("Goodbye")

app.add_typer(hello, name='hello')
app.add_typer(goodbye)


if __name__ == "__main__":
    app()

