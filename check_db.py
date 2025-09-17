from pymongo import MongoClient
import os

# MONGO_URI environment variable থেকে নেওয়া
MONGO_URI = os.getenv("mongodb+srv://test:hvM1kLeXCCSXXb1u@cluster0.mrfgvxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

if not MONGO_URI:
    print("❌ MONGO_URI environment variable is not set!")
    exit(1)

try:
    client = MongoClient(MONGO_URI)
    db = client["test_db"]  # আপনার ডাটাবেস নাম
    users_count = db.list_collection_names()
    print(f"✅ MongoDB connection successful! Collections: {users_count}")
except Exception as e:
    print(f"❌ Failed to connect to MongoDB: {e}")
