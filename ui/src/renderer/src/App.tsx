import { useStream } from "./stream";
import { AppShell, Flex, Divider } from "@mantine/core";

import {
  MonitorStateWired,
  HealthHistoryWired,
  FieldMonitorWired,
  HealthMonitorWired,
  GameMonitorWired,
  DataHistoryWired,
} from "@renderer/wired";

function App(): React.JSX.Element {
  const { data, history } = useStream();

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
            <FieldMonitorWired data={data} />
          </Flex>
          <Divider size="lg" color="blue" orientation="vertical" />
          <Flex flex={1}>
            <HealthMonitorWired data={data} />
          </Flex>
          <Divider size="lg" color="blue" orientation="vertical" />
          <Flex
            style={{
              width: "20%",
            }}
          >
            <GameMonitorWired data={data} />
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
                <HealthHistoryWired data={data} />
              </Flex>
              <Divider size="lg" color="blue" />
              <Flex>
                <DataHistoryWired history={history} />
              </Flex>
            </Flex>
          </Flex>
        </Flex>
      </Flex>
    </AppShell>
  );
}

export default App;
