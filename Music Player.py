import pygame
import os


def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def main():
    print("Welcome to the Python Music Player!")
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Unpause Music")
    print("4. Stop Music")
    print("5. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            file = input("Enter the path of the music file: ")
            if os.path.exists(file):
                play_music(file)
            else:
                print("File not found!")
        elif choice == '2':
            pause_music()
        elif choice == '3':
            unpause_music()
        elif choice == '4':
            stop_music()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
