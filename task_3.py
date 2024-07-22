import re
import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    pattern = r"(?P<Date>\d{4}-\d{2}-\d{2}) (?P<Time>\d{2}:\d{2}:\d{2}) (?P<Type>\w+) (?P<Text>.+)"
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    else:
        raise Exception("ERROR while reading lines, line:" + line.strip())


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            if not line.strip():
                continue

            log = parse_log_line(line)
            if log:
                logs.append(log)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = filter(lambda log: log.get("Type") == level, logs)
    list_logs = []
    for log in filtered_logs:
        list_logs.append(" ".join(log.values()))
    return list_logs


def count_logs_by_level(logs: list) -> dict:
    count_logs = defaultdict(int)
    for log in logs:
        count_logs[log.get("Type")] += 1

    return count_logs


def display_log_counts(counts: dict) -> None:
    print(f'{"Log level":16} | {"Count":<9}')
    print(f'{"-" * 16} | {"-" * 9}')

    for key in counts.keys():
        print(f'{key:16} | {counts[key]:<9}')
    pass


def main() -> None:
    try:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts_logs = count_logs_by_level(logs)
        display_log_counts(counts_logs)

        if len(sys.argv) > 2:
            level = sys.argv[2].upper()
            filtered_logs = filter_logs_by_level(logs, level)
            if not len(filtered_logs):
                print(f"\nNo records for level '{level}':")
                return

            print(f"\nDetails of the logs for the level '{level}':")
            for log in filtered_logs:
                print(log)
    except FileNotFoundError as error:
        print(error.strerror)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
