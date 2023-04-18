import './App.css';
import Frame from './components/Frame';
import NavBar from './components/NavBar';
import SidePanel from './components/SidePanel';
function App() {
  return (
    <>
      <NavBar logo='/elixir_logo.png' Link1="Home" Link2="Consult Doctor" Link3= "COVID-19" Link4="About" Button="SignIn"/>
      <div className='flexbox-container'>
        <div className='flexbox-item_1'><SidePanel/></div>
        <div className='flexbox-item_2'><Frame Link1='/frame_image.png' Link2='/frame_image.png' Link3='/frame_image.png' Link4='/frame_image.png'/></div>
      </div>
      </>
  );
}

export default App;
