import Swal from 'sweetalert2';


export const alertaExito = () =>{


    Swal.fire({
        title: 'Exito',
        text: 'La transacción se logro con éxito',
        icon: 'success',
        confirmButtonText: 'Cool',
    });
};