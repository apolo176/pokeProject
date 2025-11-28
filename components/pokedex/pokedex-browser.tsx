"use client"

import { useState } from "react"
import PokemonCard from "./pokemon-card"

export default function PokedexBrowser() {
  const [searchTerm, setSearchTerm] = useState("")
  const [selectedType, setSelectedType] = useState("")

  const pokemonTypes = [
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy",
  ]

  const mockPokemon = [
    { id: 1, name: "Bulbasaur", type: ["Grass", "Poison"], image: "/bulbasaur.png" },
    { id: 2, name: "Charmander", type: ["Fire"], image: "/charmander.png" },
    { id: 3, name: "Squirtle", type: ["Water"], image: "/playful-squirtle.png" },
    { id: 4, name: "Pikachu", type: ["Electric"], image: "/electric-mouse-character.png" },
  ]

  return (
    <div className="space-y-6">
      <h1 className="text-4xl font-bold">Pokedex</h1>

      <div className="card space-y-4">
        <div className="flex gap-4">
          <input
            type="text"
            placeholder="Buscar Pokemon por nombre..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="input-field flex-1"
          />
          <button className="btn-primary">Buscar</button>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Filtrar por tipo:</label>
          <div className="flex flex-wrap gap-2">
            <button
              onClick={() => setSelectedType("")}
              className={`px-3 py-1 rounded-full text-sm font-semibold transition-colors ${
                selectedType === ""
                  ? "bg-[var(--color-primary)] text-white"
                  : "bg-[var(--color-surface-light)] text-[var(--color-text)] hover:bg-[var(--color-surface)]"
              }`}
            >
              Todos
            </button>
            {pokemonTypes.map((type) => (
              <button
                key={type}
                onClick={() => setSelectedType(type)}
                className={`px-3 py-1 rounded-full text-sm font-semibold transition-colors ${
                  selectedType === type
                    ? "bg-[var(--color-accent)] text-white"
                    : "bg-[var(--color-surface-light)] text-[var(--color-text)] hover:bg-[var(--color-surface)]"
                }`}
              >
                {type}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {mockPokemon.map((pokemon) => (
          <PokemonCard key={pokemon.id} pokemon={pokemon} />
        ))}
      </div>
    </div>
  )
}
