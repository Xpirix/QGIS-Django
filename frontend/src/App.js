import logo from './logo.svg';
import './App.css';
import Header from './components/Header'

function App() {
  return (
    <div className="App">
      <Header />
      <section className="section">
        <div className="container">
          <h1 className="title">Welcome to QGIS Plugins</h1>
          <p className="subtitle">
            Transforming the QGIS plugins website to React + Django.
          </p>
        </div>
      </section>
    </div>
  );
}


export default App;
