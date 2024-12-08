import React from 'react';

const UploadImage = ({ handleUpload }) => {
  return (
    <div className="upload-image">
      <input type="file" onChange={(e) => handleUpload(e.target.files[0])} />
      <button>Upload Image</button>
    </div>
  );
};

export default UploadImage;
