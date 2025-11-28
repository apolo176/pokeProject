"use client"

import { useState } from "react"
import PersonalDataTab from "./tabs/personal-data-tab"
import TeamsTab from "./tabs/teams-tab"
import FriendsTab from "./tabs/friends-tab"
import HistoryTab from "./tabs/history-tab"

export default function TrainerProfile() {
  const [activeTab, setActiveTab] = useState("profile")

  const tabs = [
    { id: "profile", label: "Perfil", icon: "👤" },
    { id: "teams", label: "Equipos", icon: "⚽" },
    { id: "friends", label: "Amigos", icon: "👥" },
    { id: "history", label: "Historial", icon: "📜" },
  ]

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-4xl font-bold">Mi Perfil de Entrenador</h1>
        <button className="btn-primary">Editar Perfil</button>
      </div>

      <div className="card">
        <div className="flex gap-4 mb-6 pb-4 border-b border-[var(--color-border)]">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-4 py-2 rounded-lg font-semibold transition-colors ${
                activeTab === tab.id
                  ? "bg-[var(--color-primary)] text-white"
                  : "bg-[var(--color-surface-light)] text-[var(--color-text-secondary)] hover:text-[var(--color-text)]"
              }`}
            >
              {tab.icon} {tab.label}
            </button>
          ))}
        </div>

        {activeTab === "profile" && <PersonalDataTab />}
        {activeTab === "teams" && <TeamsTab />}
        {activeTab === "friends" && <FriendsTab />}
        {activeTab === "history" && <HistoryTab />}
      </div>
    </div>
  )
}
