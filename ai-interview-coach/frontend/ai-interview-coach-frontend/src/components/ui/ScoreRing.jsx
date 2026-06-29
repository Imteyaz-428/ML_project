export default function ScoreRing({ score, color = "#1976d2", label = "Resume Score" }) {
  const r = 28;
  const circ = 2 * Math.PI * r;
  const filled = circ * (score / 100);
  return (
    <div style={{ textAlign: "center", minWidth: "80px" }}>
      <svg width="76" height="76" viewBox="0 0 72 72">
        <circle cx="36" cy="36" r={r} fill="none" stroke="#e0e0e0" strokeWidth="6" />
        <circle
          cx="36" cy="36" r={r} fill="none" stroke={color} strokeWidth="6"
          strokeDasharray={`${filled} ${circ - filled}`}
          strokeLinecap="round" transform="rotate(-90 36 36)"
        />
        <text x="36" y="41" textAnchor="middle" fontSize="14" fontWeight="700" fill={color}>
          {score}
        </text>
      </svg>
      <p style={{ fontSize: "10px", color: "#aaa", marginTop: "2px" }}>{label}</p>
    </div>
  );
}
