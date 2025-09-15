import { useState, useEffect } from "react";

interface SensorData {
  [key: string]: (string | number)[];
}

function App(): React.JSX.Element {
  const [csvData, setCsvData] = useState<SensorData>({});
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Load initial CSV data
    window.api
      .getCsvData()
      .then((data) => {
        setCsvData(data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Failed to load CSV data:", error);
        setIsLoading(false);
      });

    // Start watching for file changes
    window.api.startWatchingCsv().catch((error) => {
      console.error("Failed to start watching CSV file:", error);
    });

    // Subscribe to file changes
    const unsubscribe = window.api.onCsvDataChanged((data) => {
      setCsvData(data);
    });

    // Cleanup on unmount
    return () => {
      unsubscribe();
      window.api.stopWatchingCsv().catch((error) => {
        console.error("Failed to stop watching CSV file:", error);
      });
    };
  }, []);

  if (isLoading) {
    return (
      <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
        <h1>Robot Sensor Monitor</h1>
        <p>Loading sensor data...</p>
      </div>
    );
  }

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Robot Sensor Monitor</h1>

      <div style={{ marginBottom: "20px" }}>
        <h2>Current Sensor History</h2>
        <pre
          style={{
            backgroundColor: "#f5f5f5",
            padding: "15px",
            borderRadius: "5px",
            border: "1px solid #ddd",
            fontSize: "14px",
            overflow: "auto",
          }}
        >
          {JSON.stringify(csvData, null, 2)}
        </pre>
      </div>

      <div style={{ display: "grid", gap: "15px" }}>
        {Object.entries(csvData).map(([sensor, values]) => (
          <div
            key={sensor}
            style={{
              border: "1px solid #ccc",
              borderRadius: "8px",
              padding: "15px",
              backgroundColor: "#f9f9f9",
            }}
          >
            <h3 style={{ margin: "0 0 10px 0", color: "#333" }}>{sensor}</h3>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "5px" }}>
              {values.map((value, index) => (
                <span
                  key={index}
                  style={{
                    padding: "4px 8px",
                    backgroundColor: value === "NONE" ? "#e0e0e0" : "#4CAF50",
                    color: value === "NONE" ? "#666" : "white",
                    borderRadius: "4px",
                    fontSize: "12px",
                    fontFamily: "monospace",
                  }}
                >
                  {String(value)}
                </span>
              ))}
            </div>
            <div style={{ marginTop: "8px", fontSize: "12px", color: "#666" }}>
              Latest:{" "}
              <strong>{String(values[values.length - 1] || "NONE")}</strong>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
