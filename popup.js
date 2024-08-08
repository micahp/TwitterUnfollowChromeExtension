document.getElementById('navigate').addEventListener('click', () => {
    chrome.tabs.create({ url: 'https://twitter.com/geoppls/following' });
  });
  
  document.getElementById('unfollow').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: unfollowAll
      });
    });
  });
  
  function unfollowAll() {
    const followingList = document.querySelector('div[aria-label="Timeline: Following"]');
    if (followingList) {
      const unfollowButtons = followingList.querySelectorAll('button[data-testid*="unfollow"]');
      console.log(unfollowButtons);
      
      unfollowButtons.forEach(button => {
        button.click();
        // Wait for the confirmation popup and click the confirm button
        setTimeout(() => {
          const confirmButton = document.querySelector('button[role="button"][data-testid*="confirmationSheetConfirm"]');
          if (confirmButton) {
            confirmButton.click();
          }
        }, 1000); // Adjust the timeout as needed
      });

      setTimeout(() => {
        alert(`Unfollowed ${unfollowButtons.length} users. Please refresh the page and click the button again if needed.`);
      }, 3000); // Adjust the timeout as needed
    } else {
      alert('Could not find the following list. Please make sure you are on the correct page.');
    }
  }