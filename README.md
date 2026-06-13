# 🚀 Boch-Kainal

**Tu proyecto principal de herramientas y bots para Termux Android**

## 📋 Descripción

`boch-Kainal` es el proyecto principal que integra todas tus herramientas, bots y automatizaciones para **Termux Android**. Este repositorio es tu centro de operaciones.

---

## 🎯 Objetivo

Consolidar en un único repositorio:
- ✅ Bots y automatizaciones
- ✅ Herramientas de productividad
- ✅ Scripts de mantenimiento
- ✅ Integraciones y plugins
- ✅ Documentación completa
- ✅ **NUEVA: Sistema de monitoreo en tiempo real**
- ✅ **NUEVA: Dashboard de estado**

---

## 📁 Estructura del Proyecto

```
boch-Kainal/
├── bots/                    # Bots principales
│   ├── telegram/           # Bots de Telegram
│   ├── discord/            # Integraciones Discord
│   └── README.md
├── tools/                   # Herramientas útiles
│   ├── scrapers/           # Web scrapers
│   ├── converters/         # Conversores de datos
│   └── README.md
├── automation/              # Scripts de automatización
│   ├── cron/               # Tareas programadas
│   └── README.md
├── monitoring/              # 🆕 Sistema de monitoreo
│   ├── health_check.py     # Verificar estado de servicios
│   ├── logger.py           # Logging centralizado
│   ├── alerts.py           # Sistema de alertas
│   └── dashboard.py        # Dashboard web
├── config/                  # Archivos de configuración
│   ├── .env.example        # Plantilla de variables
│   └── settings.yaml
├── docs/                    # Documentación
│   ├── INSTALACION.md      # Guía de instalación
│   ├── GUIA_USO.md         # Cómo usar
│   ├── BOTS.md             # Documentación de bots
│   ├── MONITOREO.md        # 🆕 Guía de monitoreo
│   └── SOLUCIONES.md       # Troubleshooting
├── logs/                    # Logs y registros
├── tests/                   # Tests
├── setup/                   # Setup y configuración
│   ├── install.sh
│   ├── requirements.txt
│   └── setup.py
├── .gitignore
├── .env.example
├── LICENSE
├── CHANGELOG.md
└── README.md
```

---

## ⭐ CARACTERÍSTICAS ÚNICAS

### 🆕 Sistema de Monitoreo Integrado

**Lo que hace especial a boch-Kainal:**

```python
# Monitoreo automático de todos tus procesos
from monitoring import HealthCheck, Dashboard, Alerts

# Verificar estado en tiempo real
health = HealthCheck()
status = health.check_all_services()

# Recibir alertas automáticas
alerts = Alerts()
alerts.notify_on_failure(service="telegram_bot")

# Ver dashboard web
dashboard = Dashboard(port=8000)
dashboard.start()  # Accede a http://localhost:8000
```

### 📊 Dashboard Web

- ✅ Ver estado de todos los bots en tiempo real
- ✅ Gráficas de uso y rendimiento
- ✅ Historial de eventos
- ✅ Control remoto de procesos
- ✅ Alertas visuales

### 🔔 Sistema de Alertas Inteligente

- ✅ Notificaciones por Telegram
- ✅ Alertas por Discord
- ✅ Logs centralizados
- ✅ Histórico de errores
- ✅ Estadísticas de actividad

### 📈 Logging Centralizado

```bash
# Ver todos los logs
python -m monitoring.logger --show-all

# Filtrar por servicio
python -m monitoring.logger --filter telegram_bot

# Últimas 100 líneas en tiempo real
python -m monitoring.logger --tail 100
```

---

## 🔧 Requisitos

- **Termux** (últimas versiones)
- **Python** 3.8+
- **Git**
- **API Keys** (según necesites para bots/servicios)

---

## 🚀 Instalación Rápida

### 1. Clonar el repositorio

```bash
git clone https://github.com/bochmen3/boch-Kainal.git
cd boch-Kainal
```

### 2. Ejecutar instalación

```bash
bash setup/install.sh
```

### 3. Configurar variables de entorno

```bash
cp config/.env.example config/.env
nano config/.env  # Edita con tus datos
```

### 4. Instalar dependencias

```bash
source venv/bin/activate
pip install -r setup/requirements.txt
```

### 5. Iniciar monitoreo (NUEVO)

```bash
python -m monitoring.dashboard
```

---

## 📦 Módulos Principales

### 🤖 Bots
- Telegram Bot
- Discord Integration
- Custom Bots

### 🛠️ Herramientas
- Web Scrapers
- Data Converters
- Media Tools

### ⚙️ Automatización
- Tareas Programadas
- Monitoreo
- Backups

### 🆕 Monitoreo
- Health Check en tiempo real
- Dashboard web interactivo
- Sistema de alertas automáticas
- Logging centralizado

---

## 📖 Documentación

- 📖 [Guía de Instalación](docs/INSTALACION.md)
- 🎯 [Guía de Uso](docs/GUIA_USO.md)
- 🤖 [Documentación de Bots](docs/BOTS.md)
- 📊 [Guía de Monitoreo](docs/MONITOREO.md) **← NUEVA**
- 🔧 [Solución de Problemas](docs/SOLUCIONES.md)
- 📋 [Cambios y Versiones](CHANGELOG.md)

---

## 💻 Uso Rápido

### Ejecutar un bot

```bash
python -m bots.telegram.main
```

### Ejecutar una herramienta

```bash
python -m tools.scrapers.example
```

### Monitorear servicios

```bash
python -m monitoring.health_check
```

### Iniciar dashboard

```bash
python -m monitoring.dashboard --port 8000
```

---

## 📊 Ejemplos de Monitoreo

### Verificar salud de todos los servicios

```bash
$ python -m monitoring.health_check

✓ Telegram Bot: ACTIVO (desde 2h 30m)
✓ Discord Bot: ACTIVO (desde 1h 15m)
⚠ Web Scraper: ADVERTENCIA (última ejecución: 30m atrás)
✗ API Externa: INACTIVA (sin conexión)

Estado General: 75% operacional
```

### Ver dashboard en tiempo real

```bash
$ python -m monitoring.dashboard

🌐 Dashboard iniciado en http://localhost:8000
📊 Accede para ver estadísticas en tiempo real
```

### Recibir alertas por Telegram

```bash
# Se configura automáticamente
# Recibirás mensajes como:

🚨 ALERTA CRÍTICA
Servicio: Telegram Bot
Estado: Desconectado
Tiempo: 2026-06-13 13:45:32
Acción: Reiniciando automáticamente...
```

---

## 🐛 Problemas Comunes

### Error: "No module named 'requests'"

```bash
pip install --upgrade -r setup/requirements.txt
```

### Error: "Permission denied"

```bash
chmod +x setup/install.sh
bash setup/install.sh
```

### Dashboard no accesible

```bash
# Asegúrate que el puerto 8000 está disponible
lsof -i :8000  # Verifica qué está usando el puerto

# O usa otro puerto
python -m monitoring.dashboard --port 9000
```

---

## 🔐 Seguridad

⚠️ **IMPORTANTE**: 
- Nunca commits tokens o API keys
- Usa `.env.example` para plantillas
- Mantén `config/.env` en `.gitignore`
- Guarda credenciales de forma segura
- El dashboard tiene autenticación opcional (configurable en .env)

---

## 📊 Estado del Proyecto

- ✅ Estructura base
- ✅ Documentación
- ✅ Setup automatizado
- ✅ **Sistema de monitoreo (NUEVO)**
- ✅ **Dashboard web (NUEVO)**
- 🔄 Desarrollo activo de features

---

## 🤝 Contribuyendo

Este es un proyecto personal, pero si quieres contribuir:

1. Crea una rama: `git checkout -b feature/nueva-feature`
2. Commit: `git commit -m 'Agregar nueva feature'`
3. Push: `git push origin feature/nueva-feature`
4. Pull Request

---

## 📜 Licencia

MIT License - Ver [LICENSE](LICENSE)

---

## 📧 Contacto

**Autor**: bochmen3
**Email**: bochmen3@gmail.com
**GitHub**: [@bochmen3](https://github.com/bochmen3)

---

## 🔄 Últimas Actualizaciones

- `2026-06-13`: 🆕 **Sistema de monitoreo en tiempo real agregado**
- `2026-06-13`: 🆕 **Dashboard web interactivo implementado**
- `2026-06-13`: Reorganización completa y documentación
- `2026-06-13`: Setup automatizado para Termux
- `2026-06-13`: Estructura profesional implementada

---

## 🌟 Lo que hace a boch-Kainal especial

A diferencia de otros proyectos en Termux, boch-Kainal incluye:

✨ **Sistema de monitoreo integrado** - Mantén control total de tus procesos
📊 **Dashboard web** - Interfaz visual para administrar todo
🔔 **Alertas inteligentes** - Notificaciones automáticas en caso de problemas
📈 **Logging centralizado** - Historial completo de eventos y errores
🎯 **Completamente automatizado** - Setup y configuración sencilla
🔐 **Seguro y privado** - Tu repositorio es privado

¡**Comienza ahora y optimiza tu flujo de trabajo en Termux!**
