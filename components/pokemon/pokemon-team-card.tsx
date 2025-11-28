"use client"

interface Team {
  id: number
  name: string
  pokemonCount: number
}

interface PokemonTeamCardProps {
  team: Team
}

export default function PokemonTeamCard({ team }: PokemonTeamCardProps) {
  return (
    <div className="bg-[var(--color-surface-light)] rounded-lg border border-[var(--color-border)] p-4 hover:border-[var(--color-accent)] transition-colors">
      <h3 className="text-lg font-bold mb-2">{team.name}</h3>

      <div className="grid grid-cols-3 gap-2 mb-4">
        {Array.from({ length: 6 }).map((_, i) => (
          <div
            key={i}
            className="aspect-square bg-[var(--color-background)] rounded-lg border border-[var(--color-border)] flex items-center justify-center"
          >
            {i < team.pokemonCount ? (
              <span className="text-3xl">✓</span>
            ) : (
              <span className="text-[var(--color-text-secondary)]">-</span>
            )}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <button className="btn-secondary flex-1">Editar</button>
        <button className="btn-secondary flex-1">Eliminar</button>
      </div>
    </div>
  )
}
a