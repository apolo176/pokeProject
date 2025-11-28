"use client"

import PokemonTeamCard from "@/components/pokemon/pokemon-team-card"

export default function TeamsTab() {
  const mockTeams = [
    { id: 1, name: "Fire Squad", pokemonCount: 6 },
    { id: 2, name: "Water Dragons", pokemonCount: 4 },
  ]

  return (
    <div className="space-y-4">
      <button className="btn-primary">+ Crear Nuevo Equipo</button>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {mockTeams.map((team) => (
          <PokemonTeamCard key={team.id} team={team} />
        ))}
      </div>
    </div>
  )
}
