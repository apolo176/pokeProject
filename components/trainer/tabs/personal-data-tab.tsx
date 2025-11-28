"use client"

export default function PersonalDataTab() {
  return (
    <div className="space-y-4">
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm text-[var(--color-text-secondary)] mb-2">Nombre de Entrenador</label>
          <div className="bg-[var(--color-surface-light)] px-4 py-2 rounded-lg border border-[var(--color-border)]">
            Trainer Name
          </div>
        </div>
        <div>
          <label className="block text-sm text-[var(--color-text-secondary)] mb-2">Nivel</label>
          <div className="bg-[var(--color-surface-light)] px-4 py-2 rounded-lg border border-[var(--color-border)]">
            42
          </div>
        </div>
      </div>

      <div>
        <label className="block text-sm text-[var(--color-text-secondary)] mb-2">Biografía</label>
        <textarea
          className="input-field h-24"
          placeholder="Cuéntanos sobre ti..."
          defaultValue="Trainer description goes here"
        />
      </div>

      <div className="flex gap-3">
        <button className="btn-primary">Guardar Cambios</button>
        <button className="btn-secondary">Cancelar</button>
      </div>
    </div>
  )
}
