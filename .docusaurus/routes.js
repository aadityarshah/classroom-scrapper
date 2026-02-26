import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/search',
    component: ComponentCreator('/search', '822'),
    exact: true
  },
  {
    path: '/',
    component: ComponentCreator('/', '009'),
    routes: [
      {
        path: '/',
        component: ComponentCreator('/', 'f77'),
        routes: [
          {
            path: '/tags',
            component: ComponentCreator('/tags', 'ce1'),
            exact: true
          },
          {
            path: '/tags/exact-equations',
            component: ComponentCreator('/tags/exact-equations', '548'),
            exact: true
          },
          {
            path: '/tags/first-order-od-es',
            component: ComponentCreator('/tags/first-order-od-es', '08b'),
            exact: true
          },
          {
            path: '/tags/homogeneous-equations',
            component: ComponentCreator('/tags/homogeneous-equations', 'f65'),
            exact: true
          },
          {
            path: '/tags/initial-value-problems',
            component: ComponentCreator('/tags/initial-value-problems', '47d'),
            exact: true
          },
          {
            path: '/tags/modeling',
            component: ComponentCreator('/tags/modeling', '952'),
            exact: true
          },
          {
            path: '/tags/od-es',
            component: ComponentCreator('/tags/od-es', '1b2'),
            exact: true
          },
          {
            path: '/tags/ordinary-differential-equations',
            component: ComponentCreator('/tags/ordinary-differential-equations', '00d'),
            exact: true
          },
          {
            path: '/tags/solutions',
            component: ComponentCreator('/tags/solutions', '161'),
            exact: true
          },
          {
            path: '/',
            component: ComponentCreator('/', 'f21'),
            routes: [
              {
                path: '/MA 104 Ordinary Differential Equations/Lec_01_Introduction to ODEs and First Order Equations',
                component: ComponentCreator('/MA 104 Ordinary Differential Equations/Lec_01_Introduction to ODEs and First Order Equations', '931'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/',
                component: ComponentCreator('/', '84d'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
