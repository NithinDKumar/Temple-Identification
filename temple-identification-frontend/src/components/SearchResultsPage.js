import React from 'react';
import { useLocation } from 'react-router-dom';
import './SearchResultsPage.css';

function SearchResultsPage() {
  const { state } = useLocation();
  const { results } = state || { results: [] };

  if (!results.length) {
    return <div>No results found.</div>;
  }

  const temple = results[0];

  return (
    <div className="results">
      <div className="image-section">
        <img src={temple.images[0] || '/default-image.png'} alt={temple.name} className="temple-image" />
      </div>
      <div className="details-section">
        <h2>{temple.name}</h2>
        <p>{temple.description}</p>
        <h3>Location</h3>
        <p>{temple.location}</p>
        <h3>Info</h3>
        <p>{temple.built_date}</p>
      </div>
    </div>
  );
}

export default SearchResultsPage;
