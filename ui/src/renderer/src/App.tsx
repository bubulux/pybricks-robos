import { useState, useEffect } from "react";

function App(): React.JSX.Element {
  const [logContent, setLogContent] = useState<string>("Loading log file...");

  useEffect(() => {
    // Load initial content
    window.api
      .getLogContent()
      .then((content) => {
        setLogContent(content);
      })
      .catch((error) => {
        console.error("Failed to load log content:", error);
        setLogContent("Error loading log file");
      });

    // Start watching for file changes
    window.api.startWatchingLog().catch((error) => {
      console.error("Failed to start watching log file:", error);
    });

    // Subscribe to file changes
    const unsubscribe = window.api.onLogFileChanged((content) => {
      setLogContent(content);
    });

    // Cleanup on unmount
    return () => {
      unsubscribe();
      window.api.stopWatchingLog().catch((error) => {
        console.error("Failed to stop watching log file:", error);
      });
    };
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "monospace" }}>
      <h1>Robot Log Monitor</h1>
      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          backgroundColor: "#f9f9f9",
          whiteSpace: "pre-wrap",
          maxHeight: "500px",
          overflow: "auto",
          fontSize: "12px",
          lineHeight: "1.4",
        }}
      >
        {logContent}
      </div>
    </div>
  );
}

export default App;
