# Blog API - Django REST Framework

A powerful and secure Blog API built with Django REST Framework (DRF) and JWT authentication. This API provides full CRUD operations for blog posts with role-based permissions.

## 🚀 Features

- ✅ **JWT Authentication** - Secure token-based authentication
- ✅ **Full CRUD Operations** - Create, Read, Update, Delete blog posts
- ✅ **Role-Based Permissions** - Admin users can delete posts, regular users can only edit their own
- ✅ **User Association** - Each blog post is automatically linked to its author
- ✅ **RESTful API Design** - Follows REST best practices
- ✅ **Error Handling** - Comprehensive error responses
- ✅ **SQLite Database** - Lightweight database for development

## 📋 Table of Contents

- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Error Codes](#error-codes)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Technology Stack

- **Python** 3.14+
- **Django** 4.2.11
- **Django REST Framework** 3.14.0
- **Simple JWT** 5.3.0
- **SQLite** (Development)
- **PostgreSQL** (Production ready)

## 📦 Installation

### Prerequisites

- Python 3.14 or higher
- pip package manager
- virtualenv (recommended)

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/suyog123-hub/Blog.git
cd Blog
