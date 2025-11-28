"use client"

import { useState } from "react"

export default function AdminDashboard() {
  const [activeTab, setActiveTab] = useState("moderation")

  return (
    <div className="space-y-6">
      <h1 className="text-4xl font-bold">Panel de Administración</h1>

      <div className="card">
        <div className="flex gap-4 mb-6 pb-4 border-b border-[var(--color-border)]">
          <button
            onClick={() => setActiveTab("moderation")}
            className={`px-4 py-2 rounded-lg font-semibold transition-colors ${
              activeTab === "moderation"
                ? "bg-[var(--color-primary)] text-white"
                : "bg-[var(--color-surface-light)] text-[var(--color-text-secondary)]"
            }`}
          >
            Moderación
          </button>
          <button
            onClick={() => setActiveTab("users")}
            className={`px-4 py-2 rounded-lg font-semibold transition-colors ${
              activeTab === "users"
                ? "bg-[var(--color-primary)] text-white"
                : "bg-[var(--color-surface-light)] text-[var(--color-text-secondary)]"
            }`}
          >
            Usuarios
          </button>
          <button
            onClick={() => setActiveTab("chatbot")}
            className={`px-4 py-2 rounded-lg font-semibold transition-colors ${
              activeTab === "chatbot"
                ? "bg-[var(--color-primary)] text-white"
                : "bg-[var(--color-surface-light)] text-[var(--color-text-secondary)]"
            }`}
          >
            Chatbot
          </button>
        </div>

        {activeTab === "moderation" && (
          <div className="space-y-4">
            <h3 className="text-xl font-bold">Reportes de Usuarios</h3>
            <div className="space-y-2">
              {[1, 2, 3].map((i) => (
                <div
                  key={i}
                  className="bg-[var(--color-surface-light)] p-4 rounded-lg border border-[var(--color-border)] flex justify-between items-center"
                >
                  <div>
                    <p className="font-semibold">Reporte #{i}</p>
                    <p className="text-sm text-[var(--color-text-secondary)]">
                      Usuario reportado por conducta inapropiada
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <button className="btn-secondary text-sm">Revisar</button>
                    <button className="text-[var(--color-error)] hover:text-red-400">Eliminar</button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === "users" && (
          <div className="space-y-4">
            <h3 className="text-xl font-bold">Gestión de Usuarios</h3>
            <input type="text" placeholder="Buscar usuario..." className="input-field mb-4" />
            <div className="space-y-2">
              {[1, 2, 3, 4].map((i) => (
                <div
                  key={i}
                  className="bg-[var(--color-surface-light)] p-4 rounded-lg border border-[var(--color-border)] flex justify-between items-center"
                >
                  <div>
                    <p className="font-semibold">Trainer {i}</p>
                    <p className="text-sm text-[var(--color-text-secondary)]">Nivel {30 + i}</p>
                  </div>
                  <button className="btn-secondary text-sm">Editar</button>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === "chatbot" && (
          <div className="space-y-4">
            <h3 className="text-xl font-bold">Interfaz de Chatbot</h3>
            <div className="bg-[var(--color-surface-light)] rounded-lg p-4 h-96 border border-[var(--color-border)] flex flex-col">
              <div className="flex-1 overflow-y-auto mb-4">
                <div className="space-y-2">
                  <div className="bg-[var(--color-primary)] text-white p-3 rounded-lg w-3/4">Opción 1</div>
                  <div className="bg-[var(--color-primary)] text-white p-3 rounded-lg w-3/4">Opción 2</div>
                  <div className="bg-[var(--color-accent)] text-white p-3 rounded-lg w-3/4 ml-auto">Respuesta</div>
                </div>
              </div>
              <div className="flex gap-2">
                <input type="text" placeholder="Escribir opción..." className="input-field flex-1" />
                <button className="btn-primary">Enviar</button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
