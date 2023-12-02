<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import NavAdmin from '../../Components/NavAdmin.svelte';
    import Detalles from '../../Components/Detalles.svelte';

    onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}
	});

</script>

<NavAdmin />

<Detalles x = 0 y = 0 items = { [] }/>