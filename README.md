# Mentor-Platform

## Loyiha haqida
**Mentor-Platform** — bu maktab boshqaruv tizimi bo‘lib, talabalar, ustozlar va darslarni boshqarish imkoniyatini taqdim etadi. Loyihada Django REST Framework, JWT autentifikatsiyasi va PostgreSQL ma’lumotlar bazasi ishlatilgan. Bu loyiha orqali siz real REST API yaratish, autentifikatsiya, CRUD amaliyotlari, test yozish va deploy qilish ko‘nikmalarini egallaysiz.

---

## Texnologiyalar
- Python 3.x  
- Django REST Framework  
- PostgreSQL  
- JWT (SimpleJWT)  
- pytest-django yoki Django test  
- Deployment: Render.com  

---

## Loyihaning asosiy xususiyatlari
- Talabalar va ustozlar uchun ro‘yxatdan o‘tish va autentifikatsiya  
- Talabalar, ustozlar va darslarni boshqarish uchun API endpointlar  
- CRUD operatsiyalari va filtrlash  
- Darslarga yozilish va qatnashish monitoringi  
- Testlar yordamida kod sifatini nazorat qilish  
- Loyihani Render.com’da deploy qilish  

---

## Model struktura
| Model          | Maydonlar                                  |
| -------------- | ----------------------------------------- |
| **Student**    | ism, familiya, telefon, email             |
| **Teacher**    | ism, email, fan                           |
| **Lesson**     | fan nomi, o‘qituvchi, dars sanasi, vaqt  |
| **StudentLesson** | student qaysi darsga qatnashganini ko‘rsatadi |
| **User**       | umumiy login tizimi (admin, student, teacher) |

---

## API endpointlar (namunaviy)

| Method | Endpoint          | Ta’rif                          |
| ------ | ----------------- | -------------------------------|
| POST   | `/api/register/`  | Foydalanuvchi ro‘yxatdan o‘tadi |
| POST   | `/api/login/`     | JWT token oladi                 |
| GET    | `/api/students/`  | Talabalar ro‘yxati             |
| POST   | `/api/students/`  | Yangi student qo‘shish         |
| GET    | `/api/lessons/`   | Darslar ro‘yxati               |
| POST   | `/api/enroll/`    | Student darsga yoziladi        |

---

## Loyihani ishga tushirish

### Talablar
- Python 3.x
- PostgreSQL
- virtualenv (tavsiya etiladi)



