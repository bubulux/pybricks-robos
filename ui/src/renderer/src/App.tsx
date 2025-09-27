import { useStream } from "./stream";
import { AppShell, Flex, Title } from "@mantine/core";

function App(): React.JSX.Element {
  const { data: streamData } = useStream();

  // Sample data for the chart
  const sampleData = [
    { date: "1", value: 10 },
    { date: "2", value: 15 },
    { date: "3", value: 7 },
    { date: "4", value: 20 },
  ];

  return <AppShell></AppShell>;
}

export default App;
