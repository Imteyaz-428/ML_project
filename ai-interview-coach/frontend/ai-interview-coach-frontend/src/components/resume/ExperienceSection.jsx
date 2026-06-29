import Card from "../ui/Card";
import Bullet from "../ui/Bullet";

export default function ExperienceSection({ experience }) {
  if (!experience || experience.length === 0) return null;

  return (
    <Card title="Experience">
      {experience.map((exp, i) => (
        <div key={i} style={{
          marginBottom: i < experience.length - 1 ? "14px" : 0,
          paddingBottom: i < experience.length - 1 ? "14px" : 0,
          borderBottom: i < experience.length - 1 ? "1px solid #eee" : "none",
        }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <span style={{ fontSize: "13px", fontWeight: 700, color: "#111" }}>{exp.company}</span>
            <span style={{ fontSize: "10px", color: "#aaa" }}>{exp.duration}</span>
          </div>

          <p style={{ fontSize: "11px", color: "#777", margin: "3px 0 7px" }}>{exp.role}</p>

          {(exp.description || []).map((line, j) => (
            <Bullet key={j} text={line} color="#1565c0" />
          ))}
        </div>
      ))}
    </Card>
  );
}
