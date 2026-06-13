#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logger Centralizado - boch-Kainal
Registra todos los eventos y errores de los servicios
"""

import json
import logging
from datetime import datetime
from pathlib import Path

class Logger:
    """Sistema centralizado de logging"""
    
    def __init__(self):
        self.logs_dir = Path(__file__).parent.parent / 'logs'
        self.logs_dir.mkdir(exist_ok=True)
        
        # Configurar logging
        self.setup_logging()
    
    def setup_logging(self):
        """Configura el sistema de logging"""
        log_file = self.logs_dir / f"boch_kainal_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('boch-kainal')
    
    def info(self, message, service='general', **kwargs):
        """Registra información"""
        self.logger.info(f"[{service}] {message}")
    
    def warning(self, message, service='general', **kwargs):
        """Registra advertencia"""
        self.logger.warning(f"[{service}] {message}")
    
    def error(self, message, service='general', code='UNKNOWN', **kwargs):
        """Registra error"""
        self.logger.error(f"[{service}] ({code}) {message}")
    
    def critical(self, message, service='general', **kwargs):
        """Registra error crítico"""
        self.logger.critical(f"[{service}] CRITICAL: {message}")
    
    def show_logs(self, lines=50, service=None, level=None):
        """Muestra los últimos logs"""
        log_file = list(self.logs_dir.glob('*.log'))[-1] if self.logs_dir.glob('*.log') else None
        
        if not log_file:
            print("📋 No hay logs disponibles aún.")
            return
        
        with open(log_file, 'r') as f:
            all_lines = f.readlines()
        
        # Filtrar si es necesario
        if service or level:
            filtered = []
            for line in all_lines:
                if service and service in line:
                    filtered.append(line)
                elif level and level in line:
                    filtered.append(line)
            all_lines = filtered
        
        # Mostrar últimas líneas
        for line in all_lines[-lines:]:
            print(line.rstrip())

if __name__ == '__main__':
    logger = Logger()
    logger.info('Test de información', service='test')
    logger.warning('Test de advertencia', service='test')
    logger.error('Test de error', service='test', code='TEST_ERROR')
    logger.show_logs(lines=10)
