"""
PokeAPI Integration using Pokebase
Fetches Pokemon data and populates the domain models
"""

import pokebase as pb
from typing import Optional, List, Dict
from models import (
    PokemonEspecie, Ataque, Habilidad, Pokedex, 
    GestorPokedex, Pokemon
)

class PokeAPIIntegration:
    """Integrates with PokeAPI via pokebase"""
    
    def __init__(self):
        self.cache: Dict = {}
    
    def obtenerPokemonEspecie(self, nombre: str) -> Optional[PokemonEspecie]:
        """Fetch Pokemon species from PokeAPI"""
        try:
            # Get Pokemon from PokeAPI
            pokemon_api = pb.pokemon.get(nombre.lower())
            
            # Extract types
            tipos = [t.type.name for t in pokemon_api.types]
            
            # Extract abilities
            habilidades = []
            for ability_slot in pokemon_api.abilities:
                habilidad = Habilidad(
                    nombre=ability_slot.ability.name,
                    descripcion=f"Ability: {ability_slot.ability.name}"
                )
                habilidades.append(habilidad)
            
            # Extract moves
            ataques = []
            for move_slot in pokemon_api.moves[:10]:  # Limit to first 10 moves
                move = pb.move.get(move_slot.move.name)
                ataque = Ataque(
                    nombre=move.name,
                    descripcion=move.effect_entries[0].effect if move.effect_entries else "No description",
                    tipo=move.type.name if move.type else "unknown",
                    potencia=move.power,
                    precision=move.accuracy,
                    pp=move.pp
                )
                ataques.append(ataque)
            
            # Create species object
            especie = PokemonEspecie(
                orden=pokemon_api.id,
                nombre=pokemon_api.name,
                tipo=tipos,
                rangoGenero=50.0,  # Default value
                peso=pokemon_api.weight / 10.0,  # Convert to kg
                altura=pokemon_api.height / 10.0,  # Convert to m
                listaHabilidades=habilidades,
                listaAtaques=ataques,
                imagen=pokemon_api.sprites.front_default,
                fotos=[pokemon_api.sprites.front_default, pokemon_api.sprites.back_default]
            )
            
            return especie
        except Exception as e:
            print(f"Error fetching Pokemon {nombre}: {e}")
            return None
    
    def obtenerMultiplesPokemon(self, nombres: List[str]) -> List[PokemonEspecie]:
        """Fetch multiple Pokemon species"""
        especies = []
        for nombre in nombres:
            especie = self.obtenerPokemonEspecie(nombre)
            if especie:
                especies.append(especie)
        return especies
    
    def obtenerPokemonPorTipo(self, tipo: str) -> List[PokemonEspecie]:
        """Fetch Pokemon by type"""
        try:
            tipo_obj = pb.type_.get(tipo.lower())
            especies = []
            
            # Get Pokemon of this type (limit to first 20)
            for pokemon_ref in tipo_obj.pokemon[:20]:
                pokemon_data = pb.pokemon.get(pokemon_ref.pokemon.name)
                especie = self._convertir_pokemon_api_a_especie(pokemon_data)
                if especie:
                    especies.append(especie)
            
            return especies
        except Exception as e:
            print(f"Error fetching Pokemon of type {tipo}: {e}")
            return []
    
    def obtenerGeneracion(self, numero_generacion: int) -> List[PokemonEspecie]:
        """Fetch all Pokemon from a generation"""
        try:
            generation = pb.generation.get(numero_generacion)
            especies = []
            
            for species_ref in generation.pokemon_species[:20]:  # Limit for demo
                pokemon_data = pb.pokemon.get(species_ref.name)
                especie = self._convertir_pokemon_api_a_especie(pokemon_data)
                if especie:
                    especies.append(especie)
            
            return especies
        except Exception as e:
            print(f"Error fetching generation {numero_generacion}: {e}")
            return []
    
    def _convertir_pokemon_api_a_especie(self, pokemon_api) -> Optional[PokemonEspecie]:
        """Convert PokeAPI Pokemon to domain model"""
        try:
            tipos = [t.type.name for t in pokemon_api.types]
            
            habilidades = []
            for ability_slot in pokemon_api.abilities:
                habilidad = Habilidad(
                    nombre=ability_slot.ability.name,
                    descripcion=f"Ability: {ability_slot.ability.name}"
                )
                habilidades.append(habilidad)
            
            ataques = []
            for move_slot in pokemon_api.moves[:10]:
                try:
                    move = pb.move.get(move_slot.move.name)
                    ataque = Ataque(
                        nombre=move.name,
                        descripcion=move.effect_entries[0].effect if move.effect_entries else "No description",
                        tipo=move.type.name if move.type else "unknown",
                        potencia=move.power,
                        precision=move.accuracy,
                        pp=move.pp
                    )
                    ataques.append(ataque)
                except:
                    pass
            
            especie = PokemonEspecie(
                orden=pokemon_api.id,
                nombre=pokemon_api.name,
                tipo=tipos,
                rangoGenero=50.0,
                peso=pokemon_api.weight / 10.0,
                altura=pokemon_api.height / 10.0,
                listaHabilidades=habilidades,
                listaAtaques=ataques,
                imagen=pokemon_api.sprites.front_default,
                fotos=[pokemon_api.sprites.front_default, pokemon_api.sprites.back_default]
            )
            
            return especie
        except Exception as e:
            print(f"Error converting Pokemon: {e}")
            return None
    
    def crearPokedex(self, nombre: str, pokemon_nombres: List[str]) -> Pokedex:
        """Create a Pokedex with Pokemon species"""
        pokedex = Pokedex(nombre=nombre)
        
        for pokemon_nombre in pokemon_nombres:
            especie = self.obtenerPokemonEspecie(pokemon_nombre)
            if especie:
                pokedex.listaPokemonEspecie.append(especie)
        
        return pokedex
