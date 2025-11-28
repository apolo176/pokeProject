from database import get_database_engine, get_session, PokemonEspecie, Pokemon, Ataque, Habilidad
from sqlalchemy import or_, and_

class PokedexManager:
    """Advanced Pokedex system with search and filtering"""
    
    def __init__(self, db_path='pokemon.db'):
        self.engine = get_database_engine(db_path)
        self.session = get_session(self.engine)
    
    def search_by_name(self, nombre):
        """Search Pokemon by name (partial match)"""
        return self.session.query(PokemonEspecie).filter(
            PokemonEspecie.nombre.ilike(f"%{nombre}%")
        ).all()
    
    def search_by_type(self, tipo):
        """Get all Pokemon of a specific type"""
        return self.session.query(PokemonEspecie).filter_by(tipo=tipo.lower()).all()
    
    def search_by_generation(self, generacion):
        """Get Pokemon from a specific generation"""
        return self.session.query(PokemonEspecie).filter_by(generacion=generacion).all()
    
    def get_legendary_pokemon(self):
        """Get all legendary Pokemon"""
        return self.session.query(PokemonEspecie).filter_by(es_legendario=True).all()
    
    def get_mythical_pokemon(self):
        """Get all mythical Pokemon"""
        return self.session.query(PokemonEspecie).filter_by(es_mitico=True).all()
    
    def get_baby_pokemon(self):
        """Get all baby Pokemon"""
        return self.session.query(PokemonEspecie).filter_by(es_bebe=True).all()
    
    def get_all_types(self):
        """Get list of all unique types in database"""
        return self.session.query(PokemonEspecie.tipo).distinct().all()
    
    def get_all_generations(self):
        """Get list of all unique generations in database"""
        return self.session.query(PokemonEspecie.generacion).distinct().all()
    
    def get_pokemon_count(self):
        """Get total count of Pokemon in Pokedex"""
        return self.session.query(PokemonEspecie).count()
    
    def get_pokemon_by_stat(self, stat_name, min_value=0, max_value=255):
        """Search Pokemon by stat range"""
        results = []
        all_pokemon = self.session.query(Pokemon).all()
        
        for poke in all_pokemon:
            if poke.atributos and stat_name in poke.atributos:
                stat_value = poke.atributos[stat_name]
                if min_value <= stat_value <= max_value:
                    results.append(poke)
        
        return results
    
    def get_pokemon_by_ability(self, ability_name):
        """Get all Pokemon with a specific ability"""
        return self.session.query(Pokemon).join(
            Pokemon.habilidades
        ).filter(Habilidad.nombre.ilike(f"%{ability_name}%")).all()
    
    def display_pokemon_info(self, pokemon_especie):
        """Display detailed Pokemon information"""
        info = f"""
╔═══════════════════════════════════════╗
║         {pokemon_especie.nombre.upper():^35} ║
╚═══════════════════════════════════════╝

Type:           {pokemon_especie.tipo}
Generation:     {pokemon_especie.generacion}
Habitat:        {pokemon_especie.habitat}
Gender Ratio:   {pokemon_especie.rango_genero * 100}% (estimated)

Status:
  - Legendary:  {pokemon_especie.es_legendario}
  - Mythical:   {pokemon_especie.es_mitico}
  - Baby:       {pokemon_especie.es_bebe}

Attributes:     {pokemon_especie.atributos}
Weaknesses:     {pokemon_especie.debil_contra}
Strong Against: {pokemon_especie.fuerte_contra}
"""
        return info
    
    def close(self):
        """Close database session"""
        self.session.close()
