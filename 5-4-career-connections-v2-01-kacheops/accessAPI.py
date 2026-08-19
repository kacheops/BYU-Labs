import requests

def get_summary(book, chapter):
    base_url = "https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/"
    # TODO: Create a URL string that will access the API for the given book and chapter
    # HINT: The URL should be in the format f"{base_url}{book.lower()}/{chapter}"
    url = f"{base_url}{book.lower()}/{chapter}"
    # HINT: Use the requests.get() method to access the API and return the JSON data
    response = requests.get(url)
    data = response.json()
    # HINT: Extract the summary from the JSON data and return it

    return data["chapter"]["summary"]


def run_summary_tool():

    # Print a welcome message as shown in the example. "Welcome to the Book of Mormon Summary Tool!"
    print("\nWelcome to the Book of Mormon Summary Tool!\n")
    
    # Use a while loop to allow the user to input a book and chapter
    while True:
    # Ask the user for the book and chapter they would like to view a summary of
        book = input("Which book of the Book of Mormon would you like to view? : ").capitalize()
        chapter = input("Which chapter of " + book + " are you interested in? : ")
    # Use the get_summary() function to retrieve the summary and print it
        try:
            summary = get_summary(book, chapter)
            print(f"\nSummary of {book.capitalize()} Chapter {chapter}:\n{summary}\n")
            '''print("\nSummary:")
            print(summary)'''
    # If the book or chapter is invalid, catch the KeyError and print an error message
        except KeyError:
            print(f"\nSorry, the book '{book}' or chapter '{chapter}' does not exist. Please try again.\n")
    # Ask the user if they would like to view another summary
        another = input("Would you like to view another summary? (Y/N): ").upper()

    # Exit the loop if the user does not want to view another summary
        if another != 'Y':
            
    # If the user does not want to view another summary, print "Thank you for using Book of Mormon Summary Tool!"
            print("Thank you for using Book of Mormon Summary Tool!")
                        
    # do not forget to finish or break the loop
            break

if __name__ == "__main__":
    run_summary_tool()


    