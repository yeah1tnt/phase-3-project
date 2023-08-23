

class myCLI:
    def __init__(self):
        self.main()

    def main(self):
        count = 3
        user_input = input("Enter a word: ")
        print(f"\nThe word you entered is: {user_input}")
        print(f"\nWhat do you want to do with this word?")

        while user_input != "exit":
            print("\nEnter 'add' to add the word to the dictionary")
            print("Enter 'search' to search the dictionary")
            print("Enter 'exit' to exit the program")
            user_choice = input("Enter your choice: ")
            if user_choice.lower() == "add":
                print("\nWord added to the dictionary")
                #Run function to add word
                break
            elif user_choice.lower() == "search":
                print("\nWord searched in the dictionary")
                #Run function to search word
            elif user_choice.lower() == "exit":
                print("\nProgram exited")
                #Exit program
                break
            else:
                count -= 1
                print("\nInvalid input, Please try again, tries left: {}".format(count))
                if count == 0:
                    print("\nToo many invalid inputs. Terminating program")
                    break

if __name__ == '__main__':
    myCLI()