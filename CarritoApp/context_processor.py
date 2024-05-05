def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        carrito = request.session.get("carrito", None)
        if carrito:
            for key, value in carrito.items():
                total += int(value.get("acumulado", 0))
    return {"total_carrito": total}