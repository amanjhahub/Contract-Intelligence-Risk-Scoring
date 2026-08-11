import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function Compare() {
  const navigate = useNavigate();

  const [contractA, setContractA] = useState(null);
  const [contractB, setContractB] = useState(null);

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleFileChange = (file, contract) => {
    if (!file) {
      return;
    }

    if (file.type !== "application/pdf") {
      setMessage("Please select PDF files only.");
      return;
    }

    setMessage("");
    setResult(null);

    if (contract === "A") {
      setContractA(file);
    } else {
      setContractB(file);
    }
  };

  const compareContracts = async () => {
    if (!contractA || !contractB) {
      setMessage("Please select both PDF contracts.");
      return;
    }

    const formData = new FormData();

    formData.append("contract_a", contractA);
    formData.append("contract_b", contractB);

    try {
      setLoading(true);
      setMessage("");
      setResult(null);

      const response = await API.post(
        "/compare",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("COMPARE RESULT:", response.data);

      setResult(response.data);

      setMessage("Contracts compared successfully.");

    } catch (error) {
      console.error("COMPARE ERROR:", error);

      if (error.response) {
        console.error(
          "Backend response:",
          error.response.data
        );
      }

      setMessage(
        error.response?.data?.detail ||
        "Comparison failed. Check backend connection."
      );

    } finally {
      setLoading(false);
    }
  };

  const resetComparison = () => {
    setContractA(null);
    setContractB(null);
    setResult(null);
    setMessage("");
  };

  return (
    <div className="max-w-6xl mx-auto px-6 pb-20">

      <div className="text-center mb-10">

        <h1 className="text-4xl md:text-5xl font-bold text-gray-900">
          Compare Contracts
        </h1>

        <p className="mt-4 text-lg text-gray-600 max-w-2xl mx-auto">
          Upload two contracts and compare their risks,
          clauses, and recommendations.
        </p>

      </div>


      <div className="grid md:grid-cols-2 gap-6">

        <div className="bg-white rounded-2xl shadow p-8">

          <div className="flex items-center justify-between">

            <h2 className="text-xl font-bold">
              Contract A
            </h2>

            <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-semibold">
              A
            </span>

          </div>

          <div className="mt-5 border-2 border-dashed border-blue-300 rounded-xl p-8">

            <input
              type="file"
              accept=".pdf,application/pdf"
              onChange={(e) =>
                handleFileChange(
                  e.target.files[0],
                  "A"
                )
              }
              className="block w-full"
            />

          </div>

          {contractA && (
            <div className="mt-4 bg-blue-50 rounded-lg p-4">

              <p className="text-sm font-medium text-gray-700">
                Selected file
              </p>

              <p className="text-sm text-blue-700 mt-1 break-all">
                {contractA.name}
              </p>

            </div>
          )}

        </div>


        <div className="bg-white rounded-2xl shadow p-8">

          <div className="flex items-center justify-between">

            <h2 className="text-xl font-bold">
              Contract B
            </h2>

            <span className="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm font-semibold">
              B
            </span>

          </div>

          <div className="mt-5 border-2 border-dashed border-purple-300 rounded-xl p-8">

            <input
              type="file"
              accept=".pdf,application/pdf"
              onChange={(e) =>
                handleFileChange(
                  e.target.files[0],
                  "B"
                )
              }
              className="block w-full"
            />

          </div>

          {contractB && (
            <div className="mt-4 bg-purple-50 rounded-lg p-4">

              <p className="text-sm font-medium text-gray-700">
                Selected file
              </p>

              <p className="text-sm text-purple-700 mt-1 break-all">
                {contractB.name}
              </p>

            </div>
          )}

        </div>

      </div>


      <div className="flex flex-col sm:flex-row gap-4 mt-8">

        <button
          onClick={compareContracts}
          disabled={
            loading ||
            !contractA ||
            !contractB
          }
          className="flex-1 bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
        >

          {loading
            ? "Comparing Contracts..."
            : "Compare Contracts"}

        </button>


        {(contractA || contractB || result) && (

          <button
            onClick={resetComparison}
            disabled={loading}
            className="sm:w-40 border border-gray-300 text-gray-700 py-3 rounded-lg font-semibold hover:bg-gray-100 transition"
          >
            Clear
          </button>

        )}

      </div>


      {message && (
        <div className="mt-5 text-center">

          <p
            className={
              message.includes("successfully")
                ? "text-green-600"
                : "text-gray-700"
            }
          >
            {message}
          </p>

        </div>
      )}


      {result && (

        <div className="mt-12">

          <div className="text-center mb-8">

            <h2 className="text-3xl font-bold text-gray-900">
              Comparison Result
            </h2>

            <p className="text-gray-500 mt-2">
              AI-powered comparison of both contracts.
            </p>

          </div>


          <div className="grid md:grid-cols-2 gap-6">

            <div className="bg-white rounded-2xl shadow p-8">

              <h3 className="text-lg text-gray-500">
                Contract A Score
              </h3>

              <p className="text-5xl font-bold text-blue-600 mt-3">
                {result.contract_a_score ?? 0}%
              </p>

              <div className="mt-5 w-full bg-gray-200 rounded-full h-3">

                <div
                  className="bg-blue-600 h-3 rounded-full"
                  style={{
                    width: `${Math.min(
                      Math.max(
                        Number(
                          result.contract_a_score || 0
                        ),
                        0
                      ),
                      100
                    )}%`
                  }}
                />

              </div>

            </div>


            <div className="bg-white rounded-2xl shadow p-8">

              <h3 className="text-lg text-gray-500">
                Contract B Score
              </h3>

              <p className="text-5xl font-bold text-purple-600 mt-3">
                {result.contract_b_score ?? 0}%
              </p>

              <div className="mt-5 w-full bg-gray-200 rounded-full h-3">

                <div
                  className="bg-purple-600 h-3 rounded-full"
                  style={{
                    width: `${Math.min(
                      Math.max(
                        Number(
                          result.contract_b_score || 0
                        ),
                        0
                      ),
                      100
                    )}%`
                  }}
                />

              </div>

            </div>

          </div>


          <div className="grid md:grid-cols-2 gap-6 mt-6">

            <div className="bg-white rounded-2xl shadow p-8">

              <h3 className="text-xl font-bold">
                Missing in Contract A
              </h3>

              {Array.isArray(result.missing_in_a) &&
              result.missing_in_a.length > 0 ? (

                <ul className="mt-5 space-y-3">

                  {result.missing_in_a.map(
                    (item, index) => (

                      <li
                        key={index}
                        className="bg-red-50 text-red-700 p-3 rounded-lg"
                      >
                        {typeof item === "object"
                          ? item.clause
                          : item}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p className="mt-5 text-green-600">
                  No missing clauses.
                </p>

              )}

            </div>


            <div className="bg-white rounded-2xl shadow p-8">

              <h3 className="text-xl font-bold">
                Missing in Contract B
              </h3>

              {Array.isArray(result.missing_in_b) &&
              result.missing_in_b.length > 0 ? (

                <ul className="mt-5 space-y-3">

                  {result.missing_in_b.map(
                    (item, index) => (

                      <li
                        key={index}
                        className="bg-red-50 text-red-700 p-3 rounded-lg"
                      >
                        {typeof item === "object"
                          ? item.clause
                          : item}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p className="mt-5 text-green-600">
                  No missing clauses.
                </p>

              )}

            </div>

          </div>


          <div className="bg-white rounded-2xl shadow p-8 mt-6">

            <h3 className="text-xl font-bold">
              Risk Difference
            </h3>

            <p className="text-4xl font-bold text-orange-600 mt-3">
              {result.risk_difference ?? 0}%
            </p>

          </div>


          <div className="bg-green-50 border border-green-200 rounded-2xl shadow p-8 mt-6">

            <h3 className="text-xl font-bold text-green-700">
              Recommendation
            </h3>

            <p className="text-3xl font-bold text-gray-900 mt-3">
              {result.recommendation || "No recommendation"}
            </p>

          </div>


          <div className="flex flex-col sm:flex-row gap-4 mt-8">

            <button
              onClick={() => navigate("/")}
              className="flex-1 bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700"
            >
              Analyze a Contract
            </button>

            <button
              onClick={resetComparison}
              className="flex-1 border border-gray-300 text-gray-700 py-3 rounded-lg hover:bg-gray-100"
            >
              Compare Again
            </button>

          </div>

        </div>

      )}

    </div>
  );
}

export default Compare;