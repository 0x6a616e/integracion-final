<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction} from '../js/asyncFunctions';
    import NavUser from "../Components/NavUser.svelte";
    import Detalles from "../Components/Detalles.svelte";
    
    export let params = {};
    export let x = 0;
    export let y = 0;

    let data = {};
    

    onMount( async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '0'){
			push('/');
		}

        data = await getFunction('http://34.70.30.227:5000/order/'+params.id);
	});

</script>

<NavUser />

<Detalles x = {data.latitude} y = {data.longitude} items = { data.products}/>


