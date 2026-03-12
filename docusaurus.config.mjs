// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

/**
 * Custom Remark plugin to use 'lecture_name' as the card description
 * without requiring a separate 'description' field in Markdown.
 */
const lectureNameAsDescription = () => {
  return (tree, file) => {
    // @ts-ignore
    const frontMatter = file.data.frontMatter;
    if (frontMatter && frontMatter.lecture_name && !frontMatter.description) {
      frontMatter.description = frontMatter.lecture_name;
    }
  };
};

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Classroom Notes',
  tagline: 'AI-Generated Academic Insights',
  url: 'https://aadityarshah.github.io',
  baseUrl: '/classroom-scrapper/',
  onBrokenLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'AadityaRushabhShah',
  projectName: 'classroom-scrapper',
  trailingSlash: false,

  clientModules: ['./src/js/toc-scroll.js'],

  markdown: {
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
          breadcrumbs: false,
          remarkPlugins: [remarkMath, lectureNameAsDescription],
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
    {
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap',
      type: 'text/css',
    },
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 4,
      },
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
            href: 'https://github.com/aadityarshah/classroom-scrapper',
            position: 'right',
            className: 'header-github-link',
            'aria-label': 'GitHub repository',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Developed by <b>Aaditya Rushabh Shah</b><br/>Copyright © ${new Date().getFullYear()} Classroom Scrapper.`,
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
    // Search plugin temporarily disabled due to build error build/.html
    /*
    [
      "@easyops-cn/docusaurus-search-local",
      {
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        indexPages: true,
        language: ["en"],
        docsRouteBasePath: "/",
      },
    ],
    */
  ],
};

export default config;
