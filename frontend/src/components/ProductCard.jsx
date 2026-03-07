import React from "react"
import API from "../api"

export default function ProductCard({product}){

const addToCart = async () => {

await API.post("/cart",product)

}

return(

<div className="product">

<img src={product.image} />

<h3>{product.name}</h3>

<p>${product.price}</p>

<button onClick={addToCart}>
Add to Cart
</button>

</div>

)

}
