import React, { useState } from "react";

export default function SurfboardStudio(){

const [color,setColor] = useState("#ffffff");

return (

<div>

<h2>Raging Boards Design Studio</h2>

<input
type="color"
value={color}
onChange={(e)=>setColor(e.target.value)}
/>

<div style={{
width:"300px",
height:"120px",
background:color,
borderRadius:"50px"
}}/>

</div>

)
}
