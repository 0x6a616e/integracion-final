<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import NavAdmin from '../Components/NavAdmin.svelte';
    import Tabla from '../Components/Tabla.svelte';
    import axios from 'axios';

    onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1' ){
			push('/');
		}


        const headers = {
            'Authorization': `Bearer ${localStorage.getItem('token')}` // Añade el token al encabezado 'Authorization'
        };

        axios.get('http://34.70.30.227:5000/truck', { headers })
        .then(response => {
            console.log(response);
        })
        .catch(error => {
            console.log(error);
        });
	});


 
   
   

</script>

<NavAdmin />

<Tabla tipo="Camiones" objetos= { [] } url="camion" />