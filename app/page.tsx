"use client"

import { useState } from "react"
import TrainerProfile from "@/components/trainer/trainer-profile"
import LoginForm from "@/components/auth/login-form"

export default function Home() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  if (!isLoggedIn) {
    return <LoginForm onLoginSuccess={() => setIsLoggedIn(true)} />
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <TrainerProfile />
    </div>
  )
}
