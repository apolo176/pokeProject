import type React from "react"
import type { Metadata } from "next"
import { Geist, Geist_Mono } from "next/font/google"
import { Analytics } from "@vercel/analytics/next"
import "./globals.css"

const _geist = Geist({ subsets: ["latin"] })
const _geistMono = Geist_Mono({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Pokemon Trainer Hub",
  description: "Build your ultimate Pokemon team and explore the Pokedex",
  generator: "v0.app",
  icons: {
    icon: [
      {
        url: "/icon-light-32x32.png",
        media: "(prefers-color-scheme: light)",
      },
      {
        url: "/icon-dark-32x32.png",
        media: "(prefers-color-scheme: dark)",
      },
      {
        url: "/icon.svg",
        type: "image/svg+xml",
      },
    ],
    apple: "/apple-icon.png",
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`font-sans antialiased`}>
        <nav className="sticky top-0 z-50 bg-card border-b border-border">
          <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
            <div className="text-2xl font-bold text-primary">PokeHub</div>
            <div className="flex gap-6 text-sm md:text-base">
              <a href="/" className="hover:text-accent transition-colors">
                Dashboard
              </a>
              <a href="/pokedex" className="hover:text-accent transition-colors">
                Pokedex
              </a>
              <a href="/teams" className="hover:text-accent transition-colors">
                Teams
              </a>
              <a href="/admin" className="hover:text-accent transition-colors">
                Admin
              </a>
            </div>
          </div>
        </nav>
        <main className="min-h-screen bg-background">{children}</main>
        <Analytics />
      </body>
    </html>
  )
}
