import argparse
import getpass
import re
from typing import Dict, List


CHECKS = (
    ("At least 8 characters", lambda value: len(value) >= 8),
    ("Uppercase letter", lambda value: bool(re.search(r"[A-Z]", value))),
    ("Lowercase letter", lambda value: bool(re.search(r"[a-z]", value))),
    ("Number", lambda value: bool(re.search(r"\d", value))),
    ("Special character", lambda value: bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", value))),
)


def evaluate_password(password: str) -> Dict[str, object]:
    checklist: List[Dict[str, object]] = []
    score = 0

    for label, validator in CHECKS:
      passed = validator(password)
      checklist.append({"label": label, "passed": passed})
      score += int(passed)

    if score <= 2:
        level = "weak"
    elif score <= 4:
        level = "medium"
    else:
        level = "strong"

    return {
        "score": score,
        "level": level,
        "checklist": checklist,
    }


def print_report(report: Dict[str, object]) -> None:
    print("\nPassword strength report")
    print("------------------------")
    print(f"Level: {report['level'].title()}")
    print(f"Score: {report['score']}/{len(CHECKS)}")
    print("\nChecklist:")

    for item in report["checklist"]:
        marker = "OK" if item["passed"] else "NO"
        print(f"- [{marker}] {item['label']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate password strength from the terminal."
    )
    parser.add_argument(
        "--password",
        help="Provide a password directly instead of using hidden terminal input.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    password = args.password or getpass.getpass("Enter a password to evaluate: ")

    report = evaluate_password(password)
    print_report(report)


if __name__ == "__main__":
    main()
