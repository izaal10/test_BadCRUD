FROM php:8.0-apache

# Set working directory
WORKDIR /var/www/html

# Copy application files
COPY ./ ./

# Remove unnecessary directories
RUN rm -rf .git/* && \
    rm -rf .github/*

# Install additional dependencies if needed
# RUN apt-get update && apt-get install -y <package-name>

# Expose port 80
EXPOSE 80

# Optionally, customize Apache configurations if needed
# COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Optionally, set non-root user for Apache (consider your application's requirements)
# RUN useradd -ms /bin/bash your-non-root-user
# RUN chown -R your-non-root-user:your-non-root-user /var/www/html

# Start Apache
CMD ["apache2-foreground"]
