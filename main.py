from player import Player
from rewards import reward_action

if __name__ == "__main__":
    # Crear un nuevo jugador
    player1 = Player("Alice", 1234)
    
    # Simular acciones
    reward_action(player1, "message")
    reward_action(player1, "invite")
    reward_action(player1, "challenge")

    # Mostrar el estado del jugador
    print(player1)