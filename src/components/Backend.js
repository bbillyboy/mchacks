import React, { useEffect, useState } from 'react';

const Backend = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('/api/csv')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Restaurant we recommand you</h1>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>{JSON.stringify(item)}</li>
                ))}
            </ul>
        </div>
    );
};

export default Backend;