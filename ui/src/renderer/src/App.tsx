import { useStream } from "./stream";
import { AppShell, Flex, Divider } from "@mantine/core";

import { MonitorStateWired } from "@renderer/wired";

function App(): React.JSX.Element {
  const { data } = useStream();

  return (
    <AppShell>
      <Flex
        direction={"column"}
        style={{
          height: "100vh",
          width: "100vw",
        }}
      >
        <Flex
          style={{
            height: "80%",
          }}
        >
          <Flex
            style={{
              width: "20%",
            }}
          >
            FieldStatus
          </Flex>
          <Divider size="lg" color="blue" orientation="vertical" />
          <Flex flex={1}>HealthMonitor</Flex>
          <Divider size="lg" color="blue" orientation="vertical" />
          <Flex
            style={{
              width: "20%",
            }}
          >
            GameTracker
          </Flex>
        </Flex>
        <Divider size="lg" color="blue" />
        <Flex
          style={{
            height: "20%",
          }}
        >
          <Flex flex={1}>
            <Flex style={{ width: "10%" }}>
              <MonitorStateWired data={data} />
            </Flex>
            <Divider size="lg" color="blue" orientation="vertical" />
            <Flex direction={"column"} style={{ width: "90%" }}>
              <Flex
                style={{
                  height: "70%",
                }}
              >
                HealthHistory
              </Flex>
              <Divider size="lg" color="blue" />
              <Flex>DataHistory</Flex>
            </Flex>
          </Flex>
        </Flex>
      </Flex>
    </AppShell>
  );
}

export default App;
