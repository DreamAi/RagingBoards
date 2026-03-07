import React,{useEffect,useState} from "react"
import API from "../api"

export default function ClientDashboard(){

const [orders,setOrders]=useState([])

useEffect(()=>{

API.get("/orders").then(res=>setOrders(res.data))

},[])

return(

<div>

<h2>Your Orders</h2>

{orders.map(o=>(
<div>{o.product}</div>
))}

</div>

)

}
