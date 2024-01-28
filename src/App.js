import React from 'react';
import Filters from "./components/Filters";
import Maps from "./components/Maps";
import Querybox from "./components/Querybox";
import FooterBar from "./components/FooterBar";
import Backend from "./components/Backend"
import PrintA from "./components/PrintA"

import "./index.css"

const App = () => {
  return (
    <div>
      <h1 className="title">MontrEATS!</h1>
      <div style={{ display: 'flex' }}>
        <div style={{ flex: 1 }}>
          <Filters text="Size" />
          <Filters text="Warning" />
          <Filters text="Price" />
          <Filters text="Location" />
          <PrintA />
          <Backend />
        </div>
        <div style={{ flex: 1 }}>
          <Maps />
          <Querybox />
        </div>
      </div> 
      <FooterBar />
    </div>
  );
};

export default App;

