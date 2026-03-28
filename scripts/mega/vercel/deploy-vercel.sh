#!/bin/bash

echo "Deploying to Vercel..."

npm install -g vercel

vercel login
vercel link

vercel --prod

echo "Vercel deployment complete"
