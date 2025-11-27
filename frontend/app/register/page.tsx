'use client'
import { registerUser } from '@/utils/auth'
import React, { useState } from 'react'

export default function RegisterPage() {
    const [username,setUsername] = useState("")
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")
    
    // handle submit
    const handleSubmit = async (e:any) =>{
        e.preventDefault()
        if (username === "" || password === "" || email===""){
            return
        }
        try{
            await registerUser(email,username,password)
            alert("Yay! It workded! User Created!")
        }
        catch(e){
            alert("Oops!")
        }
    }

  return (
    <div>
        <h1 className='text-2xl font-bold'>Register Page</h1>
        <form className='max-w-md mx-auto' onSubmit={handleSubmit}>
            <div className='mb-3'>
                <label htmlFor="username" className='font-semibold'>Username</label>
                <input type="text"   className='border border-neutral-300 py-3 px-1.5 rounded w-full' value={username} onChange={(e)=>{
                    setUsername(e.target.value)
                }}/>
            </div>
               <div className='mb-3'>
                <label htmlFor="email" className='font-semibold'>Email</label>
                <input type="email"   className='border border-neutral-300 py-3 rounded w-full px-1.5' value={email} onChange={(e)=>{
                    setEmail(e.target.value)
                }}/>
            </div>
              <div className='mb-3'>
                <label htmlFor="password" className='font-semibold'>Password</label>
                <input type="password"   className='border border-neutral-300 py-3 rounded w-full px-1.5' value={password} onChange={(e)=>{
                    setPassword(e.target.value)
                }}/>
            </div>

            <button type="submit" className='py-3 px-1.5 bg-neutral-950 text-white dark:bg-neutral-50 dark:text-neutral-950'>Register</button>

        </form>
    </div>
  )
}
