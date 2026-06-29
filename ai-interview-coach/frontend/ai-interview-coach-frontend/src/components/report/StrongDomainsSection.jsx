import Card from "../ui/Card";
import Pill from "../ui/Pill";

export default function StrongDomainsSection({ strongDomains }) {
  if (!strongDomains || strongDomains.length === 0) return null;

  return (
    <Card title="Strong Domains">
      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        {strongDomains.map((item, i) => (
          <div key={i} style={{ display: "flex", alignItems: "flex-start", gap: "10px" }}>
            <Pill text={item.domain} bg="#e8f0fe" color="#1565c0" />
            <p style={{ fontSize: "12px", color: "#555", lineHeight: 1.6, margin: 0, paddingTop: "4px" }}>
              {item.reason}
            </p>
          </div>
        ))}
      </div>
    </Card>
  );
}
