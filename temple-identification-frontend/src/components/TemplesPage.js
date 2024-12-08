import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './TemplesPage.css';

const TemplesPage = () => {
  const [temples, setTemples] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTemples = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/temples');
        console.log('Fetched temples:', response.data);
        setTemples(response.data);
      } catch (error) {
        console.error('Error fetching temples:', error);
      }
    };

    fetchTemples();
  }, []);

  const handleTempleClick = (temple) => {
    navigate(`/temple/${temple._id}`);
  };

  return (
    <div className="temples-page">
      <h1>Temples</h1>
      <div className="temple-grid">
        {temples.map((temple) => (
          <div key={temple._id} className="temple-box" onClick={() => handleTempleClick(temple)}>
            <div className="temple-info">
              <h3>{temple.name}</h3>
              <p>{temple.state}</p>
            </div>
            <div className="temple-image-container">
              <img src={temple.image_url} alt={temple.name} className="temple-image" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TemplesPage;
