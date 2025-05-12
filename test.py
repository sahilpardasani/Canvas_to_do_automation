from canvasapi import Canvas

# Correct Canvas API URL for Penn State
API_URL = "https://psu.instructure.com"
API_KEY = "1050~YHLELHYawffAaVYv9X3G3W3rrmvcPm9JLGntmX8X8HweKm2rCJ2Vvev4BWTyeNND"

canvas = Canvas(API_URL, API_KEY)

try:
    user = canvas.get_current_user()
    print(f"✅ Logged in as: {user.name} (ID: {user.id})")

    print("\n📚 Favorited Courses:")
    for course in user.get_favorite_courses():
        print(f"- {course.name}")

except Exception as e:
    print("❌ Something went wrong! Check your token or API URL.")
    print(e)
