"""
Interactive CLI Application for Pokemon Management System
Demonstrates the full system with PokeAPI integration
"""

from models import (
    Entrenador, Equipo, Pokemon, Pokedex, PokemonEspecie,
    GestorEntrenadores, GestorPokedex, SistemaPokemon
)
from pokeapi_integration import PokeAPIIntegration
from typing import Optional

class PokemonCLI:
    """CLI for Pokemon Management System"""
    
    def __init__(self):
        self.sistema = SistemaPokemon()
        self.api = PokeAPIIntegration()
        self.entrenador_actual: Optional[Entrenador] = None
        self.ejecutar = True
    
    def iniciar(self):
        """Start the application"""
        print("\n" + "="*50)
        print("POKEMON MANAGEMENT SYSTEM")
        print("="*50)
        self.menu_principal()
    
    def menu_principal(self):
        """Main menu"""
        while self.ejecutar:
            print("\n--- MAIN MENU ---")
            print("1. Create Trainer")
            print("2. Login Trainer")
            print("3. Browse Pokedex")
            print("4. Exit")
            
            opcion = input("\nSelect option: ").strip()
            
            if opcion == "1":
                self.crear_entrenador()
            elif opcion == "2":
                self.login_entrenador()
            elif opcion == "3":
                self.explorar_pokedex()
            elif opcion == "4":
                self.ejecutar = False
                print("Goodbye!")
            else:
                print("Invalid option. Try again.")
    
    def crear_entrenador(self):
        """Create a new trainer"""
        print("\n--- CREATE TRAINER ---")
        nombreUsuario = input("Username: ").strip()
        
        # Check if trainer already exists
        if self.sistema.gestor_entrenadores.buscarEntrenador(nombreUsuario):
            print("Trainer already exists!")
            return
        
        nombre = input("Name: ").strip()
        ciudad = input("City: ").strip()
        
        nuevo_entrenador = Entrenador(
            nombreUsuario=nombreUsuario,
            nombre=nombre,
            ciudad=ciudad,
            esAprobado=True
        )
        
        self.sistema.gestor_entrenadores.listaTodosEntrenadores.append(nuevo_entrenador)
        print(f"Trainer {nombreUsuario} created successfully!")
    
    def login_entrenador(self):
        """Login a trainer"""
        print("\n--- LOGIN ---")
        nombreUsuario = input("Username: ").strip()
        
        entrenador = self.sistema.gestor_entrenadores.buscarEntrenador(nombreUsuario)
        if not entrenador:
            print("Trainer not found!")
            return
        
        self.entrenador_actual = entrenador
        self.menu_entrenador()
    
    def menu_entrenador(self):
        """Trainer menu after login"""
        while self.entrenador_actual:
            print(f"\n--- TRAINER MENU ({self.entrenador_actual.nombre}) ---")
            print("1. View Teams")
            print("2. Create Team")
            print("3. Add Pokemon to Team")
            print("4. View Pokedex")
            print("5. Logout")
            
            opcion = input("\nSelect option: ").strip()
            
            if opcion == "1":
                self.ver_equipos()
            elif opcion == "2":
                self.crear_equipo()
            elif opcion == "3":
                self.anadir_pokemon_equipo()
            elif opcion == "4":
                self.explorar_pokedex_trainer()
            elif opcion == "5":
                self.entrenador_actual = None
            else:
                print("Invalid option.")
    
    def ver_equipos(self):
        """View trainer's teams"""
        print(f"\n--- TEAMS ---")
        if not self.entrenador_actual.listaEquipos:
            print("No teams created yet.")
            return
        
        for equipo in self.entrenador_actual.listaEquipos:
            print(f"\nTeam: {equipo.nombre} (ID: {equipo.idEquipo})")
            print(f"  Pokemon: {len(equipo.listaPokemon)}/6")
            for i, pokemon in enumerate(equipo.listaPokemon, 1):
                print(f"    {i}. {pokemon.nombre} (Level {pokemon.nivel})")
    
    def crear_equipo(self):
        """Create a new team"""
        print("\n--- CREATE TEAM ---")
        nombre = input("Team name: ").strip()
        
        id_equipo = self.entrenador_actual.crearEquipoVacio(nombre)
        print(f"Team '{nombre}' created successfully! (ID: {id_equipo})")
    
    def anadir_pokemon_equipo(self):
        """Add Pokemon to team"""
        if not self.entrenador_actual.listaEquipos:
            print("No teams. Create a team first!")
            return
        
        print("\n--- ADD POKEMON TO TEAM ---")
        print("Available teams:")
        for equipo in self.entrenador_actual.listaEquipos:
            print(f"  - {equipo.nombre}")
        
        nombre_equipo = input("Team name: ").strip()
        equipo = self.entrenador_actual.obtenerEquipo(nombre_equipo)
        
        if not equipo:
            print("Team not found!")
            return
        
        if len(equipo.listaPokemon) >= 6:
            print("Team is full! (6/6 Pokemon)")
            return
        
        nombre_pokemon = input("Pokemon name (from PokeAPI): ").strip()
        
        # Fetch from PokeAPI
        print(f"Fetching {nombre_pokemon} from PokeAPI...")
        especie = self.api.obtenerPokemonEspecie(nombre_pokemon)
        
        if not especie:
            print("Pokemon not found!")
            return
        
        # Create Pokemon instance
        pokemon = Pokemon(
            idPokemon=len(equipo.listaPokemon),
            nombre=especie.nombre,
            altura=especie.altura,
            peso=especie.peso,
            atributos={"tipos": especie.tipo},
            listaHabilidades=especie.listaHabilidades,
            listaAtraques=especie.listaAtaques,
            especie=especie,
            nivel=1,
            stats={
                "HP": 45,
                "Attack": 49,
                "Defense": 49,
                "SpA": 65,
                "SpD": 65,
                "Speed": 45
            }
        )
        
        equipo.anadirPokemon(pokemon)
        print(f"{pokemon.nombre} added to team {nombre_equipo}!")
    
    def explorar_pokedex(self):
        """Explore Pokedex without login"""
        print("\n--- POKEDEX ---")
        print("1. Search Pokemon by name")
        print("2. Search Pokemon by type")
        print("3. View Generation")
        
        opcion = input("Select option: ").strip()
        
        if opcion == "1":
            nombre = input("Pokemon name: ").strip()
            especie = self.api.obtenerPokemonEspecie(nombre)
            if especie:
                self.mostrar_pokemon(especie)
            else:
                print("Pokemon not found!")
        
        elif opcion == "2":
            tipo = input("Type (e.g., fire, water, grass): ").strip()
            print(f"Fetching {tipo} type Pokemon...")
            pokemon_list = self.api.obtenerPokemonPorTipo(tipo)
            
            if pokemon_list:
                for pokemon in pokemon_list[:10]:
                    print(f"  - {pokemon.nombre} (Types: {', '.join(pokemon.tipo)})")
            else:
                print("No Pokemon found!")
        
        elif opcion == "3":
            try:
                gen = int(input("Generation number (1-9): ").strip())
                print(f"Fetching Generation {gen}...")
                pokemon_list = self.api.obtenerGeneracion(gen)
                
                if pokemon_list:
                    for pokemon in pokemon_list[:10]:
                        print(f"  - {pokemon.nombre}")
                else:
                    print("No Pokemon found!")
            except ValueError:
                print("Invalid generation number!")
    
    def explorar_pokedex_trainer(self):
        """Explore Pokedex as trainer"""
        print("\n--- TRAINER POKEDEX ---")
        print("1. Search Pokemon by name")
        print("2. Search Pokemon by type")
        
        opcion = input("Select option: ").strip()
        
        if opcion == "1":
            nombre = input("Pokemon name: ").strip()
            especie = self.api.obtenerPokemonEspecie(nombre)
            if especie:
                self.mostrar_pokemon(especie)
            else:
                print("Pokemon not found!")
        
        elif opcion == "2":
            tipo = input("Type: ").strip()
            pokemon_list = self.api.obtenerPokemonPorTipo(tipo)
            
            if pokemon_list:
                for pokemon in pokemon_list[:10]:
                    print(f"  - {pokemon.nombre}")
            else:
                print("No Pokemon found!")
    
    def mostrar_pokemon(self, especie: PokemonEspecie):
        """Display Pokemon details"""
        print(f"\n--- {especie.nombre.upper()} ---")
        print(f"Order: {especie.orden}")
        print(f"Types: {', '.join(especie.tipo)}")
        print(f"Height: {especie.altura}m")
        print(f"Weight: {especie.peso}kg")
        
        print("\nAbilities:")
        for habilidad in especie.listaHabilidades:
            print(f"  - {habilidad.nombre}")
        
        print("\nMoves (first 5):")
        for ataque in especie.listaAtaques[:5]:
            print(f"  - {ataque.nombre} ({ataque.tipo}) - Power: {ataque.potencia}, Accuracy: {ataque.precision}%")
        
        if especie.imagen:
            print(f"Image: {especie.imagen}")

def main():
    """Main entry point"""
    cli = PokemonCLI()
    cli.iniciar()

if __name__ == "__main__":
    main()
