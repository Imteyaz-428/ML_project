import Card from "../ui/Card";

export default function EducationSection({ education }) {
  if (!education || education.length === 0) return null;

  return (
    <Card title="Education">
      {education.map((edu, i) => (
        <div key={i} style={{ marginBottom: i < education.length - 1 ? "12px" : 0 }}>
          <p style={{ fontSize: "13px", fontWeight: 700, color: "#111" }}>{edu.degree}</p>
          <p style={{ fontSize: "12px", color: "#555", marginTop: "2px" }}>{edu.institution}</p>
          <p style={{ fontSize: "11px", color: "#aaa", marginTop: "3px" }}>
            {edu.performance} · Passing: {edu.year_of_passing}
          </p>
        </div>
      ))}
    </Card>
  );
}
