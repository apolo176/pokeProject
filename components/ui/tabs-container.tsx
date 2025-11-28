"use client"

interface Tab {
  id: string
  label: string
  icon?: string
}

interface TabContainerProps {
  tabs: Tab[]
  activeTab: string
  onTabChange: (tabId: string) => void
}

export default function TabContainer({ tabs, activeTab, onTabChange }: TabContainerProps) {
  return (
    <div className="flex gap-4 mb-6 pb-4 border-b border-[var(--color-border)]">
      {tabs.map((tab) => (
        <button
          key={tab.id}
          onClick={() => onTabChange(tab.id)}
          className={`px-4 py-2 rounded-lg font-semibold transition-colors ${
            activeTab === tab.id
              ? "bg-[var(--color-primary)] text-white"
              : "bg-[var(--color-surface-light)] text-[var(--color-text-secondary)] hover:text-[var(--color-text)]"
          }`}
        >
          {tab.icon && `${tab.icon} `}
          {tab.label}
        </button>
      ))}
    </div>
  )
}
