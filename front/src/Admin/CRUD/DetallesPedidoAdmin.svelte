<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction} from '../../js/asyncFunctions';
    import NavAdmin from '../../Components/NavAdmin.svelte';
    import Detalles from '../../Components/Detalles.svelte';

    export let params = {};

    let data = {};

    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}

        data = await getFunction('http://34.70.30.227:5000/order/'+params.id);

	});

</script>

<NavAdmin />

<Detalles x = {data.latitude} y = {data.longitude} items = { data.products }/>