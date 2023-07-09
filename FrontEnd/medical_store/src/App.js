import './App.css';
import Frame from './components/Frame';
import NavBar from './components/NavBar';
import SignIn from './components/SignIn';
import Grid from './components/Grid';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import Collection from './Collection';
function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={
            <>
              <NavBar logo='/elixir_logo.png' Link1="/" Link2="/Consultation" Link3= "/Covid" Link4="/About" Button="SignIn"/> 
              <Frame Link1='/frame_image.png' Link2='/frame_image.png' Link3='/frame_image.png' Link4='/frame_image.png'/>
              <Collection image = '/images/1/1_0.png' category = "1" Link = "/"></Collection>
              <Collection image = '/images/2/2_0.jpg' category = "2" Link = "/"></Collection>
              <Collection image = '/images/3/3_0.jpg' category = "3" Link = "/"></Collection>
            </>
          } />

          <Route exact path="/SignIn" element={<SignIn logo='/frame_image.png'/>} />

          <Route exact path="/HomePage" element={
          <>
            <div><NavBar logo='../elixir_logo.png' Link1="/HomePage" Link2="/Consultation" Link3= "/Covid" Link4="/About" Button="Logout"/></div>
            <div><Frame Link1='/frame_image.png' Link2='/frame_image.png' Link3='/frame_image.png' Link4='/frame_image.png'/></div>
            <div><Grid/ ></div>
          </>
          } />

          <Route exact path="/About" element={
            <NavBar logo='../elixir_logo.png' Link1="/HomePage" Link2="/Consultation" Link3= "/Covid" Link4="/About" Button="Logout"/>
          } />

          <Route exact path="/Consultation" element={
            <>
              <NavBar logo='../elixir_logo.png' Link1="/HomePage" Link2="/Consultation" Link3= "/Covid" Link4="/About" Button="Logout"/>
              <Frame Link1='/frame_image.png' Link2='/frame_image.png' Link3='/frame_image.png' Link4='/frame_image.png'/>
            </>
          } />

          <Route exact path="/Covid" element={
            <NavBar logo='../elixir_logo.png' Link1="/HomePage" Link2="/Consultation" Link3= "/Covid" Link4="/About" Button="Logout"/>
          } />

        </Routes>
      </Router>
    </>
  );
}

export default App;
