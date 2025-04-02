import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import VncViewer from "./components/VncViewer";

console.log("URL");
console.log(window.location.href);
console.log("BASE_PATH");
console.log(import.meta.env.BASE_PATH);

type Viewer = {
  url: string;
  title: string;
};

function App() {
  const [inputUrl, setInputUrl] = useState("");
  const [viewers, setViewers] = useState<Viewer[]>([]);

  const location = useLocation();
  console.log(location.pathname); // Logs just the path, e.g., "/dashboard"
  console.log(location);
  console.log(window.location.href); // Logs full URL, still works if you need it

  useEffect(() => {
    console.log(viewers);
  }, [viewers]);

  const handleAddViewer = () => {
    const trimmed = inputUrl.trim();
    if (!trimmed) return;

    setViewers((prev) => [
      ...prev,
      {
        url: `ws://${trimmed}`,
        title: `VM ${prev.length + 1}`,
      },
    ]);
    setInputUrl("");
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        background: "#111",
        height: "100vh",
        padding: "10px",
        boxSizing: "border-box",
        color: "#fff",
      }}
    >
      <div style={{ marginBottom: "10px", display: "flex", gap: "10px" }}>
        <input
          type="text"
          placeholder="127.0.0.1:63319/qemu1"
          value={inputUrl}
          onChange={(e) => setInputUrl(e.target.value)}
          style={{
            padding: "8px",
            width: "300px",
            borderRadius: "4px",
            border: "1px solid #ccc",
            background: "#222",
            color: "#fff",
          }}
        />
        <button
          onClick={handleAddViewer}
          style={{
            padding: "8px 12px",
            borderRadius: "4px",
            border: "1px solid #ccc",
            background: "#333",
            color: "#fff",
            cursor: "pointer",
          }}
        >
          Add Viewer
        </button>
      </div>

      <div
        style={{
          display: "flex",
          gap: "10px",
          flex: 1,
          overflowX: "auto",
          overflowY: "hidden",
        }}
      >
        {viewers.map((viewer, index) => (
          <div
            key={index}
            style={{
              minWidth: "800px", // ensures consistent width
              width: "800px",
              border: "1px solid #ccc",
              height: "100%",
              display: "flex",
              flexDirection: "column",
              background: "#000",
            }}
          >
            {/* <div
              style={{
                padding: "5px 10px",
                background: "#333",
                borderBottom: "1px solid #555",
                fontWeight: "bold",
                textAlign: "center",
              }}
            >
              {viewer.title}
            </div>
            <div style={{ flex: 1 }}> */}
            <VncViewer url={viewer.url} title={viewer.title} />
            {/* </div> */}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
