function mensajeError(obj) {
    let html = '<ul>'
    $.each(obj,function (key,value) {
        html += '<li>'+ value + '</li>'
    })
    html += '</ul>'
    Swal.fire({
        title:'Error',
        html : html,
        icon : 'error'
    });
}

function guardadoExitoso() {
    Swal.fire(
        'Bien!',
        'El registro se ha guardado exitosamente!',
        'success'
    )
}