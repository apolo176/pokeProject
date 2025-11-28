import pokebase as pb
from database import (
    get_database_engine, create_tables, get_session,
    Pokemon, PokemonEspecie, Ataque, Habilidad, Pokedex
)
import json

class PokeAPILoader:
    """Load Pokemon data from PokeAPI and store in database"""
    
    def __init__(self, db_path='pokemon.db'):
        self.engine = get_database_engine(db_path)
        create_tables(self.engine)
        self.session = get_session(self.engine)
        self.loaded_pokemon = set()
    
    def load_pokemon_species(self, pokemon_id, limit=10):
        """Load Pokemon species data from PokeAPI and store in database"""
        try:
            pokemon_data = pb.pokemon(pokemon_id)
            
            if pokemon_data.id in self.loaded_pokemon:
                print(f"Pokemon {pokemon_data.name} already in database, skipping...")
                return
            
            # Extract species information
            species_name = pokemon_data.species.name
            pokemon_type = pokemon_data.types[0].type.name if pokemon_data.types else "normal"
            altura = pokemon_data.height
            peso = pokemon_data.weight
            
            # Get species details
            try:
                species = pb.pokemon_species(pokemon_data.species.name)
                es_legendario = species.is_legendary
                es_mitico = species.is_mythical
                es_bebe = species.is_baby
                generacion = species.generation.name if species.generation else "unknown"
                habitat = species.habitat.name if species.habitat else "unknown"
            except:
                es_legendario = False
                es_mitico = False
                es_bebe = False
                generacion = "unknown"
                habitat = "unknown"
            
            # Check if species exists in database
            especie_db = self.session.query(PokemonEspecie).filter_by(nombre=species_name).first()
            if not especie_db:
                especie_db = PokemonEspecie(
                    nombre=species_name,
                    tipo=pokemon_type,
                    es_legendario=es_legendario,
                    es_mitico=es_mitico,
                    es_bebe=es_bebe,
                    generacion=generacion,
                    habitat=habitat,
                    imagen=pokemon_data.sprites.front_default or "",
                    atributos=self._extract_stats(pokemon_data),
                    rango_genero=0.5
                )
                self.session.add(especie_db)
                self.session.commit()
            
            # Create Pokemon instance
            pokemon_db = Pokemon(
                id_pokemon=pokemon_data.id,
                altura=altura,
                peso=peso,
                especie=species_name,
                color=pokemon_type,
                atributos=self._extract_stats(pokemon_data),
                lista_habilidades=self._extract_abilities(pokemon_data),
                lista_ataques=self._extract_moves(pokemon_data)
            )
            
            # Add attacks
            for move_data in pokemon_data.moves[:5]:  # Limit to 5 moves
                move_name = move_data.move.name
                ataque = self.session.query(Ataque).filter_by(nombre=move_name).first()
                if not ataque:
                    try:
                        move_details = pb.move(move_name)
                        ataque = Ataque(
                            nombre=move_name,
                            descripcion=move_details.effect_entries[0].effect if move_details.effect_entries else "",
                            potencia=move_details.power or 0,
                            precision=move_details.accuracy or 100,
                            pp=move_details.pp or 0,
                            tipo=move_details.type.name
                        )
                        self.session.add(ataque)
                    except:
                        continue
                if ataque:
                    pokemon_db.ataques.append(ataque)
            
            # Add abilities
            for ability_data in pokemon_data.abilities:
                ability_name = ability_data.ability.name
                habilidad = self.session.query(Habilidad).filter_by(nombre=ability_name).first()
                if not habilidad:
                    try:
                        ability_details = pb.ability(ability_name)
                        habilidad = Habilidad(
                            nombre=ability_name,
                            descripcion=ability_details.effect_entries[0].effect if ability_details.effect_entries else "",
                            efecto=ability_details.effect
                        )
                        self.session.add(habilidad)
                    except:
                        continue
                if habilidad:
                    pokemon_db.habilidades.append(habilidad)
            
            self.session.add(pokemon_db)
            self.session.commit()
            self.loaded_pokemon.add(pokemon_data.id)
            
            print(f"Loaded Pokemon: {pokemon_data.name} (ID: {pokemon_data.id})")
            
        except Exception as e:
            print(f"Error loading Pokemon {pokemon_id}: {str(e)}")
            self.session.rollback()
    
    def load_pokemon_range(self, start=1, end=10):
        """Load a range of Pokemon into the database"""
        print(f"Loading Pokemon {start} to {end} into database...")
        for pokemon_id in range(start, end + 1):
            self.load_pokemon_species(pokemon_id)
        self.session.close()
        print(f"Successfully loaded {len(self.loaded_pokemon)} Pokemon!")
    
    def _extract_stats(self, pokemon_data):
        """Extract stats from Pokemon data"""
        return {stat.stat.name: stat.base_stat for stat in pokemon_data.stats}
    
    def _extract_abilities(self, pokemon_data):
        """Extract abilities from Pokemon data"""
        return [ability.ability.name for ability in pokemon_data.abilities]
    
    def _extract_moves(self, pokemon_data):
        """Extract moves from Pokemon data"""
        return [move.move.name for move in pokemon_data.moves[:10]]
