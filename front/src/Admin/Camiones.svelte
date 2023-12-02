<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import { getFunction } from '../js/asyncFunctions';
    import NavAdmin from '../Components/NavAdmin.svelte';
    import Tabla from '../Components/Tabla.svelte';

    let camiones = [];

    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1' ){
			push('/');
		}

        camiones = await getFunction('http://34.70.30.227:5000/data/truck');

	});


 
   
   

</script>

<NavAdmin />

<Tabla tipo="Camiones" objetos= { camiones } url="camion" />