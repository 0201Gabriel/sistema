function inti(){
    var numero1 = parseInt(document.getElementById('cantidad').value);
    var numero2 =parseInt(document.getElementById('precio').value);
    document.getElementById("resultado").innerHTML= numero1*numero2;
}

function registrar(codigo, producto, cantidad, precio_unitario, total){
    document.getElementById('codigo_agregar').value = codigo;
    document.getElementById('producto_agregar').value = producto;
    document.getElementById('cantidad_agregar').value = cantidad;
    document.getElementById('PrecioUnitario_agregar').value = precio_unitario;
    document.getElementById('total_agregar').value = total;
}
