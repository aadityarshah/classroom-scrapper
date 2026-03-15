import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

/**
 * Re-render KaTeX in the given element.
 */
function renderKaTeX(element) {
  if (window.renderMathInElement && element) {
    window.renderMathInElement(element, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\(', right: '\\)', display: false},
        {left: '\\[', right: '\\]', display: true},
      ],
      throwOnError: false,
    });
  }
}

if (ExecutionEnvironment.canUseDOM) {
  const scrollActiveIntoView = () => {
    const activeLink = document.querySelector('.table-of-contents__link--active');
    const tocContainer = document.querySelector('.theme-doc-toc-desktop');
    
    if (activeLink && tocContainer) {
      const containerRect = tocContainer.getBoundingClientRect();
      const activeRect = activeLink.getBoundingClientRect();

      if (activeRect.top < containerRect.top || activeRect.bottom > containerRect.bottom) {
        activeLink.scrollIntoView({
          behavior: 'smooth',
          block: 'nearest',
        });
      }
    }
  };

  // Sync with scroll
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

  // Initial render for TOC
  const observer = new MutationObserver((mutations) => {
    const toc = document.querySelector('.table-of-contents');
    const sidebar = document.querySelector('.theme-doc-sidebar-container');
    if (toc) renderKaTeX(toc);
    if (sidebar) renderKaTeX(sidebar);
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
}

// Docusaurus client module exports
export function onRouteUpdate() {
  if (ExecutionEnvironment.canUseDOM) {
    setTimeout(() => {
      const toc = document.querySelector('.table-of-contents');
      const sidebar = document.querySelector('.theme-doc-sidebar-container');
      if (toc) renderKaTeX(toc);
      if (sidebar) renderKaTeX(sidebar);
    }, 100);
  }
}
