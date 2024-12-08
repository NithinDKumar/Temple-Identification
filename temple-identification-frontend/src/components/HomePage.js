import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './HomePage.css';

const HomePage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [expandedIndex, setExpandedIndex] = useState(null);

  useEffect(() => {
    console.log("Search Results Updated: ", searchResults);
  }, [searchResults]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/api/temples/search/${searchQuery}`);
      console.log('Search results:', response.data);
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await axios.post('http://localhost:5000/api/temples/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Upload result:', response.data);

      const searchResponse = await axios.get(`http://localhost:5000/api/temples/search/${response.data.name}`);
      setSearchResults(searchResponse.data);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  const toggleExpand = (index) => {
    if (expandedIndex === index) {
      setExpandedIndex(null);
    } else {
      setExpandedIndex(index);
    }
  };

  const removeAsterisks = (text) => {
    return text ? text.replace(/\*\*/g, '') : '';
  };

  return (
    <div className="home-page">
      <h1>Temple Identification</h1>
      <div className="search-upload-container">
        <div className="search-section">
          <input
            type="text"
            placeholder="Search for temples..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="search-input"
          />
          <button onClick={handleSearch} className="search-button">Search</button>
        </div>
        <div className="upload-section">
          <input type="file" onChange={(e) => setSelectedFile(e.target.files[0])} className="file-input" />
          <button onClick={handleUpload} className="upload-button">Upload Image</button>
        </div>
      </div>
      {searchResults.length > 0 && (
        <div className="temple-details-container">
          {searchResults.map((result, index) => (
            <div 
              key={result._id || index}  // Use temple's unique _id or fallback to index
              className={`temple-details-box ${expandedIndex === index ? 'expanded' : 'random-color-box'}`} 
              onClick={() => toggleExpand(index)}
            >
              <h2>{result.name}</h2>
              <p><strong>State:</strong> {result.state}</p>
              {expandedIndex === index && (
                <div className="expanded-details">
                  <div className="temple-image-container">
                    {result.image_url 
                      ? <img src={result.image_url} alt={result.name} className="temple-image" />
                      : <div className="temple-image-placeholder">Picture Loading...</div>
                    }
                  </div>
                  <div className="center-content">
                    <p><strong>Built Date:</strong> {result.built_date}</p>
                  </div>
                  <div className="sub-box">
                    <h3>Info</h3>
                    <p>{removeAsterisks(result.info)}</p>
                  </div>
                  <div className="sub-box">
                    <h3>Story</h3>
                    <p>{removeAsterisks(result.story)}</p>
                  </div>
                  <div className="sub-box">
                    <h3>Architecture</h3>
                    <p>{removeAsterisks(result.architecture)}</p>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default HomePage;
