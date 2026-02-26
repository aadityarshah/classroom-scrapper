// Docusaurus configuration - minimal starter with KaTeX support
module.exports = {
  title: 'Classroom Notes',
  tagline: 'Auto-generated, curated lecture notes',
  url: 'https://your-domain.com',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org',
  projectName: 'classroom-scrapper',
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [require('rehype-katex')]
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css')
        }
      }
    ]
  ],
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css',
      type: 'text/css'
    }
  ]
};
