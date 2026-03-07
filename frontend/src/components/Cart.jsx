import React,{useEffect,useState} from "react"
import API from "../api"

export default function Cart(){

const [items,setItems]=useState([])

useEffect(()=>{

API.get("/cart").then(res=>setItems(res.data))

},[])

return(

<div>

<h2>Your Cart</h2>

{items.map(i=>(
<div>{i.name}</div>
))}

</div>

)

}
