def delete_book(books_list):
    bid = input("Enter the book ID to delete: ")
    check_book = books_list.search(bid)
    if check_book is None:
        print("The book does not exist in the library")
    else:
        books_list.delete(bid)
        print("Book deleted successfully.")
        books_list.writetxt()
#def