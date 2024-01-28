import React, { useEffect, useState } from 'react';

const Backend = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Restaurants we recommand you</h1>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>{item["latitude"]}</li>
                ))}
            </ul>
        </div>
    );
};

export default Backend;