from pokeapi_loader import PokeAPILoader
from database_queries import DatabaseQueries
from datetime import datetime

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("   POKEMON MANAGEMENT SYSTEM - DATABASE VERSION")
    print("="*50)
    print("1. Load Pokemon from PokeAPI to Database")
    print("2. Search Pokemon by Name")
    print("3. Browse Pokemon by Type")
    print("4. Manage Trainers")
    print("5. View Database Statistics")
    print("6. Exit")
    print("="*50)

def load_pokemon_menu(loader):
    """Menu for loading Pokemon"""
    print("\n--- Load Pokemon from PokeAPI ---")
    try:
        start = int(input("Enter starting Pokemon ID (1-1025): "))
        end = int(input("Enter ending Pokemon ID: "))
        
        if start < 1 or end > 1025 or start > end:
            print("Invalid range!")
            return
        
        loader.load_pokemon_range(start, end)
        print("Pokemon loaded successfully!")
    except ValueError:
        print("Please enter valid numbers!")

def search_pokemon_menu(db):
    """Menu for searching Pokemon"""
    print("\n--- Search Pokemon ---")
    nombre = input("Enter Pokemon name: ").lower()
    pokemon = db.get_pokemon_by_name(nombre)
    
    if pokemon:
        print(f"\nPokemon Found: {pokemon.nombre}")
        print(f"Type: {pokemon.tipo}")
        print(f"Generation: {pokemon.generacion}")
        print(f"Legendary: {pokemon.es_legendario}")
        print(f"Stats: {pokemon.atributos}")
    else:
        print("Pokemon not found in database!")

def browse_by_type_menu(db):
    """Menu for browsing Pokemon by type"""
    print("\n--- Browse Pokemon by Type ---")
    tipo = input("Enter Pokemon type (e.g., fire, water, grass): ").lower()
    pokemon_list = db.get_pokemon_by_type(tipo)
    
    if pokemon_list:
        print(f"\nFound {len(pokemon_list)} Pokemon of type '{tipo}':")
        for i, poke in enumerate(pokemon_list[:10], 1):
            print(f"{i}. {poke.nombre}")
        if len(pokemon_list) > 10:
            print(f"... and {len(pokemon_list) - 10} more")
    else:
        print(f"No Pokemon found with type '{tipo}'!")

def trainer_menu(db):
    """Menu for trainer management"""
    print("\n--- Trainer Management ---")
    print("1. Create New Trainer")
    print("2. View Trainer Info")
    print("3. Manage Teams")
    
    choice = input("Choose option (1-3): ")
    
    if choice == "1":
        nombre_usuario = input("Enter username: ")
        nombre = input("Enter trainer name: ")
        ciudad = input("Enter city: ")
        trainer = db.create_trainer(nombre_usuario, nombre, ciudad)
        print(f"Trainer '{nombre}' created successfully!")
    
    elif choice == "2":
        nombre_usuario = input("Enter username: ")
        trainer = db.get_trainer(nombre_usuario)
        if trainer:
            print(f"\nTrainer: {trainer.nombre}")
            print(f"Username: {trainer.nombre_usuario}")
            print(f"City: {trainer.ciudad}")
        else:
            print("Trainer not found!")
    
    elif choice == "3":
        nombre_usuario = input("Enter username: ")
        trainer = db.get_trainer(nombre_usuario)
        if trainer:
            teams = db.get_trainer_teams(trainer.id)
            print(f"\nTeams for {trainer.nombre}:")
            for i, team in enumerate(teams, 1):
                print(f"{i}. {team.nombre} ({len(team.lista_pokemon)}/6 Pokemon)")
        else:
            print("Trainer not found!")

def show_statistics(db):
    """Show database statistics"""
    stats = db.get_stats()
    print("\n--- Database Statistics ---")
    print(f"Total Pokemon Species: {stats['total_pokemon_species']}")
    print(f"Total Pokemon Instances: {stats['total_pokemon']}")
    print(f"Total Trainers: {stats['total_trainers']}")
    print(f"Total Teams: {stats['total_teams']}")

def main():
    """Main application loop"""
    loader = PokeAPILoader()
    db = DatabaseQueries()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            load_pokemon_menu(loader)
        elif choice == "2":
            search_pokemon_menu(db)
        elif choice == "3":
            browse_by_type_menu(db)
        elif choice == "4":
            trainer_menu(db)
        elif choice == "5":
            show_statistics(db)
        elif choice == "6":
            print("Exiting application...")
            db.close()
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
