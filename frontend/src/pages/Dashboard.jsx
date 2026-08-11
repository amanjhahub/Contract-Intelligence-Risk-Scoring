import { useLocation, useNavigate } from "react-router-dom";
import ChatSection from "../components/ChatSection";
import SummaryCard from "../components/SummaryCard";

function Dashboard() {
  const location = useLocation();
  const navigate = useNavigate();

  const result = location.state?.result;
  const file = location.state?.file;

  if (!result) {
    return (
      <div className="max-w-4xl mx-auto px-6 py-20 text-center">
        <div className="bg-white rounded-2xl shadow-lg p-10">
          <h1 className="text-3xl font-bold text-gray-900">
            No Analysis Available
          </h1>

          <p className="mt-4 text-gray-600">
            Please upload and analyze a contract first.
          </p>

          <button
            onClick={() => navigate("/")}
            className="mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition"
          >
            Upload Contract
          </button>
        </div>
      </div>
    );
  }

  const riskLevel = String(result.risk_level || "").toUpperCase();
  const riskScore = Number(result.risk_score || 0);

  const riskColor =
    riskLevel === "LOW"
      ? "text-green-700 bg-green-100 border-green-200"
      : riskLevel === "MEDIUM"
      ? "text-yellow-700 bg-yellow-100 border-yellow-200"
      : "text-red-700 bg-red-100 border-red-200";

  const progressColor =
    riskLevel === "LOW"
      ? "bg-green-500"
      : riskLevel === "MEDIUM"
      ? "bg-yellow-500"
      : "bg-red-500";

  const presentClauses = Array.isArray(result.present_clauses)
    ? result.present_clauses
    : [];

  const missingClauses = Array.isArray(result.missing_clauses)
    ? result.missing_clauses
    : [];

  const entities = Array.isArray(result.entities)
    ? result.entities
    : [];

  const recommendations = Array.isArray(result.recommendations)
    ? result.recommendations
    : [];

  return (
    <div className="max-w-6xl mx-auto px-6 pb-20">

      {/* Header */}

      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-5 mb-8">

        <div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900">
            Contract Risk Analysis
          </h1>

          {file && (
            <p className="mt-2 text-gray-500">
              Analyzed file:{" "}
              <span className="font-medium text-gray-700">
                {file.name}
              </span>
            </p>
          )}
        </div>

        <div className="flex flex-wrap gap-3">

          <button
            onClick={() => navigate("/compare")}
            className="bg-purple-600 text-white px-5 py-3 rounded-lg hover:bg-purple-700 transition shadow-sm"
          >
            Compare Contracts
          </button>

          <button
            onClick={() => navigate("/")}
            className="bg-blue-600 text-white px-5 py-3 rounded-lg hover:bg-blue-700 transition shadow-sm"
          >
            Analyze Another
          </button>

        </div>

      </div>


      {/* Risk Overview */}

      <div className="grid md:grid-cols-2 gap-6">

        {/* Risk Score */}

        <div className="bg-white rounded-2xl shadow-md p-8">

          <div className="flex items-center justify-between">

            <h2 className="text-lg font-medium text-gray-500">
              Risk Score
            </h2>

            <span className="text-sm text-gray-400">
              Overall Risk
            </span>

          </div>

          <p className="text-6xl font-bold text-blue-600 mt-4">
            {riskScore}%
          </p>

          <div className="mt-6 w-full bg-gray-200 rounded-full h-3 overflow-hidden">

            <div
              className={`h-3 rounded-full ${progressColor} transition-all duration-700`}
              style={{
                width: `${Math.min(Math.max(riskScore, 0), 100)}%`,
              }}
            />

          </div>

          <p className="mt-3 text-sm text-gray-500">
            Based on detected clauses, missing clauses and contract risk factors.
          </p>

        </div>


        {/* Risk Level */}

        <div className="bg-white rounded-2xl shadow-md p-8">

          <h2 className="text-lg font-medium text-gray-500">
            Risk Level
          </h2>

          <span
            className={`inline-flex items-center mt-5 px-6 py-3 rounded-full border font-bold text-lg ${riskColor}`}
          >
            {riskLevel || "UNKNOWN"}
          </span>

          <p className="mt-5 text-gray-600">

            {riskLevel === "LOW"
              ? "The contract appears to have relatively low risk based on the analysis."
              : riskLevel === "MEDIUM"
              ? "The contract contains some areas that may require additional review."
              : "The contract contains significant risk factors that should be reviewed carefully."}

          </p>

        </div>

      </div>


      {/* Present Clauses */}

      <div className="bg-white rounded-2xl shadow-md p-8 mt-8">

        <div className="flex items-center justify-between gap-4">

          <div>

            <h2 className="text-2xl font-bold text-gray-900">
              Present Clauses
            </h2>

            <p className="mt-1 text-gray-500">
              Important clauses detected in the contract.
            </p>

          </div>

          <span className="px-4 py-2 rounded-full bg-blue-100 text-blue-700 font-semibold">
            {presentClauses.length}
          </span>

        </div>


        {presentClauses.length === 0 ? (

          <div className="mt-6 bg-gray-50 rounded-xl p-6 text-center">

            <p className="text-gray-500">
              No clauses detected.
            </p>

          </div>

        ) : (

          <div className="grid md:grid-cols-2 gap-4 mt-6">

            {presentClauses.map((item, index) => {

              const clause =
                typeof item === "object"
                  ? item.clause
                  : item;

              const severity =
                typeof item === "object"
                  ? item.severity
                  : null;

              const confidence =
                typeof item === "object"
                  ? item.confidence
                  : null;

              return (
                <div
                  key={index}
                  className="border border-gray-200 rounded-xl p-5 hover:shadow-sm transition"
                >

                  <div className="flex items-start justify-between gap-3">

                    <h3 className="font-bold text-blue-600 text-lg">
                      {clause}
                    </h3>

                    {severity && (
                      <span className="text-xs px-3 py-1 rounded-full bg-gray-100 text-gray-600">
                        {severity}
                      </span>
                    )}

                  </div>

                  {typeof confidence === "number" && (

                    <div className="mt-4">

                      <div className="flex justify-between text-sm mb-2">

                        <span className="text-gray-500">
                          Confidence
                        </span>

                        <span className="font-medium text-gray-700">
                          {(confidence * 100).toFixed(1)}%
                        </span>

                      </div>

                      <div className="w-full bg-gray-200 rounded-full h-2">

                        <div
                          className="bg-blue-500 h-2 rounded-full"
                          style={{
                            width: `${Math.min(
                              Math.max(confidence * 100, 0),
                              100
                            )}%`,
                          }}
                        />

                      </div>

                    </div>

                  )}

                </div>
              );
            })}

          </div>

        )}

      </div>


      {/* Missing Clauses */}

      <div className="bg-white rounded-2xl shadow-md p-8 mt-8">

        <h2 className="text-2xl font-bold text-red-600">
          Missing Clauses
        </h2>

        <p className="mt-1 text-gray-500">
          Clauses that may require attention.
        </p>

        {missingClauses.length === 0 ? (

          <div className="mt-6 bg-green-50 border border-green-200 rounded-xl p-5">

            <p className="text-green-700 font-medium">
              No missing clauses detected 🎉
            </p>

          </div>

        ) : (

          <div className="mt-6 space-y-3">

            {missingClauses.map((item, index) => (

              <div
                key={index}
                className="bg-red-50 border border-red-100 p-4 rounded-xl"
              >

                <p className="text-red-700 font-medium">
                  {typeof item === "object"
                    ? item.clause
                    : item}
                </p>

              </div>

            ))}

          </div>

        )}

      </div>


      {/* Extracted Entities */}

      <div className="bg-white rounded-2xl shadow-md p-8 mt-8">

        <h2 className="text-2xl font-bold text-gray-900">
          Extracted Entities
        </h2>

        <p className="mt-1 text-gray-500">
          Important entities identified in the contract.
        </p>

        {entities.length === 0 ? (

          <div className="mt-6 bg-gray-50 rounded-xl p-6 text-center">

            <p className="text-gray-500">
              No entities detected.
            </p>

          </div>

        ) : (

          <div className="flex flex-wrap gap-3 mt-6">

            {entities.map((entity, index) => (

              <span
                key={index}
                className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full font-medium"
              >

                {typeof entity === "object"
                  ? `${entity.text || ""} (${entity.label || "Entity"})`
                  : entity}

              </span>

            ))}

          </div>

        )}

      </div>


      {/* Recommendations */}

      <div className="bg-white rounded-2xl shadow-md p-8 mt-8">

        <h2 className="text-2xl font-bold text-green-600">
          Recommendations
        </h2>

        <p className="mt-1 text-gray-500">
          Suggested actions based on the contract analysis.
        </p>

        {recommendations.length === 0 ? (

          <div className="mt-6 bg-gray-50 rounded-xl p-6 text-center">

            <p className="text-gray-500">
              No recommendations available.
            </p>

          </div>

        ) : (

          <div className="mt-6 space-y-4">

            {recommendations.map((item, index) => (

              <div
                key={index}
                className="border border-green-100 rounded-xl p-5 bg-green-50"
              >

                <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-3">

                  <h3 className="font-bold text-gray-800 text-lg">
                    {item.clause}
                  </h3>

                  {item.priority && (
                    <span className="inline-flex w-fit px-3 py-1 rounded-full bg-green-200 text-green-800 text-sm font-medium">
                      {item.priority}
                    </span>
                  )}

                </div>

                <p className="mt-3 text-gray-700">
                  {item.message}
                </p>

              </div>

            ))}

          </div>

        )}

      </div>


      {/* Summary */}

      <SummaryCard file={file} />


      {/* AI Chat */}

      <ChatSection />


      {/* Bottom Actions */}

      <div className="mt-10 flex flex-col sm:flex-row justify-center gap-4">

        <button
          onClick={() => navigate("/compare")}
          className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700 transition"
        >
          Compare Contracts
        </button>

        <button
          onClick={() => navigate("/")}
          className="bg-gray-800 text-white px-6 py-3 rounded-lg hover:bg-gray-900 transition"
        >
          Analyze Another Contract
        </button>

      </div>

    </div>
  );
}

export default Dashboard;