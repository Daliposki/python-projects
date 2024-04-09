import matplotlib.pyplot as plt

# Sample data for followers
usernames = ['User1', 'User2', 'User3', 'User4', 'User5']
max_followers = 100000  # Maximum number of followers
followers = [0] * len(usernames)  # Initialize with zero followers for each user

# Function to plot follower count and blue cubes
def plot_data():
    plt.figure(figsize=(10, 6))
    plt.bar(usernames, followers, color='skyblue')
    plt.xlabel('Usernames')
    plt.ylabel('Number of Followers')
    plt.title('Follower Count')
    plt.xticks(rotation=45, ha='right')

    # Plot blue cubes
    for i, follower_count in enumerate(followers):
        plt.plot([i], [follower_count], marker='o', markersize=10, color="blue", label='User' + str(i+1))

    plt.tight_layout()
    plt.show()

# Main function to run the dashboard
def main():
    print("Welcome to the Social Media Follower Count Dashboard!")
    while True:
        print("\nMenu:")
        print("1. Enter Followers for Each User")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            for i, username in enumerate(usernames):
                followers[i] = int(input(f"Enter the number of followers for {username}: "))
            plot_data()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 2.")

if __name__ == "__main__":
    main()
  
