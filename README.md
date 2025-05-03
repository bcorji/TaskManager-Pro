# TaskManager Pro

A full-stack task management application built with React and FastAPI, featuring role-based authentication, PostgreSQL database integration, and automated deployment.

## Features

- Role-based authentication and authorization
- Task creation, assignment, and management
- Real-time updates and notifications
- Responsive and modern UI
- RESTful API with FastAPI
- Secure JWT authentication
- PostgreSQL database integration
- CI/CD pipeline with GitHub Actions
- AWS deployment

## Tech Stack

### Frontend
- React with TypeScript
- Vite for build tooling
- TailwindCSS for styling
- React Query for state management
- Axios for API communication

### Backend
- FastAPI (Python)
- PostgreSQL
- SQLAlchemy ORM
- JWT authentication
- Alembic for database migrations

### DevOps
- GitHub Actions for CI/CD
- AWS (EC2, RDS, S3)
- Docker

## Project Structure

```
├── frontend/           # React frontend application
├── backend/            # FastAPI backend application
├── .github/            # GitHub Actions workflows
├── docker/             # Docker configuration files
└── docs/               # Project documentation
```

## Getting Started

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.9 or higher)
- PostgreSQL
- Docker (optional)

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TaskManager-Pro.git
cd TaskManager-Pro
```

2. Set up the frontend:
```bash
cd frontend
npm install
npm run dev
```

3. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

4. Set up the database:
```bash
cd backend
alembic upgrade head
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.