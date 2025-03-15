import csv


def write_csv_file(filename, data):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerows(data)
        print(f"Data has been written to {filename}.")


def main():
    data = [
        ["pradeep", 18, "tumkur"],
        ["rahul", 18, "tumkur"],
        ["prajwl", 18, "tumkur"],  # Added a comma here
        ["raghu", 18, "tumkur"]
    ]
    write_csv_file('people.csv', data)  # Fixed indentation


if __name__ == "__main__":
    main()
