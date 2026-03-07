import React,{useState} from "react"

export default function SurfAI(){

const [spot,setSpot] = useState("")
const [result,setResult] = useState(null)

async function generate(){

const res = await fetch(`/surf-ai?spot=${spot}`)

const data = await res.json()

setResult(data)

}

return(

<div>

<h2>AI Surfboard Generator</h2>

<input
placeholder="Surf Spot"
onChange={(e)=>setSpot(e.target.value)}
/>

<button onClick={generate}>
Generate Board
</button>

{result && (

<div>

<h3>Recommended Board</h3>

<p>Type: {result.recommended_board.type}</p>
<p>Length: {result.recommended_board.length}</p>
<p>Fin Setup: {result.recommended_board.fin_setup}</p>

</div>

)}

</div>

)

}
