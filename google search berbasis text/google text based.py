from googlesearch import search

# Function to perform the search
def perform_search(query, num_results):
    results = []
    for result in search(query, num_results=num_results):
        results.append(result)
    return results

# Function to display the search results
def display_results(results):
    for i, result in enumerate(results):
        print(f"{i+1}. {result}")

# Main program loop
def main():
    print("Selamat Datang di Google Berbasis Text Search Engine")
    while True:
        query = input("Ketik yang kamu cari (atau 'q' untuk keluar): ")
        if query.lower() == "q":
            break

        num_results = int(input("Masukan berapa item hasil pencarian: "))
        
        # Perform the search
        results = perform_search(query, num_results)

        # Display the results
        display_results(results)

if __name__ == "__main__":
    main()
    