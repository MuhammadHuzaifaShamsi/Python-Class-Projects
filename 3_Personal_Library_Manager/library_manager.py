import json
import os

# File name where library data will be saved
FILENAME = "library.txt"

# Load books from file if it exists
def load_books():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return empty list if file is corrupted or empty
    return []

# Save current library data to file
def save_books(books):
    with open(FILENAME, "w") as file:
        json.dump(books, file, indent=4)

# Display the main menu
def show_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Show all books")
    print("5. Show statistics")
    print("6. Exit")

# Add a new book to the library
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    is_read = read_input == "yes"  # Convert user input to boolean

    # Create book dictionary
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": is_read
    }

    books.append(book)  # Add book to the list
    print("Book added successfully!")

# Remove a book by title
def remove_book(books):
    title = input("Enter the title of the book to remove: ").strip()
    for book in books:
        if book["title"].lower() == title.lower():  # Case-insensitive match
            books.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Search for books by title or author
def search_books(books):
    print("Search by:\n1. Title\n2. Author")
    option = input("Enter your choice (1 or 2): ")

    query = input("Enter search keyword: ").strip().lower()
    results = []

    if option == "1":
        # Search by title
        results = [book for book in books if query in book["title"].lower()]
    elif option == "2":
        # Search by author
        results = [book for book in books if query in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    # Display results
    if results:
        print("\nSearch Results:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No books found.")

# Display all books in the library
def show_all_books(books):
    if not books:
        print("Your library is empty.")
        return

    print("\nYour Library:")
    for i, book in enumerate(books, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Show total number of books and percentage read
def show_statistics(books):
    total = len(books)
    if total == 0:
        print("No books in library yet.")
        return

    read_count = sum(1 for book in books if book["read"])
    percent = (read_count / total) * 100

    print(f"Total books: {total}")
    print(f"Percentage read: {percent:.1f}%")

# Main program loop
def main():
    books = load_books()  # Load existing books from file

    while True:
        show_menu()  # Display the menu
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            show_all_books(books)
        elif choice == "5":
            show_statistics(books)
        elif choice == "6":
            save_books(books)  # Save to file on exit
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")

# Entry point of the program
if __name__ == "__main__":
    main()
