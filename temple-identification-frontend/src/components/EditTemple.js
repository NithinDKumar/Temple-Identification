import React, { useState } from 'react';
import './EditTemple.css';

const EditTemple = ({ temple, handleUpdate }) => {
  const [updatedTemple, setUpdatedTemple] = useState(temple);

  const handleSubmit = (e) => {
    e.preventDefault();
    handleUpdate(updatedTemple);
  };

  return (
    <div className="edit-temple">
      <h2>Edit Temple Details</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={updatedTemple.name} onChange={(e) => setUpdatedTemple({...updatedTemple, name: e.target.value})} />
        </label>
        <label>
          Location:
          <input type="text" value={updatedTemple.location} onChange={(e) => setUpdatedTemple({...updatedTemple, location: e.target.value})} />
        </label>
        <label>
          State:
          <input type="text" value={updatedTemple.state} onChange={(e) => setUpdatedTemple({...updatedTemple, state: e.target.value})} />
        </label>
        <label>
          Info:
          <textarea value={updatedTemple.info} onChange={(e) => setUpdatedTemple({...updatedTemple, info: e.target.value})}></textarea>
        </label>
        <label>
          Story:
          <textarea value={updatedTemple.story} onChange={(e) => setUpdatedTemple({...updatedTemple, story: e.target.value})}></textarea>
        </label>
        <label>
          Architecture:
          <textarea value={updatedTemple.architecture} onChange={(e) => setUpdatedTemple({...updatedTemple, architecture: e.target.value})}></textarea>
        </label>
        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
};

export default EditTemple;
