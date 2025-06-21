""" word occurrences
Estimate : 60 minutes
Actual: 90 minutes """
FILENAME = "wimbledon.csv"


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = load_records(FILENAME)
    champion_to_win, countries = process_data(records)
    display_results(champion_to_win, countries)


def load_records(filename):
    """Load records from file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return sorted (records)

def process_data(records):
    """Make dictionary of the champions and countries."""
    champion_to_win = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_win[record[2]] += 1
        except KeyError:
            champion_to_win[record[2]] = 1
    return champion_to_win, countries


def display_results(champion_to_win, countries):
    """Display champions and their country"""
    print("Wimbledon Champions: ")
    for champion , wins in champion_to_win.items():
        print(champion , wins)
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))




main()