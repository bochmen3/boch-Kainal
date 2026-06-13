# 📊 Guía de Monitoreo - boch-Kainal

## ¿Qué es el sistema de monitoreo?

El sistema de monitoreo es una característica **ÚNICA** de boch-Kainal que te permite:

- 🔍 Ver el estado de todos tus servicios en tiempo real
- 📊 Obtener estadísticas y métricas de rendimiento
- 🔔 Recibir alertas automáticas cuando algo falla
- 📈 Analizar historiales de actividad
- 🎛️ Controlar procesos desde un dashboard web

---

## 🚀 Inicio Rápido

### 1. Iniciar el dashboard

```bash
cd boch-Kainal
source venv/bin/activate
python -m monitoring.dashboard
```

**Salida esperada:**
```
🌐 Dashboard iniciado en http://localhost:8000
📊 Accede desde tu navegador: http://127.0.0.1:8000
🔐 Autenticación: usuario/contraseña (ver config/.env)
```

### 2. Acceder al dashboard

Desde tu navegador en Termux o desde otro dispositivo:
```
http://localhost:8000
```

### 3. Verificar estado de servicios

```bash
python -m monitoring.health_check
```

---

## 📊 Dashboard Web

### Características principales

#### 🟢 Estado en Tiempo Real
- Indicadores visuales de cada servicio
- Color verde = activo, rojo = inactivo, amarillo = advertencia
- Tiempo de actividad (uptime)

#### 📈 Gráficas y Estadísticas
- Uso de CPU y memoria
- Número de eventos procesados
- Tasa de errores
- Actividad por hora/día/semana

#### 🔔 Centro de Alertas
- Historial de todas las alertas
- Filtrar por tipo y severidad
- Marcar como leído/resuelto

#### ⚙️ Control de Procesos
- Reiniciar servicios
- Pausar/reanudar bots
- Cambiar configuraciones
- Ver logs en tiempo real

---

## 💻 Uso Avanzado

### Verificar salud de servicios específicos

```bash
# Ver estado de Telegram Bot
python -m monitoring.health_check --service telegram

# Ver estado de todos los bots
python -m monitoring.health_check --filter bots

# Información detallada
python -m monitoring.health_check --verbose
```

### Ver logs en tiempo real

```bash
# Mostrar últimas 50 líneas
python -m monitoring.logger --tail 50

# Filtrar por nivel (ERROR, WARNING, INFO)
python -m monitoring.logger --level ERROR

# Filtrar por servicio
python -m monitoring.logger --service telegram_bot

# Ver logs en tiempo real (como tail -f)
python -m monitoring.logger --follow
```

### Configurar alertas

Edita `config/.env`:

```env
# Alertas por Telegram
ALERTS_TELEGRAM_ENABLED=True
ALERTS_TELEGRAM_CHAT_ID=your_chat_id

# Alertas por Discord
ALERTS_DISCORD_ENABLED=True
ALERTS_DISCORD_WEBHOOK=your_webhook_url

# Nivel de alertas (CRITICAL, ERROR, WARNING)
ALERTS_LEVEL=ERROR

# Intervalo de verificación (segundos)
HEALTH_CHECK_INTERVAL=300
```

### Reiniciar automáticamente si falla

Edita `monitoring/health_check.py`:

```python
config = {
    'auto_restart': True,
    'restart_delay': 30,  # segundos
    'max_retries': 3,
}
```

---

## 📈 Métricas Disponibles

### Por Servicio
- Estado actual (activo/inactivo)
- Tiempo de ejecución
- Número de restarts
- Último error
- Consumo de recursos

### Globales
- Servicios activos / totales
- Porcentaje de disponibilidad
- Eventos procesados hoy
- Errores en las últimas 24h

---

## 🔔 Sistema de Alertas

### Tipos de alertas

**🚨 CRÍTICA** - Servicio desconectado
```
🚨 ALERTA CRÍTICA: Telegram Bot desconectado
Tiempo: hace 5 minutos
Último error: Connection timeout
Acción: Reiniciando automáticamente
```

**⚠️ ADVERTENCIA** - Rendimiento bajo
```
⚠️ ADVERTENCIA: Uso de CPU elevado
Servicio: Web Scraper
CPU: 85% | Memoria: 92%
Recomendación: Revisar configuración
```

**ℹ️ INFO** - Cambios y eventos
```
ℹ️ Información: Nueva versión disponible
Servicio: Discord Bot v2.0
Acción: Actualizar antes de su próxima ejecución
```

---

## 📝 Ejemplos Prácticos

### Caso 1: Monitorear un bot de Telegram

```bash
# Iniciar bot
python -m bots.telegram.main &

# En otra terminal, monitorear
python -m monitoring.health_check --service telegram --follow

# Ver dashboard
python -m monitoring.dashboard
```

### Caso 2: Detectar y alertar sobre errores

```bash
# Configurar alertas en .env
echo "ALERTS_TELEGRAM_ENABLED=True" >> config/.env

# Iniciar el sistema
python -m monitoring.logger --follow

# Si hay un error, recibirás una alerta por Telegram
```

### Caso 3: Análisis de rendimiento

```bash
# Ver estadísticas detalladas
python -m monitoring.dashboard --stats

# Exportar datos a CSV
python -m monitoring.logger --export stats_2026_06_13.csv

# Generar reporte
python -m monitoring.reports --period week
```

---

## 🐛 Solución de Problemas

### Dashboard no se inicia

```bash
# Verificar puerto
lsof -i :8000

# Usar otro puerto
python -m monitoring.dashboard --port 9000
```

### No recibo alertas

```bash
# Verificar configuración
cat config/.env | grep ALERTS

# Probar alerta manual
python -c "from monitoring.alerts import send_alert; send_alert('TEST', 'CRITICAL')"
```

### Logs no se actualizan

```bash
# Asegúrate que el servicio está escribiendo logs
ls -la logs/

# Verificar permisos
chmod 755 logs/
```

---

## 🔐 Seguridad del Dashboard

### Autenticación

Por defecto, el dashboard requiere usuario y contraseña:

```env
DASHBOARD_AUTH_ENABLED=True
DASHBOARD_USERNAME=admin
DASHBOARD_PASSWORD=cambiar_esto
```

### Solo acceso local

```bash
python -m monitoring.dashboard --localhost-only
```

### HTTPS (si es necesario)

```bash
python -m monitoring.dashboard --ssl --cert /path/to/cert
```

---

## 📊 API de Monitoreo

Puedes integrar el monitoreo en tus propios scripts:

```python
from monitoring import HealthCheck, Alerts, Logger

# Crear instancias
health = HealthCheck()
alerts = Alerts()
logger = Logger()

# Verificar estado
status = health.check_service('telegram_bot')
if not status['active']:
    alerts.critical(f"Telegram Bot inactivo: {status['error']}")

# Registrar evento
logger.info('Procesadas 100 órdenes', service='bot')

# Registrar error
logger.error('Falló conexión a API', service='scraper', code='API_TIMEOUT')
```

---

## 📞 Soporte

Para más información:
- Revisa `docs/GUIA_USO.md`
- Ve a `docs/SOLUCIONES.md` para problemas
- Contacta a bochmen3@gmail.com

---

**¡El monitoreo centralizado es la clave para un sistema confiable! 🎯**
