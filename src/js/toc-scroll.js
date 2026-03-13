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

  const renderLatexInTOC = () => {
    const tocLinks = document.querySelectorAll('.table-of-contents__link, .theme-doc-toc-mobile .table-of-contents__link');
    if (tocLinks.length === 0 || !window.renderMathInElement) return;

    tocLinks.forEach(link => {
      // Avoid re-rendering
      if (link.querySelector('.katex')) return;

      let html = link.innerHTML;
      let changed = false;

      // 1. Recovery: If Docusaurus stripped delimiters but left LaTeX commands
      // We look for common patterns like mathbf{X}, \mathbf{X}, alpha, \alpha
      const commands = ['mathbf', 'mathbb', 'mathcal', 'sqrt', 'frac', 'alpha', 'beta', 'gamma', 'delta', 'theta', 'mu', 'sigma', 'pi', 'lambda', 'phi', 'omega'];
      
      commands.forEach(cmd => {
        // Regex to find command (optionally with backslash) not already in $
        // Handles: mathbf{X}, \mathbf{X}, \alpha, alpha
        // We use a simpler regex to avoid lookbehind issues in older browsers if any
        const regex = new RegExp('(\\\\?' + cmd + '(\\{[^{}]+\\}|\\b))', 'g');
        
        // Only replace if NOT already wrapped in $
        // We do a simple check: is there a $ before and after?
        // This is a heuristic but works for Docusaurus TOC
        if (!html.includes('$') || !html.includes(cmd)) {
          html = html.replace(regex, (match) => {
            // Ensure backslash is present
            const withBackslash = match.startsWith('\\') ? match : '\\' + match;
            return '$' + withBackslash + '$';
          });
          changed = true;
        }
      });

      if (changed) {
        link.innerHTML = html;
      }

      // 2. Trigger KaTeX
      window.renderMathInElement(link, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ],
        throwOnError: false
      });
    });
  };

  // Run on scroll for active link tracking
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

  // Watch for DOM changes to re-render LaTeX in TOC (e.g., on navigation)
  const observer = new MutationObserver((mutations) => {
    let shouldRender = false;
    for (const mutation of mutations) {
      if (mutation.addedNodes.length > 0) {
        // Check if TOC or content was added
        for (const node of mutation.addedNodes) {
          if (node.nodeType === 1 && (
            node.querySelector('.table-of-contents') || 
            node.classList.contains('table-of-contents') ||
            node.querySelector('.theme-doc-markdown')
          )) {
            shouldRender = true;
            break;
          }
        }
      }
      if (shouldRender) break;
    }
    if (shouldRender) {
      setTimeout(renderLatexInTOC, 100);
    }
  });

  // Initial and periodic rendering to ensure KaTeX catches up with Docusaurus hydration
  const init = () => {
    renderLatexInTOC();
    // Observe changes
    observer.observe(document.body, { childList: true, subtree: true });
  };

  if (document.readyState === 'complete') {
    init();
  } else {
    window.addEventListener('load', init);
  }
  
  // Re-run periodically for the first few seconds to handle slow hydration
  let count = 0;
  const interval = setInterval(() => {
    renderLatexInTOC();
    if (++count > 10) clearInterval(interval);
  }, 1000);
}
