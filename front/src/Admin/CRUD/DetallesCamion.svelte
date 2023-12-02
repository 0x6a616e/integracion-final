<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import NavAdmin from '../../Components/NavAdmin.svelte';
    import DetallesItem from '../../Components/DetallesItem.svelte';

    onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1' ){
			push('/');
		}
	});

</script>

<NavAdmin />

<DetallesItem tipo = "Camion" items = {[]}/>
