<h1>🧑‍💼 User Profile Django App</h1>

<strong>A simple and powerful Django application that allows users to upload profile pictures, edit their account details, and manage personal information with ease.</strong>

<h2>🚀 Features</h2>

🔐 User Authentication (Login / Logout)

🖼️ Profile Picture Upload with ImageField

✏️ Update Profile Information (name, email, etc.)

🗂️ Organized structure using Django’s best practices

📁 Media file handling with automatic folder creation

🎨 Easily customizable UI for any project

<h2>🛠️ Tech Stack</h2>

<div >

  <li>Django (Python Web Framework)</li>
  <li>Tailwind CSS</li>
  <li>SQLite</li>
  
</div>

<h2>📸 How It Works</h2>

User logs in

User uploads or updates their profile picture

Django saves the image in the /media/ directory

Frontend displays the image using
<strong>{{ user.profilepicture.image.url }}</strong>
