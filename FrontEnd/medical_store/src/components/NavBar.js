const handleClick = () => {
    console.log("Clicked");
};

const NavBar = (Props) => {
    const {logo, Link1, Link2, Link3, Link4, Button} = Props;
    
  return (
    <div>
        <nav className="navbar navbar-expand-md navbar-light fixed-top bg-secondary">
        <div className="container-fluid">
            <a className="navbar-brand" href="/">
                <h1><img src = {logo} alt="" width="50"/>Elixir</h1>
            </a>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item h5">
                <a className="nav-link mt-2" href="/">{Link1}</a>
              </li>
              <li className="nav-item h5">
                <a className="nav-link mt-2" href="/">{Link2}</a>
              </li>
              <li className="nav-item h5">
                <a className="nav-link mt-2" href="/">{Link3}</a>
              </li>
              <li className="nav-item h5">
                <a className="nav-link mt-2" href='/'>{Link4}</a>
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
