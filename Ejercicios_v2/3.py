class bonificaciones:
    def montoventas(self, monto):
        if monto < 500:
            return 0
        elif 500  <= monto <= 1000:
            return 0.25
        elif 1001 <= monto <= 1500:
            return 0.30
        else:
            return 0.35

