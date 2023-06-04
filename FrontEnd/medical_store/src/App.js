import './App.css';
import Frame from './components/Frame';
import NavBar from './components/NavBar';
import About from './components/About';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
function App() {
  return (
    <>
      <Router>
        
        <Routes>
          <Route exact path="/" element={<><NavBar logo='/elixir_logo.png' Link1="Home" Link2="Consult Doctor" Link3= "COVID-19" Link4="About" Button="SignIn"/> 
          <Frame Link1='/frame_image.png' Link2='/frame_image.png' Link3='/frame_image.png' Link4='/frame_image.png'/></>} />
          
          <Route exact path="/about" element={<About logo='/frame_image.png'/>} />
        </Routes>
      </Router>
      </>
  );
}

export default App;
