def display_colleges(college_data):
    """Display the list of colleges."""
    print("\nAvailable Colleges:")
    for idx, college in enumerate(college_data.keys(), start=1):
        print(f"{idx}. {college}")


def display_courses(college_data, selected_college):
    """Display the list of courses for a specific college."""
    print(f"\nCourses offered by {selected_college}:")
    for idx, course in enumerate(college_data[selected_college], start=1):
        print(f"{idx}. {course}")


def main():
    # Data: Colleges and their courses
    college_data = {
        "Harvard University": ["Computer Science", "Law", "Medicine", "Business Administration"],
        "Stanford University": ["Engineering", "Data Science", "Psychology", "Economics"],
        "MIT": ["Artificial Intelligence", "Robotics", "Physics", "Mathematics"],
        "University of Cambridge": ["Philosophy", "Architecture", "History", "Linguistics"],
    }

    print("Welcome to the College and Courses Finder!")

    while True:
        # Display the list of colleges
        display_colleges(college_data)

        # Ask the user to select a college
        try:
            college_choice = int(input("\nEnter the number of the college you want to explore (0 to exit): "))
            if college_choice == 0:
                print("Thank you for using the College and Courses Finder. Goodbye!")
                break
            elif 1 <= college_choice <= len(college_data):
                selected_college = list(college_data.keys())[college_choice - 1]
                display_courses(college_data, selected_college)
            else:
                print("Invalid choice. Please select a valid college number.")
        except ValueError:
            print("Please enter a valid number.")

        # Ask the user if they want to continue
        continue_choice = input("\nDo you want to explore another college? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Thank you for using the College and Courses Finder. Goodbye!")
            break


if __name__ == "__main__":
    main()
