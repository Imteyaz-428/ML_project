export default function Tag({ text }) {
  return (
    <span style={{
      display: "inline-block", fontSize: "10px", padding: "2px 7px",
      margin: "2px", background: "#efefef", color: "#444",
      borderRadius: "4px", border: "1px solid #ddd",
    }}>
      {text}
    </span>
  );
}
