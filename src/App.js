import React from 'react';
import Filters from "./components/Filters";
import Maps from "./components/Maps";
import Querybox from "./components/Querybox";
import FooterBar from "./components/FooterBar";
import Backend from "./components/Backend";
import logo from "./logo.png";

import "./index.css"

const App = () => {
  return (
    <div>
      <header style={headerStyles}>
        <img src={logo} alt="Company Logo" style={logoStyles} />
        <h1 className="title">MontrEATS!</h1>
      </header>
      <div style={{ display: 'flex' }}>
        <div style={{ flex: 1 }}>
          <Filters text="Size" />
          <Filters text="Warning" />
          <Filters text="Price" />
          <Filters text="Location" />
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

const headerStyles = {
  backgroundColor: '#333',
  padding: '-150px', // Adjust the padding to make the header smaller
  color: '#fff',
  textAlign: 'center',
  backgroundColor: '#29465B',
  maxHeight: '1000px',
};

const logoStyles = {
  maxWidth: '1900px',
  marginBottom: '0px',
  marginTop: '50px', // Adjust the marginTop to align the logo and title
  marginRight: '1200px', // Add some spacing between the logo and the title
};

const titleStyles = {
  marginTop: '10px', // Add some spacing between logo and title
};

export default App;
