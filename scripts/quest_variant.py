import hashlib
import json
import random
import sys


VARIANTS = [
    {
        "id": 1,
        "name": "priority",
        "baseline_count": 150,
        "broken_count": 137,
        "data_field": "priority",
        "sort_field": "priority",
        "feature_key": "min_priority",
        "feature_default": None,
        "feature_neutral": None,
        "feature_label": "minimum priority",
        "probe_value": 3,
        "probe_signature": (
            "524fc2d11b77d3825398d8c01d3e547a"
            "bf5d0fe0fb805c5c11b14161d2260bcc"
        ),
    },
    {
        "id": 2,
        "name": "score",
        "baseline_count": 160,
        "broken_count": 144,
        "data_field": "score",
        "sort_field": "score",
        "feature_key": "min_score",
        "feature_default": 50,
        "feature_neutral": None,
        "feature_label": "minimum score",
        "probe_value": 55.5,
        "probe_signature": (
            "d0e478d31c07aabe9406d914bbc21842"
            "eb85e2efca3bf7e3da98948cd6033da6"
        ),
    },
    {
        "id": 3,
        "name": "category",
        "baseline_count": 140,
        "broken_count": 126,
        "data_field": "category",
        "sort_field": "category",
        "feature_key": "category_filter",
        "feature_default": None,
        "feature_neutral": None,
        "feature_label": "category filter",
        "probe_value": "beta",
        "probe_signature": (
            "f863f756922e0a241f19d4ce321e97c7"
            "ce3031ea0ca77970b38b066ac3d29a2e"
        ),
    },
    {
        "id": 4,
        "name": "age",
        "baseline_count": 180,
        "broken_count": 165,
        "data_field": "age",
        "sort_field": "age",
        "feature_key": "max_age",
        "feature_default": 65,
        "feature_neutral": None,
        "feature_label": "maximum age",
        "probe_value": 40.5,
        "probe_signature": (
            "a25b750013463dc37c7d93f0df57528b"
            "40512c098a183149922607078db5eefd"
        ),
    },
    {
        "id": 5,
        "name": "discount",
        "baseline_count": 125,
        "broken_count": 112,
        "data_field": "discount",
        "sort_field": "discount",
        "feature_key": "min_discount",
        "feature_default": None,
        "feature_neutral": None,
        "feature_label": "minimum discount",
        "probe_value": 20,
        "probe_signature": (
            "1a35299b15a6adb9f3032e19ed0819c3"
            "a9bfe7907687d2bd12aa89a4fbd8752f"
        ),
    },
    {
        "id": 6,
        "name": "status",
        "baseline_count": 132,
        "broken_count": 120,
        "data_field": "status",
        "sort_field": "status",
        "feature_key": "allowed_statuses",
        "feature_default": [
            "active",
            "pending",
            "archived",
        ],
        "feature_neutral": None,
        "feature_label": "allowed statuses",
        "probe_value": ["active"],
        "probe_signature": (
            "80f38015d36c07ec112493f708f46021"
            "f76eecccdeb3c56b5def87f79baeb925"
        ),
    },
    {
        "id": 7,
        "name": "rating",
        "baseline_count": 154,
        "broken_count": 140,
        "data_field": "rating",
        "sort_field": "rating",
        "feature_key": "min_rating",
        "feature_default": None,
        "feature_neutral": None,
        "feature_label": "minimum rating",
        "probe_value": 4,
        "probe_signature": (
            "4c609cfeb599476b377851b384a6bc98"
            "6ef2009c74aa006b2369d105b74f33d4"
        ),
    },
    {
        "id": 8,
        "name": "region",
        "baseline_count": 144,
        "broken_count": 132,
        "data_field": "region",
        "sort_field": "region",
        "feature_key": "allowed_regions",
        "feature_default": [
            "north",
            "south",
            "west",
        ],
        "feature_neutral": None,
        "feature_label": "allowed regions",
        "probe_value": ["south"],
        "probe_signature": (
            "2c3739c0c6a3f9c4b6989d8f63042a6"
            "9797ffc3171d246b856681430924cc5e3"
        ),
    },
    {
        "id": 9,
        "name": "quantity",
        "baseline_count": 135,
        "broken_count": 120,
        "data_field": "quantity",
        "sort_field": "quantity",
        "feature_key": "max_quantity",
        "feature_default": 100,
        "feature_neutral": None,
        "feature_label": "maximum quantity",
        "probe_value": 50.5,
        "probe_signature": (
            "eb92130adccd3cb2d5eaf572ac962868"
            "c0ba292bb2778f202c4a5b1b94ca61c1"
        ),
    },
    {
        "id": 10,
        "name": "reviewed",
        "baseline_count": 128,
        "broken_count": 112,
        "data_field": "reviewed",
        "sort_field": "id",
        "feature_key": "reviewed_filter",
        "feature_default": None,
        "feature_neutral": None,
        "feature_label": "review state filter",
        "probe_value": True,
        "probe_signature": (
            "48a5a756a1a767b902f6faf3e544b27f"
            "a68faa4c9fe3b93dedfb8cf3f9abb803"
        ),
    },
    {
        "id": 11,
        "name": "date",
        "baseline_count": 156,
        "broken_count": 143,
        "data_field": "created_at",
        "sort_field": "created_at",
        "feature_key": "end_date",
        "feature_default": "2026-09-30",
        "feature_neutral": None,
        "feature_label": "end date",
        "probe_value": "2026-09-15T23:59:59",
        "probe_signature": (
            "b57f566aba50a8ce539f8304708144e3"
            "235ce2e8a11c2246a2cdb38881545caf"
        ),
    },
    {
        "id": 12,
        "name": "progress",
        "baseline_count": 170,
        "broken_count": 160,
        "data_field": "progress",
        "sort_field": "progress",
        "feature_key": "max_progress",
        "feature_default": 100,
        "feature_neutral": None,
        "feature_label": "maximum progress",
        "probe_value": 60.5,
        "probe_signature": (
            "f5a833419a7d4a7dd7e47c259e2b1f5e"
            "f13c9a59f1d242a5b9f686bf7d474671"
        ),
    },
    {
        "id": 13,
        "name": "tag",
        "baseline_count": 126,
        "broken_count": 112,
        "data_field": "tag",
        "sort_field": "id",
        "feature_key": "tag_filter",
        "feature_default": None,
        "feature_neutral": None,
        "feature_label": "tag filter",
        "probe_value": "core",
        "probe_signature": (
            "31b0ae69a83dd42dcb3e4b5f76377b38"
            "dbbbe4811909aefb9987f5cfa525789c"
        ),
    },
    {
        "id": 14,
        "name": "code",
        "baseline_count": 150,
        "broken_count": 135,
        "data_field": "code",
        "sort_field": "code",
        "feature_key": "allowed_codes",
        "feature_default": [
            "A",
            "B",
            "C",
        ],
        "feature_neutral": None,
        "feature_label": "allowed codes",
        "probe_value": ["B"],
        "probe_signature": (
            "07b3dd22c07b29d8607f6bd603edd512"
            "3830c5acd235c345521a588eb44950cf"
        ),
    },
    {
        "id": 15,
        "name": "kind",
        "baseline_count": 165,
        "broken_count": 150,
        "data_field": "kind",
        "sort_field": "kind",
        "feature_key": "allowed_kinds",
        "feature_default": [
            "typea",
            "typeb",
            "typec",
        ],
        "feature_neutral": None,
        "feature_label": "allowed kinds",
        "probe_value": ["typeb"],
        "probe_signature": (
            "c3f915299b7ea99330d800333700cb72"
            "cff12693140f53f6fe6181c14679f2e6"
        ),
    },
]


PROJECT_CHANGES = [
    {
        "id": "source",
        "commit": "data: add source metadata",
    },
    {
        "id": "timestamps",
        "commit": "data: add import timestamps",
    },
    {
        "id": "paths",
        "commit": "refactor: centralize project paths",
    },
    {
        "id": "summary",
        "commit": "feat: add report summary",
    },
    {
        "id": "title",
        "commit": "config: add report title",
    },
    {
        "id": "helpers",
        "commit": "refactor: extract common helpers",
    },
    {
        "id": "ordering",
        "commit": "refactor: extract ordering helpers",
    },
    {
        "id": "logging",
        "commit": "chore: add logging configuration",
    },
    {
        "id": "usage",
        "commit": "docs: add usage example",
    },
    {
        "id": "changelog",
        "commit": "docs: update changelog",
    },
    {
        "id": "owner",
        "commit": "config: add report owner",
    },
    {
        "id": "export",
        "commit": "feat: add export settings",
    },
    {
        "id": "schema",
        "commit": "docs: document data schema",
    },
    {
        "id": "labels",
        "commit": "data: add display labels",
    },
    {
        "id": "format",
        "commit": "config: add output format",
    },
    {
        "id": "notes",
        "commit": "docs: add maintenance notes",
    },
    {
        "id": "metadata",
        "commit": "refactor: organize report metadata",
    },
    {
        "id": "encoding",
        "commit": "chore: document text encoding",
    },
]


def stable_seed(username):
    digest = hashlib.sha256(
        username.strip().lower().encode("utf-8")
    ).digest()

    return int.from_bytes(
        digest[:8],
        "big",
    )


def select_variant(username):
    seed = stable_seed(username)

    variant = dict(
        VARIANTS[
            seed % len(VARIANTS)
        ]
    )

    rng = random.Random(seed)

    changes = list(PROJECT_CHANGES)
    rng.shuffle(changes)

    variant.update(
        {
            "username": username,
            "seed": seed,
            "project_number": (
                1000 + seed % 8000
            ),
            "changes": changes[:7],
        }
    )

    return variant


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python quest_variant.py <username>",
            file=sys.stderr,
        )
        sys.exit(1)

    variant = select_variant(
        sys.argv[1]
    )

    print(
        json.dumps(
            variant,
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()