<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import NavAdmin from '../Components/NavAdmin.svelte';
    import Tabla from '../Components/Tabla.svelte';

    onMount(() => {
		if (!isAuthenticated()){
			push('/');
		}
	});

</script>

<NavAdmin />

<Tabla tipo="Sucursal" objetos= { [] } url="sucursal" />

