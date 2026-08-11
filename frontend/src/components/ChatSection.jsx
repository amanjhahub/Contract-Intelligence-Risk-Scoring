import { useState } from "react";
import API from "../services/api";

function ChatSection() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askQuestion = async () => {
    if (!question.trim() || loading) {
      return;
    }

    try {
      setLoading(true);
      setError("");
      setAnswer("");
      setSources([]);

      const response = await API.post(
        `/ask?question=${encodeURIComponent(question.trim())}`
      );

      console.log("AI ANSWER:", response.data);

      setAnswer(
        response.data?.answer ||
        "No answer was returned."
      );

      setSources(
        Array.isArray(response.data?.sources)
          ? response.data.sources
          : []
      );

    } catch (error) {
      console.error("ASK ERROR:", error);

      if (error.response) {
        console.error(
          "Backend response:",
          error.response.data
        );
      }

      setAnswer("");
      setSources([]);

      setError(
        error.response?.data?.detail ||
        error.response?.data?.message ||
        "Unable to get an answer. Please try again."
      );

    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      askQuestion();
    }
  };

  const clearChat = () => {
    setQuestion("");
    setAnswer("");
    setSources([]);
    setError("");
  };

  return (
    <div className="bg-white rounded-2xl shadow-md p-8 mt-8">

      {/* Header */}

      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">

        <div>

          <div className="flex items-center gap-3">

            <div className="w-12 h-12 rounded-xl bg-purple-100 flex items-center justify-center text-2xl">
              🤖
            </div>

            <h2 className="text-2xl font-bold text-gray-900">
              Ask Contract AI
            </h2>

          </div>

          <p className="text-gray-500 mt-3">
            Ask questions about the analyzed contract.
          </p>

        </div>

        {(answer || question) && (
          <button
            onClick={clearChat}
            disabled={loading}
            className="text-sm text-gray-500 hover:text-red-600 transition"
          >
            Clear
          </button>
        )}

      </div>


      {/* Question Input */}

      <div className="mt-6">

        <label className="block text-sm font-medium text-gray-700 mb-2">
          Your Question
        </label>

        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyDown}
          rows="3"
          placeholder="Example: What is the termination clause?"
          disabled={loading}
          className="w-full border border-gray-300 rounded-xl p-4 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent disabled:bg-gray-100"
        />

        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mt-3">

          <p className="text-xs text-gray-400">
            Press Enter to ask
          </p>

          <button
            onClick={askQuestion}
            disabled={loading || !question.trim()}
            className="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
          >

            {loading
              ? "Thinking..."
              : "Ask AI"}

          </button>

        </div>

      </div>


      {/* Loading */}

      {loading && (

        <div className="mt-6 bg-blue-50 border border-blue-100 rounded-xl p-5">

          <div className="flex items-center gap-3">

            <div className="animate-pulse text-xl">
              🤖
            </div>

            <p className="text-blue-700 text-sm">
              AI is searching the contract for an answer...
            </p>

          </div>

        </div>

      )}


      {/* Error */}

      {error && !loading && (

        <div className="mt-6 bg-red-50 border border-red-100 rounded-xl p-5">

          <p className="text-red-700 text-sm">
            {error}
          </p>

        </div>

      )}


      {/* Answer */}

      {answer && !loading && (

        <div className="mt-6 bg-gray-50 border border-gray-200 rounded-2xl p-6">

          <div className="flex items-center gap-3 mb-4">

            <div className="w-9 h-9 rounded-full bg-blue-100 flex items-center justify-center">
              🤖
            </div>

            <h3 className="font-bold text-lg text-gray-900">
              AI Answer
            </h3>

          </div>

          <div className="border-t border-gray-200 pt-4">

            <p className="text-gray-700 leading-7 whitespace-pre-line">
              {answer}
            </p>

          </div>

        </div>

      )}


      {/* Sources */}

      {sources.length > 0 && !loading && (

        <div className="mt-6">

          <h3 className="font-bold text-gray-900">
            Sources
          </h3>

          <p className="text-sm text-gray-500 mt-1">
            Relevant contract sections used to answer the question.
          </p>

          <div className="flex flex-wrap gap-2 mt-4">

            {sources.map((source, index) => (

              <span
                key={index}
                className="bg-blue-100 text-blue-700 px-3 py-2 rounded-lg text-sm"
              >
                {typeof source === "object"
                  ? source.text ||
                    source.content ||
                    JSON.stringify(source)
                  : source}
              </span>

            ))}

          </div>

        </div>

      )}

    </div>
  );
}

export default ChatSection;