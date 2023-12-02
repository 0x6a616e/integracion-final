<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import NavUser from "../Components/NavUser.svelte";
    import Detalles from "../Components/Detalles.svelte";

    onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '0'){
			push('/');
		}
	});

</script>

<NavUser />

<Detalles x = 0 y = 0 items = {[]}/>


