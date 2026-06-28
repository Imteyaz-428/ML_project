import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

// ═══════════════════════════════════════════════════════
//  REUSABLE SMALL COMPONENTS
// ═══════════════════════════════════════════════════════

// Colored pill badge
function Pill({ text, bg = "#e8f0fe", color = "#1976d2" }) {
  return (
    <span style={{
      display: "inline-block", padding: "3px 10px", margin: "3px",
      background: bg, color, borderRadius: "20px",
      fontSize: "11px", fontWeight: 600,
    }}>
      {text}
    </span>
  );
}

// Small gray tech tag
function Tag({ text }) {
  return (
    <span style={{
      display: "inline-block", fontSize: "10px", padding: "2px 7px",
      margin: "2px", background: "#efefef", color: "#444",
      borderRadius: "4px", border: "1px solid #ddd",
    }}>
      {text}
    </span>
  );
}

// Bullet point line
function Bullet({ text, color = "#444" }) {
  return (
    <p style={{
      fontSize: "12px", color, marginBottom: "5px",
      paddingLeft: "14px", position: "relative", lineHeight: 1.6,
    }}>
      <span style={{ position: "absolute", left: 0, fontWeight: 700 }}>·</span>
      {text}
    </p>
  );
}

// Card box with title
function Card({ title, children, style = {} }) {
  return (
    <div style={{
      background: "#f9f9f9", borderRadius: "10px",
      padding: "14px 16px", border: "1px solid #e0e0e0", ...style,
    }}>
      {title && (
        <p style={{
          fontSize: "10px", fontWeight: 700, color: "#aaa",
          textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: "12px",
        }}>
          {title}
        </p>
      )}
      {children}
    </div>
  );
}

// Horizontal score bar
function Bar({ label, value }) {
  const color = value >= 75 ? "#22c55e" : value >= 55 ? "#f59e0b" : "#ef4444";
  return (
    <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "7px" }}>
      <span style={{ fontSize: "11px", color: "#666", width: "90px", flexShrink: 0 }}>{label}</span>
      <div style={{ flex: 1, height: "5px", background: "#e0e0e0", borderRadius: "3px", overflow: "hidden" }}>
        <div style={{ width: `${value}%`, height: "100%", background: color, borderRadius: "3px" }} />
      </div>
      <span style={{ fontSize: "11px", fontWeight: 700, color, minWidth: "26px", textAlign: "right" }}>
        {value}
      </span>
    </div>
  );
}

// SVG donut ring (score circle)
function ScoreRing({ score, color = "#1976d2", label = "Resume Score" }) {
  const r = 28;
  const circ = 2 * Math.PI * r;
  const filled = circ * (score / 100);
  return (
    <div style={{ textAlign: "center", minWidth: "80px" }}>
      <svg width="76" height="76" viewBox="0 0 72 72">
        <circle cx="36" cy="36" r={r} fill="none" stroke="#e0e0e0" strokeWidth="6" />
        <circle
          cx="36" cy="36" r={r} fill="none" stroke={color} strokeWidth="6"
          strokeDasharray={`${filled} ${circ - filled}`}
          strokeLinecap="round" transform="rotate(-90 36 36)"
        />
        <text x="36" y="41" textAnchor="middle" fontSize="14" fontWeight="700" fill={color}>
          {score}
        </text>
      </svg>
      <p style={{ fontSize: "10px", color: "#aaa", marginTop: "2px" }}>{label}</p>
    </div>
  );
}

// Divider line between sections
function Divider() {
  return <div style={{ height: "1px", background: "#e8e8e8", margin: "4px 0" }} />;
}

// ═══════════════════════════════════════════════════════
//  SECTION COMPONENTS  (one component = one dashboard block)
// ═══════════════════════════════════════════════════════

// ── HERO: name, badges, summary, score ring
function HeroSection({ d }) {
  const levelStyle = {
    "Fresher":   { bg: "#e8f5e9", color: "#2e7d32" },
    "Junior":    { bg: "#e3f2fd", color: "#1565c0" },
    "Mid-Level": { bg: "#fff8e1", color: "#f57f17" },
    "Senior":    { bg: "#fce4ec", color: "#b71c1c" },
    "Staff/Lead":{ bg: "#ede7f6", color: "#4527a0" },
  };
  const ls = levelStyle[d.candidate_level] || { bg: "#eee", color: "#333" };

  return (
    <div style={{
      display: "flex", justifyContent: "space-between", alignItems: "flex-start",
      gap: "20px", paddingBottom: "16px", marginBottom: "14px",
      borderBottom: "1px solid #e0e0e0",
    }}>
      <div style={{ flex: 1 }}>
        {/* Name */}
        <h2 style={{ fontSize: "22px", fontWeight: 700, marginBottom: "8px", color: "#111" }}>
          {d.candidate_name || "Candidate"}
        </h2>

        {/* Badges row */}
        <div style={{ display: "flex", flexWrap: "wrap", gap: "6px", marginBottom: "12px" }}>
          <Pill text={d.candidate_level || "Unknown"} bg={ls.bg} color={ls.color} />
          <Pill text={`⭐ ${d.primary_domain || "Unknown Domain"}`} bg="#fff8e1" color="#b45309" />
          <Pill text={`🎯 ${d.target_role   || "Not specified"}`}  bg="#f0f9ff" color="#0369a1" />
        </div>

        {/* Summary paragraph */}
        <p style={{ fontSize: "13px", color: "#555", lineHeight: 1.7, maxWidth: "560px" }}>
          {d.summary}
        </p>
      </div>

      {/* Score ring on right */}
      <ScoreRing score={d.resume_score ?? 0} />
    </div>
  );
}

// ── ATS: 6 score bars
function ATSSection({ ats }) {
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

// ── DOMAIN: bar per domain + evidence + missing skills
function DomainSection({ domains }) {
  if (!domains || domains.length === 0) return null;
  return (
    <Card title="Domain Strength">
      {domains.map((d, i) => (
        <div key={i} style={{ marginBottom: "10px" }}>
          {/* Score bar */}
          <Bar label={d.domain} value={d.score ?? 0} />

          {/* Evidence text */}
          {d.evidence && (
            <p style={{ fontSize: "10px", color: "#999", marginLeft: "98px", marginTop: "-4px", marginBottom: "3px", lineHeight: 1.4 }}>
              {d.evidence}
            </p>
          )}

          {/* Missing skills for this domain */}
          {(d.missing_skills || []).length > 0 && (
            <div style={{ marginLeft: "98px" }}>
              {d.missing_skills.map((s, j) => <Tag key={j} text={s} />)}
            </div>
          )}

          {/* Thin divider between domains */}
          {i < domains.length - 1 && <Divider />}
        </div>
      ))}
    </Card>
  );
}

// ── SKILLS: present (blue) + missing (red)
function SkillsSection({ skills, missingSkills }) {
  return (
    <Card title="Skills">
      <div style={{ marginBottom: "10px" }}>
        {(skills || []).map((s, i) => <Pill key={i} text={s} bg="#e8f0fe" color="#1565c0" />)}
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
            {missingSkills.map((s, i) => <Pill key={i} text={s} bg="#fce8e8" color="#c0392b" />)}
          </div>
        </>
      )}
    </Card>
  );
}

// ── EXPERIENCE
function ExperienceSection({ experience }) {
  if (!experience || experience.length === 0) return null;
  return (
    <Card title="Experience">
      {experience.map((exp, i) => (
        <div key={i} style={{
          marginBottom: i < experience.length - 1 ? "14px" : 0,
          paddingBottom: i < experience.length - 1 ? "14px" : 0,
          borderBottom: i < experience.length - 1 ? "1px solid #eee" : "none",
        }}>
          {/* Company + duration */}
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <span style={{ fontSize: "13px", fontWeight: 700, color: "#111" }}>{exp.company}</span>
            <span style={{ fontSize: "10px", color: "#aaa" }}>{exp.duration}</span>
          </div>
          {/* Role */}
          <p style={{ fontSize: "11px", color: "#777", margin: "3px 0 7px" }}>{exp.role}</p>
          {/* Description bullets */}
          {(exp.description || []).map((line, j) => (
            <Bullet key={j} text={line} color="#1565c0" />
          ))}
        </div>
      ))}
    </Card>
  );
}

// ── EDUCATION
function EducationSection({ education }) {
  if (!education || education.length === 0) return null;
  return (
    <Card title="Education">
      {education.map((edu, i) => (
        <div key={i} style={{ marginBottom: i < education.length - 1 ? "12px" : 0 }}>
          <p style={{ fontSize: "13px", fontWeight: 700, color: "#111" }}>{edu.degree}</p>
          <p style={{ fontSize: "12px", color: "#555", marginTop: "2px" }}>{edu.institution}</p>
          <p style={{ fontSize: "11px", color: "#aaa", marginTop: "3px" }}>
            {edu.performance}  ·  Passing: {edu.year_of_passing}
          </p>
        </div>
      ))}
    </Card>
  );
}

// ── PROJECTS
function ProjectsSection({ projects }) {
  if (!projects || projects.length === 0) return null;
  return (
    <Card title="Projects">
      {projects.map((proj, i) => (
        <div key={i} style={{
          marginBottom: i < projects.length - 1 ? "16px" : 0,
          paddingBottom: i < projects.length - 1 ? "16px" : 0,
          borderBottom: i < projects.length - 1 ? "1px solid #eee" : "none",
        }}>
          {/* Project name */}
          <p style={{ fontSize: "13px", fontWeight: 700, color: "#111", marginBottom: "5px" }}>
            {proj.name}
          </p>

          {/* Achievement bullets */}
          {(proj.description || []).map((line, j) => <Bullet key={j} text={line} />)}

          {/* Impact line in green */}
          {proj.impact && (
            <p style={{ fontSize: "11px", color: "#16a34a", margin: "5px 0 5px 14px", lineHeight: 1.5 }}>
              🎯 {proj.impact}
            </p>
          )}

          {/* Tech tags */}
          <div style={{ marginTop: "6px" }}>
            {(proj.technologies || []).map((t, j) => <Tag key={j} text={t} />)}
          </div>
        </div>
      ))}
    </Card>
  );
}

// ── STRENGTHS | WEAKNESSES | RECOMMENDATIONS  (3 equal columns)
function InsightsSection({ strengths, weaknesses, recommendations }) {
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

// ── ACHIEVEMENTS + CERTIFICATIONS  (hidden if both are empty)
function ExtrasSection({ achievements, certifications }) {
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
          {certifications.map((c, i) => <Pill key={i} text={c} bg="#f0fdf4" color="#166534" />)}
        </Card>
      )}
    </div>
  );
}

// ═══════════════════════════════════════════════════════
//  FULL DASHBOARD  –  puts every section together
// ═══════════════════════════════════════════════════════

function ResumeDashboard({ d }) {
  // 'd' is the parsed_data object (or the root object if your API returns flat JSON)
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "12px", marginTop: "24px" }}>

      {/* Row 0 — Name, level badge, domain, score ring */}
      <HeroSection d={d} />

      {/* Row 1 — ATS bars  |  Domain strength bars */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
        <ATSSection    ats={d.ats_score      || {}} />
        <DomainSection domains={d.domain_scores || []} />
      </div>

      {/* Row 2 — All skills + missing skills */}
      <SkillsSection skills={d.skills || []} missingSkills={d.missing_skills || []} />

      {/* Row 3 — Experience  |  Education */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
        <ExperienceSection experience={d.experience || []} />
        <EducationSection  education={d.education   || []} />
      </div>

      {/* Row 4 — Projects */}
      <ProjectsSection projects={d.projects || []} />

      {/* Row 5 — Strengths | Weaknesses | Recommendations */}
      <InsightsSection
        strengths={d.strengths           || []}
        weaknesses={d.weaknesses         || []}
        recommendations={d.recommendations || []}
      />

      {/* Row 6 — Achievements + Certifications (hidden when empty) */}
      <ExtrasSection
        achievements={d.achievements   || []}
        certifications={d.certifications || []}
      />
    </div>
  );
}

// ═══════════════════════════════════════════════════════
//  UPLOAD SECTION
// ═══════════════════════════════════════════════════════

function UploadSection({ onUploadSuccess }) {
  const [file,    setFile]    = useState(null);
  const [loading, setLoading] = useState(false);
  const [error,   setError]   = useState("");

  async function handleUpload() {
    setError("");

    if (!file) { setError("Please choose a PDF file first."); return; }

    const token = localStorage.getItem("token");
    if (!token) { setError("Not logged in — no token found. Please log in first."); return; }

    const formData = new FormData();
    formData.append("resume", file);
    setLoading(true);

    try {
      // Step 1 — upload the PDF
      await axios.post(
        "http://127.0.0.1:8000/resume/upload",
        formData,
        { headers: { Authorization: `Bearer ${token}`, "Content-Type": "multipart/form-data" } }
      );

      // Step 2 — fetch the analysis result
      const res = await axios.get(
        "http://127.0.0.1:8000/resume/me",
        { headers: { Authorization: `Bearer ${token}` } }
      );

      onUploadSuccess(res.data);

    } catch (err) {
      const status = err?.response?.status;
      if      (status === 401) setError("401 — Token expired. Please log in again.");
      else if (status === 422) setError("422 — Make sure you upload a valid PDF.");
      else if (status === 404) setError("404 — API endpoint not found. Check backend URL.");
      else                     setError(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ marginBottom: "8px" }}>
      {/* Input row */}
      <div style={{ display: "flex", alignItems: "center", gap: "12px", marginBottom: "8px" }}>
        <input
          type="file" accept=".pdf"
          onChange={(e) => { setFile(e.target.files[0]); setError(""); }}
        />
        <button
          onClick={handleUpload} disabled={loading}
          style={{
            padding: "9px 22px", background: "#1976d2", color: "white",
            border: "none", borderRadius: "7px", fontSize: "13px", fontWeight: 600,
            cursor: loading ? "not-allowed" : "pointer", opacity: loading ? 0.7 : 1,
          }}
        >
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>
      </div>

      {/* Error box */}
      {error && (
        <div style={{
          padding: "10px 14px", background: "#fce8e8",
          border: "1px solid #f5c6c6", borderRadius: "7px",
          color: "#c0392b", fontSize: "13px",
        }}>
          ⚠ {error}
        </div>
      )}
    </div>
  );
}

// ═══════════════════════════════════════════════════════
//  MAIN PAGE  –  top-level component
// ═══════════════════════════════════════════════════════

function Resume() {
  
  const navigate = useNavigate();
  const [resumeData, setResumeData] = useState(null);
  // Your API returns the data at resumeData.parsed_data based on your screenshots
  // If it's flat (no parsed_data wrapper), change this to just: resumeData
  const parsedData = resumeData?.parsed_data ?? resumeData;

  return (
    <div style={{
      padding: "24px", fontFamily: "Arial, sans-serif",
      maxWidth: "980px", margin: "0 auto",
    }}>
      <div
    style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "25px"
    }}
>

    <div>

        <h1
            style={{
                fontSize: "28px",
                color: "#2563eb",
                marginBottom: "6px"
            }}
        >
            📄 Resume Analyzer
        </h1>

        <p
            style={{
                color: "#666"
            }}
        >
            Upload your resume and receive an AI-powered analysis.
        </p>

    </div>

    <button
        onClick={() => navigate("/")}
        style={{
            background: "#2563eb",
            color: "white",
            border: "none",
            padding: "12px 22px",
            borderRadius: "10px",
            cursor: "pointer",
            fontWeight: "600",
            fontSize: "15px"
        }}
    >
        🏠 Dashboard
    </button>

</div>

      {/* Upload + error handling */}
      <UploadSection onUploadSuccess={setResumeData} />

      {/* Dashboard — only renders after upload */}
      {resumeData && parsedData && <ResumeDashboard d={parsedData} />}
    </div>
  );
}

export default Resume;
