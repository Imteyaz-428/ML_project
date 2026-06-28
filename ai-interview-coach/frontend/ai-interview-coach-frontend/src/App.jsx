import { BrowserRouter, Routes, Route } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import Resume from "./pages/resume";
import Report from "./pages/report";
import Interview from "./pages/interview";
import InterviewSetup from "./pages/interviewSetUp";
import Profile from "./pages/profile";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/register" element={<Register />} />
        <Route path="/" element={<Dashboard />} />
        <Route
            path="/profile"
            element={<Profile />}
        />

        <Route path="/login" element={<Login />} />

        <Route path="/resume" element={<Resume />} />

        <Route
          path="/interview-setup"
          element={<InterviewSetup />}
        />

        <Route
          path="/interview/:id"
          element={<Interview />}
        />

        <Route
          path="/report/:id"
          element={<Report />}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;