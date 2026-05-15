"""
validate_dataset.py
Saudi Legal AI Framework — Dataset Validator

يتحقق من صحة ملف saudi-contract-risk-dataset.csv قبل المساهمة.
Validates saudi-contract-risk-dataset.csv before contribution.

الاستخدام / Usage:
    python scripts/validate_dataset.py
    python scripts/validate_dataset.py --file datasets/your-file.csv
"""

import csv
import sys
import argparse
from pathlib import Path

# ── Constants ──────────────────────────────────────────────────────────────────

REQUIRED_COLUMNS = [
    "id",
    "contract_type",
    "clause_category",
    "clause_text",
    "risk_level",
    "risk_reason",
    "saudi_legal_note",
    "recommended_revision",
    "related_regulation",
    "requires_escalation",
    "language",
    "industry",
    "source_type",
    "reviewed_by_lawyer",
    "notes",
]

VALID_RISK_LEVELS = {"critical", "high", "medium", "low"}
VALID_BOOLEAN = {"yes", "no"}
VALID_LANGUAGES = {"en", "ar", "bilingual"}
VALID_SOURCE_TYPES = {"hypothetical", "abstracted", "published_case", "standard_form"}

DEFAULT_FILE = Path("datasets/saudi-contract-risk-dataset.csv")


# ── Helpers ────────────────────────────────────────────────────────────────────

class ValidationError:
    def __init__(self, row_num, column, value, message):
        self.row_num = row_num
        self.column = column
        self.value = value
        self.message = message

    def __str__(self):
        loc = f"Row {self.row_num}" if self.row_num else "Header"
        col = f" [{self.column}]" if self.column else ""
        val = f" → value: '{self.value}'" if self.value is not None else ""
        return f"  {loc}{col}{val}\n    {self.message}"


def print_section(title):
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


# ── Checks ─────────────────────────────────────────────────────────────────────

def check_file_readable(path: Path):
    errors = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            errors.append(ValidationError(None, None, None, "File is empty."))
    except FileNotFoundError:
        errors.append(ValidationError(None, None, None, f"File not found: {path}"))
    except UnicodeDecodeError:
        errors.append(ValidationError(None, None, None,
            "File is not valid UTF-8. Save with UTF-8 encoding."))
    return errors


def check_header(header: list):
    errors = []
    if header != REQUIRED_COLUMNS:
        missing = [c for c in REQUIRED_COLUMNS if c not in header]
        extra = [c for c in header if c not in REQUIRED_COLUMNS]
        wrong_order = header != REQUIRED_COLUMNS and not missing and not extra

        if missing:
            errors.append(ValidationError(None, None, None,
                f"Missing columns: {missing}"))
        if extra:
            errors.append(ValidationError(None, None, None,
                f"Unexpected extra columns: {extra}"))
        if wrong_order:
            errors.append(ValidationError(None, None, None,
                f"Column order mismatch.\n"
                f"    Expected: {REQUIRED_COLUMNS}\n"
                f"    Found:    {header}"))
    return errors


def check_row(row: dict, row_num: int):
    errors = []

    # Column count already enforced by DictReader if fieldnames match

    # id — must be non-empty and numeric
    id_val = row.get("id", "").strip()
    if not id_val:
        errors.append(ValidationError(row_num, "id", id_val, "id must not be empty."))
    elif not id_val.isdigit():
        errors.append(ValidationError(row_num, "id", id_val,
            "id must be a positive integer."))

    # risk_level — controlled vocabulary
    rl = row.get("risk_level", "").strip()
    if rl not in VALID_RISK_LEVELS:
        errors.append(ValidationError(row_num, "risk_level", rl,
            f"Must be one of: {sorted(VALID_RISK_LEVELS)}. "
            f"Check for uppercase or typos."))

    # requires_escalation — yes / no only
    re_val = row.get("requires_escalation", "").strip()
    if re_val not in VALID_BOOLEAN:
        errors.append(ValidationError(row_num, "requires_escalation", re_val,
            f"Must be 'yes' or 'no'. Found: '{re_val}'"))

    # reviewed_by_lawyer — yes / no only
    rl_val = row.get("reviewed_by_lawyer", "").strip()
    if rl_val not in VALID_BOOLEAN:
        errors.append(ValidationError(row_num, "reviewed_by_lawyer", rl_val,
            f"Must be 'yes' or 'no'. Found: '{rl_val}'"))

    # language — controlled vocabulary
    lang = row.get("language", "").strip()
    if lang not in VALID_LANGUAGES:
        errors.append(ValidationError(row_num, "language", lang,
            f"Must be one of: {sorted(VALID_LANGUAGES)}."))

    # source_type — controlled vocabulary
    st = row.get("source_type", "").strip()
    if st not in VALID_SOURCE_TYPES:
        errors.append(ValidationError(row_num, "source_type", st,
            f"Must be one of: {sorted(VALID_SOURCE_TYPES)}."))

    # Required non-empty text fields
    required_non_empty = [
        "contract_type", "clause_category", "clause_text",
        "risk_reason", "saudi_legal_note", "recommended_revision",
        "related_regulation",
    ]
    for col in required_non_empty:
        val = row.get(col, "").strip()
        if not val:
            errors.append(ValidationError(row_num, col, "",
                f"Column '{col}' must not be empty."))

    # Blank row detection — all meaningful fields empty
    meaningful = [row.get(c, "").strip() for c in REQUIRED_COLUMNS if c != "notes"]
    if all(v == "" for v in meaningful):
        errors.append(ValidationError(row_num, None, None,
            "Row appears to be entirely empty."))

    return errors


# ── Main ───────────────────────────────────────────────────────────────────────

def validate(path: Path):
    all_errors = []
    row_count = 0

    # 1. File readability
    print_section("1 / 5  File Readability")
    file_errors = check_file_readable(path)
    if file_errors:
        for e in file_errors:
            print(f"  ❌ {e}")
        print("\n  Cannot continue — fix file issues first.")
        return False
    print("  ✅ File is readable and UTF-8 encoded.")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []

        # 2. Header check
        print_section("2 / 5  Column Names & Order")
        header_errors = check_header(list(header))
        if header_errors:
            for e in header_errors:
                print(f"  ❌ {e}")
            print("\n  Cannot validate rows — fix header first.")
            return False
        print(f"  ✅ All {len(REQUIRED_COLUMNS)} columns present and in correct order.")

        # 3. Row validation
        print_section("3 / 5  Row-Level Validation")
        rows = list(reader)
        row_count = len(rows)

        if row_count == 0:
            print("  ⚠️  No data rows found (header only).")
        else:
            for i, row in enumerate(rows, start=2):
                row_errors = check_row(row, i)
                all_errors.extend(row_errors)

            if all_errors:
                for e in all_errors:
                    print(f"  ❌ {e}")
            else:
                print(f"  ✅ All {row_count} row(s) passed validation.")

    # 4. Duplicate id check
    print_section("4 / 5  Duplicate ID Check")
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ids = [row.get("id", "").strip() for row in reader if row.get("id", "").strip()]
    duplicates = [i for i in set(ids) if ids.count(i) > 1]
    if duplicates:
        print(f"  ❌ Duplicate id values found: {duplicates}")
        all_errors.append(object())  # mark as error
    else:
        print(f"  ✅ All IDs are unique.")

    # 5. Summary
    print_section("5 / 5  Summary")
    print(f"  File          : {path}")
    print(f"  Data rows     : {row_count}")
    print(f"  Total errors  : {len(all_errors)}")

    if all_errors:
        print(f"\n  ❌ Validation FAILED — fix {len(all_errors)} error(s) before committing.\n")
        return False
    else:
        print(f"\n  ✅ Validation PASSED — dataset is ready to commit.\n")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Validate saudi-contract-risk-dataset.csv"
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_FILE,
        help=f"Path to CSV file (default: {DEFAULT_FILE})",
    )
    args = parser.parse_args()

    passed = validate(args.file)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
