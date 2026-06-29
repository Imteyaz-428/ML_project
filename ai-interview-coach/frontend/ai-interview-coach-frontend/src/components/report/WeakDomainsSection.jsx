import Card from "../ui/Card";
import Pill from "../ui/Pill";

export default function WeakDomainsSection({ weakDomains }) {
  if (!weakDomains || weakDomains.length === 0) return null;

  return (
    <Card title="Weak Domains">
      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        {weakDomains.map((item, i) => (
          <div key={i} style={{ display: "flex", alignItems: "flex-start", gap: "10px" }}>
            <Pill text={item.domain} bg="#fce8e8" color="#c0392b" />
            <p style={{ fontSize: "12px", color: "#555", lineHeight: 1.6, margin: 0, paddingTop: "4px" }}>
              {item.gap}
            </p>
          </div>
        ))}
      </div>
    </Card>
  );
}
