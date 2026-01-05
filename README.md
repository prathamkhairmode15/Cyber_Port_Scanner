<p align="center"> <b>A futuristic Python + Flask powered port scanner with OS detection, vulnerability insights, PDF reporting, and sleek cyber-themed UI.</b> </p> <p align="center"> <img src="https://img.shields.io/badge/Status-Active-00ff99?style=for-the-badge" /> <img src="https://img.shields.io/badge/Backend-Python%203.8+-3776AB?style=for-the-badge" /> <img src="https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge" /> <img src="https://img.shields.io/badge/UI-HTML%20|%20CSS%20|%20JS-4dd2ff?style=for-the-badge" /> <img src="https://img.shields.io/badge/Security-Cyber%20Lab-ff4d4d?style=for-the-badge" /> </p>

# 🛡️ Cyber Port Scanner — Project Information

## 📌 Overview

**Cyber Port Scanner** is a modern cybersecurity scanning tool built using **Python + Flask**, featuring a futuristic web dashboard.

It allows users to:

- Scan systems for **open TCP ports**
- Detect the likely **Operating System (TTL-based guess)**
- Highlight **basic vulnerability indicators**
- Export results as **PDF reports**
- Visualize results clearly instead of raw terminals

This project simulates real-world tools used in:

- network auditing  
- penetration testing labs  
- security assessments  
- learning cybersecurity fundamentals  

> ⚠️ **Ethical Notice:**  
> Use this tool only on systems you **own or have explicit permission to test**.

---

## 🎯 Project Goals

- Help users understand exposed services on a host
- Teach how port visibility relates to security
- Demonstrate full-stack security development
- Provide clean, user-friendly visualization instead of console output

---

## 🧠 How It Works (Simple Explanation)

1. User enters:
   - Target IP / domain  
   - Port range  

2. Backend scans ports using Python sockets  
3. OS guess is made based on **TTL from ping**
4. Results are analyzed for common risk indicators
5. Output is displayed beautifully and can be exported to PDF

---

## 🖨 Sample Output (Example Scan)

### **Input**
Target: 127.0.0.1
Start Port: 20
End Port: 200


### **Result**
**Target:** 127.0.0.1  
**Detected OS:** Linux / Unix (likely)  
**Scan Time:** 2026-01-05 13:45  

---

### 🔎 Open Ports Found

| Port | Service         |
|------|----------------|
| 22   | SSH            |
| 80   | HTTP Server    |
| 443  | HTTPS Server   |

---

### ⚠️ Vulnerability Notes

- **Port 22 (SSH)** → Use key authentication, disable root login  
- **Port 80 (HTTP)** → Prefer HTTPS to protect data  
- **Port 443 (HTTPS)** → Check SSL configuration & headers  

If no risks exist:


---

## 💡 Why It Matters

Open ports act as **doors into a system**.

Too many exposed services increase attack surface — learning to identify them is one of the most fundamental cybersecurity skills.

This project makes that process:

- visual  
- easy to understand  
- safe for learning  
- suitable for professional demonstrations

---

## 🚀 Ideal Use Cases

- University cybersecurity capstones  
- Internship portfolios  
- Lab simulations  
- Personal learning  
- Ethical hacking practice environments  

---

## 🤝 Credits

Developed as a hands-on cybersecurity learning project.

---



