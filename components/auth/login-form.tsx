"use client"

import type React from "react"

import { useState } from "react"

interface LoginFormProps {
  onLoginSuccess: () => void
}

export default function LoginForm({ onLoginSuccess }: LoginFormProps) {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [isSignUp, setIsSignUp] = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // TODO: Connect to backend API
    onLoginSuccess()
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[var(--color-background)] to-[var(--color-surface)]">
      <div className="w-full max-w-md">
        <div className="card">
          <h1 className="text-3xl font-bold text-center mb-8 text-[var(--color-primary)]">
            {isSignUp ? "Crear Cuenta" : "Iniciar Sesión"}
          </h1>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">Usuario</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="input-field"
                placeholder="Nombre de usuario"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">Contraseña</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input-field"
                placeholder="Contraseña"
                required
              />
            </div>

            {isSignUp && (
              <div>
                <label className="block text-sm font-medium mb-2">Confirmar Contraseña</label>
                <input type="password" className="input-field" placeholder="Confirmar contraseña" required />
              </div>
            )}

            <button type="submit" className="btn-primary w-full">
              {isSignUp ? "Registrarse" : "Iniciar Sesión"}
            </button>
          </form>

          <button
            onClick={() => setIsSignUp(!isSignUp)}
            className="w-full mt-4 text-[var(--color-accent)] hover:text-[var(--color-accent-dark)] transition-colors"
          >
            {isSignUp ? "¿Ya tienes cuenta? Inicia sesión" : "¿No tienes cuenta? Regístrate"}
          </button>
        </div>
      </div>
    </div>
  )
}
