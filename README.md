## Manual server installation
1. Go to YC console and create a VM
2. Connect to VM using SSH
3. Install latest updates: `sudo apt-get update && sudo apt-get upgrade -y`
4. Install python tools: `sudo apt-get install -y python3-pip python3-venv git`
5. From your local machine copy the source code: `scp project IP:~/`
6. Install dependencies: `pip install -r project/requirements.txt`
7. Install gunicorn: `sudo pip install gunicorn`
8. Create a systemd unit for gunicorn from the template `/etc/systemd/system/gunicorn.service`
9. Reload systemd: `sudo systemctl daemon-reload`
10. Start gunicorn service: `sudo systemctl start gunicorn`
11. Install nginx: `sudo apt-get install nginx -y`
12. Start nginx: `sudo systemctl start nginx`
13. Install psycopg: `sudo pip install psycopg2-binary==2.8.6`
14. Collect static: `cd ~/project && python3 manage.py collectstatic`
15. Restart gunicorn: `sudo systemctl restart gunicorn`
16. Create a default nginx site from the template `/etc/nginx/sites-enabled/default`
17. Reload nginx: `sudo systemctl reload nginx`
18. Install postgresql: `sudo apt-get -y install postgresql postgresql-contrib`
19. Start postgresql: `sudo systemctl start postgresql`
20. Create project db: `sudo -u postgres psql -c 'CREATE DATABASE project;'`
21. Create project user: `sudo -u postgres psql -c "CREATE USER user WITH ENCRYPTED PASSWORD 'password';"`
22. Grant all privileges to project users on project DB: `sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE project TO user;'`
23. Run migrations: `cd ~/project && python3 manage.py migrate`
24. From your local machine, check the website.


