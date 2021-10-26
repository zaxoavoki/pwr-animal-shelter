import { useContext } from "react";
import { Switch, Route } from "react-router-dom";
import Footer from "./components/layout/Footer";
import Header from "./components/layout/Header";
import { AuthContext } from "./contexts/AuthContext";
import Home from "./pages/Home";

function App() {
  const { auth, setAuth } = useContext(AuthContext);

  return (
    <>
      <Header />
      <Switch>
        <Route exact path="/" component={Home} />
      </Switch>
      <Footer />
    </>
  );
}

export default App;
