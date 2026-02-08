from collections import defaultdict
from csv_reader.reports.base import Report
from csv_reader.models import Record


class AverageGDPReport(Report):
    name = "average-gdp"

    def generate(self, records: list[Record]) -> list[list]:
        totals = defaultdict(list)

        for r in records:
            totals[r.country].append(r.gdp)

        result = [
            [country, round(sum(values) / len(values), 2)]
            for country, values in totals.items()
        ]

        result.sort(key=lambda x: x[1], reverse=True)
        return result
