import json
from pathlib import Path

ROOT = Path(__file__).parent


def should_include(record, config):
    if not record.get("enabled", True):
        return False

    value = config.get("max_progress")

    if (
        value is not None
        and record["progress"] > value
    ):
        return False

    return True


def build_report():
    with open(
        ROOT / "data.json",
        encoding="utf-8",
    ) as f:
        records = json.load(f)

    with open(
        ROOT / "config.json",
        encoding="utf-8",
    ) as f:
        config = json.load(f)

    result = [
        record
        for record in records
        if should_include(record, config)
    ]

    result.sort(
        key=lambda record: (
            record[config["sort_by"]],
            record["id"],
        ),
        reverse=config["descending"],
    )

    return result


if __name__ == "__main__":
    result = build_report()
    print(
        f"Report contains {len(result)} records"
    )
