RAGING BOARDS
Oracle Cloud Free Tier Deployment

STEP 1
Create Oracle Cloud Account

https://www.oracle.com/cloud/free/

STEP 2
Create VM Instance

Image:
Ubuntu 22.04

Shape:
VM.Standard.E2.1.Micro (Free Tier)

STEP 3
Open Ports

Allow:

22 SSH
80 HTTP
443 HTTPS
3000 Frontend
5000 Backend

STEP 4
Connect to server

ssh ubuntu@your-server-ip

STEP 5
Install dependencies

sudo apt update
sudo apt install git docker docker-compose nodejs npm python3 python3-pip -y

STEP 6
Clone repository

git clone https://github.com/yourusername/raging-boards

cd raging-boards

STEP 7
Run installer

bash install.sh

STEP 8
Platform will start

Backend
http://server-ip:5000

Frontend
http://server-ip:3000
