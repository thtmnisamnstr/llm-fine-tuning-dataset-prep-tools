Quick recap. My personal website sucks. I'm updating it using [Gatsby](https://www.gatsbyjs.org) and the [Novela theme](https://github.com/narative/gatsby-theme-novela) by narative, because it's popular, and I'm basic.

* **[GitHub Repo for this website](https://github.com/thtmnisamnstr/thtmnisamnstr-dotcom)**
* **[My personal website](https://thtmnisamnstr.com)**

*FYI, I'm using a Mac, so there may be some Mac-specific commands.*
  

Alright, part 2, customizing your site. Part 1 was very entry-level, very basic. Part 2 is much more involved. Part 2 is where you make your site your own. Let's not waste any more time. Let's get started.

## Update your site metadata
* In Terminal, cd to your website directory
* `git checkout -b initial_customizations`

Your terminal output should be something like the following.
```
Switched to a new branch 'initial_customizations'
```
* Open `gatsby-config.js` in your code editor (I use [Visual Studio Code](https://code.visualstudio.com/))
  * Update your site metadata and save. Here's mine.

```
module.exports = {
  siteMetadata: {
    title: `thtmnisamnstr`,
    name: `thtmnisamnstr`,
    siteUrl: `https://thtmnisamnstr.com/`,
    description: `Gavin Johnson's personal site. Resume, blog posts, tech product marketing stuff, maybe some tech-y stuff too.`,
    hero: {
      heading: `Hi. I'm Gavin. My handle is usually thtmnisamnstr. This is my site.`,
      maxWidth: 652,
    },
    social: [
      {
        name: `twitter`,
        url: `https://twitter.com/gavinjtech`,
      },
      {
        name: `devto`,
        url: `https://dev.to/thtmnisamnstr`,
      },
      {
        name: `github`,
        url: `https://github.com/thtmnisamnstr`,
      },
      {
        name: `linkedin`,
        url: `https://www.linkedin.com/in/gavin-johnson/`,
      },
      {
        name: `instagram`,
        url: `https://www.instagram.com/thtmnisamnstr`,
      },
    ],
  },
  plugins: [
    {
      resolve: "@narative/gatsby-theme-novela",
      options: {
        contentPosts: "content/posts",
        contentAuthors: "content/authors",
        basePath: "/",
        authorsPage: true,
        sources: {
          local: true,
        },
      },
    },
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `Novela by Narative`,
        short_name: `Novela`,
        start_url: `/`,
        background_color: `#fff`,
        theme_color: `#fff`,
        display: `standalone`,
        icon: `src/assets/favicon.png`,
      },
    },
    {
      resolve: `gatsby-plugin-netlify-cms`,
      options: {
      },
    },
  ],
};

```

*I also changed the favicon,*`././src/assets/favicon.png`

## Add your author info
* Add your author info for your author page
  * Create a new file under `./content/authors/`
    * Name it `authors.yml` and add your `name`, `bio`, `avatar`, `featured`, `social` parameters, and save. Here's mine.
```
- name: Gavin Johnson
  bio: |
    Gavin is a programmer-turned-marketer with experience in IT, consulting, and marketing. 
    He has been at New Relic since 2018, focusing his time and efforts on helping New Relic 
    be more open and telling New Relic's open source story. Gavin started his career as a 
    programmer and sys admin prior to attending business school at the University of Southern 
    California. Following b-school, he worked for Deloitte Digital as a Senior Consultant and 
    Manager, designing and delivering custom applications for clients. He then moved to AT&T, 
    working as a Lead Product Marketing Manager for their digital video products. Gavin is an 
    Oregon native but has made Los Angeles his home since 2009. He is a happily married, 
    Brazilian Jiu Jitsu purple belt, film photographer, homebrewer, and former marathoner.
  shortBio: |
    Open Source marketing person at New Relic. Ex-AT&T marketer. Ex-Deloitte consultant. Ex-sys 
    admin. (Sometimes)Ex-developer.
  avatar: ./avatars/gavin-johnson.jpg
  social:
    - url: https://twitter.com/gavinjtech
    - url: https://dev.to/thtmnisamnstr
    - url: https://github.com/thtmnisamnstr
    - url: https://www.linkedin.com/in/gavin-johnson/
    - url: https://www.instagram.com/thtmnisamnstr
  featured: true
```
  * Create a new folder under `./content/authors/`. Name it `avatars`.
  * Add your avatar image to `./content/authors/avatars/`. Name it `[your-name].jpg`. Here's mine.

* Update the existing example blog post to use your author info
  * Open `./content/posts/2020-01-01-my-first-post-using-novela-by-narative/index.md`
    * Change the `author` parameter to [your name] and save. Here's the first few lines of mine.
```
```

* Delete the example author files
  * Delete `./content/authors/authors/` and all files under it

## Change the site logo
* I'm changing the site logo to simple text by shadowing the Logo component.
  * In your root directory, `mkdir -p './src/@narative/gatsby-theme-novela/components/Logo/'`
  * `cp './node_modules/@narative/gatsby-theme-novela/src/components/Logo/Logo.tsx' './src/@narative/gatsby-theme-novela/components/Logo/Logo.tsx'`
  * Open `./src/@narative/gatsby-theme-novela/components/Logo/Logo.tsx`
  * Update your SVG info and save. Here's mine.

```
import React from "react";
import styled from "@emotion/styled";

import mediaqueries from "@styles/media";

import { Icon } from '@types';

const Logo: Icon = ({ fill = "white" }) => {
  return (
    
      
        {/* Gavin 20200719: Changed SVG logo to text */}
        
          thtmnisamnstr
        
        
          
            
          
        
      

      
        
          thtmnisamnstr
        
      
    
  );
};

export default Logo;

const LogoContainer = styled.div`
  .Logo__Mobile {
    display: none;
  }

  ${mediaqueries.tablet`
    .Logo__Desktop {
      display: none;
    }
    
    .Logo__Mobile{
      display: block;
    }
  `}
`;
```

* Run `gatsby develop` to see what your site looks like. Here's mine.

I don't love how big the bio text is. I want a short bio. So I'mma add a new key to the Authors YAML, `shortBio`, and put that in the Featured Author section.
* Add shortBio to the authors YAML
  * Open `/content/authors/authors.yml`
  * Add a short bio. Here's my authors file.

```
- name: Gavin Johnson
  bio: |
    Gavin is a programmer-turned-marketer with experience in IT, consulting, and marketing. 
    He has been at New Relic since 2018, focusing his time and efforts on helping New Relic 
    be more open and telling New Relic's open source story. Gavin started his career as a 
    programmer and sys admin prior to attending business school at the University of Southern 
    California. Following b-school, he worked for Deloitte Digital as a Senior Consultant and 
    Manager, designing and delivering custom applications for clients. He then moved to AT&T, 
    working as a Lead Product Marketing Manager for their digital video products. Gavin is an 
    Oregon native but has made Los Angeles his home since 2009. He is a happily married, 
    Brazilian Jiu Jitsu purple belt, film photographer, homebrewer, and former marathoner.
  shortBio: |
    Open Source marketing person at New Relic. Ex-AT&T marketer. Ex-Deloitte consultant. Ex-sys 
    admin. (Sometimes)Ex-developer.
  avatar: ./avatars/gavin-johnson.jpg
  social:
    - url: https://twitter.com/gavinjtech
    - url: https://dev.to/thtmnisamnstr
    - url: https://github.com/thtmnisamnstr
    - url: https://www.linkedin.com/in/gavin-johnson/
    - url: https://www.instagram.com/thtmnisamnstr
  featured: true
```

## Add a short bio to the Author markdown for use in the featured author component
* Shadow the Bio component, `Bio.tsx`
  * In your root directory, `mkdir -p './src/@narative/gatsby-theme-novela/components/Bio/'`
  * `cp './node_modules/@narative/gatsby-theme-novela/src/components/Bio/Bio.tsx' './src/@narative/gatsby-theme-novela/components/Bio/Bio.tsx'`
  * Open `./src/@narative/gatsby-theme-novela/components/Bio/Bio.tsx`
  * Change `author.bio` to `author.shortBio` and save. Here's mine.

```
import React from 'react';
import { Link } from 'gatsby';
import styled from '@emotion/styled';

import Image from '@components/Image';
import { IAuthor } from '@types';

const Bio: React.FC = ({ author }) => {
  return (
    
      
        
          
        
      
       {/* Gavin, 20200719: Changed to shortBio */}
      
    
  );
};

export default Bio;

const BioContainer = styled.div`
  display: flex;
  align-items: center;
  position: relative;
  left: -10px;
`;

const BioAvatar = styled.div`
  display: block;
  position: relative;
  height: 40px;
  width: 40px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.25);
  margin-right: 16px;
  margin: 10px 26px 10px 10px;

  &::after {
    content: '';
    position: absolute;
    left: -5px;
    top: -5px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 1px solid rgba(0, 0, 0, 0.25);
  }

  &[data-a11y='true']:focus::after {
    content: '';
    position: absolute;
    left: -5px;
    top: -5px;
    width: 50px;
    height: 50px;
    border: 2px solid ${p => p.theme.colors.accent};
  }
`;

const RoundedImage = styled(Image)`
  border-radius: 50%;
`;

const BioAvatarInner = styled.div`
  height: 40px;
  width: 40px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.25);
  margin-right: 16px;
  overflow: hidden;
`;

const BioText = styled.p`
  max-width: 430px;
  font-size: 14px;
  line-height: 1.45;
  color: ${p => p.theme.colors.grey};

  a {
    color: ${p => p.theme.colors.grey};
    text-decoration: underline;
  }
`;
```

* Shadow the `IAuthor` interface in `index.d.ts`
  * In your root directory, `mkdir -p './src/@narative/gatsby-theme-novela/types/'`
  * `cp './node_modules/@narative/gatsby-theme-novela/src/types/index.d.ts' './src/@narative/gatsby-theme-novela/types/index.d.ts'`
  * Open `./src/@narative/gatsby-theme-novela/types/index.d.ts`
  * Add `shortBio` to your `IAuthor` interface and save. Here's mine.

```
import React from "react";

export interface IPaginator {
  pageCount: number;
  index: number;
  pathPrefix: string;
}

interface IGatsbyImage {
  src: string;
  base64?: string;
  srcWebp?: string;
  srcSet?: string;
  srcSetWebp?: string;
  tracedSVG?: string;
}

interface IGatsbyImageFluid extends IGatsbyImage {
  maxHeight: number;
  maxWidth: number;
}

interface IGatsbyImageFixed extends IGatsbyImage {
  height: number;
  width: number;
}

export interface IAuthor {
  authorsPage?: boolean;
  featured?: boolean;
  name: string;
  slug: string;
  bio: string;
  // Gavin, 20200719: Added shortBio
  shortBio: string;
  avatar: {
    image: IGatsbyImageFluid;
    full: IGatsbyImageFluid;
  };
}

export interface IArticle {
  slug: string;
  authors: IAuthor[];
  excerpt: string;
  body: string;
  id: string;
  hero: {
    full: IGatsbyImageFluid;
    preview: IGatsbyImageFluid;
    regular: IGatsbyImageFluid;
    seo: string;
  };
  timeToRead: number;
  date: string;
  secret: boolean;
}

interface IArticleQuery {
  edges: {
    node: IArticle;
  }[];
}

export interface IProgress {
  height: number;
  offset: number;
  title: string;
  mode: string;
  onClose?: () => void;
}

export type Icon = React.FC

export type Template = React.FC
```

* The correct thing to do next would be to shadow `data.query.js` and add the `shortBio` field, but that isn't working for some reason. So let's do it directly in the Novela theme module.
  * Open `./node_modules/@narative/gatsby-theme-novela/src/gatsby/data/data.query.js`
  * Add `shortBio` to your author queries and save. Here's mine.

```
/* eslint-disable */

// https://github.com/gatsbyjs/gatsby/blob/master/packages/gatsby-transformer-sharp/src/fragments.js

const GatsbyFluid_withWebp = `
  base64
  aspectRatio
  src
  srcSet
  srcWebp
  srcSetWebp
  sizes
`;

module.exports.local = {
  articles: `{
    articles: allArticle(
      sort: { fields: [date, title], order: DESC }
      limit: 1000
    ) {
      edges {
        node {
          id
          slug
          secret
          title
          author
          date(formatString: "MMMM Do, YYYY")
          dateForSEO: date
          timeToRead
          excerpt
          canonical_url
          subscription
          body
          hero {
            full: childImageSharp {
              fluid(maxWidth: 944, quality: 100) {
                ${GatsbyFluid_withWebp}
              }
            }
            regular: childImageSharp {
              fluid(maxWidth: 653, quality: 100) {
                ${GatsbyFluid_withWebp}
              }
            }
            narrow: childImageSharp {
              fluid(maxWidth: 457, quality: 100) {
                ${GatsbyFluid_withWebp}
              }
            }
            seo: childImageSharp {
              fixed(width: 1200, quality: 100) {
                src
              }
            }
          }
        }
      }
    }
  }`,
  authors: `{
    authors: allAuthor {
      edges {
        node {
          authorsPage
          bio
          shortBio
          id
          name
          featured
          social {
            url
          }
          slug
          avatar {
            small: childImageSharp {
              fluid(maxWidth: 50, quality: 100) {
                ${GatsbyFluid_withWebp}
              }
            }
            medium: childImageSharp {
              fluid(maxWidth: 100, quality: 100) {
                ${GatsbyFluid_withWebp}
              }
            }
            large: childImageSharp {
              fluid(maxWidth: 328, quality: 100) {
                ${GatsbyFluid_withWebp}
              }
            }
          }
        }
      }
    }
  }`,
};

module.exports.contentful = {
  articles: `{
    articles: allContentfulArticle(sort: {fields: [date, title], order: DESC}, limit: 1000) {
      edges {
        node {
          body {
            childMdx {
              body
              timeToRead
            }
          }
          excerpt
          title
          slug
          secret
          date(formatString: "MMMM Do, YYYY")
          dateForSEO: date
          hero {
            full: fluid(maxWidth: 944, quality: 100) {
              ${GatsbyFluid_withWebp}
            }
            regular: fluid(maxWidth: 653, quality: 100) {
              ${GatsbyFluid_withWebp}
            }
            narrow: fluid(maxWidth: 457, quality: 100) {
              ${GatsbyFluid_withWebp}
            }
            seo: fixed(width: 1200, quality: 100) {
              src
            }
          }
          id
          author {
            name
          }
        }
      }
    }
  }
  `,
  authors: `{
    authors: allContentfulAuthor {
      edges {
        node {
          avatar {
            small: fluid(maxWidth: 50, quality: 100) {
              ${GatsbyFluid_withWebp}
            }
            medium: fluid(maxWidth: 100, quality: 100) {
              ${GatsbyFluid_withWebp}
            }
            large: fluid(maxWidth: 328, quality: 100) {
              ${GatsbyFluid_withWebp}
            }
          }
          fields {
            authorsPage
            slug
          }
          bio
          shortBio
          id
          name
          social
          featured
        }
      }
    }
  }`,
};
```

* Because `data.query.js` couldn't be shadowed, add the Novela theme under `node_modules` to your git repo
  * Open `./.gitignore`
  * Update to include the Novela theme folder in your repo and save. Here's mine.

```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage

# nyc test coverage
.nyc_output

# Grunt intermediate storage (http://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (http://nodejs.org/api/addons.html)
build/Release

# Dependency directories
jspm_packages/
# Gavin, 20200719: Including the Novela theme directory under node_modules
node_modules/*
!node_modules/@narative/
node_modules/@narative/*
!node_modules/@narative/gatsby-theme-novela/

# Typescript v1 declaration files
typings/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# dotenv environment variables file
.env

# gatsby files
.cache/
public

# Mac files
.DS_Store

# Yarn
yarn-error.log
.pnp/
.pnp.js
# Yarn Integrity file
.yarn-integrity

.netlify/
```

* Run `gatsby develop` to see what your site looks like. Here's mine.

* Click on the author avatar to go to the Author page. Note that it still uses the standard `bio` field. This is what I was aiming for. Here's mine.

## Add a resume page and navigation
I also want a resume page as well. I could go and create a new content type, update the query to include it, add it to `createPages`, ..., or I could create a static page, but I just want a resume I can write in markdown and direct-link to. Plus, I'm trying to learn Gatsby anyway, so I'm going to make a resume page by making a secret post that includes a slug.
* Create a secret post for the resume page
  * `mkdir -p './content/posts/SECRET-20200719-Resume/images/'`
  * `touch './content/posts/SECRET-20200719-Resume/index.md'`
  * Open `./content/posts/SECRET-20200719-Resume/index.md`
  * Write your resume and save make sure you set `secret: true` and `slug: [first]-[last]-resume`. Here's mine.

```
*Experienced marketer and strategist with a record of approaching business questions through an analytical lens and driving action through that analysis.*
* *Data analysis and data driven decision making*
* *Marketing strategy and content development*
* *Executive presentation and public speaking*
* *Technical background, both as a dev and dev lead*

## Experience

### New Relic *-- Los Angeles, CA (Remote)*
#### Principal Product Marketing Manager, Open Source *-- May 2020-Present*
Led go-to-market strategy and execution for [New Relic Open Source](https://opensource.newrelic.com) and for [New Relic's open source instrumentation](https://blog.newrelic.com/product-news/introducing-open-source-agents-and-projects/).
#### Principal Solutions Marketing Manager, Digital Customer Experience (now Digital Experience Management) *-- November 2018-May 2020*
Built the strategy for New Relic’s Digital Customer (DCX) solution and executed on it. Led creation of DCX Marketing and Sales content. Integrated DCX into New Relic’s campaigns and tactics. Represented New Relic as an external speaker.
* Built New Relic’s DCX solution strategy. Analyzed internal and external content developed for and tactics previously used by other New Relic solutions. Performed competitive analysis. Developed a DCX content and tactics roadmap and calendar.
* Wrote New Relic’s DCX solution positioning and messaging. Described how we wanted the DCX solution perceived by the market, who our targeted personas were, and wrote taglines, copy blocks, and email templates for use by Marketing and Sales.
* Created DCX solution content for Sales. Collaborated with the solution consulting group from Sales to build industry specific DCX content (e.g. pitch decks, solution guide decks, industry primers, discovery questions, objection handling, etc.). Targeted four industries: Media, Retail, FinServ, and Travel.
* Integrated DCX solution into Marketing campaigns and tactics. Worked cross-functionally with demand generation, content and creative, digital marketing, and field marketing. Led creation of and co-wrote content (e.g. articles, solution sheets, white papers, etc.) and landing pages. Developed an event response campaign and cadence.
* Represented New Relic as an external speaker. Presented on the importance of DCX for modern, digital businesses and connecting technical application performance to business outcomes. Presented at New Relic’s FutureStack Los Angeles 2019, WP Engine Summit 2019, and Gartner IT Symposium Xpo 2019.

### AT&T Mobility & Entertainment *-- El Segundo, CA*
#### Lead Product Marketing Manager, Video Lifecycle Strategy *-- June 2017-November 2018*
Built analytical models and business cases for strategic project analysis. Managed enablement projects for product go-to-market, ensuring ancillary systems and processes worked correctly for customers.
* Built the analytical model and business case that got Netflix on AT&T TV’s upcoming streaming box. Built analytical scenario model comparing multiple levels of integration with Netflix. Collaborated across teams in Marketing and Corporate Strategy to align on assumptions, key takeaways, and to build the executive presentation deck.
* Developed product sunsetting strategy for AT&T’s IPTV service. Built a yearly profitability model for the IPTV service. Used existing subscriber and revenue as well as churn and churn acceleration projections to project revenue 5 years forward. Collaborated with engineering to build a 5-year IPTV cost projection model.
* Managed product enablement projects. Insured customer-impacting issues did not occur because of internal, cross-team coordination issues. (e.g. Got a customer authentication feature for AT&T TV’s upcoming streaming box in the product backlog, engaged a 3rd party to provide at-home delivery for AT&T TV’s upcoming streaming box, etc.).
* Built profitability models, business cases, and recommendations for VP and SVP-initiated innovation proposals (e.g. TV service for Cricket Mobile customers, a hyperlocal video service, etc.).

### Deloitte Digital / Deloitte Consulting (*Los Angeles, CA*)
#### Manager, Consulting *-- August 2016-June 2017*
Trusted partner to clients, consulting at Fox for ~2 years. Led teams to create, expand, and maintain custom-built business applications for a diverse set of companies, from startup (Human Longevity Inc.) to Fortune 10 (AT&T).
* Led expansion and maintenance of Fox Theatrical’s global release planning application. Managed two different teams of onshore and offshore consultants and developers through two major expansion projects. Led a cross-functional teams of marketing users, IT leadership, and our consultants through the entire SDLC for each project.
* Served as a trusted client partner. Traveled with my primary client at Fox to Europe and Asia to introduce Global Marketing to major updates of the global release planning application and promote application use in non-Domestic regions. Also used these trips to gather first-hand feedback on the application that informed future features and fixes.
* Recognized with “Extraordinary Moments” award from company leadership for being a company-wide top performer at my level multiple years consecutively.
#### Senior Consultant *-- July 2014-August 2016*
* Managed tech consulting projects for a variety of companies. Led teams of business analysts, consultants, and developers through project design and delivery (e.g. Led a team through development of a digital marketing transformation roadmap for a major grocery wholesaler, led a team through the deployment of a tailored Salesforce CRM application for a biotech startup, etc.).
#### Summer Associate (*June 2013-August 2013*)
* Defined program management processes and quality management plan for a multi-project, customer service enhancement program at T-Mobile. Established PMO reporting templates and cadence.

### National Technical Systems *-- Calabasas, CA*
#### Microsoft Dynamics ERP Administrator *-- June 2009-July 2012*
Led a cross-company ERP implementation serving 600+ business users at 20+ facilities. Managed 2 internal developers and 7 consultants through design, development, and delivery of system customizations.
* Led cross-functional team of business users from finance, sales, marketing, operations, and IT; developers; and consultants to consolidate fragmented CRM, sales, and financial systems into a single ERP system.
* Owned yearly project CapEx budget for the ERP system. Worked with CIO to build yearly CapEx requests. Managed hardware purchases, software licensing, 3rd party add-on licensing, and consulting costs.

### Timber Products Company *-- Springfield, OR*
#### Computer Programmer / Analyst  *-- June 2007-June 2009*
Collaborated with business users from inventory management, sales, logistics, accounting, and finance to design, development, and delivery of enhancements to the company’s Microsoft Dynamics ERP system.

### ViewPlus Technologies *-- Corvallis, OR*
#### Product Development Assistant *-- November 2004-June 2007*
Developed testing protocols for and tested Braille printer drivers and firmware for release. Developed a text-to-Braille application for release.

## Education

### University of Southern California
#### MBA, Masters of Business Administration *-- Graduated May 2014*
* Beta Gamma Sigma, Business Honor Society.
* Program Lead, Marshall Case Competition Program.
  * Trained fellow MBA candidates on how to compete in case competitions, and coached case competition teams. Program achieved 89% participation rate for the class of 2015.
* Asia-Pacific Economic Cooperation (APEC), Business Advisory Council Research Project. Foreign Direct Investment across APEC: Impediments and Opportunities for Improvement.
  * Large, 12-person, MBA research project sponsored by and presented to APEC.
  * Led data analysis team. Sourced and sanitized data, built SQL database, developed data analysis methodology, and led team of 3 MBA candidates though creation of country data analysis slides.
* Director of Technology Consulting, Marshall Consulting & Strategy Club.
* Business of Entertainment Graduate Certificate from the USC School of Cinematic Arts.

### Oregon State University
#### BS, Computer Science *-- Graduated June 2007*
* Cum Laude.
* Upsilon Pi Epsilon, Computer Science Honor Society.
Other
```

I also want to change the default behavior of posts to not have a hero image if one isn't defined, like in the resume post.
* Shadow the `Article.Hero.tsx` section component
  * In your root directory, `mkdir -p './src/@narative/gatsby-theme-novela/sections/article/'`
  * `cp -R './node_modules/@narative/gatsby-theme-novela/src/sections/article/' './src/@narative/gatsby-theme-novela/sections/article/'`

*Yes, you have to shadow all the damn files in the folder even though you really only want to change one."*

  * Open './src/@narative/gatsby-theme-novela/sections/article/Article.Hero.tsx'
  * Update to not render hero image if none is specified and save. Here's mine.

```
import React from 'react';
import styled from '@emotion/styled';

import Headings from '@components/Headings';
import Image, { ImagePlaceholder } from '@components/Image';

import mediaqueries from '@styles/media';
import { IArticle, IAuthor } from '@types';

import ArticleAuthors from './Article.Authors';

interface ArticleHeroProps {
  article: IArticle;
  authors: IAuthor[];
}

const ArticleHero: React.FC = ({ article, authors }) => {
  const hasCoAUthors = authors.length > 1;
  const hasHeroImage =
    article.hero &&
    Object.keys(article.hero.full).length !== 0 &&
    article.hero.full.constructor === Object;

  return (
    
      
        {article.title}
        
          
          
            {article.date} · {article.timeToRead} min read
          
        
      
      
        {hasHeroImage && (
          
        )}
      
    
  );
};

export default ArticleHero;

const Hero = styled.div`
  ${p => mediaqueries.phablet`
    &::before {
      content: "";
      width: 100%;
      height: 20px;
      background: ${p.theme.colors.primary};
      position: absolute;
      left: 0;
      top: 0;
      transition: ${p.theme.colorModeTransition};
    }

    &::after {
      content: "";
      width: 100%;
      height: 10px;
      background: ${p.theme.colors.background};
      position: absolute;
      left: 0;
      top: 10px;
      border-top-left-radius: 25px;
      border-top-right-radius: 25px;
      transition: ${p.theme.colorModeTransition};
    }
  `}
`;

const ArticleMeta = styled.div`
  margin-left: ${p => (p.hasCoAUthors ? '10px' : '0')};

  ${mediaqueries.phablet`
    margin-left: 0;
  `}
`;

/* Gavin 20200722: Reduced bottom margin on the Header because it looked too
  big w/ no hero */
const Header = styled.header`
  position: relative;
  z-index: 10;
  margin:50px auto 120px;
  padding-left: 68px;
  max-width: 749px;

  ${mediaqueries.desktop`
    padding-left: 53px;
    max-width: calc(507px + 53px);
    margin: 50px auto 70px;
  `}

  ${mediaqueries.tablet`
    padding-left: 0;
    margin: 50px auto 70px;
    max-width: 480px;
  `}

  ${mediaqueries.phablet`
    margin: 50px auto 180px;
    padding: 0 40px;
  `}

  @media screen and (max-height: 700px) {
    margin: 50px auto;
  }
`;

const HeroHeading = styled(Headings.h1)`
  font-size: 48px;
  font-family: ${p => p.theme.fonts.serif};
  margin-bottom: 25px;
  font-weight: bold;
  line-height: 1.32;

  ${mediaqueries.tablet`
    margin-bottom: 20px;
    font-size: 36px;
  `}

  ${mediaqueries.phablet`
    font-size: 32px;
  `}
`;

const HeroSubtitle = styled.div`
  position: relative;
  display: flex;
  font-size: 18px;
  color: ${p => p.theme.colors.grey};

  ${p => mediaqueries.phablet`
    font-size: 14px;
    flex-direction: column;

    ${p.hasCoAUthors &&
      `
        &::before {
          content: '';
          position: absolute;
          left: -20px;
          right: -20px;
          top: -10px;
          bottom: -10px;
          border: 1px solid ${p.theme.colors.horizontalRule};
          opacity: 0.5;
          border-radius: 5px;
        }
    `}

    strong {
      display: block;
      font-weight: 500;
      margin-bottom: 5px;
    }
  `}
`;

/* Gavin 20200724: Changed from 'height: 220px' to 'max-width: 100%' for phablet */
const HeroImage = styled.div`
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 944px;
  overflow: hidden;
  margin: 0 auto;
  box-shadow: 0 30px 60px -10px rgba(0, 0, 0, 0.2),
    0 18px 36px -18px rgba(0, 0, 0, 0.22);

  ${mediaqueries.tablet`
    max-width: 100%;
  `}

  ${mediaqueries.phablet`
    margin: 0 auto;
    max-width: 100%;

    & > div {
      max-width: 100%;
    }
`}
`;
```

Now I need to create a link to the resume in the navigation. I'm throwing in a Home L1 as well, because it looks weird without one.
* Shadow `Navigation.Header.tsx` component
  * In your root directory, `mkdir -p './src/@narative/gatsby-theme-novela/components/Navigation/'`
  * `cp './node_modules/@narative/gatsby-theme-novela/src/components/Navigation/Navigation.Header.tsx' './src/@narative/gatsby-theme-novela/components/Navigation/Navigation.Header.tsx'`
  * Open `./src/@narative/gatsby-theme-novela/components/Navigation/Navigation.Header.tsx`
  * Hardcode and style (I know, I'm lazy) the navigation links and save. Here's mine.

```
import React, { useState, useEffect } from "react";
import styled from "@emotion/styled";
import { Link, navigate, graphql, useStaticQuery } from "gatsby";
import { useColorMode } from "theme-ui";

import Section from "@components/Section";
import Logo from "@components/Logo";

import Icons from "@icons";
import mediaqueries from "@styles/media";
import {
  copyToClipboard,
  getWindowDimensions,
  getBreakpointFromTheme,
} from "@utils";

const siteQuery = graphql`
  {
    sitePlugin(name: { eq: "@narative/gatsby-theme-novela" }) {
      pluginOptions {
        rootPath
        basePath
      }
    }
  }
`;

const DarkModeToggle: React.FC = () => {
  const [colorMode, setColorMode] = useColorMode();
  const isDark = colorMode === `dark`;

  function toggleColorMode(event) {
    event.preventDefault();
    setColorMode(isDark ? `light` : `dark`);
  }

  return (
    
      
      
    
  );
};

const SharePageButton: React.FC = () => {
  const [hasCopied, setHasCopied] = useState(false);
  const [colorMode] = useColorMode();
  const isDark = colorMode === `dark`;
  const fill = isDark ? "#fff" : "#000";

  function copyToClipboardOnClick() {
    if (hasCopied) return;

    copyToClipboard(window.location.href);
    setHasCopied(true);

    setTimeout(() => {
      setHasCopied(false);
    }, 1000);
  }

  return (
    
      
      
        Copied
      
    
  );
};

const NavigationHeader: React.FC = () => {
  const [showBackArrow, setShowBackArrow] = useState(false);
  const [previousPath, setPreviousPath] = useState("/");
  const { sitePlugin } = useStaticQuery(siteQuery);

  const [colorMode] = useColorMode();
  const fill = colorMode === "dark" ? "#fff" : "#000";
  const { rootPath, basePath } = sitePlugin.pluginOptions;

  useEffect(() => {
    const { width } = getWindowDimensions();
    const phablet = getBreakpointFromTheme("phablet");

    const prev = localStorage.getItem("previousPath");
    const previousPathWasHomepage =
      prev === (rootPath || basePath) || (prev && prev.includes("/page/"));
    const currentPathIsHomepage =
      location.pathname === (rootPath || basePath) || location.pathname.includes("/page/");

    setShowBackArrow(
      previousPathWasHomepage && !currentPathIsHomepage && width 
      
        
          {showBackArrow && (
            
              
            
          )}
          
          Navigate back to the homepage
          {/* Gavin 20200719: Lazy ass navigation links */}
          Home
          Resume
        
        
          {showBackArrow ? (
             navigate(previousPath)}
              title="Navigate back to the homepage"
              aria-label="Navigate back to the homepage"
            >
              
            
          ) : (
            <>
              
              
            
          )}
        
      
    
  );
};

export default NavigationHeader;

const BackArrowIconContainer = styled.div`
  transition: 0.2s transform var(--ease-out-quad);
  opacity: 0;
  padding-right: 30px;
  animation: fadein 0.3s linear forwards;

  @keyframes fadein {
    to {
      opacity: 1;
    }
  }

  ${mediaqueries.desktop_medium`
    display: none;
  `}
`;

const NavContainer = styled.div`
  position: relative;
  z-index: 100;
  padding-top: 100px;
  display: flex;
  justify-content: space-between;

  ${mediaqueries.desktop_medium`
    padding-top: 50px;
  `};

  @media screen and (max-height: 800px) {
    padding-top: 50px;
  }
`;

const LogoLink = styled(Link)`
  position: relative;
  display: flex;
  align-items: center;
  left: ${p => (p.back === "true" ? "-54px" : 0)};

  ${mediaqueries.desktop_medium`
    left: 0
  `}

  &[data-a11y="true"]:focus::after {
    content: "";
    position: absolute;
    left: -10%;
    top: -30%;
    width: 120%;
    height: 160%;
    border: 2px solid ${p => p.theme.colors.accent};
    background: rgba(255, 255, 255, 0.01);
    border-radius: 5px;
  }

  &:hover {
    ${BackArrowIconContainer} {
      transform: translateX(-3px);
    }
  }
`;

const NavControls = styled.div`
  position: relative;
  display: flex;
  align-items: center;

  ${mediaqueries.phablet`
    right: -5px;
  `}
`;

const ToolTip = styled.div`
  position: absolute;
  padding: 4px 13px;
  background: ${p => (p.isDark ? "#000" : "rgba(0,0,0,0.1)")};
  color: ${p => (p.isDark ? "#fff" : "#000")};
  border-radius: 5px;
  font-size: 14px;
  top: -35px;
  opacity: ${p => (p.hasCopied ? 1 : 0)};
  transform: ${p => (p.hasCopied ? "translateY(-3px)" : "none")};
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;

  &::after {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    bottom: -6px;
    margin: 0 auto;
    width: 0;
    height: 0;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 6px solid ${p => (p.isDark ? "#000" : "rgba(0,0,0,0.1)")};
  }
`;

const IconWrapper = styled.button`
  opacity: 0.5;
  position: relative;
  border-radius: 5px;
  width: 40px;
  height: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.3s ease;
  margin-left: 30px;

  &:hover {
    opacity: 1;
  }

  &[data-a11y="true"]:focus::after {
    content: "";
    position: absolute;
    left: 0;
    top: -30%;
    width: 100%;
    height: 160%;
    border: 2px solid ${p => p.theme.colors.accent};
    background: rgba(255, 255, 255, 0.01);
    border-radius: 5px;
  }

  ${mediaqueries.tablet`
    display: inline-flex;
    transform: scale(0.708);
    margin-left: 10px;

    &:hover {
      opacity: 0.5;
    }
  `}
`;

// This is based off a codepen! Much appreciated to: https://codepen.io/aaroniker/pen/KGpXZo
const MoonOrSun = styled.div`
  position: relative;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: ${p => (p.isDark ? "4px" : "2px")} solid
    ${p => p.theme.colors.primary};
  background: ${p => p.theme.colors.primary};
  transform: scale(${p => (p.isDark ? 0.55 : 1)});
  transition: all 0.45s ease;
  overflow: ${p => (p.isDark ? "visible" : "hidden")};

  &::before {
    content: "";
    position: absolute;
    right: -9px;
    top: -9px;
    height: 24px;
    width: 24px;
    border: 2px solid ${p => p.theme.colors.primary};
    border-radius: 50%;
    transform: translate(${p => (p.isDark ? "14px, -14px" : "0, 0")});
    opacity: ${p => (p.isDark ? 0 : 1)};
    transition: transform 0.45s ease;
  }

  &::after {
    content: "";
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin: -4px 0 0 -4px;
    position: absolute;
    top: 50%;
    left: 50%;
    box-shadow: 0 -23px 0 ${p => p.theme.colors.primary},
      0 23px 0 ${p => p.theme.colors.primary},
      23px 0 0 ${p => p.theme.colors.primary},
      -23px 0 0 ${p => p.theme.colors.primary},
      15px 15px 0 ${p => p.theme.colors.primary},
      -15px 15px 0 ${p => p.theme.colors.primary},
      15px -15px 0 ${p => p.theme.colors.primary},
      -15px -15px 0 ${p => p.theme.colors.primary};
    transform: scale(${p => (p.isDark ? 1 : 0)});
    transition: all 0.35s ease;

    ${p => mediaqueries.tablet`
      transform: scale(${p.isDark ? 0.92 : 0});
    `}
  }
`;

const MoonMask = styled.div`
  position: absolute;
  right: -1px;
  top: -8px;
  height: 24px;
  width: 24px;
  border-radius: 50%;
  border: 0;
  background: ${p => p.theme.colors.background};
  transform: translate(${p => (p.isDark ? "14px, -14px" : "0, 0")});
  opacity: ${p => (p.isDark ? 0 : 1)};
  transition: ${p => p.theme.colorModeTransition}, transform 0.45s ease;
`;

const Hidden = styled.span`
  position: absolute;
  display: inline-block;
  opacity: 0;
  width: 0px;
  height: 0px;
  visibility: hidden;
  overflow: hidden;
`;
```

* Run `gatsby develop` to see what your site looks like. Here's mine.

* Click on the Resume L1 menu item to go to the Resume page. Here's mine.

Now that we've gotten rid of the hero image, there is a gap between the author info and the resume body that I don't like. So let's fix that.
* Shadow the `article.template.tsx` template
  * In your root directory, `mkdir -p './src/@narative/gatsby-theme-novela/templates/'`
  * `cp './node_modules/@narative/gatsby-theme-novela/src/templates/article.template.tsx' './src/@narative/gatsby-theme-novela/templates/article.template.tsx'`
  * Open './src/@narative/gatsby-theme-novela/templates/article.template.tsx'
  * Update the top padding on `ArticleBody` and save. Here's mine.

```
import React, { useRef, useState, useEffect } from "react";
import styled from "@emotion/styled";
import throttle from "lodash/throttle";
import { graphql, useStaticQuery } from "gatsby";

import Layout from "@components/Layout";
import MDXRenderer from "@components/MDX";
import Progress from "@components/Progress";
import Section from "@components/Section";
import Subscription from "@components/Subscription";

import mediaqueries from "@styles/media";
import { debounce } from "@utils";

import ArticleAside from "../sections/article/Article.Aside";
import ArticleHero from "../sections/article/Article.Hero";
import ArticleControls from "../sections/article/Article.Controls";
import ArticlesNext from "../sections/article/Article.Next";
import ArticleSEO from "../sections/article/Article.SEO";
import ArticleShare from "../sections/article/Article.Share";

import { Template } from "@types";

const siteQuery = graphql`
  {
    allSite {
      edges {
        node {
          siteMetadata {
            name
          }
        }
      }
    }
  }
`;

const Article: Template = ({ pageContext, location }) => {
  const contentSectionRef = useRef(null);

  const [hasCalculated, setHasCalculated] = useState(false);
  const [contentHeight, setContentHeight] = useState(0);

  const results = useStaticQuery(siteQuery);
  const name = results.allSite.edges[0].node.siteMetadata.name;

  const { article, authors, mailchimp, next } = pageContext;

  useEffect(() => {
    const calculateBodySize = throttle(() => {
      const contentSection = contentSectionRef.current;

      if (!contentSection) return;

      /**
       * If we haven't checked the content's height before,
       * we want to add listeners to the content area's
       * imagery to recheck when it's loaded
       */
      if (!hasCalculated) {
        const debouncedCalculation = debounce(calculateBodySize);
        const $imgs = contentSection.querySelectorAll("img");

        $imgs.forEach($img => {
          // If the image hasn't finished loading then add a listener
          if (!$img.complete) $img.onload = debouncedCalculation;
        });

        // Prevent rerun of the listener attachment
        setHasCalculated(true);
      }

      // Set the height and offset of the content area
      setContentHeight(contentSection.getBoundingClientRect().height);
    }, 20);

    calculateBodySize();
    window.addEventListener("resize", calculateBodySize);

    return () => window.removeEventListener("resize", calculateBodySize);
  }, []);

  return (
    
      
      
      
        
      
      
        
      
      
        
          
        
      
      {mailchimp && article.subscription && }
      {next.length > 0 && (
        
          More articles from {name}
          
          
        
      )}
    
  );
};

export default Article;

const MobileControls = styled.div`
  position: relative;
  padding-top: 60px;
  transition: background 0.2s linear;
  text-align: center;

  ${mediaqueries.tablet_up`
    display: none;
  `}
`;

/* Gavin 20200722: Reduced top padding on the ArticleBody because it looked too
  big w/ no hero */
const ArticleBody = styled.article`
  position: relative;
  padding: 50px 0 35px;
  padding-left: 68px;
  transition: background 0.2s linear;

  ${mediaqueries.desktop`
    padding-left: 53px;
  `}
  
  ${mediaqueries.tablet`
    padding: 25px 0 80px;
  `}

  ${mediaqueries.phablet`
    padding: 20px 0;
  `}
`;

const NextArticle = styled(Section)`
  display: block;
`;

const FooterNext = styled.h3`
  position: relative;
  opacity: 0.25;
  margin-bottom: 100px;
  font-weight: 400;
  color: ${p => p.theme.colors.primary};

  ${mediaqueries.tablet`
    margin-bottom: 60px;
  `}

  &::after {
    content: '';
    position: absolute;
    background: ${p => p.theme.colors.grey};
    width: ${(910 / 1140) * 100}%;
    height: 1px;
    right: 0;
    top: 11px;

    ${mediaqueries.tablet`
      width: ${(600 / 1140) * 100}%;
    `}

    ${mediaqueries.phablet`
      width: ${(400 / 1140) * 100}%;
    `}

    ${mediaqueries.phone`
      width: 90px
    `}
  }
`;

const FooterSpacer = styled.div`
  margin-bottom: 65px;
`;
```

* Open './src/@narative/gatsby-theme-novela/templates/article.template.tsx'
  * Reduce the bottom margin on `Header` and save. Here's mine.

```
import React from 'react';
import styled from '@emotion/styled';

import Headings from '@components/Headings';
import Image, { ImagePlaceholder } from '@components/Image';

import mediaqueries from '@styles/media';
import { IArticle, IAuthor } from '@types';

import ArticleAuthors from './Article.Authors';

interface ArticleHeroProps {
  article: IArticle;
  authors: IAuthor[];
}

const ArticleHero: React.FC = ({ article, authors }) => {
  const hasCoAUthors = authors.length > 1;
  const hasHeroImage =
    article.hero &&
    Object.keys(article.hero.full).length !== 0 &&
    article.hero.full.constructor === Object;

  return (
    
      
        {article.title}
        
          
          
            {article.date} · {article.timeToRead} min read
          
        
      
      
        {hasHeroImage && (
          
        )}
      
    
  );
};

export default ArticleHero;

const Hero = styled.div`
  ${p => mediaqueries.phablet`
    &::before {
      content: "";
      width: 100%;
      height: 20px;
      background: ${p.theme.colors.primary};
      position: absolute;
      left: 0;
      top: 0;
      transition: ${p.theme.colorModeTransition};
    }

    &::after {
      content: "";
      width: 100%;
      height: 10px;
      background: ${p.theme.colors.background};
      position: absolute;
      left: 0;
      top: 10px;
      border-top-left-radius: 25px;
      border-top-right-radius: 25px;
      transition: ${p.theme.colorModeTransition};
    }
  `}
`;

const ArticleMeta = styled.div`
  margin-left: ${p => (p.hasCoAUthors ? '10px' : '0')};

  ${mediaqueries.phablet`
    margin-left: 0;
  `}
`;

/* Gavin 20200722: Reduced bottom margin on the Header because it looked too
  big w/ no hero */
const Header = styled.header`
  position: relative;
  z-index: 10;
  margin:50px auto 120px;
  padding-left: 68px;
  max-width: 749px;

  ${mediaqueries.desktop`
    padding-left: 53px;
    max-width: calc(507px + 53px);
    margin: 50px auto 70px;
  `}

  ${mediaqueries.tablet`
    padding-left: 0;
    margin: 50px auto 70px;
    max-width: 480px;
  `}

  ${mediaqueries.phablet`
    margin: 50px auto 180px;
    padding: 0 40px;
  `}

  @media screen and (max-height: 700px) {
    margin: 50px auto;
  }
`;

const HeroHeading = styled(Headings.h1)`
  font-size: 48px;
  font-family: ${p => p.theme.fonts.serif};
  margin-bottom: 25px;
  font-weight: bold;
  line-height: 1.32;

  ${mediaqueries.tablet`
    margin-bottom: 20px;
    font-size: 36px;
  `}

  ${mediaqueries.phablet`
    font-size: 32px;
  `}
`;

const HeroSubtitle = styled.div`
  position: relative;
  display: flex;
  font-size: 18px;
  color: ${p => p.theme.colors.grey};

  ${p => mediaqueries.phablet`
    font-size: 14px;
    flex-direction: column;

    ${p.hasCoAUthors &&
      `
        &::before {
          content: '';
          position: absolute;
          left: -20px;
          right: -20px;
          top: -10px;
          bottom: -10px;
          border: 1px solid ${p.theme.colors.horizontalRule};
          opacity: 0.5;
          border-radius: 5px;
        }
    `}

    strong {
      display: block;
      font-weight: 500;
      margin-bottom: 5px;
    }
  `}
`;

const HeroImage = styled.div`
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 944px;
  overflow: hidden;
  margin: 0 auto;
  box-shadow: 0 30px 60px -10px rgba(0, 0, 0, 0.2),
    0 18px 36px -18px rgba(0, 0, 0, 0.22);

  ${mediaqueries.tablet`
    max-width: 100%;
  `}

  ${mediaqueries.phablet`
    margin: 0 auto;
    width: calc(100vw - 40px);
    height: 220px;

    & > div {
      height: 220px;
    }
`}
`;
```

* Run `gatsby develop` and click on the Resume L1 menu item to go to the Resume page. Here's mine.

Much better. Now let's commit your changes to your repo.

## Merge your changes into your repo
* Add all new files
  * `git add --all`
* Commit your changes
  * `git commit -a -m "[your commit message]"`
* Push your branch to your repo on GitHub
  * `git push -u origin initial_customizations`

**Boom!** Your branch and changes have been saved to your repo. Now create a pull request on GitHub and merge your changes into the main branch.

*If you got an "Authentication failed..." error even though you entered your GitHub username and password correctly, you may have to create and use a personal access token. Read [this Medium blog](https://medium.com/@ginnyfahs/github-error-authentication-failed-from-command-line-3a545bfd0ca8#:~:text=How%20to%20Authenticate%20on%20GitHub,requires%20a%20personal%20access%20token.&text=Make%20sure%20you%20copy%20the,authenticate%20via%20the%20command%20line) for details on how to do that.*

* In your repo on GitHub, click on the "Pull Requests" tab

* Click on the "New pull request" button

* Click the "Compare" dropdown and select the `initial_customizations` branch

* Compare your changes
* When you are good with all of the change made, click the "Create pull request" button

* Write your PR notes and click the "Create pull request" button

* Click the "Merge pull request" button

* Click the "Confirm merge" button

*You should see "Pull request successfully merged and closed."*
* In Terminal, `git checkout main`

**Boom!**
Changes have been merged, and you are back on the `main` branch, ready to move forward.

**That's it for today.**
*I'll post tutorial next week on how to deploy your site to Firebase and maybe how to automate deploys with GitHub Actions. We'll see what I have time to get around to.*