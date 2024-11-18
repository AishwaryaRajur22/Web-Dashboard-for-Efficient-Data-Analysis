# Web dashboard for efficient data analysis

This project is a web-based dashboard designed to visualize real-time process data originating from a bioreactor. It allows users to monitor key metrics like Temperature, pH, Distilled Oxygen, and Pressure over time using a PostgreSQL database as the data source.

---

## Features

- **Visualizations**:
  - Time-series plots for:
    - **Temperature** (°C)
    - **pH** (unitless)
    - **Distilled Oxygen** (%)
    - **Pressure** (psi)
- **Real-Time Data**: The dashboard updates dynamically, reflecting the most recent data available in the database.
- **Web Interface**: Accessible locally via [http://localhost:8888](http://localhost:8888).

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://www.docker.com/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/bioreactor-dashboard.git
   cd bioreactor-dashboard

### The database

The data you'll be visualizing will be in a Postgres database, also configured in `compose.yaml`. Credentials to access this database will be provided in the following environment variables:
- `POSTGRES_HOST` provides the host
- `POSTGRES_PORT` provides the port
- `POSTGRES_USER` provides the user
- `POSTGRES_PASSWORD` provides the password
- `POSTGRES_DB` provides the database

An example can be found in `local.env`. Note that these will be subject to change, so make sure not to hard code these.

### The data

The tables in the database:
```
brx1=# \dt
                      List of relations
 Schema |           Name           | Type  |      Owner       
--------+--------------------------+-------+------------------
 public | CM_HAM_DO_AI1/Temp_value | table | process_trending
 public | CM_HAM_PH_AI1/pH_value   | table | process_trending
 public | CM_PID_DO/Process_DO     | table | process_trending
 public | CM_PRESSURE/Output       | table | process_trending
 ```

Each table has the same schema, like so:
```
brx1=# \d public."CM_HAM_DO_AI1/Temp_value"
                Table "public.CM_HAM_DO_AI1/Temp_value"
 Column |            Type             | Collation | Nullable | Default 
--------+-----------------------------+-----------+----------+---------
 time   | timestamp without time zone |           |          | 
 value  | double precision            |           |          | 
```

Each table contains the following data:
| Table                    | Name             | Units   |
|--------------------------|------------------|---------|
| CM_HAM_DO_AI1/Temp_value | Temperature      | Celsius |
| CM_HAM_PH_AI1/pH_value   | pH               | n/a     |
| CM_PID_DO/Process_DO     | Distilled Oxygen | %       |
| CM_PRESSURE/Output       | Pressure         | psi     |

### How to test your code

Run `docker compose up` and navigate your browser to http://localhost:8888/. That's it!

## Minimum Viable Project

The dashboard should allow the user to plot each of these four series (Temperature, pH, Distilled Oxygen, and Pressure) over time.
