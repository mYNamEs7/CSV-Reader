import tempfile
import subprocess
import sys
from pathlib import Path


def test_cli_runs():
    csv_content = """country,year,gdp
USA,2022,100
USA,2023,300
"""

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "data.csv"
        path.write_text(csv_content)

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "csv_reader.main",
                "--files",
                str(path),
                "--report",
                "average-gdp",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "USA" in result.stdout
