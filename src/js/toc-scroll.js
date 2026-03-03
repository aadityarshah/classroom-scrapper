import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

if (ExecutionEnvironment.canUseDOM) {
  const scrollActiveIntoView = () => {
    const activeLink = document.querySelector('.table-of-contents__link--active');
    const tocContainer = document.querySelector('.theme-doc-toc-desktop');
    
    if (activeLink && tocContainer) {
      const containerRect = tocContainer.getBoundingClientRect();
      const activeRect = activeLink.getBoundingClientRect();

      // If the active link is above or below the visible area of the sticky TOC container
      if (activeRect.top < containerRect.top || activeRect.bottom > containerRect.bottom) {
        activeLink.scrollIntoView({
          behavior: 'smooth',
          block: 'nearest',
        });
      }
    }
  };

  // We use requestAnimationFrame to sync with Docusaurus's own scroll listener
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        scrollActiveIntoView();
        ticking = false;
      });
      ticking = true;
    }
  });
}
