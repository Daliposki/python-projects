import subprocess


games = {
    "1": "Fortnite",
    "2": "Counter-Strike 2",
    "3": "Minecraft",
    "4": "The Forest"
}


def optimize_game(game_name):
    """
    Optimize the computer's performance for the specified game.
    This can involve tasks like closing background processes,
    setting high-performance mode, etc.
    """
    print(f"Optimizing performance for {game_name}...")

    # Example: Close non-essential processes using subprocess
    subprocess.run("taskkill /f /im chrome.exe", shell=True)
    subprocess.run("taskkill /f /im spotify.exe", shell=True)

    print("Performance optimized successfully!")


def main():
    print("Welcome to Game Booster!")

    print("Select a game to optimize:")
    for key, value in games.items():
        print(f"{key}. {value}")

    selected_game = input("Enter the number of the game: ")
    selected_game_name = games.get(selected_game)

    if selected_game_name:
        optimize_game(selected_game_name)
    else:
        print("Invalid game selection. Please try again.")


if __name__ == "__main__":
    main()
