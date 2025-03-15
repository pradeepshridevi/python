import csv


def read_csv_file(filename):
    try:
        
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            
            
            header = next(reader)  
            print("Header:", header)
            
           
            print("\nData:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    
    read_csv_file('people.csv')

if __name__ == "__main__":
    main()
