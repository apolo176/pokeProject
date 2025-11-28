"use client"

import { useState } from "react"
import PokemonSelector from "./pokemon-selector"

export default function TeamBuilder() {
  const [teamName, setTeamName] = useState("")
  const [team, setTeam] = useState<number[]>([])

  return (
    <div className="space-y-6">
      <h1 className="text-4xl font-bold">Construir Equipo</h1>

      <div className="card space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Nombre del Equipo</label>
          <input
            type="text"
            value={teamName}
            onChange={(e) => setTeamName(e.target.value)}
            placeholder="Mi Equipo Épico"
            className="input-field"
          />
        </div>

        <div>
          <h3 className="text-lg font-bold mb-4">Mi Equipo (máximo 6 Pokemon)</h3>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mb-6">
            {Array.from({ length: 6 }).map((_, i) => (
              <div
                key={i}
                className="aspect-square bg-[var(--color-surface-light)] rounded-lg border-2 border-dashed border-[var(--color-border)] flex items-center justify-center hover:border-[var(--color-accent)] transition-colors cursor-pointer"
              >
                {team[i] ? (
                  <div className="text-center">
                    <div className="text-3xl mb-2">✓</div>
                    <p className="text-sm">Pokemon {team[i]}</p>
                  </div>
                ) : (
                  <span className="text-[var(--color-text-secondary)]">Slot {i + 1}</span>
                )}
              </div>
            ))}
          </div>
        </div>

        <PokemonSelector />

        <div className="flex gap-3">
          <button className="btn-primary">Guardar Equipo</button>
          <button className="btn-secondary">Cancelar</button>
        </div>
      </div>
    </div>
  )
}
