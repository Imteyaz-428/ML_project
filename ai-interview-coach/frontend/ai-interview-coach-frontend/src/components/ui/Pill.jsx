export default function Pill({ text, bg = "#e8f0fe", color = "#1976d2" }) {
  return (
    <span style={{
      display: "inline-block", padding: "3px 10px", margin: "3px",
      background: bg, color, borderRadius: "20px",
      fontSize: "11px", fontWeight: 600,
    }}>
      {text}
    </span>
  );
}
