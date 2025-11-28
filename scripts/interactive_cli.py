from pokedex_manager import PokedexManager
from database_queries import DatabaseQueries
from pokeapi_loader import PokeAPILoader
import os

class PokemonCLI:
    """Interactive CLI for Pokemon Management System"""
    
    def __init__(self):
        self.pokedex = PokedexManager()
        self.db = DatabaseQueries()
        self.loader = PokeAPILoader()
        self.current_trainer = None
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def main_menu(self):
        """Main menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(" "*10 + "POKEMON MANAGEMENT SYSTEM")
            print("="*60)
            print("\n1. PokeAPI Data Management")
            print("2. Search & Browse Pokedex")
            print("3. Trainer Management")
            print("4. Database Statistics")
            print("5. Exit")
            print("\n" + "="*60)
            
            choice = input("\nSelect option (1-5): ").strip()
            
            if choice == "1":
                self.api_menu()
            elif choice == "2":
                self.pokedex_menu()
            elif choice == "3":
                self.trainer_menu()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                print("\nThanks for using Pokemon Management System!")
                self.cleanup()
                break
            else:
                input("Invalid choice! Press Enter to continue...")
    
    def api_menu(self):
        """PokeAPI data management menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(" "*15 + "PokeAPI DATA LOADER")
            print("="*60)
            print("\n1. Load Pokemon Range")
            print("2. Load Single Pokemon")
            print("3. Back to Main Menu")
            print("\n" + "="*60)
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == "1":
                self.load_pokemon_range()
            elif choice == "2":
                self.load_single_pokemon()
            elif choice == "3":
                break
            else:
                input("Invalid choice! Press Enter to continue...")
    
    def load_pokemon_range(self):
        """Load a range of Pokemon"""
        self.clear_screen()
        print("\n" + "="*60)
        print("LOAD POKEMON RANGE")
        print("="*60)
        print("Note: PokeAPI has Pokemon IDs from 1 to 1025+")
        
        try:
            start = int(input("\nEnter starting Pokemon ID: "))
            end = int(input("Enter ending Pokemon ID: "))
            
            if start < 1 or start > end:
                print("Invalid range!")
                input("Press Enter to continue...")
                return
            
            print(f"\nLoading Pokemon {start} to {end}...")
            self.loader.load_pokemon_range(start, end)
            print(f"\nSuccessfully loaded {end - start + 1} Pokemon!")
            input("Press Enter to continue...")
            
        except ValueError:
            print("Please enter valid numbers!")
            input("Press Enter to continue...")
    
    def load_single_pokemon(self):
        """Load a single Pokemon by ID"""
        self.clear_screen()
        try:
            pokemon_id = int(input("Enter Pokemon ID: "))
            print(f"\nLoading Pokemon {pokemon_id}...")
            self.loader.load_pokemon_species(pokemon_id)
            print("Pokemon loaded successfully!")
            input("Press Enter to continue...")
        except ValueError:
            print("Please enter a valid ID!")
            input("Press Enter to continue...")
    
    def pokedex_menu(self):
        """Pokedex search and browse menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(" "*15 + "POKEDEX BROWSER")
            print("="*60)
            print(f"Total Pokemon in Pokedex: {self.pokedex.get_pokemon_count()}")
            print("\n1. Search by Name")
            print("2. Browse by Type")
            print("3. Browse by Generation")
            print("4. View Legendary Pokemon")
            print("5. View Mythical Pokemon")
            print("6. View Baby Pokemon")
            print("7. View All Types")
            print("8. Back to Main Menu")
            print("\n" + "="*60)
            
            choice = input("\nSelect option (1-8): ").strip()
            
            if choice == "1":
                self.search_by_name()
            elif choice == "2":
                self.browse_by_type()
            elif choice == "3":
                self.browse_by_generation()
            elif choice == "4":
                self.view_legendary()
            elif choice == "5":
                self.view_mythical()
            elif choice == "6":
                self.view_baby()
            elif choice == "7":
                self.view_all_types()
            elif choice == "8":
                break
            else:
                input("Invalid choice! Press Enter to continue...")
    
    def search_by_name(self):
        """Search Pokemon by name"""
        self.clear_screen()
        nombre = input("Enter Pokemon name (or partial): ").strip().lower()
        
        results = self.pokedex.search_by_name(nombre)
        
        if results:
            self.display_pokemon_list(results)
        else:
            print("No Pokemon found!")
        
        input("Press Enter to continue...")
    
    def browse_by_type(self):
        """Browse Pokemon by type"""
        self.clear_screen()
        print("Available Types:")
        types = self.pokedex.get_all_types()
        for idx, type_tuple in enumerate(types, 1):
            print(f"{idx}. {type_tuple[0]}")
        
        try:
            choice = int(input("\nSelect type number: "))
            if 1 <= choice <= len(types):
                tipo = types[choice - 1][0]
                results = self.pokedex.search_by_type(tipo)
                self.display_pokemon_list(results, f"Pokemon of type: {tipo}")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")
        
        input("Press Enter to continue...")
    
    def browse_by_generation(self):
        """Browse Pokemon by generation"""
        self.clear_screen()
        generaciones = self.pokedex.get_all_generations()
        
        print("Available Generations:")
        for idx, gen_tuple in enumerate(generaciones, 1):
            print(f"{idx}. {gen_tuple[0]}")
        
        try:
            choice = int(input("\nSelect generation number: "))
            if 1 <= choice <= len(generaciones):
                gen = generaciones[choice - 1][0]
                results = self.pokedex.search_by_generation(gen)
                self.display_pokemon_list(results, f"Pokemon from: {gen}")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")
        
        input("Press Enter to continue...")
    
    def view_legendary(self):
        """View legendary Pokemon"""
        self.clear_screen()
        results = self.pokedex.get_legendary_pokemon()
        self.display_pokemon_list(results, "Legendary Pokemon")
        input("Press Enter to continue...")
    
    def view_mythical(self):
        """View mythical Pokemon"""
        self.clear_screen()
        results = self.pokedex.get_mythical_pokemon()
        self.display_pokemon_list(results, "Mythical Pokemon")
        input("Press Enter to continue...")
    
    def view_baby(self):
        """View baby Pokemon"""
        self.clear_screen()
        results = self.pokedex.get_baby_pokemon()
        self.display_pokemon_list(results, "Baby Pokemon")
        input("Press Enter to continue...")
    
    def view_all_types(self):
        """View all available types"""
        self.clear_screen()
        print("Available Pokemon Types:")
        print("="*60)
        types = self.pokedex.get_all_types()
        for idx, type_tuple in enumerate(types, 1):
            print(f"{idx:2}. {type_tuple[0]}")
        input("\nPress Enter to continue...")
    
    def display_pokemon_list(self, pokemon_list, title="Pokemon List"):
        """Display a list of Pokemon"""
        self.clear_screen()
        print("\n" + "="*60)
        print(f" {title:^58} ")
        print("="*60)
        
        for idx, poke in enumerate(pokemon_list[:20], 1):
            print(f"{idx:2}. {poke.nombre:20} | Type: {poke.tipo:10} | Gen: {poke.generacion}")
        
        if len(pokemon_list) > 20:
            print(f"\n... and {len(pokemon_list) - 20} more Pokemon")
        
        if pokemon_list:
            try:
                choice = int(input("\nEnter Pokemon number to view details (0 to skip): "))
                if 1 <= choice <= len(pokemon_list):
                    self.display_pokemon_details(pokemon_list[choice - 1])
            except ValueError:
                pass
    
    def display_pokemon_details(self, pokemon):
        """Display detailed Pokemon information"""
        self.clear_screen()
        print(self.pokedex.display_pokemon_info(pokemon))
        input("Press Enter to continue...")
    
    def trainer_menu(self):
        """Trainer management menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(" "*15 + "TRAINER MANAGEMENT")
            print("="*60)
            print("\n1. Create New Trainer")
            print("2. View Trainer Info")
            print("3. Manage Teams")
            print("4. Back to Main Menu")
            print("\n" + "="*60)
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == "1":
                self.create_trainer()
            elif choice == "2":
                self.view_trainer()
            elif choice == "3":
                self.manage_teams()
            elif choice == "4":
                break
            else:
                input("Invalid choice! Press Enter to continue...")
    
    def create_trainer(self):
        """Create a new trainer"""
        self.clear_screen()
        print("\n" + "="*60)
        print("CREATE NEW TRAINER")
        print("="*60)
        
        nombre_usuario = input("\nEnter username: ").strip()
        nombre = input("Enter trainer name: ").strip()
        ciudad = input("Enter city: ").strip()
        
        trainer = self.db.create_trainer(nombre_usuario, nombre, ciudad)
        print(f"\nTrainer '{nombre}' created successfully!")
        self.current_trainer = trainer
        input("Press Enter to continue...")
    
    def view_trainer(self):
        """View trainer information"""
        self.clear_screen()
        nombre_usuario = input("Enter trainer username: ").strip()
        trainer = self.db.get_trainer(nombre_usuario)
        
        if trainer:
            self.clear_screen()
            print("\n" + "="*60)
            print(f" TRAINER: {trainer.nombre}")
            print("="*60)
            print(f"Username: {trainer.nombre_usuario}")
            print(f"City: {trainer.ciudad}")
            print(f"Admin: {trainer.es_admin}")
            print(f"Approved: {trainer.es_aprobado}")
            
            teams = self.db.get_trainer_teams(trainer.id)
            print(f"\nTeams ({len(teams)}):")
            for team in teams:
                print(f"  - {team.nombre}: {len(team.lista_pokemon)}/6 Pokemon")
        else:
            print("Trainer not found!")
        
        input("Press Enter to continue...")
    
    def manage_teams(self):
        """Manage trainer teams"""
        if not self.current_trainer:
            nombre_usuario = input("Enter trainer username: ").strip()
            self.current_trainer = self.db.get_trainer(nombre_usuario)
        
        if self.current_trainer:
            self.clear_screen()
            teams = self.db.get_trainer_teams(self.current_trainer.id)
            
            print(f"\nTeams for {self.current_trainer.nombre}:")
            for idx, team in enumerate(teams, 1):
                print(f"{idx}. {team.nombre}")
            
            choice = input("\nEnter team number to manage (0 to create new): ")
            
            if choice == "0":
                team_name = input("Enter new team name: ")
                team = self.db.create_team(team_name, self.current_trainer.id)
                print(f"Team '{team_name}' created!")
        
        input("Press Enter to continue...")
    
    def show_statistics(self):
        """Show database statistics"""
        self.clear_screen()
        print("\n" + "="*60)
        print(" "*18 + "DATABASE STATISTICS")
        print("="*60)
        
        stats = self.db.get_stats()
        
        print(f"\nTotal Pokemon Species in Pokedex: {stats['total_pokemon_species']}")
        print(f"Total Pokemon Instances:          {stats['total_pokemon']}")
        print(f"Total Trainers:                   {stats['total_trainers']}")
        print(f"Total Teams:                      {stats['total_teams']}")
        
        print("\n" + "="*60)
        input("Press Enter to continue...")
    
    def cleanup(self):
        """Clean up resources"""
        self.pokedex.close()
        self.db.close()

def main():
    """Launch the Pokemon Management System"""
    cli = PokemonCLI()
    cli.main_menu()

if __name__ == "__main__":
    main()
