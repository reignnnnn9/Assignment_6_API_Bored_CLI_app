import requests
import json

def show_menu():
    """Display the main menu"""
    print("\nBored Activity Finder")
    print("=" * 21)
    print("1. Get a random activity")
    print("2. Get activity by type")
    print("3. Get activity by participants")
    print("4. Exit")

def main():
    """Main function with menu loop"""
    print("Welcome to the Bored Activity Finder!")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nChoose an option (1-4): ")
            
            if choice == '1':
                get_random_activity()
            elif choice == '2':
                get_activity_by_type()
            elif choice == '3':
                get_activity_by_participants()
            elif choice == '4':
                print("Thanks for using Bored Activity Finder!")
                break
            else:
                print("Invalid choice! Please choose 1-4.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
    
def get_random_activity():
    url = "https://bored-api.appbrewery.com/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("\nRandom Activity Suggestion:")
        print(f"Activity: {data['activity']}")
        print(f"Type: {data['type']}")
        print(f"Participants: {data['participants']}")
        print("Ready to try it?")
    else:
        return None
    
    """
    Get a completely random activity suggestion
    API: https://bored-api.appbrewery.com/random
    """
    # YOUR CODE HERE
    # 1. Make a GET request to the API
    # 2. Parse the JSON response  
    # 3. Print the activity and type nicely
    # 4. Handle any errors

def get_activity_by_type():
    print("""Search by activity type:
          education
          recreational
          social
          diy
          charity
          cooking
          relaxation
          music
          busywork""")
    search_type = input("Please enter what type to search by: ")
    param = {
        "type": search_type,
        "_limit": 1
    }
    url = "https://bored-api.appbrewery.com/filter?"
    response = requests.get(url, params=param)
    if response.status_code == 200:
        result = response.json()
        print("\nActivity Suggestion by type:")
        print(f"Activity: {result[0]['activity']}")
        print(f"Type: {result[2]['type']}")
        print(f"Participants: {result[3]['participants']}")
    else:
        print("Please enter valid activity type.")
    """
    Let user choose an activity type and get a suggestion
    API: https://bored-api.appbrewery.com/filter?type={type}
    Types: education, recreational, social, diy, charity, cooking, relaxation, music, busywork
    """
    # YOUR CODE HERE - requires query parameters
    # 1. Show the user available types
    # 2. Get their choice
    # 3. Make API request with type parameter
    # 4. Display the result
    pass

def get_activity_by_participants():
    print("Search by number of participants:")
    search_num = int(input("Please choose between 1-6 or 8 participants to search by: "))
    param = {
        "participants": search_num,
        "_limit": 1
    }
    url = "https://bored-api.appbrewery.com/filter?"
    response = requests.get(url, params=param)
    if search_num >= 1 and search_num <= 6 or search_num == 8:
        result = response.json()
        print("\nActivity Suggestion by # of participants:")
        print(f"Activity: {result[0]['activity']}")
        print(f"Type: {result[2]['type']}")
        print(f"Participants: {result[3]['participants']}")
    else:
        print("Please enter valid #, 1-6 or 8.")
    """
    Get activity suggestions based on number of participants
    
    API: https://bored-api.appbrewery.com/filter?participants={number}
    """
    # YOUR CODE HERE - requires query parameters
    # 1. Ask user how many participants
    # 2. Make API request with participants parameter
    # 3. Display the activity suggestion
    pass

if __name__ == "__main__":
    main()