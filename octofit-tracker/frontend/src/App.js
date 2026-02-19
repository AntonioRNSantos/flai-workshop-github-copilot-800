import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import logo from './octofitapp-small.png';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
          <div className="container">
            <Link className="navbar-brand" to="/">
              <img src={logo} alt="OctoFit Tracker Logo" />
              OctoFit Tracker
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">📊 Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">🏆 Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">👥 Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">👤 Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">💪 Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-5">
              <div className="text-center mb-5">
                <h1 className="display-3 fw-bold mb-3">Welcome to OctoFit Tracker</h1>
                <p className="lead fs-4 text-muted">Track your fitness activities, compete with your team, and stay motivated!</p>
              </div>
              
              <div className="row g-4 mb-5">
                <div className="col-md-4">
                  <div className="card shadow-sm border-0">
                    <div className="card-body text-center p-4">
                      <div className="mb-3" style={{fontSize: '3rem'}}>📊</div>
                      <h5 className="card-title fw-bold">Track Activities</h5>
                      <p className="card-text text-muted">Log your workouts and monitor your progress over time.</p>
                      <Link to="/activities" className="btn btn-primary mt-2">View Activities</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4">
                  <div className="card shadow-sm border-0">
                    <div className="card-body text-center p-4">
                      <div className="mb-3" style={{fontSize: '3rem'}}>👥</div>
                      <h5 className="card-title fw-bold">Join a Team</h5>
                      <p className="card-text text-muted">Connect with others and compete together for glory.</p>
                      <Link to="/teams" className="btn btn-primary mt-2">View Teams</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4">
                  <div className="card shadow-sm border-0">
                    <div className="card-body text-center p-4">
                      <div className="mb-3" style={{fontSize: '3rem'}}>🏆</div>
                      <h5 className="card-title fw-bold">Check Leaderboard</h5>
                      <p className="card-text text-muted">See how you rank against others in the community.</p>
                      <Link to="/leaderboard" className="btn btn-primary mt-2">View Leaderboard</Link>
                    </div>
                  </div>
                </div>
              </div>

              <div className="row g-4">
                <div className="col-md-6">
                  <div className="card bg-light border-0 h-100">
                    <div className="card-body p-4">
                      <h4 className="card-title mb-3">💪 Personalized Workouts</h4>
                      <p className="card-text">Get customized workout suggestions based on your fitness level and goals.</p>
                      <Link to="/workouts" className="btn btn-success">Explore Workouts</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-6">
                  <div className="card bg-light border-0 h-100">
                    <div className="card-body p-4">
                      <h4 className="card-title mb-3">👤 User Community</h4>
                      <p className="card-text">Connect with fellow fitness enthusiasts and share your journey.</p>
                      <Link to="/users" className="btn btn-success">View Users</Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>

        <footer className="mt-5 py-4 bg-dark text-white text-center">
          <div className="container">
            <p className="mb-0">© 2026 OctoFit Tracker - Your Fitness Journey Starts Here</p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
