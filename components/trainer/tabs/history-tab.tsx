"use client"

export default function HistoryTab() {
  const mockHistory = [
    { id: 1, event: "Batallas ganadas", value: 127 },
    { id: 2, event: "Pokémon capturados", value: 245 },
    { id: 3, event: "Entrenadores derrotados", value: 42 },
  ]

  return (
    <div className="space-y-4">
      {mockHistory.map((item) => (
        <div
          key={item.id}
          className="bg-[var(--color-surface-light)] px-4 py-3 rounded-lg border border-[var(--color-border)] flex justify-between items-center"
        >
          <p className="font-medium">{item.event}</p>
          <p className="text-[var(--color-primary)] font-bold text-lg">{item.value}</p>
        </div>
      ))}
    </div>
  )
}
