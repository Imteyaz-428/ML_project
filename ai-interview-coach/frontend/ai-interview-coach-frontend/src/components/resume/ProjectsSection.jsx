import Card from "../ui/Card";
import Bullet from "../ui/Bullet";
import Tag from "../ui/Tag";

export default function ProjectsSection({ projects }) {
  if (!projects || projects.length === 0) return null;

  return (
    <Card title="Projects">
      {projects.map((proj, i) => (
        <div key={i} style={{
          marginBottom: i < projects.length - 1 ? "16px" : 0,
          paddingBottom: i < projects.length - 1 ? "16px" : 0,
          borderBottom: i < projects.length - 1 ? "1px solid #eee" : "none",
        }}>
          <p style={{ fontSize: "13px", fontWeight: 700, color: "#111", marginBottom: "5px" }}>
            {proj.name}
          </p>

          {(proj.description || []).map((line, j) => <Bullet key={j} text={line} />)}

          {proj.impact && (
            <p style={{ fontSize: "11px", color: "#16a34a", margin: "5px 0 5px 14px", lineHeight: 1.5 }}>
              🎯 {proj.impact}
            </p>
          )}

          <div style={{ marginTop: "6px" }}>
            {(proj.technologies || []).map((t, j) => <Tag key={j} text={t} />)}
          </div>
        </div>
      ))}
    </Card>
  );
}
