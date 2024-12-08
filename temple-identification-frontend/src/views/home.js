import React from 'react';
import Header from '../components/Header';
import SearchBar from '../components/SearchBar';
import UploadImage from '../components/UploadImage';
import TempleSearchResult from '../components/TempleSearchResult';
import TempleDetails from '../components/TempleDetails';

const Home = ({
  searchQuery,
  setSearchQuery,
  handleSearch,
  searchResults,
  handleUpload,
  selectedTemple,
  handleTempleSelect
}) => {
  return (
    <div className="home">
      <Header />
      <SearchBar
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        handleSearch={handleSearch}
      />
      <UploadImage handleUpload={handleUpload} />
      {searchResults.length > 0 && (
        <TempleSearchResult temples={searchResults} onSelect={handleTempleSelect} />
      )}
      {selectedTemple && <TempleDetails temple={selectedTemple} />}
    </div>
  );
};

export default Home;
