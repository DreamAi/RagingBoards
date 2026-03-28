#!/bin/bash

echo "🗄️ Running database migrations..."

npx prisma migrate deploy
npx prisma db seed

echo "✅ Database ready"
