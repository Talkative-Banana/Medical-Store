import React from 'react'
import Axios from 'axios';
import { useForm } from 'react-hook-form';
import { useNavigate } from "react-router-dom";


function SignIn(Props) {
    const {logo} = Props;
    const navigate = useNavigate();
    const form = useForm();
    const { register, handleSubmit } = form;

    const onsubmit = (data) => {
        const {email, password} = data;
        Axios.post('http://localhost:3001/SignIn', {id: email, password: password}).then((result) => {
            console.log(result.data.id);
            if(result.data.id === undefined){
                console.log("Wrong Password!");
            } else if(result.data.id.employee_login_id === Number(email)){
                navigate('/HomePage');
            } else{
                console.log("Id not matching");
            }
        });
    }

  return (
    <div className='flexbox-container_about'>
        <div><img src = {logo} alt="" width="750" height="815"/></div>
    <div className='right_container_about'>
        <h3>Login in to Elixir</h3>
        <form onSubmit={handleSubmit(onsubmit)}>
            <div className="mb-3">
                <label htmlFor="email" className="form-label">Email address</label>
                <input type="number" className="form-control" id="email" {...register("email")} aria-describedby="emailHelp" />
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div className="mb-3">
                <label htmlFor="password" className="form-label">Password</label>
                <input type="password" className="form-control" id="password" {...register("password")}/>
            </div>
            <div className="mb-3 form-check">
                <input type="checkbox" className="form-check-input" id="exampleCheck1" />
                <label className="form-check-label" htmlFor="exampleCheck1">Check me out</label>
            </div>
            <button type="submit" className="btn btn-primary" >Submit</button>
        </form>
    </div>
    </div>
  )
}

export default SignIn
