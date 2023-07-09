import React from 'react';
import { Link , useNavigate } from "react-router-dom";

function Card(Props) {
  const {Image, Name, Price, Link1} = Props;
  return (
    <div class = "card-prod">
      <div>
        <Link className="navbar-brand" to={Link1}>
          <img src = {Image} alt ="" width = "150"></img>
        </Link>
      </div>
      <div> {Name} </div>
      <div> {Price}</div>
      <div><button className="btn btn-info"><div className='btn_text'>Add to Cart</div></button></div>
    </div>
  )
}

export default Card
