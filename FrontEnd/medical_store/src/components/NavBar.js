import React from 'react'
import { Link , useNavigate } from "react-router-dom";

const NavBar = (Props) => {
    const navigate = useNavigate();
    const {logo, Link1, Link2, Link3, Link4, Button} = Props;
    
  return (
    <div>
        <nav className="navbar navbar-expand-md navbar-light fixed-top bg-secondary">
        <div className="container-fluid">
            <Link className="navbar-brand" to={Link1}>
                <h1><img src = {logo} alt="" width="50"/>Elixir</h1>
            </Link>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to={Link1}>Home</Link>
              </li>
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to={Link2}>Consult Doctor</Link>
              </li>
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to={Link3}>COVID-19</Link>
              </li>
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to={Link4}>About</Link>
              </li>
            </ul>
            <button className="btn btn-outline-warning" type="submit" onClick={() => navigate('/SignIn')}>{Button}</button>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default NavBar
