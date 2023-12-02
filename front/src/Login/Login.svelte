<script>
    import {push} from 'svelte-spa-router';
    import { onMount } from 'svelte';
    import {isAuthenticated } from '../js/auth';
    import Swal from 'sweetalert2';
    import axios from 'axios';

    onMount(() => {

       if (isAuthenticated() && localStorage.getItem('admin') === '1'){
			push('/pedidos/admin');
		}


       if (isAuthenticated() && localStorage.getItem('admin') === '0'){
			push('/pedidos');
		}

    });

    let user = '';
    let password = '';

    const login = () =>{
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
</script>


<div class="container mt-5 bg-white rounded shadow pt-3 w-50"  style="height: 5rem;">
    <h1 class="text-center"> Log in </h1>
</div>


<div class="container mt-4 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-50">
    <form action="" method="POST" on:submit|preventDefault={login} id="loginForm">
        <div class="mb-3">
            <label for="nombre" class="form-label">Usuario</label>
            <input type="text" class="form-control" id="nombre" name="username" placeholder="Curvos" value={user} on:input={event => (user = event.target.value)}>
        </div>
        
        <div class="mb-3 mt-4">
            <label for="direccion" class="form-label">Contraseña</label>
            <input type="password" class="form-control" id="direccion" name="password" placeholder="1234" value={password} on:input={event => (password = event.target.value)}>
        </div>



        <div class="mb-3 mt-5 justiy-content-center">
            <button type="submit" class="btn center w-100 btn-lg btn-block shadow-lg text-light" style=" background-color: #8973D9">Iniciar sesión</button>
        </div>
    </form>
</div>