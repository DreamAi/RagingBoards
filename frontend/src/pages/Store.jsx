import React from "react"
import ProductCard from "../components/ProductCard"

const products=[

{
name:"Custom Surfboard Design",
price:99,
image:"/board.png"
},

{
name:"Pro Surfboard Graphic Pack",
price:59,
image:"/graphic.png"
}

]

export default function Store(){

return(

<div>

<h1>Raging Boards Store</h1>

{products.map(p=>(
<ProductCard product={p}/>
))}

</div>

)

}
