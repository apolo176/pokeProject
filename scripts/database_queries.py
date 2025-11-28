from database import get_database_engine, get_session, Pokemon, PokemonEspecie, Entrenador, Equipo, Ataque, Habilidad

class DatabaseQueries:
    """Query helper class for Pokemon database"""
    
    def __init__(self, db_path='pokemon.db'):
        self.engine = get_database_engine(db_path)
        self.session = get_session(self.engine)
    
    def get_pokemon_by_name(self, nombre):
        """Get Pokemon species by name"""
        return self.session.query(PokemonEspecie).filter_by(nombre=nombre).first()
    
    def get_pokemon_by_type(self, tipo):
        """Get all Pokemon of a specific type"""
        return self.session.query(PokemonEspecie).filter_by(tipo=tipo).all()
    
    def get_all_pokemon_species(self, limit=None):
        """Get all Pokemon species"""
        query = self.session.query(PokemonEspecie)
        if limit:
            query = query.limit(limit)
        return query.all()
    
    def get_pokemon_by_generation(self, generation):
        """Get all Pokemon from a specific generation"""
        return self.session.query(PokemonEspecie).filter_by(generacion=generation).all()
    
    def get_trainer(self, nombre_usuario):
        """Get trainer by username"""
        return self.session.query(Entrenador).filter_by(nombre_usuario=nombre_usuario).first()
    
    def create_trainer(self, nombre_usuario, nombre, ciudad=""):
        """Create a new trainer"""
        trainer = Entrenador(
            nombre_usuario=nombre_usuario,
            nombre=nombre,
            ciudad=ciudad,
            es_aprobado=True
        )
        self.session.add(trainer)
        self.session.commit()
        return trainer
    
    def get_trainer_teams(self, trainer_id):
        """Get all teams for a trainer"""
        return self.session.query(Equipo).filter_by(entrenador_id=trainer_id).all()
    
    def create_team(self, nombre, entrenador_id):
        """Create a new team for a trainer"""
        team = Equipo(
            nombre=nombre,
            entrenador_id=entrenador_id,
            lista_pokemon=[]
        )
        self.session.add(team)
        self.session.commit()
        return team
    
    def add_pokemon_to_team(self, team_id, pokemon_especie_nombre):
        """Add a Pokemon to a team"""
        team = self.session.query(Equipo).filter_by(id=team_id).first()
        if team:
            if len(team.lista_pokemon) < 6:
                team.lista_pokemon.append(pokemon_especie_nombre)
                self.session.commit()
                return True
        return False
    
    def get_stats(self):
        """Get database statistics"""
        total_pokemon_species = self.session.query(PokemonEspecie).count()
        total_pokemon = self.session.query(Pokemon).count()
        total_trainers = self.session.query(Entrenador).count()
        total_teams = self.session.query(Equipo).count()
        
        return {
            'total_pokemon_species': total_pokemon_species,
            'total_pokemon': total_pokemon,
            'total_trainers': total_trainers,
            'total_teams': total_teams
        }
    
    def close(self):
        """Close database session"""
        self.session.close()
