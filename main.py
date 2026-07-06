<!-- ... existing code ... -->
@app.get("/api/v1/health")
def system_status():
    return {
        "service": "Maps API",
        "status": "Healthy",
        "database": "Disconnected (For now!)"
    }

# 4. Start the Server (Required for Cloud running)
# This tells the server to run continuously and listen for internet traffic
if __name__ == "__main__":
    import uvicorn
    # 0.0.0.0 means it will accept connections from the outside internet
    uvicorn.run(app, host="0.0.0.0", port=8000)
