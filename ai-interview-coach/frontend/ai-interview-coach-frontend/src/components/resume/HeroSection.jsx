import Pill from "../ui/Pill";
import ScoreRing from "../ui/ScoreRing";

const LEVEL_STYLES = {
  "Fresher":    { bg: "#e8f5e9", color: "#2e7d32" },
  "Junior":     { bg: "#e3f2fd", color: "#1565c0" },
  "Mid-Level":  { bg: "#fff8e1", color: "#f57f17" },
  "Senior":     { bg: "#fce4ec", color: "#b71c1c" },
  "Staff/Lead": { bg: "#ede7f6", color: "#4527a0" },
};

export default function HeroSection({ d }) {
  const ls = LEVEL_STYLES[d.candidate_level] || { bg: "#eee", color: "#333" };

  return (
    <div style={{
      display: "flex", justifyContent: "space-between", alignItems: "flex-start",
      gap: "20px", paddingBottom: "16px", marginBottom: "14px",
      borderBottom: "1px solid #e0e0e0",
    }}>
      <div style={{ flex: 1 }}>
        <h2 style={{ fontSize: "22px", fontWeight: 700, marginBottom: "8px", color: "#111" }}>
          {d.candidate_name || "Candidate"}
        </h2>

        <div style={{ display: "flex", flexWrap: "wrap", gap: "6px", marginBottom: "12px" }}>
          <Pill text={d.candidate_level || "Unknown"} bg={ls.bg} color={ls.color} />
          <Pill text={`⭐ ${d.primary_domain || "Unknown Domain"}`} bg="#fff8e1" color="#b45309" />
          <Pill text={`🎯 ${d.target_role   || "Not specified"}`}  bg="#f0f9ff" color="#0369a1" />
        </div>

        <p style={{ fontSize: "13px", color: "#555", lineHeight: 1.7, maxWidth: "560px" }}>
          {d.summary}
        </p>
      </div>

      <ScoreRing score={d.resume_score ?? 0} />
    </div>
  );
}
