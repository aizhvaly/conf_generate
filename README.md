### For run it:  
sudo mkdir -p /app/static  
sudo mkdir -p /app/storage  
\# Move or copy all static file from conf_generate/app/static to /app/static
mv conf/webapp/conf /etc/nginx/conf.d/webapp.conf  
sudo docker pull artyom1789/app:v0.0.1   
sudo docker run -d -p 127.0.0.1:8000:8000 -v /app/static/:/app/static/ -v /app/storage/:/app/storage artyom1789/app:v0.0.1   
sudo systemctl start nginx  
