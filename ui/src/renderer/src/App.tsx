import { useStream } from "./stream";
import { AppShell, Flex, Divider } from "@mantine/core";

import {
  HealthHistoryWired,
  FieldMonitorWired,
  HealthMonitorWired,
  GameMonitorWired,
  DataHistoryWired,
} from "@renderer/wired";

function App(): React.JSX.Element {
  const { data, history, resetHistory } = useStream();

  return (
    <AppShell h={"100vh"} w={"100vw"}>
      <Flex direction={"column"} h={"100%"} w={"100%"} p={24}>
        <Flex h={"70%"}>
          <Flex w={"20%"}>
            <FieldMonitorWired data={data} />
          </Flex>
          <Divider size="lg" orientation="vertical" />
          <Flex flex={1}>
            <HealthMonitorWired data={data} />
          </Flex>
          <Divider size="lg" orientation="vertical" />
          <Flex w={"20%"}>
            <GameMonitorWired data={data} />
          </Flex>
        </Flex>
        <Divider size="lg" />
        <Flex flex={1}>
          <Flex direction={"column"} flex={1}>
            <Flex h={"90%"}>
              <HealthHistoryWired data={data} />
            </Flex>
            <Divider size="lg" />
            <Flex flex={1}>
              <DataHistoryWired
                history={history}
                data={data}
                resetHistory={resetHistory}
              />
            </Flex>
          </Flex>
        </Flex>
      </Flex>
    </AppShell>
  );
}

export default App;
