import React, { useState } from "react";

function App() {

  const [image, setImage] = useState(null);

  const handleFile = (file) => {
    if (file && file.type.startsWith("image/")) {
      setImage(URL.createObjectURL(file));
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    handleFile(file);
  };

  const handleBrowse = (e) => {
    const file = e.target.files[0];
    handleFile(file);
  };

  return (
    <div className="d-flex flex-column min-vh-100">

      {/* Header */}
      <header className="bg-dark text-white text-center p-3">
        <h2>Online Product Price Intelligence</h2>
      </header>

      {/* Navigation */}
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <span className="navbar-brand">Home</span>
          <span className="navbar-brand">Upload</span>
        </div>
      </nav>

      {/* Main Content */}
      <main className="container flex-grow-1 mt-5">

        <h3 className="text-center mb-4">Upload Product Image</h3>

        <div
          className="border border-2 border-secondary p-5 text-center rounded"
          onDragOver={(e) => e.preventDefault()}
          onDrop={handleDrop}
        >
          <p>Drag and Drop Image Here</p>
          <p>OR</p>

          <input
            type="file"
            accept="image/*"
            className="form-control"
            onChange={handleBrowse}
          />
        </div>

        {image && (
          <div className="text-center mt-4">
            <h5>Image Preview</h5>
            <img src={image} alt="preview" className="img-fluid" width="300" />
          </div>
        )}

      </main>

      {/* Footer */}
      <footer className="bg-dark text-white text-center p-3 mt-auto">
        <p>© 2026 Price Intelligence System</p>
      </footer>

    </div>
  );
}

export default App;
