<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction} from '../../js/asyncFunctions';
    import Editar from "../../Components/Editar.svelte";
    import NavAdmin from "../../Components/NavAdmin.svelte";    
    
    export let params = {};

    let atributos = [];
    
    onMount( async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}

        atributos = await getFunction('http://34.70.30.227:5000/attr/branch');

	});
</script>

<NavAdmin />

<Editar label = "Sucursal" table = "branch" id = "{ params.id }" attrs = {atributos}/>