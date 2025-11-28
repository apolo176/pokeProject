"use client"

interface Pokemon {
  id: number
  name: string
  type: string[]
  image: string
}

interface PokemonCardProps {
  pokemon: Pokemon
}

export default function PokemonCard({ pokemon }: PokemonCardProps) {
  const getTypeColor = (type: string) => {
    const typeColors: Record<string, string> = {
      Fire: "bg-[var(--color-type-fire)]",
      Water: "bg-[var(--color-type-water)]",
      Grass: "bg-[var(--color-type-grass)]",
      Electric: "bg-[var(--color-type-electric)]",
      Ice: "bg-[var(--color-type-ice)]",
      Fighting: "bg-[var(--color-type-fighting)]",
      Poison: "bg-[var(--color-type-poison)]",
      Ground: "bg-[var(--color-type-ground)]",
      Flying: "bg-[var(--color-type-flying)]",
      Psychic: "bg-[var(--color-type-psychic)]",
      Bug: "bg-[var(--color-type-bug)]",
      Rock: "bg-[var(--color-type-rock)]",
      Ghost: "bg-[var(--color-type-ghost)]",
      Dragon: "bg-[var(--color-type-dragon)]",
      Dark: "bg-[var(--color-type-dark)]",
      Steel: "bg-[var(--color-type-steel)]",
      Fairy: "bg-[var(--color-type-fairy)]",
    }
    return typeColors[type] || "bg-gray-500"
  }

  return (
    <div className="card hover:border-[var(--color-accent)] transition-all hover:shadow-lg hover:shadow-[var(--color-accent)]/20 cursor-pointer">
      <img
        src={pokemon.image || "/placeholder.svg"}
        alt={pokemon.name}
        className="w-full h-48 object-cover rounded-lg mb-3"
      />
      <h3 className="text-lg font-bold mb-2">{pokemon.name}</h3>
      <div className="flex gap-2 flex-wrap">
        {pokemon.type.map((type) => (
          <span key={type} className={`badge-type ${getTypeColor(type)}`}>
            {type}
          </span>
        ))}
      </div>
    </div>
  )
}
