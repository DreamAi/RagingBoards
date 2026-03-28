#!/bin/bash

echo "Deploying to Netlify..."

npm install -g netlify-cli

netlify login
netlify init

npm run build

netlify deploy --prod

echo "Netlify deployment complete"
