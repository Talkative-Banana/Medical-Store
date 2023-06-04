import { Link } from "react-router-dom";

const handleClick = () => {
    console.log("Clicked");
};

const NavBar = (Props) => {
    const {logo, Link1, Link2, Link3, Link4, Button} = Props;
    
  return (
    <div>
        <nav className="navbar navbar-expand-md navbar-light fixed-top bg-secondary">
        <div className="container-fluid">
            <Link className="navbar-brand" to="/">
                <h1><img src = {logo} alt="" width="50"/>Elixir</h1>
            </Link>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to="/">{Link1}</Link>
              </li>
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to="/">{Link2}</Link>
              </li>
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to="/">{Link3}</Link>
              </li>
              <li className="nav-item h5">
                <Link className="nav-link mt-2" to='/about'>{Link4}</Link>
              </li>
            </ul>
            <button className="btn btn-outline-warning" type="submit" onClick={handleClick}>{Button}</button>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default NavBar
