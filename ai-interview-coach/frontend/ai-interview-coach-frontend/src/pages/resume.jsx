import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const API = "https://ai-interview-backend-p8gl.onrender.com";

export default function UploadPage() {
  const navigate = useNavigate();
  const [file,    setFile]    = useState(null);
  const [loading, setLoading] = useState(false);
  const [checking,setChecking]= useState(false);
  const [error,   setError]   = useState("");

  function getToken() {
    const token = localStorage.getItem("token");
    if (!token) { setError("Not logged in. Please log in first."); return null; }
    return token;
  }

  // Upload new resume → go to analysis page
  async function handleUpload() {
    setError("");
    if (!file) { setError("Please choose a PDF file first."); return; }
    const token = getToken(); if (!token) return;

    const formData = new FormData();
    formData.append("resume", file);
    setLoading(true);

    try {
      await axios.post(`${API}/resume/upload`, formData, {
        headers: { Authorization: `Bearer ${token}`, "Content-Type": "multipart/form-data" },
      });

      const res = await axios.get(`${API}/resume/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      // Pass analysis data via navigation state
      navigate("/resume/analysis", { state: { data: res.data } });

    } catch (err) {
      const status = err?.response?.status;
      if      (status === 401) setError("Session expired. Please log in again.");
      else if (status === 422) setError("Invalid file. Please upload a valid PDF.");
      else if (status === 404) setError("API endpoint not found. Check backend URL.");
      else                     setError(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  }

  // Fetch previous analysis (if exists) → go to analysis page
  async function handleViewPrevious() {
    setError("");
    const token = getToken(); if (!token) return;
    setChecking(true);

    try {
      const res = await axios.get(`${API}/resume/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      navigate("/resume/analysis", { state: { data: res.data } });
    } catch (err) {
      const status = err?.response?.status;
      if (status === 404) setError("No previous analysis found. Please upload your resume first.");
      else if (status === 401) setError("Session expired. Please log in again.");
      else setError(`Error: ${err.message}`);
    } finally {
      setChecking(false);
    }
  }

  return (
    <div style={{
      minHeight: "100vh", background: "#f0f4ff",
      display: "flex", alignItems: "center", justifyContent: "center",
      fontFamily: "Arial, sans-serif", padding: "24px",
    }}>
      <div style={{
        background: "#fff", borderRadius: "16px", padding: "40px 48px",
        boxShadow: "0 4px 24px rgba(0,0,0,0.08)", maxWidth: "480px", width: "100%",
      }}>
        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: "32px" }}>
          <div style={{ fontSize: "48px", marginBottom: "12px" }}>📄</div>
          <h1 style={{ fontSize: "24px", fontWeight: 700, color: "#111", marginBottom: "8px" }}>
            Resume Analyzer
          </h1>
          <p style={{ fontSize: "13px", color: "#888", lineHeight: 1.6 }}>
            Upload your resume and get an instant AI-powered analysis — ATS score, skill gaps, and recommendations.
          </p>
        </div>

        {/* File picker */}
        <div style={{
          border: "2px dashed #c7d7fa", borderRadius: "10px",
          padding: "24px", textAlign: "center", marginBottom: "20px",
          background: "#f8faff", cursor: "pointer",
        }}>
          <input
            type="file" accept=".pdf" id="resume-file"
            style={{ display: "none" }}
            onChange={(e) => { setFile(e.target.files[0]); setError(""); }}
          />
          <label htmlFor="resume-file" style={{ cursor: "pointer" }}>
            <div style={{ fontSize: "28px", marginBottom: "8px" }}>☁️</div>
            <p style={{ fontSize: "13px", color: "#555", marginBottom: "4px" }}>
              {file ? `✅ ${file.name}` : "Click to select your resume"}
            </p>
            <p style={{ fontSize: "11px", color: "#aaa" }}>PDF files only</p>
          </label>
        </div>

        {/* Error */}
        {error && (
          <div style={{
            padding: "10px 14px", background: "#fce8e8",
            border: "1px solid #f5c6c6", borderRadius: "8px",
            color: "#c0392b", fontSize: "13px", marginBottom: "16px",
          }}>
            ⚠ {error}
          </div>
        )}

        {/* Upload button */}
        <button
          onClick={handleUpload} disabled={loading || checking}
          style={{
            width: "100%", padding: "12px", background: "#2563eb", color: "white",
            border: "none", borderRadius: "9px", fontSize: "14px", fontWeight: 600,
            cursor: loading ? "not-allowed" : "pointer", opacity: loading ? 0.7 : 1,
            marginBottom: "12px",
          }}
        >
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>

        {/* Divider */}
        <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "12px" }}>
          <div style={{ flex: 1, height: "1px", background: "#e0e0e0" }} />
          <span style={{ fontSize: "11px", color: "#aaa" }}>or</span>
          <div style={{ flex: 1, height: "1px", background: "#e0e0e0" }} />
        </div>

        {/* View previous analysis button */}
        <button
          onClick={handleViewPrevious} disabled={loading || checking}
          style={{
            width: "100%", padding: "12px", background: "transparent", color: "#2563eb",
            border: "2px solid #2563eb", borderRadius: "9px", fontSize: "14px", fontWeight: 600,
            cursor: checking ? "not-allowed" : "pointer", opacity: checking ? 0.7 : 1,
          }}
        >
          {checking ? "Checking..." : "📊 View Previous Analysis"}
        </button>

        {/* Back to dashboard */}
        <p style={{ textAlign: "center", marginTop: "20px" }}>
          <button
            onClick={() => navigate("/")}
            style={{
              background: "none", border: "none", color: "#888",
              fontSize: "12px", cursor: "pointer", textDecoration: "underline",
            }}
          >
            ← Back to Dashboard
          </button>
        </p>
      </div>
    </div>
  );
}
