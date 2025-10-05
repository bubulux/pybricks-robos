import { FieldMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";

import { selectMostRecentSensorData } from "@renderer/utils";
import { TField } from "@renderer/types";

type TProps = {
  data: TRobotSensorData;
};

export default function FieldMonitor({ data }: TProps): React.JSX.Element {
  const { Light } = selectMostRecentSensorData(data);

  function determineField(): TField {
    if (Light === "PROTECTED-DAMAGING") return "Protected-Damaging";
    if (Light === "FORBIDDEN") return "Forbidden";
    if (Light === "DAMAGING") return "Damaging";
    if (Light === "WIN") return "Won";
    if (Light === "HEALING") return "Healing";
    if (Light === "PROTECTED") return "Protected";

    return "Neutral";
  }

  return <FieldMonitorPartial field={determineField()} />;
}
