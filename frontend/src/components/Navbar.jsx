import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-white shadow-sm">

      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">

        <Link
          to="/"
          className="text-2xl font-bold text-blue-600"
        >
          AI Contract Intelligence
        </Link>

        <div className="flex gap-6 text-gray-700">

          <Link
            to="/"
            className="hover:text-blue-600"
          >
            Home
          </Link>

          <Link
            to="/dashboard"
            className="hover:text-blue-600"
          >
            Dashboard
          </Link>

          <Link
            to="/compare"
            className="hover:text-blue-600"
          >
            Compare
          </Link>

          <Link
            to="/about"
            className="hover:text-blue-600"
          >
            About
          </Link>

        </div>

      </div>

    </nav>
  );
}

export default Navbar;