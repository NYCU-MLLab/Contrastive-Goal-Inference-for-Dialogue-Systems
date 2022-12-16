# Webpage demo

## 1. How to run

### Preparation
* You need to get CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN and setup on [LINE Developers](https://developers.line.biz)
* You can refer to linebot.md

### Build
* You need to change <CHANNEL_SECRET>, <CHANNEL_ACCESS_TOKEN> to your's
```bash
git clone https://github.com/hsuanchi/Flask-LINE-Bot-GCP.git
cd /Flask-LINE-Bot-GCP/flask/
echo "export CHANNEL_SECRET='<CHANNEL_SECRET>'" >> .flaskenv
echo "export CHANNEL_ACCESS_TOKEN='<CHANNEL_ACCESS_TOKEN>'" >> .flaskenv
cd ..
sudo docker-compose up --build
```

## 2. How to access
Using Line app and scan QR code from [LINE Developers](https://developers.line.biz) Messaging API

### Demo

![](https://mllab.asuscomm.com:12950/hackmd/uploads/upload_24d3a1c8387ed6277b08ce3c1a479331.jpg =x500)


## 1. How to use
* Restaurant:
  * We can book the restaurant by offering the information about type of food and the price range.
  * After the system suggests the restaurant, we can ask for the address and phone number.
* Hotel:
  * We can book the hotel by offering the information about the price range and stars rated.
  * After the system suggests the hotel, we can ask for the address and phone number.
* Attraction:
  * We can find the attraction by offering the information about the area and attraction type.
  * After the system suggests the attraction, we can ask for the address and phone number.
