import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">

      {/* Navbar */}
      <nav className="flex items-center justify-between border-b border-slate-800 px-8 py-5">

        <h1 className="text-2xl font-bold">
          TransformAI
        </h1>

        <div className="flex gap-6 text-slate-300">
          <Link href="/">
            Home
          </Link>

          <Link href="/upload">
            Get Started
          </Link>
        </div>

      </nav>

      {/* Hero */}
      <section className="flex min-h-[80vh] flex-col items-center justify-center px-6 text-center">

        <div className="mb-5 rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300">
          AI-Powered Content Transformation
        </div>

        <h2 className="max-w-4xl text-5xl font-bold leading-tight md:text-6xl">
          Transform One Source Into
          <span className="text-blue-400">
            {" "}Multiple Outputs
          </span>
        </h2>

        <p className="mt-6 max-w-2xl text-lg text-slate-400">
          Upload your source document and generate professional,
          audience-specific content using AI.
        </p>

        <Link
          href="/upload"
          className="mt-8 rounded-xl bg-blue-600 px-8 py-4 font-semibold transition hover:bg-blue-700"
        >
          Start Transforming →
        </Link>

      </section>

      {/* Features */}
      <section className="grid gap-6 px-8 pb-20 md:grid-cols-3">

        <Feature
          icon="📄"
          title="Upload"
          text="Upload your source document."
        />

        <Feature
          icon="🤖"
          title="Transform"
          text="Generate multiple content formats."
        />

        <Feature
          icon="🔎"
          title="Validate"
          text="Check generated content against the source."
        />

      </section>

    </main>
  );
}

function Feature({ icon, title, text }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <div className="text-3xl">
        {icon}
      </div>

      <h3 className="mt-4 text-xl font-semibold">
        {title}
      </h3>

      <p className="mt-2 text-slate-400">
        {text}
      </p>

    </div>
  );
}