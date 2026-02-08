import csv
from typing import Iterable
from csv_reader.models import Record


def read_records(file_paths: Iterable[str]) -> list[Record]:
    records: list[Record] = []

    for path in file_paths:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(
                    Record(
                        country=row["country"],
                        gdp=float(row["gdp"]),
                    )
                )

    return records
