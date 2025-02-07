
# 📖 API Documentation

## **1️⃣ Users API**

### **🔹 Tạo người dùng**

**Endpoint:** `POST /users/`

#### **Request Body for Creating User**

```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "securepassword",
  "full_name": "John Doe",
  "bio": "Software Developer",
  "profile_picture": "https://example.com/avatar.jpg"
}
```

#### **Response for Creating User**

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "bio": "Software Developer",
  "profile_picture": "https://example.com/avatar.jpg",
  "created_at": "2025-02-10T10:00:00",
  "updated_at": "2025-02-10T10:00:00"
}
```

---

### **🔹 Lấy danh sách người dùng**

**Endpoint:** `GET /users/`

#### **Response for Getting Users List**

```json
[
  {
    "id": 1,
    "username": "johndoe",
    "email": "johndoe@example.com",
    "full_name": "John Doe"
  }
]
```

---

### **🔹 Lấy chi tiết người dùng**

**Endpoint:** `GET /users/{user_id}`

#### **Response for Getting User Details**

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe"
}
```

---

## **2️⃣ Categories API**

### **🔹 Tạo danh mục**

**Endpoint:** `POST /categories/`

#### **Request Body for Creating Category**

```json
{
  "name": "Technology",
  "slug": "technology",
  "description": "All about technology."
}
```

#### **Response for Creating Category**

```json
{
  "id": 1,
  "name": "Technology",
  "slug": "technology",
  "description": "All about technology."
}
```

---

## **3️⃣ Tags API**

### **🔹 Tạo thẻ (Tag)**

**Endpoint:** `POST /tags/`

#### **Request Body for Creating Tag**

```json
{
  "name": "FastAPI",
  "slug": "fastapi"
}
```

#### **Response for Creating Tag**

```json
{
  "id": 1,
  "name": "FastAPI",
  "slug": "fastapi"
}
```

---

## **4️⃣ Posts API**

### **🔹 Tạo bài viết**

**Endpoint:** `POST /posts/`

#### **Request Body for Creating Post**

```json
{
  "user_id": 1,
  "category_id": 1,
  "title": "Introduction to FastAPI",
  "slug": "intro-fastapi",
  "content": "FastAPI is a modern web framework...",
  "is_published": true
}
```

#### **Response for Creating Post**

```json
{
  "id": 1,
  "title": "Introduction to FastAPI",
  "slug": "intro-fastapi",
  "content": "FastAPI is a modern web framework...",
  "is_published": true
}
```

## **5️⃣ Comments API**

### **🔹 Tạo bình luận**

**Endpoint:** `POST /comments/`

#### **Request Body**

```json
{
  "post_id": 1,
  "user_id": 2,
  "content": "Great article!"
}
```

#### **Response**

#### **Response for Creating Comment**

```json
{
  "id": 1,
  "post_id": 1,
  "user_id": 2,
  "content": "Great article!"
}
```

## **6️⃣ Post Tags API**

### **🔹 Gắn tag vào bài viết**

**Endpoint:** `POST /post-tags/`

#### **Request Body for Adding Tag to Post**

```json
{
  "post_id": 1,
  "tag_id": 2
}
```

#### **Response for Adding Tag to Post**

```json
{
  "post_id": 1,
  "tag_id": 2
}
```

# 📌 **Tổng kết**

| API | Method | Chức năng |
|------|--------|-----------|
| `/users/` | `POST` | **Tạo người dùng** |
| `/users/` | `GET` | **Lấy danh sách người dùng** |
| `/users/{user_id}` | `GET` | **Lấy chi tiết người dùng** |
| `/categories/` | `POST` | **Tạo danh mục** |
| `/tags/` | `POST` | **Tạo thẻ (Tag)** |
| `/posts/` | `POST` | **Tạo bài viết** |
| `/comments/` | `POST` | **Tạo bình luận** |
| `/post-tags/` | `POST` | **Gắn tag vào bài viết** |

📌 **Hệ thống API đã được hoàn thiện, có thể sử dụng với FastAPI!** 🚀
