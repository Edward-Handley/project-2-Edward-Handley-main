//////////////MEMBERS ANIMATION/////////////////////
// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Add click event to the icon with id 'members-icon'
  document.getElementById('members-icon').addEventListener('click', function() {
    window.location.href = '/members';  // Redirect to the Members page
  });

  // Add click event to the icon with id 'members-icon'
  document.getElementById('team-icon').addEventListener('click', function() {
    window.location.href = '/team';  // Redirect to the Members page
  });

  document.getElementById('venue-icon').addEventListener('click', function() {
    window.location.href = '/venue';  // Redirect to the Members page
  });
  document.getElementById('training-icon').addEventListener('click', function() {
    window.location.href = '/trainings';  // Redirect to the Members page
  });
  document.getElementById('dashboard-icon').addEventListener('click', function() {
    window.location.href = '/dashboard';  // Redirect to the Members page
  });
  document.getElementById('sponsor-icon').addEventListener('click', function() {
    window.location.href = '/sponsor';  // Redirect to the Members page
  });

});


