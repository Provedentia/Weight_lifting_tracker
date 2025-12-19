# Weight Lifting Tracker

Full stack mobile app: React Native + FastAPI

## Structure

```
├── mobile/     # React Native app
├── backend/    # FastAPI backend
├── shared/     # Shared code
└── docs/       # Documentation
```

## Quick Start

**Backend:**
```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Mobile:**
```bash
cd mobile
npm install
npm start
```

