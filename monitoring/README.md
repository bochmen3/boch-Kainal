# Sistema de Monitoreo de boch-Kainal

Este directorio contiene el **sistema de monitoreo centralizado** - la característica única que diferencia a boch-Kainal.

## Archivos

- `health_check.py` - Verificador de salud de servicios
- `logger.py` - Logger centralizado
- `alerts.py` - Sistema de alertas automáticas
- `dashboard.py` - Dashboard web (en desarrollo)

## Uso Rápido

```bash
# Verificar estado de servicios
python -m monitoring.health_check

# Ver logs
python -m monitoring.logger

# Iniciar dashboard
python -m monitoring.dashboard
```

## Más información

Revisa `docs/MONITOREO.md` para la guía completa.
