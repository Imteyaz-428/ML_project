export default function Card({ title, children, style = {} }) {
  return (
    <div style={{
      background: "#f9f9f9", borderRadius: "10px",
      padding: "14px 16px", border: "1px solid #e0e0e0", ...style,
    }}>
      {title && (
        <p style={{
          fontSize: "10px", fontWeight: 700, color: "#aaa",
          textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: "12px",
        }}>
          {title}
        </p>
      )}
      {children}
    </div>
  );
}
