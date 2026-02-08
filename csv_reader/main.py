import argparse
from tabulate import tabulate

from csv_reader.io_utils import read_records
from csv_reader.reports.average_gdp import AverageGDPReport
from csv_reader.reports.base import Report


REPORTS: dict[str, Report] = {
    AverageGDPReport.name: AverageGDPReport(),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    if args.report not in REPORTS:
        raise ValueError(f"Unknown report: {args.report}")

    records = read_records(args.files)
    report = REPORTS[args.report]

    table = report.generate(records)

    print(
        tabulate(
            table,
            headers=["country", "gdp"],
            showindex=True,
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    main()
