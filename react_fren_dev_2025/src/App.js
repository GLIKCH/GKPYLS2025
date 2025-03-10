import React from 'react';
import { BrowserRouter as Router, Route, Routes  } from 'react-router-dom';
import Navbar from './components/navbar'; // Import the Navbar component
import Home from './pages/home';
import Products from './pages/products';
import Services from './pages/services';
import Projects from './pages/projects';
import Contact from './pages/contact';

const App = () => {
  return (
    <Router>
      <div>
        <Navbar /> {/* Use Navbar here */}
        <Routes>
          <Route path="/" exact component={Home} />
          <Route path="/products" component={Products} />
          <Route path="/services" component={Services} />
          <Route path="/projects" component={Projects} />
          <Route path="/contact" component={Contact} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
