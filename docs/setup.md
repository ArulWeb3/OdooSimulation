# Setup Guide

## Prerequisites

- Docker & Docker Compose
- Python 3.10+
- Git

## Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/ArulWeb3/OdooSimulation.git
cd OdooSimulation
```

2. **Environment Setup**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
- Copy `.env.example` to `.env`
- Update configuration values

5. **Initialize Database**
```bash
./scripts/init_db.sh
```

## Docker Setup

1. **Build Images**
```bash
docker-compose build
```

2. **Start Services**
```bash
docker-compose up -d
```

3. **Verify Installation**
```bash
docker-compose ps
```

## Next Steps

- [Development Guide](development.md)
- [Testing Guide](testing.md)
- [Troubleshooting](troubleshooting.md)