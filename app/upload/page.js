"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const router = useRouter();

  function handleFile(event) {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      setFile(selectedFile);
    }
  }

  async function continueNext() {
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    try {
      setUploading(true);

      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        "http://127.0.0.1:8000/upload/",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Upload failed");
      }

      const data = await response.json();

      localStorage.setItem("uploadedFile", file.name);
      localStorage.setItem("documentId", data.document_id);

      router.push("/configure");

    } catch (error) {
      console.error(error);
      alert(
        "Upload failed. Make sure the backend is running."
      );
    } finally {
      setUploading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-10 text-white">

      <div className="mx-auto max-w-3xl">

        <h1 className="text-4xl font-bold">
          Upload Your Source
        </h1>

        <p className="mt-3 text-slate-400">
          Upload the document you want to transform.
        </p>

        <div className="mt-10 rounded-2xl border-2 border-dashed border-slate-700 bg-slate-900 p-12 text-center">

          <div className="text-5xl">
            📄
          </div>

          <h2 className="mt-5 text-xl font-semibold">
            Drag & Drop your file
          </h2>

          <p className="mt-2 text-slate-400">
            PDF, DOCX, TXT or image
          </p>

          <label className="mt-6 inline-block cursor-pointer rounded-xl bg-blue-600 px-6 py-3 font-semibold hover:bg-blue-700">

            Browse Files

            <input
              type="file"
              accept=".pdf,.doc,.docx,.txt,.png,.jpg,.jpeg"
              className="hidden"
              onChange={handleFile}
            />

          </label>

        </div>

        {file && (
          <div className="mt-6 rounded-xl border border-green-700 bg-green-950/30 p-5">

            <p className="font-semibold">
              ✓ File Selected
            </p>

            <p className="mt-2 text-slate-300">
              {file.name}
            </p>

            <p className="text-sm text-slate-500">
              {(file.size / 1024 / 1024).toFixed(2)} MB
            </p>

          </div>
        )}

        <button
          onClick={continueNext}
          disabled={uploading}
          className="mt-8 w-full rounded-xl bg-blue-600 py-4 font-semibold hover:bg-blue-700 disabled:opacity-50"
        >
          {uploading ? "Uploading..." : "Continue →"}
        </button>

      </div>

    </main>
  );
}