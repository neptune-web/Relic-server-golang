# Our first stage, that is the Builder
FROM node:14-buster-slim AS build
WORKDIR /app
COPY . .
RUN yarn install
RUN yarn build

FROM node:14-buster-slim AS runtime
WORKDIR /app
COPY --from=build ./app/build ./dist
COPY --from=build ./app/contract ./dist/contract
COPY package* ./
RUN yarn install --production
RUN yarn global add pm2 
CMD ["pm2-runtime","dist/index.js"]