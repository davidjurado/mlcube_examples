"""MLCube handler file"""
import os
import typer
import subprocess


app = typer.Typer()


class EvaluateTask:
    """Runs evaluation metrics given the predictions and ground truth files"""

    @staticmethod
    def run(
        data_path: str, parameters_file: str, output_file: str
    ) -> None:
        cmd = f"python3 logic.py --data_path={data_path} --parameters_file={parameters_file} --output_file={output_file}"
        splitted_cmd = cmd.split()

        process = subprocess.Popen(splitted_cmd, cwd=".")
        process.wait()


@app.command("evaluate")
def evaluate(
    data_path: str = typer.Option(..., "--data_path"),
    parameters_file: str = typer.Option(..., "--parameters_file"),
    output_path: str = typer.Option(..., "--output_path"),
):
    EvaluateTask.run(data_path, parameters_file, output_path)


@app.command("test")
def test():
    pass


if __name__ == "__main__":
    app()
