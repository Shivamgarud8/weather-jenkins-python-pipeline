#  Flask Weather App with OpenWeatherMap API on Amazon EC2

![](./img/Screenshot%202025-08-06%20094701.png)
![](./img/Screenshot%202025-08-06%20094721.png)
![](./img/Screenshot%202025-08-06%20094912.png)



This project is a simple **Flask web application** that allows users to enter a city name and retrieve **real-time weather information** using the [OpenWeatherMap API](https://openweathermap.org/). The app is hosted on an **Amazon EC2 instance** running **Amazon Linux 2**.

---

##  Tech Stack

- **Python 3**
- **Flask**
- **OpenWeatherMap API**
- **Amazon EC2 (Amazon Linux 2)**
- **Virtualenv**

---

##  Prerequisites

- An AWS EC2 instance (Amazon Linux 2)
- Port `5000` open in EC2 Security Group
- A valid OpenWeatherMap API key ([Get one here](https://openweathermap.org/api))

---

##  Setup Instructions

### 🔹 1. Connect to Your EC2 Instance
```bash
ssh -i your-key.pem ec2-user@<your-ec2-public-ip>
sudo yum install python3 -y
pip3 install --upgrade pip
pip3 install virtualenv

mkdir weatherly
cd weatherly
virtualenv myenv
source myenv/bin/activate
pip freeze > requirements.txt
source myenv/bin/activate
python app.py


