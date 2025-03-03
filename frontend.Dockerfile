# Use the latest node image
FROM node:latest

# Set working directory
WORKDIR /app

# Copy frontend files
COPY react_fren_dev_2025 /app

# Install dependencies
RUN npm install
RUN npm install react-router-dom

# Build the React app
RUN npm run build

# Expose frontend port
EXPOSE 3000

# Serve the React app
CMD ["npm", "start"]
