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
      <Flex direction={"column"} h={"100vh"} w={"100vw"}>
        <Flex h={"80%"}>
          <Flex w={"20%"}>
            <FieldMonitorWired data={data} />
          </Flex>
          <Divider size="lg" color="blue" orientation="vertical" />
          <Flex flex={1}>
            <HealthMonitorWired data={data} />
          </Flex>
          <Divider size="lg" color="blue" orientation="vertical" />
          <Flex w={"20%"}>
            <GameMonitorWired data={data} />
          </Flex>
        </Flex>
        <Divider size="lg" color="blue" />
        <Flex h={"20%"}>
          <Flex flex={1}>
            <Flex w={"10%"}>
              <MonitorStateWired data={data} />
            </Flex>
            <Divider size="lg" color="blue" orientation="vertical" />
            <Flex direction={"column"} w={"90%"}>
              <Flex h={"90%"}>
                <HealthHistoryWired data={data} />
              </Flex>
              <Divider size="lg" color="blue" />
              <Flex flex={1}>
                <DataHistoryWired history={history} data={data} />
              </Flex>
            </Flex>
          </Flex>
        </Flex>
      </Flex>
    </AppShell>
  );
}

export default App;
