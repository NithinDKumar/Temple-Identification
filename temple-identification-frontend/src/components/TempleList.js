import React from 'react';

const TempleList = ({ temples, onSelect }) => {
  return (
    <div className="temple-list">
      {temples.map((temple, index) => (
        <div key={index} className="temple-item" onClick={() => onSelect(temple)}>
          <img src={temple.image} alt={temple.name} />
          <p>{temple.name}</p>
        </div>
      ))}
    </div>
  );
};

export default TempleList;
