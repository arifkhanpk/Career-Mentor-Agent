def show_header():
    print("-------------🎓 Career Mentor Agent-------------------")
    print("Helping you navigate your professional journey\n")

def display_menu(options, title):
    print(f"{title}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return int(input("Enter your choice: ")) - 1

def show_career_details(career):
    print(f"\n🚀 Career: {career.name}")
    print(f"📝 Description: {career.description}")
    print(f"📈 Growth Outlook: {career.growth}")
    print(f"💰 Salary: {career.salary}")