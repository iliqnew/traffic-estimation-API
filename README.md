# Traffic Estimation API

## Overview

The Traffic Estimation API estimates traffic opportunities based on historical data. Users can query the API using criteria such as country, browser, platform, and vertical to get an estimated traffic count.

## Setup

### Prerequisites

- Python 3.7+
- Pip

### Installation Steps

1. **Clone the Repository**:
```
git clone https://github.com/iliqnew/traffic-estimation-api.git
cd traffic-estimation-api
```

2. **Install Dependencies**:
```
pip install -r requirements.txt
```

3. **Run the Application**:
```
uvicorn app:app --reload
```

The API will be accessible at http://127.0.0.1:8000.


## API Usage
### /opportunities Endpoint
Request Parameters (All Optional):
1. browser (e.g., Chrome, Edge)
2. platform (e.g., Windows, Mac)
3. vertical (e.g., 280000000000, 261400000000)
4. country (e.g., US, BG)

### Example Requests:
Estimate traffic for Chrome on Windows in the US:

GET /opportunities?browser=Chrome&platform=Windows&country=US
Response:

{
    "estimated_traffic": 2.2178887734538666e+28
}

License: This project is licensed under the MIT License.