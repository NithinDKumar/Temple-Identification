# Temple Identification System

## Project Overview  
The **Temple Identification System** is a web-based application that enables users to upload temple images, search for temple details, and view comprehensive information about Indian temples. The system utilizes **React.js** for the frontend, **Flask** for the backend, **MongoDB** for database storage, and **TensorFlow** for image recognition.  

This project aims to promote cultural heritage by offering an easy way to identify and learn about temples.

---

## Features  
### User Features  
- **Upload Temple Images**: Upload images to identify temples.  
- **Search Temples**: Search for temples using keywords.  
- **View Temple Details**: Explore detailed information such as name, state, history, architecture, and images.

---

## Technologies Used  
### Frontend  
- **React.js**: For building an interactive user interface.  
- **CSS**: For styling the components.

### Backend  
- **Flask**: A Python-based microframework for handling server requests.  
- **TensorFlow**: For temple image recognition and classification.  
- **MongoDB**: For storing temple data.

---

## Installation and Setup  
### Prerequisites  
- **Node.js** and **npm**  
- **Python 3.x**  
- **MongoDB**  

### Steps  
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/your-username/temple-identification.git
   cd temple-identification

2. **Backend Setup**
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    pip install -r requirements.txt
    flask run

3. **FrontendSetup**
    cd frontend
    npm install
    npm start

4. **Run the Application**
    Backend: http://localhost:5000
    Frontend: http://localhost:3000


