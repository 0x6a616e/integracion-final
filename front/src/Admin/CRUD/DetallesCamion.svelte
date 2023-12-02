<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction} from '../../js/asyncFunctions';
    import NavAdmin from '../../Components/NavAdmin.svelte';
    import DetallesItem from '../../Components/DetallesItem.svelte';

    export let params = {};

    const zip = (a, b) => a.map((k, i) => [k, b[i]]);

    let table = [];

    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1' ){
			push('/');
		}

        let attrs = await getFunction('http://34.70.30.227:5000/attr/truck');
        let values = await getFunction('http://34.70.30.227:5000/data/truck/id/'+params.id);
        table = zip(attrs, Object.entries(values[0]));

	});

</script>

<NavAdmin />

<DetallesItem tipo = "Camion" tables = {table}/>
