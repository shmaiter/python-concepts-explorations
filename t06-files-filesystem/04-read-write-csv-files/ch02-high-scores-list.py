from pathlib import Path
import csv


def sort_by_name_and_score(data):
    return sorted(data, key=lambda x: (x["name"], x["score"]), reverse=True)


def process_dict(data):
    headers = list(data[0].keys())
    for item in data:
        item[headers[1]] = int(item[headers[1]])
    return sort_by_name_and_score(data)


high_scores = []

file_path = Path.cwd() / "scores.csv"
with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    scores_list = process_dict(list(reader).copy())
    headers = list(scores_list[0].keys())

    name_values = {row[headers[0]] for row in scores_list}

    for row in scores_list:
        if len(high_scores) > 0:
            if row[headers[0]] in name_values:
                high_scores.append(row)
                name_values.remove(row[headers[0]])
        else:
            high_scores.append(row)
            name_values.remove(row[headers[0]])

output_csv_file = Path.cwd() / "high_scores.csv"
with output_csv_file.open(mode="w", encoding="utf-8", newline="\n") as file:
    writer = csv.DictWriter(file, fieldnames=high_scores[0].keys())
    writer.writeheader()
    writer.writerows(high_scores)
