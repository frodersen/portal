# Using an official Node base image
FROM node:16-slim

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the project files into the Docker image
COPY . .

# Expose port 8080 for the Vue.js development server
EXPOSE 8080

# Command to run the development server
CMD ["npm", "run", "serve"]

