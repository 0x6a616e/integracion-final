<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import Editar from "../../Components/Editar.svelte";
    import NavAdmin from "../../Components/NavAdmin.svelte";    
    export let params = {};
    onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}
	});
</script>

<NavAdmin />

<Editar label = "Camion" table = "truck" id = "{ params.id}"/>
