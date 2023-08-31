// Wait for the DOM to be fully loaded
// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Wait for 5 seconds (5000 milliseconds)
    setTimeout(function() {
      // Find the element with the class 'tick-container' and add the class 'tick-stop'
      document.querySelector('.tick-container').classList.add('tick-stop');
      document.querySelector('.tick-circle').classList.add('hidden');

    }, 2000);
  });
  