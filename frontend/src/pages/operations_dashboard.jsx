import React,{useEffect,useState} from "react"
import axios from "axios"

export default function Dashboard(){

const [data,setData]=useState({})

useEffect(()=>{

axios.get("/operations")
.then(res=>setData(res.data))

},[])

return(

<div>

<h1>Raging Boards Operations Center</h1>

<h2>Revenue</h2>
<p>{data.revenue?.total_revenue}</p>

<h2>AI Agents</h2>
<p>{data.ai?.count}</p>

<h2>System Status</h2>
<p>{data.system?.status}</p>

<h2>Marketing Campaigns</h2>
<p>{data.marketing?.campaign_count}</p>

<h2>Marketplace Orders</h2>
<p>{data.marketplace?.orders_today}</p>

</div>

)

}
