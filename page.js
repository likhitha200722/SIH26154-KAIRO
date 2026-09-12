"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function ConfigurePage() {
  const router = useRouter();

  const [audience, setAudience] = useState("General Public");
  const [tone, setTone] = useState("Clear and Professional");
  const [language, setLanguage] = useState("English");
  const [detailLevel, setDetailLevel] = useState("Concise");
  const [objective, setObjective] = useState("Inform");
  const [outputType, setOutputType] = useState("Advisory");
  const [transforming, setTransforming] = useState(false);

  async function continueNext() {
    const documentId = localStorage.getItem("documentId");

    if (!documentId) {
      alert("No uploaded document found. Please upload a document first.");
      return;
    }

    try {
  setTransforming(true);

  // First analyze the uploaded document
  const analyzeResponse = await fetch(
    `http://127.0.0.1:8000/analyze/${documentId}`,
    {
      method: "POST",
    }
  );

  if (!analyzeResponse.ok) {
    const errorText = await analyzeResponse.text();
    console.error("Analyze error:", errorText);
    throw new Error("Document analysis failed");
  }

  // Then transform the analyzed document
  const response = await fetch(
    "http://127.0.0.1:8000/transform/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            document_id: Number(documentId),
            audience: audience,
            tone: tone,
            language: language,
            detail_level: detailLevel,
            objective: objective,
          outputs: [outputType],
          }),
        }
      );

      if (!response.ok) {
        const errorText = await response.text();
        console.error("Transform error:", errorText);
        throw new Error("Transformation failed");
      }

      const data = await response.json();

      console.log("Transformation successful:", data);

      localStorage.setItem("transformationData", JSON.stringify(data));

      localStorage.setItem("audience", audience);
      localStorage.setItem("tone", tone);
      localStorage.setItem("language", language);
      localStorage.setItem("detailLevel", detailLevel);
      localStorage.setItem("objective", objective);
      localStorage.setItem("outputType", outputType);

      router.push("/results");

    } catch (error) {
      console.error(error);
      alert(
        "Transformation failed. Make sure the backend and AI service are running."
      );
    } finally {
      setTransforming(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-10 text-white">

      <div className="mx-auto max-w-4xl">

        <h1 className="text-4xl font-bold">
          Configure Transformation
        </h1>

        <p className="mt-3 text-slate-400">
          Choose how you want your source document transformed.
        </p>

        <div className="mt-10 grid gap-6 md:grid-cols-2">

          <Setting
            label="Audience"
            value={audience}
            onChange={setAudience}
            options={[
              "General Public",
              "Students",
              "Professionals",
              "Technical Audience"
            ]}
          />

          <Setting
            label="Tone"
            value={tone}
            onChange={setTone}
            options={[
              "Clear and Professional",
              "Formal",
              "Simple",
              "Educational"
            ]}
          />

          <Setting
            label="Language"
            value={language}
            onChange={setLanguage}
            options={[
              "English",
              "Hindi",
              "Telugu"
            ]}
          />

          <Setting
            label="Detail Level"
            value={detailLevel}
            onChange={setDetailLevel}
            options={[
              "Concise",
              "Balanced",
              "Detailed"
            ]}
          />

          <Setting
            label="Objective"
            value={objective}
            onChange={setObjective}
            options={[
              "Inform",
              "Educate",
              "Summarize",
              "Present"
            ]}
          />

          <Setting
            label="Output Type"
            value={outputType}
            onChange={setOutputType}
            options={[
              "Advisory",
              "Report",
              "Presentation",
              "Summary"
            ]}
          />

        </div>

        <button
          onClick={continueNext}
          disabled={transforming}
          className="mt-10 w-full rounded-xl bg-blue-600 py-4 font-semibold hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {transforming
            ? "Transforming with AI..."
            : "Transform Document →"}
        </button>

      </div>

    </main>
  );
}

function Setting({ label, value, onChange, options }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <label className="text-sm text-slate-400">
        {label}
      </label>

      <select
        value={value}
        onChange={(event) => onChange(event.target.value)}
        className="mt-3 w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-white"
      >
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>

    </div>
  );
}