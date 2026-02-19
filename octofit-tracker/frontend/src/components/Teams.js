import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams API URL:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results ? data.results : data;
        console.log('Teams processed data:', teamsData);
        setTeams(teamsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-5"><div className="loading-spinner"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-3">Loading teams...</p></div></div>;
  if (error) return <div className="container mt-5"><div className="alert alert-danger error-message" role="alert"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-5">
      <h2 className="mb-4">👥 Teams</h2>
      <div className="row">
        {teams.length > 0 ? (
          teams.map((team, index) => (
            <div key={team.id || index} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-header bg-primary text-white">
                  <h5 className="card-title mb-0 text-white">🏅 {team.name || 'Team'}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text">
                    <span className="text-muted">{team.description || 'No description available'}</span>
                  </p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      <small className="text-muted">Members</small>
                      <h4 className="mb-0">{team.member_count || 0}</h4>
                    </div>
                    <div className="text-end">
                      <small className="text-muted">Created</small>
                      <p className="mb-0">
                        <strong>{team.created_at ? new Date(team.created_at).toLocaleDateString() : 'N/A'}</strong>
                      </p>
                    </div>
                  </div>
                </div>
                <div className="card-footer bg-transparent">
                  <button className="btn btn-sm btn-outline-primary w-100">View Details</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <h4 className="alert-heading">No Teams Yet!</h4>
              <p>Be the first to create a team and start competing.</p>
              <hr />
              <button className="btn btn-primary">Create New Team</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Teams;
