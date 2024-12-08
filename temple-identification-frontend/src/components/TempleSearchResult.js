import React from 'react';

const TempleSearchResult = ({ temples, onSelect }) => {
  return (
    <div className="temple-search-result">
      {temples.map((temple, index) => (
        <div key={index} onClick={() => onSelect(temple)} className="temple-item">
          <h3>{temple.name}</h3>
          <p>{temple.location}</p>
        </div>
      ))}
    </div>
  );
};

export default TempleSearchResult;
