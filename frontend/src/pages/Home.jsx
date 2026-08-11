import { useState } from "react";
import { useNavigate } from "react-router-dom";

import UploadCard from "../components/UploadCard";

function Home() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);

  const handleAnalysisComplete = (result, uploadedFile) => {
    setFile(uploadedFile);

    navigate("/dashboard", {
      state: {
        result: result,
        file: uploadedFile,
      },
    });
  };

  return (
    <div className="min-h-[calc(100vh-80px)] bg-gradient-to-b from-blue-50 via-white to-white">

      {/* Hero Section */}
      <section className="max-w-6xl mx-auto px-6 pt-16 pb-12">

        <div className="text-center">

          <div className="inline-flex items-center px-4 py-2 rounded-full bg-blue-100 text-blue-700 text-sm font-semibold mb-6">
            AI-Powered Contract Analysis
          </div>

          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 leading-tight">
            Understand Your Contracts
            <span className="block text-blue-600">
              With AI
            </span>
          </h1>

          <p className="mt-6 text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Analyze contracts for risks, detect important clauses,
            extract legal entities, generate summaries, and ask
            questions using AI.
          </p>

        </div>

      </section>


      {/* Upload Section */}
      <section className="max-w-6xl mx-auto px-6 pb-16">

        <UploadCard
          onAnalysisComplete={handleAnalysisComplete}
          setFile={setFile}
        />

      </section>


      {/* Features Section */}
      <section className="max-w-6xl mx-auto px-6 pb-20">

        <div className="text-center mb-10">

          <h2 className="text-3xl font-bold text-gray-900">
            Everything You Need to Analyze Contracts
          </h2>

          <p className="mt-3 text-gray-600">
            One platform for intelligent contract analysis.
          </p>

        </div>


        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

          <div className="bg-white rounded-2xl shadow-sm border p-6 hover:shadow-md transition">

            <div className="w-12 h-12 rounded-xl bg-red-100 flex items-center justify-center text-2xl mb-4">
              ⚠️
            </div>

            <h3 className="text-lg font-bold text-gray-900">
              Risk Analysis
            </h3>

            <p className="mt-2 text-gray-600 text-sm leading-relaxed">
              Identify contract risks and receive an overall risk
              score and risk level.
            </p>

          </div>


          <div className="bg-white rounded-2xl shadow-sm border p-6 hover:shadow-md transition">

            <div className="w-12 h-12 rounded-xl bg-blue-100 flex items-center justify-center text-2xl mb-4">
              📄
            </div>

            <h3 className="text-lg font-bold text-gray-900">
              Clause Detection
            </h3>

            <p className="mt-2 text-gray-600 text-sm leading-relaxed">
              Detect important clauses and identify missing contract
              provisions.
            </p>

          </div>


          <div className="bg-white rounded-2xl shadow-sm border p-6 hover:shadow-md transition">

            <div className="w-12 h-12 rounded-xl bg-green-100 flex items-center justify-center text-2xl mb-4">
              📝
            </div>

            <h3 className="text-lg font-bold text-gray-900">
              AI Summary
            </h3>

            <p className="mt-2 text-gray-600 text-sm leading-relaxed">
              Generate a concise AI-powered summary of your contract.
            </p>

          </div>


          <div className="bg-white rounded-2xl shadow-sm border p-6 hover:shadow-md transition">

            <div className="w-12 h-12 rounded-xl bg-purple-100 flex items-center justify-center text-2xl mb-4">
              ⚖️
            </div>

            <h3 className="text-lg font-bold text-gray-900">
              Compare Contracts
            </h3>

            <p className="mt-2 text-gray-600 text-sm leading-relaxed">
              Compare two contracts and identify differences in risk
              and clauses.
            </p>

          </div>

        </div>

      </section>


      {/* How It Works */}
      <section className="bg-gray-50 border-t">

        <div className="max-w-6xl mx-auto px-6 py-16">

          <div className="text-center mb-10">

            <h2 className="text-3xl font-bold text-gray-900">
              How It Works
            </h2>

            <p className="mt-3 text-gray-600">
              Analyze a contract in three simple steps.
            </p>

          </div>


          <div className="grid md:grid-cols-3 gap-8">

            <div className="text-center">

              <div className="mx-auto w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg">
                1
              </div>

              <h3 className="mt-4 text-lg font-bold">
                Upload
              </h3>

              <p className="mt-2 text-gray-600">
                Upload your PDF contract to the platform.
              </p>

            </div>


            <div className="text-center">

              <div className="mx-auto w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg">
                2
              </div>

              <h3 className="mt-4 text-lg font-bold">
                Analyze
              </h3>

              <p className="mt-2 text-gray-600">
                AI analyzes clauses, risks, and legal entities.
              </p>

            </div>


            <div className="text-center">

              <div className="mx-auto w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg">
                3
              </div>

              <h3 className="mt-4 text-lg font-bold">
                Understand
              </h3>

              <p className="mt-2 text-gray-600">
                Review the results, summary, recommendations,
                and ask questions.
              </p>

            </div>

          </div>

        </div>

      </section>


      {/* Bottom CTA */}
      <section className="max-w-4xl mx-auto px-6 py-16 text-center">

        <h2 className="text-3xl font-bold text-gray-900">
          Ready to Analyze a Contract?
        </h2>

        <p className="mt-3 text-gray-600">
          Upload a PDF and let AI help you understand the risks.
        </p>

        <button
          onClick={() =>
            window.scrollTo({
              top: 0,
              behavior: "smooth",
            })
          }
          className="mt-6 bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition"
        >
          Analyze Contract
        </button>

      </section>

    </div>
  );
}

export default Home;