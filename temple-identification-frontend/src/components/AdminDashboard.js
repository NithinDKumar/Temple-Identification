import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AdminDashboard.css';

const AdminDashboard = () => {
  const [temples, setTemples] = useState([]);
  const [selectedTemple, setSelectedTemple] = useState(null);

  useEffect(() => {
    const fetchTemples = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/temples');
        setTemples(response.data);
      } catch (error) {
        console.error('Error fetching temples:', error);
      }
    };

    fetchTemples();
  }, []);

  const handleTempleSelect = (temple) => {
    setSelectedTemple(temple);
  };

  const handleUpdate = async (updatedTemple) => {
    try {
      await axios.put(`http://localhost:5000/api/temples/${updatedTemple._id}`, updatedTemple);
      setTemples(temples.map(t => t._id === updatedTemple._id ? updatedTemple : t));
      setSelectedTemple(null);
    } catch (error) {
      console.error('Error updating temple:', error);
    }
  };

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <div className="temples-list">
        {temples.map((temple, index) => (
          <div key={temple._id} className="temple-card" onClick={() => handleTempleSelect(temple)}>
            <h3>{temple.name}</h3>
            <p>{temple.state}</p>
          </div>
        ))}
      </div>
      {selectedTemple && (
        <div className="temple-edit">
          <h2>Edit Temple Details</h2>
          <form onSubmit={(e) => {
            e.preventDefault();
            handleUpdate(selectedTemple);
          }}>
            <label>
              Name:
              <input type="text" value={selectedTemple.name} onChange={(e) => setSelectedTemple({...selectedTemple, name: e.target.value})} />
            </label>
            <label>
              State:
              <input type="text" value={selectedTemple.state} onChange={(e) => setSelectedTemple({...selectedTemple, state: e.target.value})} />
            </label>
            <label>
              Info:
              <textarea value={selectedTemple.info} onChange={(e) => setSelectedTemple({...selectedTemple, info: e.target.value})}></textarea>
            </label>
            <label>
              Story:
              <textarea value={selectedTemple.story} onChange={(e) => setSelectedTemple({...selectedTemple, story: e.target.value})}></textarea>
            </label>
            <label>
              Architecture:
              <textarea value={selectedTemple.architecture} onChange={(e) => setSelectedTemple({...selectedTemple, architecture: e.target.value})}></textarea>
            </label>
            <button type="submit">Save Changes</button>
          </form>
        </div>
      )}
    </div>
  );
};

export default AdminDashboard;
