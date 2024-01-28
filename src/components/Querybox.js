
import React, { useState } from 'react';
import '../index.css';

const containerStyle = {
  display: 'flex',
  flexDirection: 'row',
  width: '900px',
  height: '500px',
  border: 'solid'
};

const Querybox = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (inputValue.trim() !== '') {
      setMessages([...messages, { text: inputValue, sender: 'user' }]);
      setInputValue('');
    }
    // Here you can add logic to send the user's input to the backend for processing
    // and receive a response to display in the Querybox.
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Write your query..."
          value={inputValue}
          onChange={handleInputChange}
          class = "querybox"
        />
        <button type="submit" class="button">Send</button>
      </form>
      <br></br>
      <p class = "Query Response"></p>
    </div>
  );
};

export default Querybox;