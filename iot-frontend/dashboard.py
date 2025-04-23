# import streamlit as st
# import requests

# API_URL = "http://localhost:8000"

# st.title("IoT Smart Home Dashboard")

# if st.button("Get Devices"):
#     response = requests.get(f"{API_URL}/devices/")
#     st.json(response.json())


import streamlit as st
import requests

# Define your API URL (Backend FastAPI URL)
API_URL = "http://iot-backend:8000"  # Change this if using a remote backend

# Streamlit UI Title
st.title("IoT Smart Home Dashboard")

# CRUD Operations for Devices
st.header("Devices Management")

# Get Devices
if st.button("Get Devices"):
    response = requests.get(f"{API_URL}/devices/")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to fetch devices!")

# Add New Device
st.subheader("Add New Device")
device_name = st.text_input("Device Name")
device_location = st.text_input("Device Location")
device_type = st.selectbox("Device Type", ["light", "fan", "thermostat", "sensor"])
device_status = st.radio("Device Status", ("On", "Off"))

if st.button("Add Device"):
    data = {
        "name": device_name,
        "location": device_location,
        "type": device_type,
        "status": True if device_status == "On" else False
    }
    response = requests.post(f"{API_URL}/devices/", json=data)
    if response.status_code == 201:
        st.success("Device added successfully!")
    else:
        st.error("Failed to add device!")

# Update Device
st.subheader("Update Device")
device_id = st.number_input("Device ID", min_value=1, step=1)
new_status = st.radio("New Device Status", ("On", "Off"))

if st.button("Update Device"):
    data = {
        "status": True if new_status == "On" else False
    }
    response = requests.put(f"{API_URL}/devices/{device_id}", json=data)
    if response.status_code == 200:
        st.success("Device updated successfully!")
    else:
        st.error("Failed to update device!")

# Delete Device
st.subheader("Delete Device")
delete_device_id = st.number_input("Device ID to Delete", min_value=1, step=1)

if st.button("Delete Device"):
    response = requests.delete(f"{API_URL}/devices/{delete_device_id}")
    if response.status_code == 204:
        st.success("Device deleted successfully!")
    else:
        st.error("Failed to delete device!")

# CRUD Operations for Users
st.header("Users Management")

# Get Users
if st.button("Get Users"):
    response = requests.get(f"{API_URL}/users/")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to fetch users!")

# Add New User
st.subheader("Add New User")
user_name = st.text_input("User Name")
user_email = st.text_input("User Email")
user_role = st.selectbox("User Role", ["admin", "user"])

if st.button("Add User"):
    data = {
        "name": user_name,
        "email": user_email,
        "role": user_role
    }
    response = requests.post(f"{API_URL}/users/", json=data)
    if response.status_code == 201:
        st.success("User added successfully!")
    else:
        st.error("Failed to add user!")

# Update User
st.subheader("Update User")
user_id = st.number_input("User ID", min_value=1, step=1)
new_role = st.selectbox("New User Role", ["admin", "user"])

if st.button("Update User"):
    data = {
        "role": new_role
    }
    response = requests.put(f"{API_URL}/users/{user_id}", json=data)
    if response.status_code == 200:
        st.success("User updated successfully!")
    else:
        st.error("Failed to update user!")

# Delete User
st.subheader("Delete User")
delete_user_id = st.number_input("User ID to Delete", min_value=1, step=1)

if st.button("Delete User"):
    response = requests.delete(f"{API_URL}/users/{delete_user_id}")
    if response.status_code == 204:
        st.success("User deleted successfully!")
    else:
        st.error("Failed to delete user!")
