"""
Pokemon Domain Models
Following the class diagram specification for the Pokemon Management System
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import json

# Attack/Habilidad Models
@dataclass
class Ataque:
    """Represents an Attack/Move"""
    nombre: str
    descripcion: str
    tipo: str
    potencia: Optional[int] = None
    precision: Optional[int] = None
    pp: Optional[int] = None
    
    def metodo(self, tipo: str) -> str:
        return f"Executing {self.nombre} of type {tipo}"

@dataclass
class Habilidad:
    """Represents an Ability"""
    nombre: str
    descripcion: str
    
    def metodo(self, tipo: str) -> str:
        return f"Using ability {self.nombre}"

# Pokemon Especie Model
@dataclass
class PokemonEspecie:
    """Represents a Pokemon Species"""
    orden: int
    nombre: str
    tipo: List[str]
    rangoGenero: float
    peso: float
    altura: float
    listaHabilidades: List[Habilidad] = field(default_factory=list)
    listaAtaques: List[Ataque] = field(default_factory=list)
    esBebes: bool = False
    esLegendario: bool = False
    esMitico: bool = False
    generacion: int = 1
    habitat: str = ""
    imagen: str = ""
    fotos: List[str] = field(default_factory=list)
    cadaEvolutiva: List['PokemonEspecie'] = field(default_factory=list)
    
    def getNombre(self) -> str:
        return self.nombre
    
    def eresTuIdPoke(self) -> bool:
        return True
    
    def crearPokemonNombPoke(self, nombre: str, idEq: int) -> 'Pokemon':
        """Create a Pokemon instance from this species"""
        return Pokemon(
            idPokemon=idEq,
            altura=self.altura,
            atributos={"tipo": self.tipo},
            nombre=nombre,
            peso=self.peso,
            listaHabilidades=self.listaHabilidades.copy(),
            listaAtraques=self.listaAtaques.copy()
        )

# Pokemon Model
@dataclass
class Pokemon:
    """Represents an individual Pokemon instance"""
    idPokemon: int
    nombre: str
    altura: float = 0.0
    color: str = ""
    atributos: Dict = field(default_factory=dict)
    peso: float = 0.0
    listaHabilidades: List[Habilidad] = field(default_factory=list)
    listaAtraques: List[Ataque] = field(default_factory=list)
    especie: Optional[PokemonEspecie] = None
    experiencia: int = 0
    nivel: int = 1
    stats: Dict = field(default_factory=dict)  # HP, Attack, Defense, etc.
    
    def getNombre(self) -> str:
        return self.nombre
    
    def eresTuIdPoke(self) -> bool:
        return True
    
    def crearPokemonNombPoke(self, nombre: str, idEq: int) -> 'Pokemon':
        return Pokemon(
            idPokemon=idEq,
            altura=self.altura,
            atributos=self.atributos.copy(),
            nombre=nombre,
            peso=self.peso,
            listaHabilidades=self.listaHabilidades.copy(),
            listaAtraques=self.listaAtraques.copy()
        )
    
    def obtenerStatsPokeIdPoke(self, idEq: int) -> Dict:
        return self.stats.copy()
    
    def subirNivel(self):
        """Increase Pokemon level"""
        self.nivel += 1
        self.experiencia += 100

# Team Model
@dataclass
class Equipo:
    """Represents a Pokemon Team"""
    idEquipo: int
    nombre: str
    listaPokemon: List[Pokemon] = field(default_factory=list)
    
    def getEquipo(self) -> 'Equipo':
        return self
    
    def getNombre(self) -> str:
        return self.nombre
    
    def getIdEquipo(self) -> int:
        return self.idEquipo
    
    def anadirPokemon(self, pokemon: Pokemon) -> None:
        """Add Pokemon to team (max 6)"""
        if len(self.listaPokemon) < 6:
            self.listaPokemon.append(pokemon)
    
    def obtenerPokemonOrdenEquipo(self, orden: int) -> Optional[Pokemon]:
        """Get Pokemon at specific order in team"""
        if 0 <= orden < len(self.listaPokemon):
            return self.listaPokemon[orden]
        return None

# Pokedex Model
@dataclass
class Pokedex:
    """Represents a Pokemon Pokedex"""
    nombre: str
    listaPokemonEspecie: List[PokemonEspecie] = field(default_factory=list)
    
    def buscarPokemonNombre(self, nombre: str) -> Optional[PokemonEspecie]:
        """Search for Pokemon by name"""
        for pokemon_esp in self.listaPokemonEspecie:
            if pokemon_esp.nombre.lower() == nombre.lower():
                return pokemon_esp
        return None
    
    def obtenerNombrePokemon(self, nombrePokemon: str) -> Optional[str]:
        """Get Pokemon name"""
        pokemon = self.buscarPokemonNombre(nombrePokemon)
        return pokemon.nombre if pokemon else None
    
    def crearNombrePokemon(self, nombrePokemon: str) -> Optional[Pokemon]:
        """Create Pokemon instance from species"""
        especie = self.buscarPokemonNombre(nombrePokemon)
        if especie:
            return especie.crearPokemonNombPoke(nombrePokemon, len(self.listaPokemonEspecie))
        return None
    
    def obtenerPokemonPorTipos(self, tipos: List[str]) -> List[PokemonEspecie]:
        """Get Pokemon by types"""
        resultado = []
        for pokemon_esp in self.listaPokemonEspecie:
            if any(t in pokemon_esp.tipo for t in tipos):
                resultado.append(pokemon_esp)
        return resultado
    
    def obtenerPokemonPorAtaque(self, ataque: str) -> List[PokemonEspecie]:
        """Get Pokemon that can learn specific move"""
        resultado = []
        for pokemon_esp in self.listaPokemonEspecie:
            if any(a.nombre.lower() == ataque.lower() for a in pokemon_esp.listaAtaques):
                resultado.append(pokemon_esp)
        return resultado

# Trainer Model
@dataclass
class Entrenador:
    """Represents a Pokemon Trainer"""
    esAdmin: bool = False
    esAprobado: bool = False
    correo: str = ""
    nombreUsuario: str = ""
    contrasena: str = ""
    ciudad: str = ""
    nombre: str = ""
    genero: str = ""
    fechaNacimiento: Optional[str] = None
    listaEquipos: List[Equipo] = field(default_factory=list)
    listaEventos: List[str] = field(default_factory=list)
    
    def eresTuNombreUsuario(self, nombre: str) -> bool:
        return self.nombreUsuario.lower() == nombre.lower()
    
    def crearEquipoVacio(self, nombre: str) -> int:
        """Create a new team"""
        nuevo_equipo = Equipo(
            idEquipo=len(self.listaEquipos),
            nombre=nombre
        )
        self.listaEquipos.append(nuevo_equipo)
        return nuevo_equipo.idEquipo
    
    def obtenerEquipo(self, nombreEquipo: str) -> Optional[Equipo]:
        """Get team by name"""
        for equipo in self.listaEquipos:
            if equipo.nombre.lower() == nombreEquipo.lower():
                return equipo
        return None
    
    def buscarEquipo(self, nombreEquipo: str) -> Optional[Equipo]:
        return self.obtenerEquipo(nombreEquipo)
    
    def anadirPokemonEquipo(self, nombreEquipo: str, pokemon: Pokemon) -> bool:
        """Add Pokemon to team"""
        equipo = self.obtenerEquipo(nombreEquipo)
        if equipo:
            equipo.anadirPokemon(pokemon)
            return True
        return False
    
    def borrarEquipoIdEq(self, idEq: int) -> bool:
        """Delete team by ID"""
        self.listaEquipos = [eq for eq in self.listaEquipos if eq.idEquipo != idEq]
        return True
    
    def obtenerTodosPokemonEntidad(self) -> List[Pokemon]:
        """Get all Pokemon across all teams"""
        todos_pokemon = []
        for equipo in self.listaEquipos:
            todos_pokemon.extend(equipo.listaPokemon)
        return todos_pokemon

# Manager Classes
@dataclass
class GestorEntrenadores:
    """Manages all trainers"""
    listaTodosEntrenadores: List[Entrenador] = field(default_factory=list)
    
    def buscarEntrenador(self, nombreUsuario: str) -> Optional[Entrenador]:
        """Search for trainer by username"""
        for entrenador in self.listaTodosEntrenadores:
            if entrenador.eresTuNombreUsuario(nombreUsuario):
                return entrenador
        return None
    
    def obtenerEntrenadorEquipos(self, nombreUsuario: str) -> Optional[List[Equipo]]:
        """Get trainer's equipment"""
        entrenador = self.buscarEntrenador(nombreUsuario)
        return entrenador.listaEquipos if entrenador else None
    
    def getEquipo(self, nombreEquipo: str, equipo: Equipo) -> Equipo:
        return equipo
    
    def anadirNuevoEntrenador(self, poke_pokemon: Pokemon, idEq: int, nombreUsuario: str) :
        """Add new trainer"""
        nuevo_entrenador = Entrenador(nombreUsuario=nombreUsuario)
        self.listaTodosEntrenadores.append(nuevo_entrenador)
    
    def borrarEquipoIdEq(self, idEq: int, nombreUsuario: str) -> bool:
        """Delete equipment by ID"""
        entrenador = self.buscarEntrenador(nombreUsuario)
        if entrenador:
            return entrenador.borrarEquipoIdEq(idEq)
        return False
    
    def buscarMejorPokemon(self, nombreEquipo: str, param: str) -> Optional[Pokemon]:
        """Find best Pokemon by parameter"""
        # Implementation depends on param (level, stats, etc.)
        pass
    
    def obtenerStatsPokeIndividualnombreUsuario(self, nombrePokemon: str, param: str, idEq: int, nombreUsuario: str) -> Dict:
        """Get individual Pokemon stats"""
        entrenador = self.buscarEntrenador(nombreUsuario)
        if entrenador:
            todos_pokemon = entrenador.obtenerTodosPokemonEntidad()
            for pokemon in todos_pokemon:
                if pokemon.nombre.lower() == nombrePokemon.lower():
                    return pokemon.obtenerStatsPokeIdPoke(idEq)
        return {}
    
    def eliminarPokemonnombreUsuario(self, idPoke: int, nombreUsuario: str) -> bool:
        """Remove Pokemon"""
        entrenador = self.buscarEntrenador(nombreUsuario)
        if entrenador:
            todos_pokemon = entrenador.obtenerTodosPokemonEntidad()
            entrenador_pokemon = [p for p in todos_pokemon if p.idPokemon != idPoke]
            return len(entrenador_pokemon) < len(todos_pokemon)
        return False

@dataclass
class GestorPokedex:
    """Manages the Pokedex"""
    listaPodedex: List[Pokedex] = field(default_factory=list)
    
    def buscarPokedex(self, nombre: str) -> Optional[Pokedex]:
        """Search for Pokedex by name"""
        for pokedex in self.listaPodedex:
            if pokedex.nombre.lower() == nombre.lower():
                return pokedex
        return None
    
    def encontrarEspecie(self, nombrePokedex: str, nombrePokemon: str) -> Optional[PokemonEspecie]:
        """Find Pokemon species"""
        pokedex = self.buscarPokedex(nombrePokedex)
        if pokedex:
            return pokedex.buscarPokemonNombre(nombrePokemon)
        return None

# System Model
@dataclass
class SistemaPokemon:
    """Main Pokemon System"""
    gestor_entrenadores: GestorEntrenadores = field(default_factory=GestorEntrenadores)
    gestor_pokedex: GestorPokedex = field(default_factory=GestorPokedex)
    
    def obtenerEquiposEntrenador(self, nombreUsuario: str) -> Optional[List[Equipo]]:
        """Get trainer's teams"""
        return self.gestor_entrenadores.obtenerEntrenadorEquipos(nombreUsuario)
    
    def crearEquipoEntrenador(self, nombreUsuario: str, nombreEquipo: str) -> Optional[int]:
        """Create new team for trainer"""
        entrenador = self.gestor_entrenadores.buscarEntrenador(nombreUsuario)
        if entrenador:
            return entrenador.crearEquipoVacio(nombreEquipo)
        return None
    
    def anadirPokemonEquipo(self, nombreUsuario: str, nombreEquipo: str, pokemon: Pokemon) -> bool:
        """Add Pokemon to team"""
        entrenador = self.gestor_entrenadores.buscarEntrenador(nombreUsuario)
        if entrenador:
            return entrenador.anadirPokemonEquipo(nombreEquipo, pokemon)
        return False
