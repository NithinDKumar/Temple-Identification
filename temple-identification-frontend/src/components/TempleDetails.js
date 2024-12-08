import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import './TempleDetails.css';

const TempleDetailsPage = () => {
  const { id } = useParams();
  const [temple, setTemple] = useState(null);

  useEffect(() => {
    const fetchTempleDetails = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/api/temples/${id}`);
        setTemple(response.data);
      } catch (error) {
        console.error('Error fetching temple details:', error);
      }
    };

    fetchTempleDetails();
  }, [id]);

  if (!temple) return <div>Loading...</div>;

  return (
    <div className="temple-details-page">
      <h1>{temple.name}</h1>
      <img src={temple.image_url} alt={temple.name} className="temple-image" />
      <p><strong>State:</strong> {temple.state}</p>
      <div className="temple-details">
        <div className="sub-box">
          <h3>Info</h3>
          <p>{temple.info}</p>
        </div>
        <div className="sub-box">
          <h3>Story</h3>
          <p>{temple.story}</p>
        </div>
        <div className="sub-box">
          <h3>Architecture</h3>
          <p>{temple.architecture}</p>
        </div>
      </div>
    </div>
  );
};

export default TempleDetailsPage;
