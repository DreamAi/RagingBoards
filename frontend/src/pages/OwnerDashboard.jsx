import React,{useEffect,useState} from "react"
import API from "../api"

export default function OwnerDashboard(){

const [stats,setStats]=useState({})

useEffect(()=>{

API.get("/dashboard/revenue")
.then(res=>setStats(res.data))

},[])

return(

<div>

<h1>Owner Dashboard</h1>

<p>Total Orders: {stats.total_orders}</p>

<p>Total Revenue: ${stats.revenue}</p>

</div>

)

}
