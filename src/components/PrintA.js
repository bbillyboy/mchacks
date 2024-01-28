import React, { useState, useEffect } from 'react';

const DictionaryComponent = () => {
  const [dictionaryData, setDictionaryData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/profile');
        const data = await response.json();
        setDictionaryData(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Dictionary Data</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          {dictionaryData.map((item, index) => (
            <div key={index}>
              <h2>{item.word}</h2>
              <p>{item.definition}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default DictionaryComponent;
