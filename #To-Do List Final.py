#To-Do List
#1/18/24
#Alma Marhshall

#functions
movies= [ ]

#Adds a movie to the list.
def AddTask(): 
    newmovie= input("Add a movie: ")
    movies.insert(1, newmovie)
#Allows user to view their list.
def view(): 
    print(movies)
#Marks a task as complete.
def MarkTask(): 
    print(movies)
    watched= int(input("What movie did you watch? Please type it's number placement on the list, minus one."))
    movies[watched]= movies[watched] + " ✓"
#Removes an item you select from the list.
def Remove():
    delete= (input("Remove a movie currently on your list by typing its name."))
    movies.remove(delete)
#Clears all items from list.
def Clear():
    movies.clear()
#Sorts all items on list in alphabetical order. 
def order(): 
    movies.sort()
    print(movies)
#Prints the number of items on list.
def count():
    length=len(movies)
    print(length)

#Presents the user with a menu and 8 options to choose from in order to preform the prior functions created. 
def movielist(): 
    option= int(input("This is the menu. Choose an option to continue: \n 1. Add a movie to list \n 2. View list \n 3. Mark a movie as watched \n 4. Remove a movie from list \n 5. Remove ALL movies from current list \n 6. Sort list alphabetically \n 7. Show number of movies on list \n 8. Quit list"))
    if (option == 1):
        AddTask()
        movielist()
    if (option == 2):
        view()
        movielist()
    if (option == 3): 
        MarkTask()
        movielist()
    if (option == 4):
        Remove()
        movielist()
    if (option== 5):
        Clear()
        movielist()
    if (option== 6):
        order()
        movielist()
    if (option==7):
        count()
        movielist()
    if (option== 8):
        print("Bye!")
        quit()
    elif (option != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):
        print ("ERROR! Please retuen to your Movielist menu. ")
        movielist()

#The entire program plus an opening greeting. 
def ToDoList():
    print ("Welcome to your movie list! Use this list to keep track of all the movies you asipire to see." )
    movielist()
    
#functions
ToDoList()