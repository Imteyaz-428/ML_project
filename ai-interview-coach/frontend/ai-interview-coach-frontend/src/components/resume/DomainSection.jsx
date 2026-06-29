import Card from "../ui/Card";
import Bar from "../ui/Bar";
import Tag from "../ui/Tag";
import Divider from "../ui/Divider";

export default function DomainSection({ domains }) {
  if (!domains || domains.length === 0) return null;

  return (
    <Card title="Domain Strength">
      {domains.map((d, i) => (
        <div key={i} style={{ marginBottom: "10px" }}>
          <Bar label={d.domain} value={d.score ?? 0} />

          {d.evidence && (
            <p style={{
              fontSize: "10px", color: "#999",
              marginLeft: "98px", marginTop: "-4px", marginBottom: "3px", lineHeight: 1.4,
            }}>
              {d.evidence}
            </p>
          )}

          {(d.missing_skills || []).length > 0 && (
            <div style={{ marginLeft: "98px" }}>
              {d.missing_skills.map((s, j) => <Tag key={j} text={s} />)}
            </div>
          )}

          {i < domains.length - 1 && <Divider />}
        </div>
      ))}
    </Card>
  );
}
