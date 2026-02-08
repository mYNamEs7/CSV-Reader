from csv_reader.reports.average_gdp import AverageGDPReport
from csv_reader.models import Record


def test_average_gdp():
    records = [
        Record("USA", 100),
        Record("USA", 300),
        Record("China", 200),
    ]

    report = AverageGDPReport()
    result = report.generate(records)

    assert result == [
        ["USA", 200.0],
        ["China", 200.0],
    ]
