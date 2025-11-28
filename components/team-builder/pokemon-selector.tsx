"use client"

export default function PokemonSelector() {
  return (
    <div className="bg-[var(--color-surface-light)] rounded-lg p-4">
      <h4 className="font-bold mb-3">Seleccionar Pokemon</h4>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
        {Array.from({ length: 8 }).map((_, i) => (
          <button
            key={i}
            className="bg-[var(--color-background)] border border-[var(--color-border)] rounded-lg p-3 hover:bg-[var(--color-surface)] hover:border-[var(--color-accent)] transition-colors text-center"
          >
            <div className="text-2xl mb-1">✓</div>
            <p className="text-sm">Pokemon {i + 1}</p>
          </button>
        ))}
      </div>
    </div>
  )
}
