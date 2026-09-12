"use client";

import Link from "next/link";

export default function ResultsPage() {

  const outputs = [
    {
      icon: "📄",
      title: "Executive Summary",
      description:
        "Concise summary designed for decision makers."
    },
    {
      icon: "📢",
      title: "Public Advisory",
      description:
        "Clear and action-oriented public communication."
    },
    {
      icon: "📊",
      title: "Presentation",
      description:
        "Professional slide structure generated from the source."
    },
    {
      icon: "🎨",
      title: "Infographic",
      description:
        "Key information organized for visual communication."
    }
  ];

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-10 text-white">

      <div className="mx-auto max-w-6xl">

        {/* Header */}

        <div className="flex flex-col justify-between gap-4 md:flex-row md:items-center">

          <div>

            <p className="text-sm text-green-400">
              ✓ Generation Complete
            </p>

            <h1 className="mt-2 text-4xl font-bold">
              Your Results
            </h1>

          </div>

          <Link
            href="/upload"
            className="rounded-xl bg-blue-600 px-5 py-3 text-center font-semibold"
          >
            New Transformation
          </Link>

        </div>

        {/* Scores */}

        <section className="mt-10 grid gap-5 md:grid-cols-3">

          <Score
            title="Fact Consistency"
            value="98%"
          />

          <Score
            title="Source Coverage"
            value="94%"
          />

          <Score
            title="Quality Score"
            value="96%"
          />

        </section>

        {/* Validation */}

        <section className="mt-8 rounded-2xl border border-yellow-700 bg-yellow-950/20 p-6">

          <h2 className="text-xl font-semibold">
            ⚠ Potential Inconsistency Detected
          </h2>

          <p className="mt-3 text-slate-300">
            One generated output may contain information
            that differs from the source document.
          </p>

          <button className="mt-5 rounded-lg border border-yellow-600 px-5 py-2">
            Review Issue
          </button>

        </section>

        {/* Outputs */}

        <h2 className="mt-12 text-2xl font-bold">
          Generated Outputs
        </h2>

        <section className="mt-6 grid gap-5 md:grid-cols-2">

          {outputs.map(output => (

            <div
              key={output.title}
              className="rounded-2xl border border-slate-800 bg-slate-900 p-6"
            >

              <div className="text-4xl">
                {output.icon}
              </div>

              <h3 className="mt-4 text-xl font-semibold">
                {output.title}
              </h3>

              <p className="mt-2 text-slate-400">
                {output.description}
              </p>

              <div className="mt-6 flex gap-3">

                <button className="rounded-lg bg-blue-600 px-4 py-2">
                  View
                </button>

                <button className="rounded-lg border border-slate-700 px-4 py-2">
                  Download
                </button>

              </div>

            </div>

          ))}

        </section>

      </div>

    </main>
  );
}

function Score({ title, value }) {

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <p className="text-slate-400">
        {title}
      </p>

      <p className="mt-3 text-4xl font-bold">
        {value}
      </p>

    </div>
  );
}