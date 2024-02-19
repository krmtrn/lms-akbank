class Library:
    def __init__(self, books):
        self.books = books
        self.file = open(self.books, "a+")

    def __del__(self):
        self.file.close()

    def listbooks():
        with open("books.txt", "a+") as dtbs:
            dtbs.seek(0)
            dataread = dtbs.read()
            print(dataread)
            # The reason why I didn't use readlines() is that it returns a list of lines, and I don't want to print the list with brackets and commas which is not aesthetic.

    def removebook(inf):
        lastdecision = input(f"Are you sure to delete '{choicetodelete}' ? \nYes, Delete '{choicetodelete}' - 1 \nNo, Back to The Menu - 0 \nEnter Key : ")
        if lastdecision == "1":
            try:
                with open("books.txt", "r", encoding="utf-8") as dtbs:
                    data = dtbs.readlines()

                with open("books.txt", "w", encoding="utf-8") as dtbs:
                    found = False
                    for datum in data:
                        if inf not in datum:
                            dtbs.write(datum)
                        else:
                            found = True
                            print(f"Line(s) Containing '{inf}' is deleted. \n")
                    if not found:
                        print(f"There Is No Such Data Containing '{inf}' In The Database. \n")
            except Exception as Err:
                print(f"Unexpected : {Err}")
        else:
            pass
 
    def addbook(data):
        try:
            with open("books.txt", "a", encoding="utf-8") as dtbs:
                for datum in data:
                    dtbs.write(datum + "\n")
        except Exception as Err:
            print(f"Unexpected : {Err}")

from lms import Library as lib

while True:
    print("LMS MAIN MENU")
    print("1- List Books")
    print("2- Add Book(s)")
    print("3- Remove Book(s)")
    print("Q- Exit")
    choice = input("Enter Key: ")
    if choice == "1":
        print("\n")
        print("BOOK LISTS")
        lib.listbooks()
    elif choice == "2":
        print("\n")
        print("BOOK ADDING PORTAL")
        userdata = []
        while True:
            data = input("Enter Data as 'Title, Author, Release Year, Number of Pages' (To Exit Press 'Q'): ")
            if data.lower() == "q":
                print("Data Entry Is Completed.")
                print("\n")
                break
            else:
                userdata.append(data)
                print(f"'{data}' Is Saved.")
        lib.addbook(userdata)
    elif choice == "3":
        print("\n")
        print("BOOK REMOVE")
        global choicetodelete
        choicetodelete = input("Enter The Name Of The Book You Want To Delete: ")
        lib.removebook(choicetodelete)
    elif choice.lower() == "q":
        print("\n")
        print("Are You Sure To Exit?")
        print("Yes, Exit - 1")
        print("No, Keep on LMS - 0")
        print("\n")
        choiceexit = input("Enter Key: ")
        if choiceexit == "1":
            exit()
        else:
            print("\n")
            pass
    else:
        pass    

