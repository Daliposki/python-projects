import random
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 10

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        time.sleep(1)


class Enemy:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.hp -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage.")
        time.sleep(1)


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    enemy = Enemy("Goblin", 50, 5)

    print("A wild Goblin appears!")
    while player.hp > 0 and enemy.hp > 0:
        print("\n" + "="*20)
        print(f"{player.name}: HP {player.hp}")
        print(f"{enemy.name}: HP {enemy.hp}")
        print("="*20)

        action = input("What will you do? [attack/run]: ").lower()

        if action == "attack":
            player.attack(enemy)
            if enemy.hp <= 0:
                print(f"{enemy.name} has been defeated!")
                break
            enemy.attack(player)
            if player.hp <= 0:
                print("You have been defeated!")
                break
        elif action == "run":
            print("You ran away!")
            break
        else:
            print("Invalid action. Try again.")


if __name__ == "__main__":
    main()
    
