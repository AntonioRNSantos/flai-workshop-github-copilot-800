import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API URL:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results ? data.results : data;
        console.log('Workouts processed data:', workoutsData);
        setWorkouts(workoutsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'Easy': 'bg-success',
      'Medium': 'bg-warning',
      'Hard': 'bg-danger'
    };
    return badges[difficulty] || 'bg-secondary';
  };

  const getWorkoutIcon = (type) => {
    const icons = {
      'Cardio': '🏃',
      'Strength': '💪',
      'Flexibility': '🧘',
      'HIIT': '🔥',
      'Yoga': '🧘‍♀️'
    };
    return icons[type] || '🏋️';
  };

  if (loading) return <div className="container mt-5"><div className="loading-spinner"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading workouts...</p></div></div>;
  if (error) return <div className="container mt-5"><div className="alert alert-danger error-message" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-5">
      <h2 className="mb-4">💪 Workout Suggestions</h2>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout, index) => (
            <div key={workout.id || index} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-header bg-light">
                  <h5 className="card-title mb-0">
                    {getWorkoutIcon(workout.workout_type)} {workout.name || 'Workout'}
                  </h5>
                </div>
                <div className="card-body">
                  <div className="mb-3">
                    <span className="badge bg-primary me-2">{workout.workout_type || 'N/A'}</span>
                    <span className={`badge ${getDifficultyBadge(workout.difficulty)}`}>
                      {workout.difficulty || 'N/A'}
                    </span>
                  </div>
                  <p className="card-text text-muted">
                    {workout.description || 'No description available'}
                  </p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      <small className="text-muted">Duration</small>
                      <h5 className="mb-0">{workout.duration || 'N/A'} min</h5>
                    </div>
                    <button className="btn btn-success">Start Workout</button>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <h4 className="alert-heading">No Workouts Available!</h4>
              <p>Check back soon for personalized workout suggestions.</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
