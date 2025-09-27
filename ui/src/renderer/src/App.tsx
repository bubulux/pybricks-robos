import { useStream } from "./stream";

function App(): React.JSX.Element {
  const { data, history } = useStream();

  return <div>Hello World</div>;
}

export default App;
