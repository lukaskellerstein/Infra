# QEMU

---

# AKS

The k8s nodes needs to support `nested virtualization`.

Ex. `Dv3` and `Dsv3` does.

Dv3
https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dv3-series?tabs=sizebasic

Dsv3
https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dsv3-series?tabs=sizebasic

---

# Default functionality

## Parameter QEMU_ARGS

## 🧠 `-vnc <host>:<display>` in QEMU

This syntax doesn't follow the typical IP:PORT convention — QEMU uses a concept of **VNC display numbers**, not raw ports.

### ✅ The full format is:

```bash
-vnc <host>:<display>[,<options>]
```

- `<host>` = the interface to bind (e.g., `127.0.0.1`, `0.0.0.0`)
- `<display>` = the **VNC display number**
- Each display corresponds to a **TCP port**:

---

## 🔢 Port Mapping in QEMU

| Display | Port |
| ------- | ---- |
| `:0`    | 5900 |
| `:1`    | 5901 |
| `:2`    | 5902 |
| ...     | ...  |

So:

```bash
-vnc 0.0.0.0:0
```

Means:

- QEMU will listen on **all interfaces** (`0.0.0.0`)
- On **display `:0`**, which maps to **TCP port 5900**

---

## ❌ You **cannot** specify raw port numbers directly

You can't write:

```bash
-vnc 0.0.0.0:5900  # ❌ Invalid!
```

That would actually try to bind to display `:5900`, which maps to port **11,800** (i.e., 5900 + 5900 😅).

---

## 🧩 If you want to use a specific port

Just calculate the display as:

```bash
display = port - 5900
```

Examples:

```bash
-vnc 0.0.0.0:1  # Binds to port 5901
-vnc 127.0.0.1:5  # Binds to port 5905, localhost-only
```

---

## ✅ TL;DR

| QEMU Syntax        | What it means                                      |
| ------------------ | -------------------------------------------------- |
| `-vnc 0.0.0.0:0`   | Listen on all interfaces, port 5900                |
| `-vnc 127.0.0.1:1` | Listen on localhost, port 5901                     |
| `-vnc 0.0.0.0:5`   | Listen on all interfaces, port 5905                |
| `-vnc 127.0.0.1:0` | 🔒 Secure default, binds only localhost, port 5900 |

---
