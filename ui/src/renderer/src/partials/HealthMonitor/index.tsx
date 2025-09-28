import { Stack, Title, Group, Flex, ThemeIcon, Image } from "@mantine/core";
import {
  IconArrowBigUp,
  IconArrowBigDown,
  IconPlus,
  IconMinus,
} from "@tabler/icons-react";
import terryImage from "./terry.jpg";

type TProps = {
  health: number;
  currentEffect: "harm" | "heal" | "neutral";
  effectImpact: number;
};

export default function HealthMonitor({
  health,
  currentEffect,
  effectImpact,
}: TProps): React.JSX.Element {
  return (
    <Group flex={1} pr={16} pb={16} justify="center" align="center">
      <Stack w={"70%"} h={"100%"}>
        <Flex h={"50%"} w={"100%"} justify={"center"} align={"center"}>
          <Image src={terryImage} radius="md" h={"100%"} w="auto" />
        </Flex>
        <Group flex={1} justify="center" align="center">
          {currentEffect === "harm" && (
            <Stack justify="center" align="center">
              <ThemeIcon size={128} color="red" variant="light">
                <IconArrowBigDown size={128} />
              </ThemeIcon>
              <Group gap={0}>
                <IconMinus size={32} />
                <Title order={1}> {effectImpact}</Title>
              </Group>
            </Stack>
          )}
          {currentEffect === "heal" && (
            <Stack justify="center" align="center">
              <ThemeIcon color="green" variant="light" size={128}>
                <IconArrowBigUp size={128} />
              </ThemeIcon>
              <Group gap={0}>
                <IconPlus size={32} />
                <Title order={1}> {effectImpact}</Title>
              </Group>
            </Stack>
          )}
          {currentEffect === "neutral" && (
            <Group justify="center" align="center">
              <ThemeIcon size={128} color="grey" variant="light">
                <IconArrowBigDown size={128} />
              </ThemeIcon>
              <ThemeIcon size={128} color="grey" variant="light">
                <IconArrowBigUp size={128} />
              </ThemeIcon>
            </Group>
          )}
        </Group>
      </Stack>
      <Stack flex={1} h={"100%"} gap={0} bd={"4px solid white"} bdrs={"md"}>
        <Flex bg="red.5" w="100%" h={`${100 - health}%`} />
        <Flex
          bg="green.5"
          w="100%"
          h={`${health}%`}
          justify={"center"}
          align={"center"}
        >
          <Title c="white">{health}</Title>
        </Flex>
      </Stack>
    </Group>
  );
}
