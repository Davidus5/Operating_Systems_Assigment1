# הגדרת תמונת הבסיס - פייתון 3.9 בגרסה רזה כדי לחסוך במקום, כפי שנדרש
FROM python:3.9-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ דרישות הספריות פנימה
COPY requirements.txt .

# התקנת הספריות הדרושות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד האפליקציה פנימה (את ה-inventory.txt ואת ה-.env לא נעתיק דרך כאן)
COPY app.py .

# חשיפת הפורט שעליו רץ שרת הפלאסק
EXPOSE 5000

# הפקודה שתרוץ כשהקונטיינר יעלה
CMD ["python", "app.py"]