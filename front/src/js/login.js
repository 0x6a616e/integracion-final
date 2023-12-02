import Swal from 'sweetalert2';
import axios from 'axios';

export const login = () =>{
    if(user != '' || password != ''){
        const form = document.getElementById('loginForm');

        axios.post('http://34.121.173.64:5000/login', new FormData(form))
        .then(res =>{
            
            const data = res.data;

            localStorage.setItem('id', data.user_id);
            localStorage.setItem('admin', data.is_admin);
            localStorage.setItem('token', data.token);

            if(localStorage.getItem('admin') === '1'){
                push('/pedidos/admin');
            }else{
                push('/pedidos');
            }

        })
        .catch(error => {
            console.log(error);
        });


        Swal.fire({
            title: 'Loggeado',
            text: 'Inicio de sesión correcto',
            icon: 'success',
            confirmButtonText: 'Cool',
        });

        push('/pedidos');
    }else{
        Swal.fire('Oops', 'Datos incompletos', 'error');
    }
}