# Webpage demo

## 1. How to run

```bash
sudo docker run -itd -p ${port}:80 --name demo --shm-size 32G --privileged --gpus all chin0880ee/cgi:web
```

## 2. How to access
Using browser 
>http://serverip:port/dialog 

### Demo

![](https://mllab.asuscomm.com:12950/hackmd/uploads/upload_dc8887acb8142677c6e50b36d3caa277.png)
<img src="./web.png" width="800">

## 3. How to use
* Restaurant:
  * We can book the restaurant by offering the information about type of food and the price range.
  * After the system suggests the restaurant, we can ask for the address and phone number.
* Hotel:
  * We can book the hotel by offering the information about the price range and stars rated.
  * After the system suggests the hotel, we can ask for the address and phone number.
* Attraction:
  * We can find the attraction by offering the information about the area and attraction type.
  * After the system suggests the attraction, we can ask for the address and phone number.
