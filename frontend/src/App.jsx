import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import NotFound from "./pages/NotFound";
import Compare from "./pages/Compare";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <main className="min-h-screen bg-gray-50 py-10">

        <Routes>

          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/dashboard"
            element={<Dashboard />}
          />

          <Route
            path="/compare"
            element={<Compare />}
          />

          <Route
            path="/about"
            element={
              <div className="max-w-4xl mx-auto px-6 py-12">

                <h1 className="text-4xl font-bold text-gray-900">
                  About AI Contract Intelligence
                </h1>

                <p className="mt-5 text-gray-600 text-lg">
                  AI Contract Intelligence is an AI-powered system
                  designed to analyze contracts, identify potential
                  risks, detect important clauses, extract legal
                  entities, generate summaries, compare contracts,
                  and answer questions about contract content.
                </p>

              </div>
            }
          />

          <Route
            path="*"
            element={<NotFound />}
          />

        </Routes>

      </main>

    </BrowserRouter>
  );
}

export default App;