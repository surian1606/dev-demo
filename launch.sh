#!/bin/bash
# To connect to your EC2 instance and install the Apache web server with PHP
yum update -y
yum install -y httpd php8.1
systemctl enable httpd.service
systemctl start httpd
cd /var/www/html
cat > index.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-size: 36px;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    Welcome to AWS Technical Essentials
</body>
</html>
EOF