// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Classroom Notes',
  tagline: 'AI-Generated Academic Insights',
  url: 'https://your-github-username.github.io',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org',
  projectName: 'classroom-scrapper',

  markdown: {
    // Smart format: Use 'md' for notes to support LaTeX/braces, 'mdx' for homepage
    format: 'detect', 
    mermaid: true,
    // @ts-ignore
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    }
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.mjs',
          routeBasePath: '/',
          breadcrumbs: false, // Removes the "Index" text from above the notes
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
      type: 'text/css',
    },
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Classroom Notes',
        logo: {
          alt: 'Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'index',
            position: 'left',
            label: 'Home',
          },
          {
            href: 'https://github.com/your-github-username/classroom-to-gh-pages',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} Classroom Scrapper.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
    }),

  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        indexPages: true,
        language: ["en"],
        docsRouteBasePath: "/",
      },
    ],
  ],
};

export default config;
