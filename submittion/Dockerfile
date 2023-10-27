#vanilla Alpine Linux as the base image
FROM alpine:latest

#Set a non-root user
RUN adduser -D -u 1000 -g 'www' www

#Set the working directory to /app
WORKDIR /app

#Install Nginx
RUN apk --no-cache add nginx

#Copy the Nginx configuration file and index.html
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /app/index.html
COPY machineName.env /app/machineName.env
COPY tesenium.py /app/tesenium.py

#Create a symbolic link to /dev/stdout for Nginx logging
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stdout /var/log/nginx/error.log

#Set the machine name as an environment variable
ENV MACHINE_NAME=ThisIsMyMachine

# Change the permissions to allow the non-root user to write to the /app directory
RUN chown -R www:www /app

# Expose port 80
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]