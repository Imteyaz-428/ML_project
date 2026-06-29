import Card from "../ui/Card";
import Bullet from "../ui/Bullet";

export default function InsightsSection({ strengths, weaknesses, recommendations }) {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "12px" }}>
      <Card title="Strengths">
        {(strengths || []).map((s, i) => <Bullet key={i} text={s} color="#16a34a" />)}
      </Card>
      <Card title="Weaknesses">
        {(weaknesses || []).map((w, i) => <Bullet key={i} text={w} color="#dc2626" />)}
      </Card>
      <Card title="Recommendations">
        {(recommendations || []).map((r, i) => <Bullet key={i} text={r} color="#1976d2" />)}
      </Card>
    </div>
  );
}
