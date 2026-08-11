import { useState } from "react";
import API from "../services/api";

function UploadCard({ setFile, onAnalysisComplete }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [dragActive, setDragActive] = useState(false);

  const MAX_FILE_SIZE = 10 * 1024 * 1024;

  const validateFile = (file) => {
    if (!file) {
      return false;
    }

    if (file.type !== "application/pdf") {
      setMessage("Please select a valid PDF file.");
      return false;
    }

    if (file.size > MAX_FILE_SIZE) {
      setMessage("File size must be less than 10 MB.");
      return false;
    }

    return true;
  };

  const handleFile = (file) => {
    if (!validateFile(file)) {
      setSelectedFile(null);
      setFile(null);
      return;
    }

    setSelectedFile(file);
    setFile(file);
    setMessage("");
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    handleFile(file);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setDragActive(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setDragActive(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragActive(false);

    const file = e.dataTransfer.files[0];
    handleFile(file);
  };

  const uploadContract = async () => {
    if (!selectedFile) {
      setMessage("Please select a PDF file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      setLoading(true);
      setMessage("");

      const response = await API.post(
        "/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("ANALYSIS RESULT:", response.data);

      onAnalysisComplete(
        response.data,
        selectedFile
      );

    } catch (error) {
      console.error("Upload error:", error);

      if (error.response) {
        console.error(
          "Backend response:",
          error.response.data
        );

        setMessage(
          error.response.data?.detail ||
          error.response.data?.message ||
          "Contract analysis failed."
        );
      } else {
        setMessage(
          "Unable to connect to the backend."
        );
      }

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white max-w-2xl mx-auto p-8 md:p-10 rounded-2xl shadow-lg">

      {/* Header */}

      <div className="text-center">

        <div className="mx-auto w-16 h-16 rounded-full bg-blue-100 flex items-center justify-center text-3xl">
          📄
        </div>

        <h2 className="text-2xl md:text-3xl font-bold text-gray-900 mt-5">
          Upload Contract
        </h2>

        <p className="text-gray-500 mt-2">
          Upload a PDF contract for AI-powered risk analysis.
        </p>

      </div>


      {/* Upload Area */}

      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        className={`mt-8 border-2 border-dashed rounded-2xl p-10 text-center transition ${
          dragActive
            ? "border-blue-600 bg-blue-50"
            : "border-blue-300 bg-gray-50"
        }`}
      >

        <div className="text-4xl mb-4">
          ⬆️
        </div>

        <p className="font-medium text-gray-700">
          Drag & drop your PDF here
        </p>

        <p className="text-sm text-gray-500 mt-2">
          or select a file from your computer
        </p>

        <label className="inline-block mt-5">

          <span className="cursor-pointer bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
            Choose PDF
          </span>

          <input
            type="file"
            accept="application/pdf,.pdf"
            onChange={handleFileChange}
            className="hidden"
          />

        </label>

        <p className="text-xs text-gray-400 mt-4">
          PDF only • Maximum size 10 MB
        </p>

      </div>


      {/* Selected File */}

      {selectedFile && (
        <div className="mt-5 flex items-center justify-between gap-4 bg-blue-50 border border-blue-100 rounded-xl p-4">

          <div className="flex items-center gap-3 min-w-0">

            <div className="text-2xl">
              📄
            </div>

            <div className="min-w-0">

              <p className="font-medium text-gray-800 truncate">
                {selectedFile.name}
              </p>

              <p className="text-sm text-gray-500">
                {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
              </p>

            </div>

          </div>

          <button
            type="button"
            onClick={() => {
              setSelectedFile(null);
              setFile(null);
              setMessage("");
            }}
            className="text-red-500 hover:text-red-700 font-medium"
          >
            Remove
          </button>

        </div>
      )}


      {/* Analyze Button */}

      <button
        onClick={uploadContract}
        disabled={loading}
        className="mt-6 w-full bg-blue-600 text-white py-3.5 rounded-lg font-semibold hover:bg-blue-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {loading
          ? "Analyzing Contract..."
          : "Analyze Contract"}
      </button>


      {/* Loading Information */}

      {loading && (
        <div className="mt-5 bg-blue-50 rounded-xl p-4">

          <p className="text-sm text-blue-700 text-center">
            🔄 AI is analyzing your contract. Please wait...
          </p>

        </div>
      )}


      {/* Message */}

      {message && !loading && (
        <div className="mt-5 bg-red-50 border border-red-100 rounded-xl p-4">

          <p className="text-sm text-red-700 text-center">
            {message}
          </p>

        </div>
      )}

    </div>
  );
}

export default UploadCard;