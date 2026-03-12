import React, {type ReactNode} from 'react';
import Layout from '@theme-original/DocItem/Layout';
import type LayoutType from '@theme/DocItem/Layout';
import type {WrapperProps} from '@docusaurus/types';
import {useDoc} from '@docusaurus/plugin-content-docs/client';

type Props = WrapperProps<typeof LayoutType>;

export default function LayoutWrapper(props: Props): ReactNode {
  const {metadata, frontMatter} = useDoc();
  
  // Only show download options if it's a lecture note (has lecture_number)
  const isLecture = !!frontMatter.lecture_number;

  const githubRepoUrl = "https://github.com/aadityarshah/classroom-scrapper";
  const sourcePath = metadata.source.replace("@site/", "");
  const mdDownloadUrl = `${githubRepoUrl}/blob/main/${sourcePath}?raw=true`;

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="doc-layout-wrapper">
      {isLecture && (
        <div className="lecture-header-actions">
          <div className="download-pills">
            <a 
              href={mdDownloadUrl}
              target="_blank" 
              rel="noopener noreferrer"
              className="download-pill md-pill"
              title="Download Markdown"
            >
              <span className="pill-icon">M↓</span> .md
            </a>
            <button 
              onClick={handlePrint}
              className="download-pill pdf-pill"
              title="Save as PDF"
            >
              <span className="pill-icon">PDF</span> .pdf
            </button>
          </div>
        </div>
      )}
      <Layout {...props} />
    </div>
  );
}
