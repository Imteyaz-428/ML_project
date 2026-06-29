import Card from "../ui/Card";
import Bar from "../ui/Bar";

export default function ATSSection({ ats }) {
  return (
    <Card title="ATS Breakdown">
      <Bar label="Skills"     value={ats.skills     ?? 0} />
      <Bar label="Projects"   value={ats.projects   ?? 0} />
      <Bar label="Experience" value={ats.experience ?? 0} />
      <Bar label="Education"  value={ats.education  ?? 0} />
      <Bar label="Keywords"   value={ats.keywords   ?? 0} />
      <Bar label="Formatting" value={ats.formatting ?? 0} />
    </Card>
  );
}
