from icecream import ic
from server import app
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="3002")
    ic("Running server...🏃🏾 in port 3002 🐍👨🏾‍💻")