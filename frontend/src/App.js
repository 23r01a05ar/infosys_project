import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [message, setMessage] = useState("");

  const MAX_SIZE = 10 * 1024 * 1024; // 10MB

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    if (file.size > MAX_SIZE) {
      alert("File size exceeds 10MB limit!");
      return;
    }

    setImage(file);
    setPreview(URL.createObjectURL(file));
    setMessage("");
  };

  const handleRemoveImage = () => {
    setImage(null);
    setPreview(null);
    setMessage("");
  };

  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image first");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/api/upload-image",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (response.ok) {
        setMessage(`Upload Successful! Image ID: ${data.image_id}`);
      } else {
        setMessage(data.error);
      }
    } catch {
      setMessage("Server error");
    }
  };

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
        <span className="navbar-brand fw-bold">
          Online Product Price Intelligence System
        </span>

        <div className="ms-auto">
          <button className="btn btn-outline-light me-2">Login</button>
          <button className="btn btn-warning">Sign Up</button>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="text-center mt-5">
        <h1>Welcome to OPPI System</h1>
        <p className="text-muted">
          Upload product images to analyze and track pricing intelligence.
        </p>
      </div>

      {/* Upload Section */}
      <div className="container mt-5 text-center">
        <h3>Upload Product Image</h3>

        <input
          type="file"
          accept="image/*"
          className="form-control mt-3"
          onChange={handleImageChange}
        />

        {/* Image Preview */}
        {preview && (
          <div className="mt-3">
            <img
              src={preview}
              alt="Preview"
              style={{ width: "300px", borderRadius: "10px" }}
            />
            <br />
            <button
              className="btn btn-danger mt-3"
              onClick={handleRemoveImage}
            >
              Remove Image
            </button>
          </div>
        )}

        <br />

        <button className="btn btn-primary mt-3" onClick={handleUpload}>
          Upload Image
        </button>

        {message && <p className="mt-3 fw-bold">{message}</p>}
      </div>

      {/* Footer */}
      <footer className="bg-dark text-white text-center p-3 mt-5">
        © 2026 Online Product Price Intelligence System
      </footer>
    </div>
  );
}

export default App;
