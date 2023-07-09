import React from 'react';
import Card from './components/Card';

const Collection = (props) => {

const {image, category, lst, Link, tag} = props;
  return (
    <div className='collections' style = {{backgroundImage: `url(${image})`, backgroundSize: "cover", height: "50%" }}>
      <div className='collections_tag'> HELLO </div> 
      <div className='collections_item'><Card Image = {"/images/" + category + "/" + category + "_1" + ".jpg"} Name = "MuscleBlaze Creatine Monohydrate 100 gm" Price = "Rs. 1000.00" info = "Some Info"> </Card></div>
      <div className='collections_item'><Card Image = {"/images/" + category + "/" + category + "_2" + ".jpg"} Name = "MuscleBlaze Creatine Monohydrate 100 gm" Price = "Rs. 1000.00" info = "Some Info"> </Card></div>
      <div className='collections_item'><Card Image = {"/images/" + category + "/" + category + "_3" + ".jpg"} Name = "MuscleBlaze Creatine Monohydrate 100 gm" Price = "Rs. 1000.00" info = "Some Info"> </Card></div>
      <div className='collections_item'><Card Image = {"/images/" + category + "/" + category + "_4" + ".jpg"} Name = "MuscleBlaze Creatine Monohydrate 100 gm" Price = "Rs. 1000.00" info = "Some Info"> </Card></div>
    </div>
  )
}

export default Collection
