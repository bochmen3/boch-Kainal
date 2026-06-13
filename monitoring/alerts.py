#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Alertas - boch-Kainal
Envía notificaciones de eventos importantes
"""

from datetime import datetime

class Alerts:
    """Sistema de alertas automáticas"""
    
    def __init__(self):
        self.alerts_history = []
    
    def critical(self, message, service='general'):
        """Alerta crítica"""
        alert = {
            'type': 'CRITICAL',
            'message': message,
            'service': service,
            'timestamp': datetime.now().isoformat(),
        }
        self.alerts_history.append(alert)
        
        print(f"\n🚨 ALERTA CRÍTICA")
        print(f"├─ Servicio: {service}")
        print(f"├─ Mensaje: {message}")
        print(f"└─ Hora: {alert['timestamp']}\n")
        
        # Aquí iría envío por Telegram, Discord, etc.
        self._notify_telegram(alert)
    
    def warning(self, message, service='general'):
        """Alerta de advertencia"""
        alert = {
            'type': 'WARNING',
            'message': message,
            'service': service,
            'timestamp': datetime.now().isoformat(),
        }
        self.alerts_history.append(alert)
        
        print(f"\n⚠️  ADVERTENCIA")
        print(f"├─ Servicio: {service}")
        print(f"├─ Mensaje: {message}")
        print(f"└─ Hora: {alert['timestamp']}\n")
    
    def info(self, message, service='general'):
        """Alerta informativa"""
        alert = {
            'type': 'INFO',
            'message': message,
            'service': service,
            'timestamp': datetime.now().isoformat(),
        }
        self.alerts_history.append(alert)
        
        print(f"ℹ️  INFORMACIÓN")
        print(f"├─ Servicio: {service}")
        print(f"├─ Mensaje: {message}")
        print(f"└─ Hora: {alert['timestamp']}")
    
    def _notify_telegram(self, alert):
        """Envía notificación por Telegram (stub)"""
        # Implementar envío real aquí
        pass
    
    def _notify_discord(self, alert):
        """Envía notificación por Discord (stub)"""
        # Implementar envío real aquí
        pass
    
    def get_history(self, limit=20):
        """Obtiene historial de alertas"""
        return self.alerts_history[-limit:]

if __name__ == '__main__':
    alerts = Alerts()
    alerts.critical('Telegram Bot se desconectó', service='telegram')
    alerts.warning('Uso de CPU alto', service='scraper')
    alerts.info('Nueva versión disponible', service='system')
