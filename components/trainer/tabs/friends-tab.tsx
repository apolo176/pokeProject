"use client"

export default function FriendsTab() {
  const mockFriends = [
    { id: 1, name: "Friend 1", level: 35 },
    { id: 2, name: "Friend 2", level: 42 },
    { id: 3, name: "Friend 3", level: 38 },
  ]

  return (
    <div className="space-y-4">
      <div className="flex gap-3">
        <input type="text" placeholder="Buscar amigos..." className="input-field flex-1" />
        <button className="btn-primary">Agregar</button>
      </div>

      <div className="space-y-2">
        {mockFriends.map((friend) => (
          <div
            key={friend.id}
            className="bg-[var(--color-surface-light)] px-4 py-3 rounded-lg border border-[var(--color-border)] flex justify-between items-center"
          >
            <div>
              <p className="font-semibold">{friend.name}</p>
              <p className="text-sm text-[var(--color-text-secondary)]">Nivel {friend.level}</p>
            </div>
            <button className="text-[var(--color-accent)]">Ver Perfil</button>
          </div>
        ))}
      </div>
    </div>
  )
}
