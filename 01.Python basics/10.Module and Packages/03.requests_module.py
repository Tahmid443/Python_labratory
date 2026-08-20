# Make a request to a web page, and print the response text:
import requests

x = requests.get("https://w3schools.com/python/demopage.htm")

print(x.text)
# pip install requests
# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

"""
================================================================================
REQUESTS MODULE - COMPLETE METHOD REFERENCE WITH CODES AND EXAMPLES
================================================================================

All methods return a Response object containing the server's response.

================================================================================
METHOD SUMMARY TABLE
================================================================================

Method              Description
------------------  ------------------------------------------------------------
delete(url, args)   Sends a DELETE request to the specified url
get(url, params, args)  Sends a GET request to the specified url
head(url, args)     Sends a HEAD request to the specified url
patch(url, data, args)  Sends a PATCH request to the specified url
post(url, data, json, args)  Sends a POST request to the specified url
put(url, data, args)  Sends a PUT request to the specified url
request(method, url, args)  Sends a request of the specified method

================================================================================
1. DELETE - Delete a resource
================================================================================
"""
import requests

# DELETE request to remove a resource
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 (success) or 404 (not found)

# DELETE with headers
headers = {"Authorization": "Bearer token123"}
response = requests.delete("https://api.example.com/users/5", headers=headers)

# DELETE with timeout
response = requests.delete("https://api.example.com/resource/10", timeout=5)

"""
================================================================================
2. GET - Retrieve a resource
================================================================================
"""

# Basic GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200
print(response.json())  # Parsed JSON response

# GET with query parameters
params = {"userId": 1, "id": 2}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.url)  # https://jsonplaceholder.typicode.com/posts?userId=1&id=2

# GET with headers
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
response = requests.get("https://api.github.com/users/octocat", headers=headers)

# GET with timeout and verify SSL
response = requests.get("https://api.example.com/data", timeout=5, verify=True)

# GET with authentication
response = requests.get("https://api.example.com/secure", auth=("username", "password"))

"""
================================================================================
3. HEAD - Get headers only (no response body)
================================================================================
"""

# HEAD request - returns only headers, no body
response = requests.head("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200
print(response.headers)  # Headers dictionary
print(response.text)  # Empty string (no body)

# HEAD with headers
headers = {"Accept-Encoding": "gzip"}
response = requests.head("https://www.example.com", headers=headers)

# HEAD with timeout
response = requests.head("https://api.example.com/status", timeout=3)

"""
================================================================================
4. PATCH - Partially update a resource
================================================================================
"""

# PATCH request to update specific fields
data = {"title": "Updated Title"}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", data=data)
print(response.status_code)  # 200
print(response.json())

# PATCH with JSON data
json_data = {"status": "active", "priority": 5}
response = requests.patch("https://api.example.com/tasks/10", json=json_data)

# PATCH with headers
headers = {"Content-Type": "application/json"}
data = {"name": "New Name"}
response = requests.patch("https://api.example.com/users/5", data=data, headers=headers)

# PATCH with authentication
response = requests.patch(
    "https://api.example.com/items/3", json={"quantity": 10}, auth=("user", "pass")
)

"""
================================================================================
5. POST - Create a new resource
================================================================================
"""

# POST with form data
data = {"title": "New Post", "body": "Content here", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
print(response.status_code)  # 201 (Created)
print(response.json())  # Response with new resource ID

# POST with JSON data
json_data = {"name": "John Doe", "email": "john@example.com", "age": 30}
response = requests.post("https://api.example.com/users", json=json_data)

# POST with files
files = {"file": ("filename.txt", b"File content here")}
response = requests.post("https://httpbin.org/post", files=files)

# POST with headers and authentication
headers = {"X-Custom-Header": "CustomValue"}
data = {"action": "create"}
response = requests.post(
    "https://api.example.com/resource",
    data=data,
    headers=headers,
    auth=("admin", "password"),
)

# POST with timeout
response = requests.post(
    "https://api.example.com/process", json={"data": "value"}, timeout=10
)

"""
================================================================================
6. PUT - Fully update/replace a resource
================================================================================
"""

# PUT request to replace entire resource
data = {"title": "Complete Update", "body": "New content", "userId": 1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=data)
print(response.status_code)  # 200

# PUT with JSON
json_data = {"name": "Updated Name", "email": "new@example.com", "age": 35}
response = requests.put("https://api.example.com/users/5", json=json_data)

# PUT with headers
headers = {"If-Match": "etag123"}
data = {"status": "completed"}
response = requests.put("https://api.example.com/tasks/10", data=data, headers=headers)

# PUT with authentication
response = requests.put(
    "https://api.example.com/orders/7",
    json={"status": "shipped"},
    auth=("user", "pass"),
)

"""
================================================================================
7. REQUEST - Generic request method (any HTTP method)
================================================================================
"""

# GET using request()
response = requests.request("GET", "https://jsonplaceholder.typicode.com/posts/1")
print(response.json())

# POST using request()
response = requests.request(
    "POST", "https://jsonplaceholder.typicode.com/posts", json={"title": "Test"}
)

# PUT using request()
response = requests.request(
    "PUT", "https://jsonplaceholder.typicode.com/posts/1", data={"title": "New"}
)

# DELETE using request()
response = requests.request("DELETE", "https://jsonplaceholder.typicode.com/posts/1")

# PATCH using request()
response = requests.request(
    "PATCH", "https://jsonplaceholder.typicode.com/posts/1", data={"title": "Patched"}
)

# HEAD using request()
response = requests.request("HEAD", "https://jsonplaceholder.typicode.com/posts/1")
print(response.headers)

# Request with full parameter set
response = requests.request(
    method="POST",
    url="https://api.example.com/resource",
    headers={"Authorization": "Bearer token"},
    json={"data": "value"},
    timeout=5,
    verify=True,
    auth=("username", "password"),
)

"""
================================================================================
COMMON RESPONSE OBJECT PROPERTIES
================================================================================
"""

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)  # HTTP status code (200, 404, etc.)
print(response.headers)  # Response headers dictionary
print(response.text)  # Response body as string
print(response.content)  # Response body as bytes
print(response.json())  # Response body as JSON (parsed)
print(response.url)  # Final URL (after redirects)
print(response.elapsed)  # Time taken for request
print(response.encoding)  # Encoding of response
print(response.cookies)  # Cookies from response
print(response.history)  # List of redirect responses

"""
================================================================================
HANDLING ERRORS AND STATUS CODES
================================================================================
"""

# Check if request was successful
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("Success!")
else:
    print(f"Failed with status: {response.status_code}")

# Using response.raise_for_status() (raises exception on error)
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/invalid")
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError:
    print("Connection Error")
except requests.exceptions.Timeout:
    print("Timeout occurred")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")

"""
================================================================================
EXCEPTION HANDLING - BEST PRACTICE
================================================================================
"""

try:
    response = requests.get(
        "https://api.example.com/data", params={"limit": 10}, timeout=10, verify=True
    )
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")
except requests.exceptions.ConnectionError as err:
    print(f"Connection error: {err}")
except requests.exceptions.Timeout as err:
    print(f"Timeout error: {err}")
except requests.exceptions.RequestException as err:
    print(f"General error: {err}")

"""
================================================================================
QUICK REFERENCE - ALL METHODS
================================================================================

delete(url, args)               DELETE request
get(url, params, args)          GET request with optional params
head(url, args)                 HEAD request (headers only)
patch(url, data, args)          PATCH request (partial update)
post(url, data, json, args)     POST request (create)
put(url, data, args)            PUT request (full update/replace)
request(method, url, args)      Generic request with specified method

COMMON ARGUMENTS:
- params: Query parameters (dict)
- data: Form data or request body (dict)
- json: JSON request body (dict, automatically serialized)
- headers: HTTP headers (dict)
- cookies: Cookies (dict or CookieJar)
- auth: Authentication (tuple or AuthBase subclass)
- timeout: Timeout in seconds (int or tuple)
- verify: SSL verification (bool or string path to cert)
- allow_redirects: Follow redirects (bool)
- stream: Stream response content (bool)
- files: Files to upload (dict)
"""
