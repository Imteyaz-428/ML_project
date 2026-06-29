import Card from "../ui/Card";
import Pill from "../ui/Pill";

export default function SkillsSection({ skills, missingSkills }) {
  return (
    <Card title="Skills">
      <div style={{ marginBottom: "10px" }}>
        {(skills || []).map((s, i) => (
          <Pill key={i} text={s} bg="#e8f0fe" color="#1565c0" />
        ))}
      </div>

      {(missingSkills || []).length > 0 && (
        <>
          <p style={{
            fontSize: "10px", fontWeight: 700, color: "#aaa",
            textTransform: "uppercase", letterSpacing: "0.06em", margin: "10px 0 6px",
          }}>
            Missing for Target Role
          </p>
          <div>
            {missingSkills.map((s, i) => (
              <Pill key={i} text={s} bg="#fce8e8" color="#c0392b" />
            ))}
          </div>
        </>
      )}
    </Card>
  );
}
