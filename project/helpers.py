def normalize_text(value):
    return " ".join(
        str(value).split()
    )


def record_name(record):
    return normalize_text(
        record.get("name", "")
    )
