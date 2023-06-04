import React from 'react'

const handleClick = (emailId, password) => {
    console.log("Clicked");
};

function About(Props) {
    const {logo} = Props;
  return (
    <div className='flexbox-container_about'>
        <div><img src = {logo} alt="" width="815" height="815"/></div>
    <div className='right_container_about'>
        <h3>Login in to Elixir</h3>
        <form>
            <div className="mb-3">
                <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div className="mb-3">
                <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                <input type="password" className="form-control" id="exampleInputPassword1" />
            </div>
            <div className="mb-3 form-check">
                <input type="checkbox" className="form-check-input" id="exampleCheck1" />
                <label className="form-check-label" htmlFor="exampleCheck1">Check me out</label>
            </div>
            <button type="submit" className="btn btn-primary"  onClick={() => handleClick()}>Submit</button>
        </form>
    </div>
    </div>
  )
}

export default About
