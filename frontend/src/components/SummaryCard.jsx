import { useState } from "react";
import API from "../services/api";

function SummaryCard({ file }) {
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState(false);

  const generateSummary = async () => {
    if (!file) {
      setMessage("Please upload a contract first.");
      setError(true);
      return;
    }

    try {
      setLoading(true);
      setMessage("");
      setError(false);
      setSummary("");

      const formData = new FormData();
      formData.append("file", file);

      const response = await API.post(
        "/summary",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("SUMMARY RESULT:", response.data);

      if (response.data?.summary) {
        setSummary(response.data.summary);
        setMessage("Summary generated successfully.");
        setError(false);
      } else {
        setMessage("The backend returned an empty summary.");
        setError(true);
      }

    } catch (error) {
      console.error("SUMMARY ERROR:", error);

      if (error.response) {
        console.error(
          "Backend response:",
          error.response.data
        );

        setMessage(
          error.response.data?.detail ||
          error.response.data?.message ||
          "Unable to generate summary."
        );
      } else {
        setMessage(
          "Unable to connect to the backend."
        );
      }

      setError(true);

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-md p-8 mt-8">

      {/* Header */}

      <div className="flex items-start gap-4">

        <div className="w-12 h-12 rounded-xl bg-blue-100 flex items-center justify-center text-2xl">
          📝
        </div>

        <div>

          <h2 className="text-2xl font-bold text-gray-900">
            Contract Summary
          </h2>

          <p className="text-gray-500 mt-1">
            Generate an AI-powered summary of the uploaded contract.
          </p>

        </div>

      </div>


      {/* File Information */}

      {!file ? (

        <div className="mt-6 bg-yellow-50 border border-yellow-200 rounded-xl p-5">

          <p className="text-yellow-700 font-medium">
            No contract uploaded yet.
          </p>

          <p className="text-yellow-600 text-sm mt-1">
            Upload and analyze a contract to generate its summary.
          </p>

        </div>

      ) : (

        <div className="mt-6 flex items-center gap-3 bg-blue-50 border border-blue-100 rounded-xl p-4">

          <span className="text-2xl">
            📄
          </span>

          <div className="min-w-0">

            <p className="text-sm text-gray-500">
              Contract
            </p>

            <p className="font-medium text-gray-800 truncate">
              {file.name}
            </p>

          </div>

        </div>

      )}


      {/* Generate Button */}

      <button
        onClick={generateSummary}
        disabled={!file || loading}
        className="mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
      >

        {loading
          ? "Generating Summary..."
          : "Generate Summary"}

      </button>


      {/* Loading State */}

      {loading && (

        <div className="mt-5 bg-blue-50 border border-blue-100 rounded-xl p-4">

          <p className="text-blue-700 text-sm">
            🔄 AI is reading and summarizing the contract...
          </p>

        </div>

      )}


      {/* Status Message */}

      {message && !loading && (

        <div
          className={`mt-5 rounded-xl p-4 border ${
            error
              ? "bg-red-50 border-red-100"
              : "bg-green-50 border-green-100"
          }`}
        >

          <p
            className={`text-sm ${
              error
                ? "text-red-700"
                : "text-green-700"
            }`}
          >
            {message}
          </p>

        </div>

      )}


      {/* Summary Result */}

      {summary && (

        <div className="mt-6 bg-gray-50 border border-gray-200 rounded-2xl p-6">

          <div className="flex items-center justify-between gap-4 mb-4">

            <h3 className="font-bold text-xl text-gray-900">
              AI Summary
            </h3>

            <span className="text-xs font-medium px-3 py-1 rounded-full bg-blue-100 text-blue-700">
              AI Generated
            </span>

          </div>

          <div className="border-t border-gray-200 pt-5">

            <p className="text-gray-700 leading-7 whitespace-pre-line">
              {summary}
            </p>

          </div>

        </div>

      )}

    </div>
  );
}

export default SummaryCard;