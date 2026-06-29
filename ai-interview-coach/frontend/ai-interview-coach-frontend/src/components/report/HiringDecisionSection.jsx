import Card from "../ui/Card";

const DECISION_STYLES = {
  "Strong Hire": { bg: "#dcfce7", color: "#15803d", border: "#86efac", emoji: "🚀" },
  "Hire":        { bg: "#dbeafe", color: "#1d4ed8", border: "#93c5fd", emoji: "✅" },
  "Maybe":       { bg: "#fef9c3", color: "#a16207", border: "#fde047", emoji: "🤔" },
  "No Hire":     { bg: "#fee2e2", color: "#b91c1c", border: "#fca5a5", emoji: "❌" },
};

export default function HiringDecisionSection({ hiringDecision, hiringJustification, performance }) {
  if (!hiringDecision) return null;

  const style = DECISION_STYLES[hiringDecision] || { bg: "#f3f4f6", color: "#374151", border: "#d1d5db", emoji: "📋" };

  return (
    <Card title="Hiring Decision">
      {/* Decision badge */}
      <div style={{
        display: "inline-flex", alignItems: "center", gap: "8px",
        padding: "10px 20px", borderRadius: "10px",
        background: style.bg, border: `2px solid ${style.border}`,
        marginBottom: "12px",
      }}>
        <span style={{ fontSize: "20px" }}>{style.emoji}</span>
        <span style={{ fontSize: "18px", fontWeight: 700, color: style.color }}>
          {hiringDecision}
        </span>
      </div>

      {/* Justification */}
      {hiringJustification && (
        <p style={{ fontSize: "13px", color: "#444", lineHeight: 1.6, marginBottom: "8px" }}>
          <strong>Reason:</strong> {hiringJustification}
        </p>
      )}

      {/* Performance summary */}
      {performance && (
        <p style={{ fontSize: "12px", color: "#666", lineHeight: 1.6, margin: 0 }}>
          {performance}
        </p>
      )}
    </Card>
  );
}
