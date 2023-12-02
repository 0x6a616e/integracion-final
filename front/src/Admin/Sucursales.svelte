<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction} from '../js/asyncFunctions';
    import NavAdmin from '../Components/NavAdmin.svelte';
    import Tabla from '../Components/Tabla.svelte';

    let sucursales = [];

    onMount( async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}

        sucursales = await getFunction('http://34.70.30.227:5000/branch');

	});

</script>

<NavAdmin />

<Tabla tipo="Sucursal" objetos= { sucursales } url="sucursal" />

