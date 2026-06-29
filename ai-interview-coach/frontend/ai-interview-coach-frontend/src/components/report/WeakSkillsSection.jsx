import Card from "../ui/Card";
import Pill from "../ui/Pill";

export default function WeakSkillsSection({ weakSkills }) {
  if (!weakSkills || weakSkills.length === 0) return null;

  return (
    <Card title="Skills to Improve">
      <div>
        {weakSkills.map((skill, i) => (
          <Pill key={i} text={skill} bg="#fff7ed" color="#c2410c" />
        ))}
      </div>
    </Card>
  );
}
