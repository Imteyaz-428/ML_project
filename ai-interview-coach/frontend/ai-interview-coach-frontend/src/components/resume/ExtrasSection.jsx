import Card from "../ui/Card";
import Bullet from "../ui/Bullet";
import Pill from "../ui/Pill";

export default function ExtrasSection({ achievements, certifications }) {
  const hasA = achievements   && achievements.length   > 0;
  const hasC = certifications && certifications.length > 0;
  if (!hasA && !hasC) return null;

  return (
    <div style={{ display: "grid", gridTemplateColumns: hasA && hasC ? "1fr 1fr" : "1fr", gap: "12px" }}>
      {hasA && (
        <Card title="Achievements">
          {achievements.map((a, i) => <Bullet key={i} text={a} color="#7c3aed" />)}
        </Card>
      )}
      {hasC && (
        <Card title="Certifications">
          {certifications.map((c, i) => (
            <Pill key={i} text={c} bg="#f0fdf4" color="#166534" />
          ))}
        </Card>
      )}
    </div>
  );
}
