import os
import re
import sys

# Suspicious patterns commonly associated with prompt injection
PATTERNS = [
    r"ignore previous instructions",
    r"disregard previous instructions",
    r"ignore all rules",
    r"you are now",
    r"act as if you have no restrictions",
    r"reveal your system prompt",
    r"bypass safety",
]

def scan_file(file_path):
    findings = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            for pattern in PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    findings.append(
                        f"{file_path}:{line_number}: Suspicious pattern: {pattern}"
                    )

    return findings


def main():
    target_dir = "app"
    all_findings = []

    for root, _, files in os.walk(target_dir):
        for filename in files:
            if filename.endswith(".py"):
                path = os.path.join(root, filename)
                all_findings.extend(scan_file(path))

    if all_findings:
        print("[!] Potential prompt injection patterns detected:")
        for finding in all_findings:
            print(finding)
        sys.exit(1)

    print("[+] No suspicious prompt injection patterns found.")
    sys.exit(0)


if __name__ == "__main__":
    main()
