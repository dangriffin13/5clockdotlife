# 5oclock.life

Global leader in just-in-time libation recipe delivery mechanisms

## Build Process

One-time setup:

1. Install node.js from https://nodejs.org/en/ if it is not already installed
2. On the command line, navigate to this repository and run `npm install`

During development the following commands are available:

`npm run watch`
- watches for scss changes and compiles to /dist/css/style.css
- uses Autoprefixer to add any browser prefixes automatically
- loads a BrowserSync window that automatically updates styles whenever style.css is compiled

`npm run imagemin`
- compresses all images found in /src/images to /dist/images

See package.json for all logic.
