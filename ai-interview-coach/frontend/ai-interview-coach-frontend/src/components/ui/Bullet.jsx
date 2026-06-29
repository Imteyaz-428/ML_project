export default function Bullet({ text, color = "#444" }) {
  return (
    <p style={{
      fontSize: "12px", color, marginBottom: "5px",
      paddingLeft: "14px", position: "relative", lineHeight: 1.6,
    }}>
      <span style={{ position: "absolute", left: 0, fontWeight: 700 }}>·</span>
      {text}
    </p>
  );
}
