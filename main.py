SEPARATOR = ";"


def readValues(filename: str) -> str:
    """Reads numbers (one per row) from a file and returns them separated with ;"""
    file = open(filename, "r", encoding="utf-8")
    values: str = ""
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        row = line.strip()
        if len(row) == 0:
            continue
        if len(values) > 0:
            values += SEPARATOR
        values += row
    file.close()
    return values


def analyseValues(values: str) -> str:
    """Analyses the numbers and returns the result as CSV text (header row + data row)."""
    count: int = 0
    total: int = 0
    greatest: int = 0
    average: float = 0.0
    if len(values) > 0:
        parts = values.split(SEPARATOR)
        greatest = int(parts[0])
        for part in parts:
            number = int(part)
            count += 1
            total += number
            if number > greatest:
                greatest = number
        average = total / count
    result: str = "Count;Sum;Greatest;Average\n"
    result += "{0:d};{1:d};{2:d};{3:.2f}\n".format(count, total, greatest, average)
    return result


def displayResults(filename: str, results: str) -> None:
    print("#### Number analysis - START ####")
    print('File "{0:s}" results:'.format(filename))
    print(results)
    print("#### Number analysis - END ####")


def main() -> None:
    print("Program starting.")
    filename: str = input("Insert filename: ")
    values: str = readValues(filename)
    results: str = analyseValues(values)
    displayResults(filename, results)
    print("Program ending.")

if __name__ == "__main__":
    main()
