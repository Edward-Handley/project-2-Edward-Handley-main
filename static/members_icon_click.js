//////////////MEMBERS ANIMATION/////////////////////
// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Add click event to the icon with id 'members-icon'
  document.getElementById('members-icon').addEventListener('click', function() {
    window.location.href = '/members';  // Redirect to the Members page
  });
});
