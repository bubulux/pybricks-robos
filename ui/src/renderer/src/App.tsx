import { useRobotDataStream } from "./hooks/useRobotDataStream";

function App(): React.JSX.Element {
  const { data: csvData, isLoading, error, isConnected } = useRobotDataStream();

  if (isLoading) {
    return (
      <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
        <h1>Robot Sensor Monitor</h1>
        <p>Loading sensor data...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
        <h1>Robot Sensor Monitor</h1>
        <div
          style={{
            color: "red",
            padding: "10px",
            backgroundColor: "#ffe6e6",
            borderRadius: "5px",
          }}
        >
          <strong>Error:</strong> {error}
        </div>
      </div>
    );
  }

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Robot Sensor Monitor</h1>

      {/* Connection Status */}
      <div
        style={{
          marginBottom: "20px",
          display: "flex",
          alignItems: "center",
          gap: "10px",
        }}
      >
        <div
          style={{
            width: "10px",
            height: "10px",
            borderRadius: "50%",
            backgroundColor: isConnected ? "#4CAF50" : "#f44336",
          }}
        />
        <span style={{ fontSize: "14px", color: "#666" }}>
          {isConnected ? "Connected" : "Disconnected"}
        </span>
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
