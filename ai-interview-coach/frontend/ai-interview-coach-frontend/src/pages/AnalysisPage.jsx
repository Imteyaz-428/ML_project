import { useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import HeroSection       from "../components/resume/HeroSection";
import ATSSection        from "../components/resume/ATSSection";
import DomainSection     from "../components/resume/DomainSection";
import SkillsSection     from "../components/resume/SkillsSection";
import ExperienceSection from "../components/resume/ExperienceSection";
import EducationSection  from "../components/resume/EducationSection";
import ProjectsSection   from "../components/resume/ProjectsSection";
import InsightsSection   from "../components/resume/InsightsSection";
import ExtrasSection     from "../components/resume/ExtrasSection";

export default function AnalysisPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const reportRef = useRef(null);
  const [downloading, setDownloading] = useState(false);

  // Backend GET /resume/me returns { resume_path, analysis }
  const raw = location.state?.data;
  const d = raw?.analysis ?? raw?.parsed_data ?? raw;

  // No data → show message
  if (!d) {
    return (
      <div style={{ textAlign: "center", marginTop: "100px", fontFamily: "Arial" }}>
        <p>No analysis found.</p>
        <button onClick={() => navigate("/resume")}
          style={{ marginTop: "16px", padding: "10px 24px", background: "#2563eb", color: "#fff", border: "none", borderRadius: "8px", cursor: "pointer" }}>
          Upload Resume
        </button>
      </div>
    );
  }

  // Download PDF
  async function handleDownload() {
    try {
      setDownloading(true);
      const [{ default: html2canvas }, { default: jsPDF }] = await Promise.all([
        import("html2canvas"),
        import("jspdf"),
      ]);
      const canvas = await html2canvas(reportRef.current, { scale: 2, useCORS: true, backgroundColor: "#ffffff" });
      const pdf = new jsPDF({ orientation: "portrait", unit: "mm", format: "a4" });
      const pageW = pdf.internal.pageSize.getWidth();
      const pageH = pdf.internal.pageSize.getHeight();
      const imgH = (canvas.height * pageW) / canvas.width;
      let y = 0;
      while (y < imgH) {
        if (y > 0) pdf.addPage();
        pdf.addImage(canvas.toDataURL("image/png"), "PNG", 0, -y, pageW, imgH);
        y += pageH;
      }
      pdf.save(`Resume_Analysis_${d.candidate_name || "Report"}.pdf`);
    } catch {
      alert("Run: npm install html2canvas jspdf");
    } finally {
      setDownloading(false);
    }
  }

  return (
    <div style={{ padding: "24px", fontFamily: "Arial, sans-serif", maxWidth: "980px", margin: "0 auto" }}>

      {/* Top bar — NOT inside reportRef so it won't appear in PDF */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "24px" }}>
        <div>
          <h1 style={{ fontSize: "26px", color: "#2563eb", marginBottom: "4px" }}>📊 Resume Analysis</h1>
          <p style={{ color: "#888", fontSize: "13px" }}>AI-powered breakdown of your resume</p>
        </div>
        <div style={{ display: "flex", gap: "10px" }}>
          <button onClick={handleDownload} disabled={downloading}
            style={{ padding: "9px 18px", background: downloading ? "#86efac" : "#16a34a", color: "#fff", border: "none", borderRadius: "8px", cursor: "pointer", fontWeight: 600, fontSize: "13px" }}>
            {downloading ? "⏳ Generating..." : "⬇ Download PDF"}
          </button>
          <button onClick={() => navigate("/resume")}
            style={{ padding: "9px 18px", background: "transparent", color: "#2563eb", border: "2px solid #2563eb", borderRadius: "8px", cursor: "pointer", fontWeight: 600, fontSize: "13px" }}>
            ↑ Upload New
          </button>
          <button onClick={() => navigate("/")}
            style={{ padding: "9px 18px", background: "#2563eb", color: "#fff", border: "none", borderRadius: "8px", cursor: "pointer", fontWeight: 600, fontSize: "13px" }}>
            🏠 Dashboard
          </button>
        </div>
      </div>

      {/* Report — ref captures this for PDF */}
      <div ref={reportRef} style={{ background: "#fff", padding: "8px", display: "flex", flexDirection: "column", gap: "12px" }}>

        <HeroSection d={d} />

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
          <ATSSection    ats={d.ats_score      || {}} />
          <DomainSection domains={d.domain_scores || []} />
        </div>

        <SkillsSection skills={d.skills || []} missingSkills={d.missing_skills || []} />

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
          <ExperienceSection experience={d.experience || []} />
          <EducationSection  education={d.education   || []} />
        </div>

        <ProjectsSection projects={d.projects || []} />

        <InsightsSection
          strengths={d.strengths             || []}
          weaknesses={d.weaknesses           || []}
          recommendations={d.recommendations || []}
        />

        <ExtrasSection achievements={d.achievements || []} certifications={d.certifications || []} />

      </div>
    </div>
  );
}