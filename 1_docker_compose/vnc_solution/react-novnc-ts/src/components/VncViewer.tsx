import RFB from "@novnc/novnc/lib/rfb";
import { useEffect, useRef } from "react";

interface VncViewerProps {
  url: string;
  title: string;
}

export default function VncViewer({ url }: VncViewerProps) {
  const screenRef = useRef<HTMLDivElement | null>(null);
  const rfbRef = useRef<RFB | null>(null);

  useEffect(() => {
    if (!screenRef.current) return;

    const rfb = new RFB(screenRef.current, url, {
      credentials: { target: "", username: "", password: "" },
    });

    rfb.viewOnly = false;
    rfb.scaleViewport = true;
    rfb.background = "black";

    rfbRef.current = rfb;

    return () => {
      rfb.disconnect();
    };
  }, [url]);

  return (
    <div style={{ flex: 1, margin: "10px", border: "2px solid #ccc" }}>
      <h3 style={{ textAlign: "center", color: "white", background: "#333" }}>
        {url}
      </h3>
      <div
        ref={screenRef}
        style={{ width: "100%", height: "500px", backgroundColor: "black" }}
      />
    </div>
  );
}
