export default function Bar({ label, value }) {
  const color = value >= 75 ? "#22c55e" : value >= 55 ? "#f59e0b" : "#ef4444";
  return (
    <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "7px" }}>
      <span style={{ fontSize: "11px", color: "#666", width: "90px", flexShrink: 0 }}>{label}</span>
      <div style={{ flex: 1, height: "5px", background: "#e0e0e0", borderRadius: "3px", overflow: "hidden" }}>
        <div style={{ width: `${value}%`, height: "100%", background: color, borderRadius: "3px" }} />
      </div>
      <span style={{ fontSize: "11px", fontWeight: 700, color, minWidth: "26px", textAlign: "right" }}>
        {value}
      </span>
    </div>
  );
}
