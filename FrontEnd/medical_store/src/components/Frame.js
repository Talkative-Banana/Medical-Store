import '../App.css';
import { useState, useEffect } from 'react';
function Frame(Props) {
    const {Link1, Link2, Link3, Link4} = Props;
    
    
    const [y, setY] = useState(0);
    
    useEffect(() => {
      const handleMouseMove = (event) => {
        setY(window.scrollY);
        const track = document.getElementById("tracker");
        const maxy = window.outerHeight;
        const percentage = Math.min(70, y / maxy * 100);
        track.animate({
          transform : `translate(-${percentage}%, 0%)`
        }, {duration: 1000, fill : "forwards"})
      };
  
      window.addEventListener("scroll", handleMouseMove);
  
      return () => {
        window.removeEventListener(
          'scroll',
          handleMouseMove
        );
      };
    }, [y]);

  return (
    <>
    <div className='flexbox-container_frame'>

      <div id="tracker" className="myframe">
            <img className= "image" src={Link1} alt="frame_image" draggable="false"/>
            <img className= "image" src={Link2} alt="frame_image" draggable="false"/>
            <img className= "image" src={Link3} alt="frame_image" draggable="false"/>
            <img className= "image" src={Link4} alt="frame_image" draggable="false"/>
    </div>
    </div>
    </>
  )
}

export default Frame