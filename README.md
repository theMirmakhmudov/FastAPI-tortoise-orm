# Tortoise ORM and Aerich 
### 1.Virtualenv yaratish va faollashtirish

**MacOS/Linux**
```bash
    python -m venv .venv
    source .venv/bin/activate
```
**Windows**
```bash
    python -m venv .venv
```

### 2. Kerakli paketlarni yuklaymiz:
```bash
  pip install tortoise-orm aerich
```

### 3. aerich ni birinchi marta ishga tushirish:
```bash
  aerich init -t db.DB_CONFIG
```

### 4. db yaratish:
```bash
  aerich init-db
```

### 5. o'zgarishlar qo‘shilgach:
```bash
  aerich migrate
```
```bash
  aerich upgrade
```