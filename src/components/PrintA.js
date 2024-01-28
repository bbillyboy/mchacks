import React, { useEffect, useState } from 'react';

const PrintA = () => {
    const [data, setData] = useState('');

    useEffect(() => {
        // Fetching data from the local Flask API
        fetch('/data')
            .then(response => response.text())  // Change to text() for a single character
            .then(data => setData(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Data from Flask API</h1>
            <p>{data}</p>
        </div>
    );
};

export default PrintA;