import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Activities API URL:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results ? data.results : data;
        console.log('Activities processed data:', activitiesData);
        setActivities(activitiesData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-5"><div className="loading-spinner"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading activities...</p></div></div>;
  if (error) return <div className="container mt-5"><div className="alert alert-danger error-message" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-5">
      <h2 className="mb-4">📊 Activities Log</h2>
      <div className="table-responsive">
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Activity Type</th>
              <th scope="col">User</th>
              <th scope="col">Duration (min)</th>
              <th scope="col">Distance (km)</th>
              <th scope="col">Calories</th>
              <th scope="col">Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.length > 0 ? (
              activities.map((activity, index) => (
                <tr key={activity.id || index}>
                  <th scope="row">{index + 1}</th>
                  <td>
                    <span className="badge bg-primary rounded-pill">
                      {activity.activity_type || 'Activity'}
                    </span>
                  </td>
                  <td>{activity.user || 'N/A'}</td>
                  <td>{activity.duration || 'N/A'}</td>
                  <td>{activity.distance || 'N/A'}</td>
                  <td>
                    <strong>{activity.calories || 'N/A'}</strong>
                  </td>
                  <td>{activity.date ? new Date(activity.date).toLocaleDateString() : 'N/A'}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7" className="text-center text-muted py-4">
                  <em>No activities found. Start logging your workouts!</em>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
