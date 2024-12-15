# Seaker-Alert-App

## Overview
**Seaker-Alert-App** is a lightweight system monitoring and alert application designed to track key metrics such as CPU usage, RAM consumption, disk utilization, uptime, and device temperature (if available). The app provides real-time metrics visualization using Grafana, historical data storage with Prometheus, and customizable threshold-based alerts via notifications (e.g., Telegram).

---

## Features
- **Real-Time Metrics Monitoring**:
  - CPU usage (%)
  - RAM usage (GB)
  - Disk usage (GB)
  - Device uptime (hours)
  - Device temperature (if supported by hardware)
- **Dashboard**:
  - Powered by Grafana with customizable, user-friendly visualizations.
  - Supports real-time and historical data visualization.
- **Alerts and Notifications**:
  - Threshold-based alerts configurable by the user.
  - Notifications sent via Telegram.
- **Data Export**:
  - Export data in JSON or CSV format for analysis.
- **Dockerized Deployment**:
  - Fully containerized for ease of setup and portability.

---

## System Architecture
```plaintext
+-------------+           +------------+          +-------------+
| System Data |----> API  | Prometheus |----> DB  |    Grafana   |
+-------------+           +------------+          +-------------+
       |                                                  |
       +---------------------- Notifications -------------+
```

---

## Prerequisites
1. **System Requirements**:
   - Python 3.8 or higher
   - Docker (optional for containerized deployment)
   - Prometheus and Grafana
2. **Libraries**:
   - Flask
   - psutil
   - requests
3. **Optional Tools**:
   - Stress (for testing and alert simulations)

---

## Setup Instructions

### **Local Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Seaker-Alert-App.git
   cd Seaker-Alert-App/app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python main.py
   ```
4. Access the API:
   - Metrics endpoint: `http://localhost:5000/metrics`
   - Alerts endpoint: `http://localhost:5000/alerts`

---

### **Dockerized Deployment**
1. Build the Docker image:
   ```bash
   docker build -t seaker-alert-app .
   ```
2. Run the container:
   ```bash
   docker run -d -p 5000:5000 seaker-alert-app
   ```
3. Set up Prometheus:
   ```bash
   docker run -d -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
   ```
4. Set up Grafana:
   ```bash
   docker run -d -p 3000:3000 grafana/grafana
   ```

---

## Configuration
1. **Prometheus**:
   - Modify `prometheus.yml` to match your API endpoint.
2. **Grafana**:
   - Import the provided dashboard JSON file or configure your own.
3. **Alerts**:
   - Customize thresholds in `alerts.py`:
     ```python
     THRESHOLDS = {
         "cpu": 80,  # CPU usage threshold in %
         "ram": 8,   # RAM usage threshold in GB
         "disk": 50  # Disk space usage threshold in GB
     }
     ```

---

## Simulating Alerts
1. Install `stress`:
   ```bash
   sudo apt-get install stress
   ```
2. Simulate high CPU usage:
   ```bash
   stress --cpu 4 --timeout 60
   ```
3. Verify alerts via Telegram or in the logs.

---

## Data Export
- Export metrics as **CSV** or **JSON** via the `/export` endpoint:
  ```bash
  curl http://localhost:5000/export?format=csv -o metrics.csv
  ```

---

## Example Alerts Configuration
Modify the `alerts.py` file to set thresholds:
```python
THRESHOLDS = {
    "cpu": 85,  # Adjust CPU usage alert threshold
    "ram": 10,  # Adjust RAM usage alert threshold
    "disk": 20  # Adjust disk space usage alert threshold
}
```

---

## Live Demo
During a live demonstration:
1. Deploy the application locally or with Docker.
2. Open Grafana at `http://localhost:3000`.
3. Simulate an alert scenario using the `stress` tool.
4. Verify real-time alerts and notifications.

---

## Repository and Image Links
- GitHub Repository: [Seaker-Alert-App](https://github.com/your-username/Seaker-Alert-App)
- Docker Hub Image: [seaker-alert-app](https://hub.docker.com/r/your-username/seaker-alert-app)

---

## Optional Features
- **IoT Protocol Support**: MQTT integration for pushing metrics to/from IoT devices.
- **Role-Based Access Control**: Add admin/viewer roles for dashboard access.
- **Temperature Monitoring**: Extend support for device temperature (if hardware allows).

---

## License
This project is open-source and licensed under the MIT License.

---

Feel free to customize this `README.md` with specific repository links or additional details!
