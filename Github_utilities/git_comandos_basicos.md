
# 🧾 Git Cheat Sheet – Comandos básicos

## 🔍 1. Ver cambios actuales
```
git status
```
Muestra qué archivos fueron modificados, agregados o eliminados desde el último commit.

---

## ➕ 2. Agregar archivos al "stage"

### a. Agregar **todos los cambios**:
```
git add .
```

### b. Agregar **un archivo específico**:
```
git add archivo.py
```

---

## 💬 3. Hacer un commit
```
git commit -m "Descripción clara de lo que hiciste"
```
Guarda los cambios en tu historial local de Git.

---

## 📤 4. Subir cambios a GitHub (push)

### Si tu rama principal se llama `main`:
```
git push origin main
```

### Si tu rama principal es `master`:
```
git push origin master
```

---

## 📥 5. Descargar cambios desde GitHub (pull)
```
git pull origin main
```
Útil si hiciste cambios en GitHub directamente o si trabajás en equipo.

---

## 📂 6. Ver el historial de commits
```
git log
```
Muestra los commits anteriores con detalles como autor, fecha y mensaje.

---

## 🧼 7. Ignorar archivos (opcional)
Si no querés subir archivos como `.env`, carpetas `__pycache__`, etc., creá un archivo llamado `.gitignore` y escribí ahí los nombres o extensiones a ignorar, por ejemplo:

```
__pycache__/
*.log
.env
```
